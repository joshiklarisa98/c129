#import required modules
from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium import webdriver

#create an empty list to store scraped data
data = []

#define scrape() method to scrape all column data
def scrape():
    url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
    driver = webdriver.Chrome(executable_path="/path/to/chromedriver") #specify the path to chromedriver
    driver.get(url)
    time.sleep(5) #give time for page to load

# Find <table>
bright_star_table = soup.find("table", attrs={"class", "wikitable"})

# Find <tbody>
table_body = bright_star_table.find('tbody')

# Find <tr>
table_rows = table_body.find_all('tr')

# Get data from <td>
for row in table_rows:
    table_cols = row.find_all('td')
    print(table_cols)

    for col_data in table_cols:
        # Print Only colums textual data using ".text" property
        print(col_data.text)

        #Remove Extra white spaces using strip() method
        temp_list = []
        data = col_data.text.strip()
        print(data)

       temp_list.append(data)
       # Append data to star data list
      data.append(temp_list)

    #save data to CSV
    stars_data = []

    for i in range(0,len(data)):
        star_name = data[i][1]
        distance = data[i][3]
        mass = data[i][5]
        radius = data[i][6]
        luminosity = data[i][7]
        stars_data.append([star_name, distance, mass, radius, luminosity])

# Define Header
headers = ['star_name', 'Distance', 'Mass', 'Radius', 'Luminosity']

# Define pandas DataFrame
star_df_1 = pd.DataFrame(stars_data, columns=headers)

#Convert to cSV
star_df_1.to_csv('scraped_data.csv',index=True, index_label="id")

#call the scrape() method to initiate scraping
scrape()