import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

data = pd.read_csv('team_data.csv', encoding='latin1')

filtered_teams = data[data['Team'].notna()]
filtered_team_bosses = data[data['Team Boss'].notna()]
filtered_cars = data[data['Car'].notna()]
filtered_engines = data[data['Engine'].notna()]

filtered_teams.reset_index(drop=True, inplace=True)
filtered_team_bosses.reset_index(drop=True, inplace=True)
filtered_cars.reset_index(drop=True, inplace=True)
filtered_engines.reset_index(drop=True, inplace=True)

team_df = pd.DataFrame(filtered_teams['Team'], columns=['Team'])
team_boss_df = pd.DataFrame(filtered_team_bosses['Team Boss'], columns=['Team Boss'])
car_df = pd.DataFrame(filtered_cars['Car'], columns=['Car'])

engine = filtered_engines['Engine'].str.strip().str.lower().str.replace('motor', '')
engine_df = pd.DataFrame(engine, columns=['Engine'])

merged_data = pd.concat([team_df, team_boss_df, car_df, engine_df], axis=1)

merged_data['Engine'] = merged_data['Engine'].str.replace('\s+', ' ', regex=True)
merged_data['Engine'] = merged_data['Engine'].apply(lambda x: x.title())  

teams_by_engine = merged_data.groupby('Engine')['Team'].apply(','.join).reset_index()
teams_by_engine.columns = ['Engine', 'Teams']
engine_counts = merged_data['Engine'].value_counts()

engine_labels = engine_counts.index
engine_counts = engine_counts.values

print(teams_by_engine)

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
plt.figure(figsize=(10, 6))

legend_patches = [mpatches.Patch(color=color, label=f'{engine}: {teams}')
                  for engine, teams, color in zip(teams_by_engine['Engine'], teams_by_engine['Teams'], colors)]

plt.legend(handles=legend_patches, loc='center left', bbox_to_anchor=(0.75, 1))
plt.pie(engine_counts, labels=engine_labels, autopct='%.0f%%', colors=colors, startangle=360)

plt.title("Engines used by teams 2023", fontsize=16, pad=20) 
plt.axis('equal')

plt.show()
