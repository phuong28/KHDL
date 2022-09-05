
import requests, json
github_user = "phuong28"
endpoint = f"https://api.github.com/users/{github_user}/repos"
repos = json.loads(requests.get(endpoint).text)

from collections import Counter
from dateutil.parser import parse
dates = [parse(repo["created_at"]) for repo in repos]
month_counts = Counter(date.month for date in dates)
weekday_counts = Counter(date.weekday() for date in dates)
last_5_repositories = sorted(repos,key=lambda r: r["pushed_at"],reverse=True)[:5]
last_5_languages = [repo["language"]for repo in last_5_repositories]
print(last_5_languages)
print(last_5_repositories)