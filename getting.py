import csv
import requests
from bs4 import BeautifulSoup

class GetURL:
    def __init__(self, url):
        self.url = url
        self.page = requests.get(url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")


class RankingDrivers(GetURL):
    def __init__(self, url):
        super().__init__(url)

    def get_ranking_data(self):
        ranking_table = self.soup.select('div.pilots.col-lg-8.col-md-8.col-sm-8.col-xs-8')
        rows = ranking_table[0].find_all("div", class_="calc-height")

        with open('ranking_drivers.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Position', 'Driver Name', 'Team Name', 'Points'])

            for row in rows:
                driver_entries = row.select('ul')
                drivers = driver_entries[0].find_all("li", class_="one_row")

                for driver in drivers:
                    position = driver.find("span", class_='position').text
                    driver_name = driver.find("p", class_='pilot_name').text
                    team_name = driver.find("sub", class_='team').text
                    points = driver.find("strong").text

                    writer.writerow([position, driver_name, team_name, points])


class RankingTeams(GetURL):
    def __init__(self, url):
        super().__init__(url)

    def get_ranking_teams(self):
        ranking_table = self.soup.select('div.teams.col-lg-8.col-md-8.col-sm-8.col-xs-8')
        rows = ranking_table[0].find_all("div", class_="calc-height")

        with open('ranking_teams.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Position', 'Team Name', 'Points'])

            for row in rows:
                team_entries = row.select('ul')
                teams = team_entries[0].find_all("li", class_="two_row")

                for team in teams:
                    position = team.find("span", class_='position').text
                    team_name = team.find("p", class_='team_name').text
                    points = team.find("strong").text

                    writer.writerow([position, team_name, points])


class TeamsInfo(GetURL):
    def __init__(self, url):
        super().__init__(url)

    def get_team_data(self):
        content_wrapper = self.soup.find("div", class_="article__content-wrapper")
        body = content_wrapper.find("div", class_="article__content--body article__content--internal")
        rows = body.find_all("ul")
        test = body.find_all('strong')
        results = []

        with open('team_data.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Team', 'Team Boss', 'Car', 'Engine'])

            for element in test:
                if element is not None:
                    team_element = element.get_text().strip()
                    team = team_element.split("Equipe: ")[-1]

                    if team != "Fórmula 1":
                        data = {'Team': team}
                        results.append(data)
                        writer.writerow([team, "", "", ""])

            for row in rows:
                boss_elements = row.find_all("li", class_='text')
                data = {}

                for boss in boss_elements:
                    content = boss.text
                    if "Chefe de equipe:" in content:
                        team_boss = content.replace("Chefe de equipe:", "").strip()
                        data["Team Boss"] = team_boss
                    elif "Carro:" in content:
                        car = content.replace("Carro:", "").strip()
                        data["Car"] = car
                    elif "Motor:" in content:
                        engine = content.replace("Motor:", "").strip()
                        data["Engine"] = engine

                if data:
                    results.append(data)
                    writer.writerow([data.get("Team", ""), data.get("Team Boss", ""), data.get("Car", ""), data.get("Engine", "")])
                            
        return results


if __name__ == "__main__":
    drivers_ranking = RankingDrivers("https://www.uol.com.br/esporte/f1/classificacao/")
    drivers_ranking.get_ranking_data()
    
    team_ranking = RankingTeams("https://www.uol.com.br/esporte/f1/classificacao/")
    team_ranking.get_ranking_teams()

    teams_info = TeamsInfo("https://www.terra.com.br/esportes/automobilismo/formula1/formula-1-pilotos-e-equipes-do-grid-para-2023,57fb3af3c2cd95537c7c9fbb385d6d364j1pxnjm.html")
    team_data = teams_info.get_team_data()
