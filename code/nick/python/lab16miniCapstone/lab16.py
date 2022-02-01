from openpyxl.styles import fonts
from openpyxl.chart import Reference, BarChart
from openpyxl import load_workbook
import requests
from bs4 import BeautifulSoup
import pandas as pd
import glob




years = range(1991,2022)

for year in years:
    url = f'https://www.basketball-reference.com/leagues/NBA_{year}_per_game.html'

    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')

    table_header = [th.getText() for th in soup.find_all('tr')[0].find_all('th')]

    header = table_header[1:]

    rows = soup.find_all('tr')[1:]
    player_stats = [[td.getText()for td in rows[i].find_all('td')] for i in range(len(rows))]

    stats = pd.DataFrame(player_stats, columns=header)
    stats.dtypes
    stats[['MP','FG','FGA','FG%','3P','3PA','3P%','2P','2PA','2P%','eFG%','FT','FTA','FT%','ORB','DRB','TRB','AST','STL','BLK','TOV','PF','PTS']]=stats[['MP','FG','FGA','FG%','3P','3PA','3P%','2P','2PA','2P%','eFG%','FT','FTA','FT%','ORB','DRB','TRB','AST','STL','BLK','TOV','PF','PTS']].apply(pd.to_numeric)
        # print(stats.head(10))
        # stats['MP'] = pd.to_numeric(stats['MP'], downcast='float')
        # print(stats.sort_values('MP', ascending=False).head(5))
    stats.sort_values('PTS', ascending=False).head(25).to_excel(f"C:\\Users\\nickc\\Documents\\nba_stats\\nba_stats_{year}.xlsx", index=False)


############################################################################


# source_data = 'C:\\Users\\nickc\\Documents\\nba_stats'

# stat_files = list(Path(source_data).glob('*.xlsx'))

# combined_wb = xw.Book()
# for stat_file in stat_files:
#     wb = xw.Book(stat_file)
#     for sheet in wb.sheets:
#         sheet.api.Copy(After=combined_wb.sheets[0].api)
#     wb.close()

# combined_wb.sheets[0].delete()
# combined_wb.save('C:\\Users\\nickc\\Documents\\nba_stats\\all_nba_stats.xlsx')

file_path = 'C:\\Users\\nickc\\Documents\\nba_stats\\*.xlsx'

files = glob.glob(file_path)

df = pd.DataFrame()
for file in files:
    tempdf = pd.read_excel(file)
    df= df.append(tempdf, ignore_index=True)

print(df)

pivot = pd.pivot_table