import csv
from collections import defaultdict
import json


def data_collection():
    '''
    collect all the data, batsman name and total runs over the history of IPL.
    '''

    top_batsman = defaultdict(int)
    # open the csv file and clean data
    with open('deliveries.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_reader.__next__()
        for line in csv_reader:
            name = line[6]
            run = int(line[-6])
            top_batsman[name] += int(run)

    return top_batsman


if __name__ == "__main__":
    data = data_collection()
    sort_data = {k: v for k, v in sorted(data.items(),
                 key=lambda item: item[1], reverse=True)[:10]
                 }
    with open(
        "../assets/top_batsman_for_royal_challengers_bangalore.json", "w"
              ) as outfile:
        json.dump(sort_data, outfile)
