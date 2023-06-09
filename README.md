
# Formula 1 Rankings and Teams Information
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This Python script allows you to scrape and retrieve Formula 1 rankings and teams information from specific websites. The script uses the BeautifulSoup library to parse HTML content and the requests library to make HTTP requests. The retrieved data is then stored in CSV files.

## Prerequisites

To run this script, make sure you have the following installed:

- Python 3
- `pip` package manager

You also need to install the required Python libraries by running the following command:

```
pip install beautifulsoup4 pandas matplotlib
```

## Usage

1. Clone the repository or download the Python script.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Run the script using the following command:

   ```
   python formula1.py
   ```

4. The script will scrape the data from the specified websites and store it in three separate CSV files:

   - `ranking_drivers.csv`: Contains the rankings of Formula 1 drivers, including their position, name, team, and points.
   - `ranking_teams.csv`: Contains the rankings of Formula 1 teams, including their position, name, and points.
   - `team_data.csv`: Contains additional information about Formula 1 teams, including the team boss, car, and engine.

5. After running the script, you can generate additional plots using the following commands:

   - **Teams by Engine Pie Chart**:
     ```
     python teams_by_engine.py
     ```
     ![Engines](https://github.com/Kelvinsantosyz/Formula1Scraper/assets/109118257/562a5359-806c-4dc3-95fb-e58c69223469)

     

     This will generate a pie chart showing the distribution of Formula 1 teams by engine used. The chart will be displayed on the screen.

   - **Ranking of Teams Bar Chart**:
     ```
     python ranking_teams_plot.py
     ```
     ![Ranking](https://github.com/Kelvinsantosyz/Formula1Scraper/assets/109118257/5b6affe0-ae3e-49c3-a757-8d9aab1de511)


     This will generate a horizontal bar chart showing the ranking of Formula 1 teams based on points. The chart will be displayed on the screen.

   - **Ranking of Drivers Bar Chart**:
     ```
     python ranking_drivers_plot.py
     ```
      ![Drivers](https://github.com/Kelvinsantosyz/Formula1Scraper/assets/109118257/38dbd968-4005-4ad2-9cc3-0ea493dffa9c)

     This will generate a horizontal bar chart showing the ranking of Formula 1 drivers based on points. The chart will be displayed on the screen.

Note: Make sure you have the necessary CSV files generated by running the main script (`formula1.py`) before generating the additional plots.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- This script was created using the BeautifulSoup, pandas, and matplotlib libraries for web scraping, data manipulation, and data visualization.
- The script was inspired by the need to retrieve Formula 1 rankings and teams information from specific websites.

Feel free to customize the README to include any additional information or instructions specific to your use case.
