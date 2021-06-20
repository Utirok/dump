import csv

with open(r"C:\Users\Фёдор\PycharmProjects\dump\stage3_test.csv", 'r', encoding='utf-8') as csv_file:
    with open('stage3_test', 'w', encoding='utf-8') as to_write:
        dictreader = csv.DictReader(csv_file)
        dictwriter = csv.DictWriter(to_write, fieldnames=dictreader.fieldnames)
        dictwriter.writeheader()
        for list in dictreader:
            if list['Images'].count(',') >= 2:
                dictwriter.writerow(list)