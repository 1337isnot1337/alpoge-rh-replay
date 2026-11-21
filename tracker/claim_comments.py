"""Group paginated repository comments by their owning claim issue."""

from collections import defaultdict
from datetime import datetime, timedelta
from itertools import islice

COMMENT_FEED = 'issues/comments?sort=updated&direction=asc&per_page=100'


def repository_comments(read_pages, route=COMMENT_FEED, window_size=30_000):
    """Resume GitHub's bounded REST history at the last visible update."""
    window = route
    while True:
        count = 0
        for count, comment in enumerate(islice(read_pages(window), window_size), 1):
            yield comment
        if count < window_size:
            return
        # The since filter uses updated_at with second precision. Re-read the
        # boundary second in case additional comments share the last timestamp.
        end = datetime.fromisoformat(comment['updated_at'].replace('Z', '+00:00'))
        since = (end - timedelta(seconds=1)).isoformat().replace('+00:00', 'Z')
        next_window = f'{route}&since={since}'
        if next_window == window:
            raise RuntimeError(f'Comment pagination did not advance beyond {since}')
        window = next_window


def comments_by_issue(issues, comments):
    numbers = {issue['url']: issue['number'] for issue in issues if issue['comments']}
    grouped = defaultdict(dict)
    if numbers:
        for comment in comments:
            number = numbers.get(comment['issue_url'])
            if number is not None:
                grouped[number][comment['id']] = comment
    return defaultdict(list, {number: list(by_id.values()) for number, by_id in grouped.items()})
