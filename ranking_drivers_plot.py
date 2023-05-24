import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('ranking_drivers.csv', encoding='latin1')

positions = data['Position'].tolist()
driver_names = data['Driver Name'].tolist()
points = data['Points'].tolist()

plt.style.use('seaborn-v0_8-whitegrid')
plt.figure(figsize=(10, 8)) 
bars = plt.barh(positions[::-1], points[::-1])

plt.xlabel('Points', fontsize=12)
plt.title('Ranking of Drivers 2023', fontsize=14)

for i, bar in enumerate(bars):
    plt.text(bar.get_width() + 2, bar.get_y() + bar.get_height() / 2,
             f'{driver_names[::-1][i]} {points[::-1][i]}', fontsize=12)

for i, bar in enumerate(bars):
    if i % 2 == 0:
        bar.set_facecolor('#eb0707')
    else:
        bar.set_facecolor('#0576f7')

subtitle = ("Position")
plt.text(-0.15, 0.50, subtitle, ha='left', fontsize=13, transform=plt.gca().transAxes)
plt.tight_layout()
plt.xlim(0, 220)
plt.show()
