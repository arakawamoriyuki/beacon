import os, io, csv, json

from access_points import get_scanner

def fetch_datasets(label='default place', size=1):
    X = []
    y = []
    wifi_scanner = get_scanner()
    for index in range(int(size)):
        print('scan ' + str(index+1) + ' access point')
        access_points = wifi_scanner.get_access_points()
        X.append({' '.join([ap.ssid, ap.bssid]): ap.quality for ap in access_points })
        y.append(label)
    return X, y

def save_datasets(X, y, path='datasets/datasets.csv'):
    dir_name = os.path.dirname(os.path.abspath(path))
    if not os.path.exists(dir_name): os.mkdir(dir_name)
    csv_writer = csv.writer(
        io.open(path, 'a', encoding='utf-8'),
        delimiter='\t'
    )
    for Xi, yi in zip(X, y):
        csv_writer.writerow([yi, json.dumps(Xi)])

def load_datasets(path='datasets/datasets.csv'):
    csv_reader = csv.reader(
        io.open(path, 'r', encoding='utf-8'),
        delimiter='\t'
    )
    X = []
    y = []
    for line in csv_reader:
        y.append(line[0])
        X.append(json.loads(line[1]))
    return X, y









#
