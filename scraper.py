# Importing libraries.

import pandas as pd
import requests
from datetime import datetime
import bs4 as bs
from tqdm import tqdm

print('--Starting Fresquito Scraper--\n')

df = pd.read_csv('AEMET.csv')

hour = datetime.now().hour

id_list = df['id'].tolist()


def scraper():
    # Scraping all links and holding the data as a list of dictionaries.
    meteo = []

    def fetch_links(n: str, session: requests.Session):
        now_hour = datetime.now().hour
        try:
            page = 'https://www.aemet.es/xml/municipios_h/localidad_h_' + str(n) + '.xml'
            url_link = session.get(page)
            print('--Scraping ' + page + ' --')

            # Parsing the xml:
            file = bs.BeautifulSoup(url_link.text, features="lxml")
            c = str(file.contents[1].extract()).split('>\n<')

            # Holding the rows that contain either a date or temperature:
            temps = [item for item in c if 'temperatura' in item or 'dia fecha' in item]

            # Creating one dict for each entry:
            for p in temps:
                if 'dia' in p:
                    day = p.split('dia fecha="')[1].split('" ocaso')[0]
                else:
                    hour = p.split('temperatura periodo="')[1].split('">')[0]
                    temp = p.split('</temperatura')[0].split('">')[1]
                    temp_dict = {'id': n, 'day': day, 'hour': hour, 'temp': temp}
                    meteo.append(temp_dict)
        except:
            pass

    # Applying the scraper function to every link:
    with requests.Session() as session:
        for link_n in tqdm(id_list):
            fetch_links(link_n, session)

    # Storing the result as a dataframe, merging it with the original and saving:
    meteo_data = pd.merge(df, pd.DataFrame(meteo), on=['id'])
    meteo_data.to_csv('meteo_data.csv', index=False)


scraper()

print('--Process finished--')
