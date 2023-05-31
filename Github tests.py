from github import Github
import pandas as pd
from io import StringIO
from io import BytesIO
import urllib.request
#import pandas as pd  

import os
#import pandas as pd

#gets your current directory
dirname = os.path.dirname(__file__)

#concatenates your current directory with your desired subdirectory
results = os.path.join(dirname, r'Super Smash Bros. Ultimate Patch 13.1 Frame Data.xlsx')

#reads the excel file in a dataframe
df = pd.read_excel(results)

print(df)