from pathlib import Path
import xlwings as xw
import requests
from bs4 import BeautifulSoup
import pandas as pd




years = range(1991,2022)

for year in years:
       url = f'https://www.basketball-reference.com/leagues/NBA_{year}_per_game.html'

       r = requests.get(url)

       soup = BeautifulSoup(r.content, 'lxml')

       header = [th.getText() for th in soup.find_all('tr')[0].find_all('th')]
       header = header[1:]
       rows = soup.find_all('tr')[1:]

       player_stats = [[td.getText() for td in rows[i].find_all('td')] for i in range(len(rows))]

       stats = pd.DataFrame(player_stats, columns=header)

       stats[['MP','FG','FGA','FG%','3P','3PA','3P%','2P','2PA','2P%','eFG%','FT','FTA','FT%','ORB','DRB','TRB','AST','STL','BLK','TOV','PF','PTS']] = stats[['MP','FG','FGA','FG%','3P','3PA','3P%','2P','2PA','2P%','eFG%','FT','FTA','FT%','ORB','DRB','TRB','AST','STL','BLK','TOV','PF','PTS']].apply(pd.to_numeric)
       stats = stats.sort_values('PTS', ascending=False).head(10)
       stats.to_excel(f'C:\\Users\\nickc\\Documents\\nba_stats\\{year}_nba_stats.xlsx')


source_dir = 'C:\\Users\\nickc\\Documents\\nba_stats'

excel_files = list(Path(source_dir).glob('*.xlsx'))
combined_wb = xw.Book()

for excel_file in excel_files:
       wb = xw.Book(excel_file)
       for sheet in wb.sheets:
              sheet.api.Copy(After=combined_wb.sheets[0].api)
       wb.close()

combined_wb.sheets[0].delete()
combined_wb.save(f'C:\\Users\\nickc\\Documents\\nba_stats\\all_nba_stats.xlsx')

# workbook = writer.book
# worksheet = writer.sheets['sheet 1']
# chart = workbook.add_chart({'type':'bar'})

# data = [stats['PTS']]

# writer = pd.ExcelWriter('C:\\Users\\nickc\\Documents\\nba_stats\\2022_nba_stats.xlsx', engine='xlsxwriter')

# pd.DataFrame.to_excel(stats, "C:\\Users\\nickc\\Documents\\nba_stats\\2022_nba_stats.xlsx")

# with open('C:\\Users\\nickc\\Documents\\nba_stats\\2022_nba_stats.csv') as csv_file:
#          csv_reader = csv.DictReader(csv_file)
#          players = []
#          points = []
#          for row in csv_reader:
#                 players.append(row['Player'])
#                 points.append(row['PTS'])

# plt.barh(players, points)

# plt.title('Players by most points')
# plt.ylabel('players')
# plt.xlabel('points')
# plt.tight_layout()
# plt.savefig('C:\\Users\\nickc\\Documents\\nba_stats\\top_10_ppg.png')

# read_file = pd.read_csv('C:\\Users\\nickc\\Documents\\nba_stats\\2022_nba_stats.csv')
# read_file.to_excel('C:\\Users\\nickc\\Documents\\nba_stats\\2022_nba_stats.xlsx', index= None, header=True)
