from os.path import exists
import os
from csv import DictReader, DictWriter


FILENAME = 'log.csv'
FIELDNAMES = ['id', 'address', 'distance']


def read_logs():
    """ Will verify if a file named log.csv exists. If not, will create a log.csv file and write a header with the fieldnames. """

    if not exists(FILENAME) or os.stat(FILENAME).st_size == 0:
        with open(FILENAME, 'w') as f:
            writer = DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()

    logs = []

    with open(FILENAME, 'r') as f:
        reader = DictReader(f)
        for log in reader:
            logs.append(log)

    return logs


def create_id():
    """ Will create a numeric sequence to be used as IDs for the log.csv entries. """

    id_list = []

    logs = read_logs()
    for log in logs:
        id_list.append(int(log['id']))

    return sorted(id_list)[-1] + 1 if id_list != [] else 1


def create_log(log):
    """ Will create add a new log to log.csv. """

    with open(FILENAME, 'a') as f:
        writer = DictWriter(f, fieldnames=FIELDNAMES)
        writer.writerow(log)
