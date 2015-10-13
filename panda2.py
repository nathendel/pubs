import sys
import os
import pandas as pd

data = pd.read_table("phosphosites.tsv")
print data['Positions']
