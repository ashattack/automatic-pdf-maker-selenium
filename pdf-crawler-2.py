
from selenium import webdriver
import pandas as pd
from tqdm import tqdm

df_parts = pd.read_csv("LIST OF PDF FILENAMES.csv")
df_parts.head()


part_num = df_parts['NAME OF COLUMN']
len(part_num)


len(set(part_num))


part_num[0]


error = []
for part in tqdm(part_num):
    try:
        download_dir = "C: PATH TO SCRAPPED PDF FOLDER" # for linux/*nix, download_dir="/usr/Public"
        options = webdriver.ChromeOptions()

        profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}], # Disable Chrome's PDF Viewer
                       "download.default_directory": download_dir , "download.extensions_to_open": "applications/pdf"}
        options.add_experimental_option("prefs", profile)
        driver = webdriver.Chrome(chrome_options=options)  # Optional argument, if not specified will search path.
        driver.get('WEBSITE WHERE PDFS ARE LOCATED/{}'.format(part))
    except:
        error.append(part)
        pass
    
driver.close();






