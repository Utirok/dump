import csv
with open(r"C:\Users\Фёдор\PycharmProjects\dump\stage3_test.csv", 'r', encoding='utf-8') as csv_file:
    with open('stage3_test.csv', 'w', encoding='utf-8') as to_write:
        dictreader = csv.reader(csv_file)
        dictwriter = csv.writer(to_write)
        for row in dictreader:
            if row[4] == 'Price':
                dictwriter.writerow(row)
            else:
                if 10000 <= float(row[4]) <= 50000:
                    dictwriter.writerow(row)