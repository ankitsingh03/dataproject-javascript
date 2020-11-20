import csv
import json


def data_collection():
    '''
    Collect all the data, team name and total runs over the history of IPL.
    '''
    teams_runs = {}

    # open the csv file and clean data
    with open('deliveries.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_reader.__next__()

        for line in csv_reader:
            team_name = line[2]
            runs = int(line[-4])
            teams_runs[team_name] = teams_runs.get(team_name, 0) + runs

    return teams_runs


if __name__ == "__main__":
    data = data_collection()
    sort_data = {k: v for k, v in sorted(data.items(),
                 key=lambda item: item[1], reverse=True)
                 }
    with open("../assets/total_runs_scored_by_team.json", "w") as outfile:
        json.dump(sort_data, outfile)
