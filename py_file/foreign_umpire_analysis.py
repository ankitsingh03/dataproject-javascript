import csv
from collections import defaultdict
import json


def data_collection():
    '''
    collect all the data, country and number \
    of umpire over the history of IPL.
    '''
    umpire_count = defaultdict(int)
    with open('umpire_data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_reader.__next__()
        for line in csv_reader:
            if line[1] == "India":
                continue
            umpire_count[line[1]] += 1

    return umpire_count


if __name__ == "__main__":
    data = data_collection()
    sort_data = {k: v for k, v in sorted(data.items(),
                 key=lambda item: item[1], reverse=True)
                 }
    with open(
        "../assets/foreign_umpire_analysis.json", "w"
              ) as outfile:
        json.dump(sort_data, outfile)
