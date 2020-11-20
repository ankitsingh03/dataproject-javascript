import csv
from collections import defaultdict
import json


def data_collection():
    """
    collect all the data according to this form \
    {season: {team: number of matches played in one season}} \
    and list of teams
    """
    season = defaultdict(list)
    teams = set()
    with open('matches.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_reader.__next__()
        # creating dict {season: list of teams name}
        for line in csv_reader:
            season[line[1]].extend([line[4], line[5]])
            teams.update({line[4], line[5]})

    # creating dict {season: {team: number of matches played in one season}}
    total = {}
    for p, q in season.items():
        for i in q:
            total[p] = {i: q.count(i) for i in q}

    # return total, list(teams)
    year = sorted(total.keys())

    # firmation dict {team_name: [data over the year]}
    team_data = defaultdict(list)
    for i in teams:
        for j in year:
            team_data[i].append(total[j].get(i, 0))

    return {'years': year,
            'team_data':
            [{'name': i, 'data': j} for i, j in team_data.items()]
            }


if __name__ == "__main__":
    data = data_collection()
    with open(
        "../assets/stacked_chart_of_matches_played_by_team_by_season.json", "w"
              ) as outfile:
        json.dump(data, outfile)
