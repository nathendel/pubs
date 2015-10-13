import sys
import os
import pandas as pd

data = pd.read_table("phosphosites.tsv")
print data['Positions']


# data = pd.read_cs(FILEPATH)
#cpub_count = open("pub_count")

# for example search term keratin within "Protein Names"
elem = data[data['Protein Names'].str.contains("keratin") == True]
print elem

