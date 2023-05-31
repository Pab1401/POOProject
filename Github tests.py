from github import Github
import pandas as pd

g = Github(base_url="organization.github.com", login_or_token="access_token")
repos = g.get_user().get_repo("POOProject")
a = repos.get_contents("Super Smash Bros. Ultimate Patch 13.1 Frame Data.xlsx")
df = pd.read_excel(a)
print(df)