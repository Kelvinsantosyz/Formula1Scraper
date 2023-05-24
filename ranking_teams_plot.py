import pandas as pd
import matplotlib.pyplot as plt

ranking = pd.read_csv('ranking_teams.csv', encoding='latin1')

position = ranking['Position'].tolist()
team_name = ranking['Team Name'].tolist()
points = ranking['Points'].tolist()

plt.style.use('seaborn-v0_8-whitegrid')
plt.figure(figsize=(10, 8))
bars = plt.barh(position[::-1], points[::-1])

plt.xlabel('Points', fontsize=12)
plt.title('Ranking Team 2023', fontsize=14)

for i, bar in enumerate(bars):
    plt.text(bar.get_width() + 1, bar.get_y() + bar.get_height() / 2,
             f'{team_name[::-1][i]} {points[::-1][i]}', fontsize=12,
             fontweight='bold',)

for i, bar in enumerate(bars):
    if i % 2 == 0:
        bar.set_facecolor('#eb0707')
    else:
        bar.set_facecolor('#0576f7')

subtitle = ("Position")
plt.text(-0.15, 0.50, subtitle, ha='left', fontsize=13, fontweight='bold',
         transform=plt.gca().transAxes)
plt.xlim(0, 400)
plt.show()
