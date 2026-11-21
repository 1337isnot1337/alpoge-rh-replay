"""Bounded retries for GitHub rate limits, preserving permission failures."""

import sys
import time
from urllib.error import HTTPError


ATTEMPTS = 4


def rate_limit_delay(error, attempt):
    if error.code not in (403, 429):
        return None
    headers = error.headers
    retry = headers.get('Retry-After', '')
    reset = headers.get('X-RateLimit-Reset', '')
    exhausted = headers.get('X-RateLimit-Remaining') == '0'
    if not (error.code == 429 or retry.isdigit() or exhausted
            or b'rate limit' in error.read().lower()):
        return None
    delays = [int(retry)] if retry.isdigit() else []
    if exhausted and reset.isdigit():
        delays.append(max(1, int(reset) - int(time.time()) + 1))
    return max(delays) if delays else 60 * 2 ** attempt

def wait_for_rate_limit(error, attempt, action):
    delay = rate_limit_delay(error, attempt)
    if delay is None or attempt == ATTEMPTS - 1:
        raise error
    error.close()
    print(f'GitHub rate limit (HTTP {error.code}). {action} after {delay}s.',
          file=sys.stderr, flush=True)
    time.sleep(delay)


def retry_rate_limited(operation, action):
    for attempt in range(ATTEMPTS):
        try:
            return operation()
        except HTTPError as error:
            wait_for_rate_limit(error, attempt, action)
