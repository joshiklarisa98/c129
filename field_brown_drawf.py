#import required modules
from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium import webdriver
import requests

#Make a page request using the request module.
url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(url)

#Get all the tables of the page using find_all() method
tables = soup.find_all("table")

#Create an empty list
stars = []

#Get all the <tr> tags from the table
tr_tags = table_body.find_all('tr')

# For loop to take out all the <td> tags
for tr in tr_tags:
        td_tags = tr.find_all('td')
        
        # Keep all the <td> rows in the empty list made earlier
        if len(td_tags) > 0:
            stars.append([td.text.strip() for td in td_tags])
    
# Convert list into Pandas DataFrame
 df = pd.DataFrame(stars)
    
# Save into CSV
df.to_csv("stars_data.csv", index=False)



import pandas as pd

# Load the csv file of brown dwarf stars
brown_dwarf_stars = pd.read_csv("brown_dwarf_stars.csv")

# Clean the data by deleting NAN values
brown_dwarf_stars.dropna(inplace=True)

# Convert the Mass and radius column to the floating point values
brown_dwarf_stars['Mass'] = brown_dwarf_stars['Mass'].astype(float)
brown_dwarf_stars['Radius'] = brown_dwarf_stars['Radius'].astype(float)

# Multiply each value in the radius column with 0.102763 to convert to solar radius
brown_dwarf_stars['Radius'] = brown_dwarf_stars['Radius'] * 0.102763

# Multiply each value in the mass column with 0.000954588 to convert to solar mass
brown_dwarf_stars['Mass'] = brown_dwarf_stars['Mass'] * 0.000954588

# Make a new csv file
brown_dwarf_stars.to_csv("cleaned_brown_dwarf_stars.csv", index=False)

# Merge this csv file with the csv file of brightest stars
# Assuming the csv file of brightest stars is named 'brightest_stars.csv'
brightest_stars = pd.read_csv("brightest_stars.csv")
merged_data = pd.concat([brightest_stars, brown_dwarf_stars], ignore_index=True)

# Save the merged data to a new csv file
merged_data.to_csv("merged_stars_data.csv", index=False)