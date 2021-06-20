import csv
with open(r"C:\Users\Фёдор\PycharmProjects\dump\stage3_test.csv", 'r', encoding='utf-8') as csv_file:
    with open('stage3_test.csv', 'w', encoding='utf-8') as it:
        dictreader = csv.reader(csv_file)
        dictwriter = csv.writer(it)
        for list in dictreader:
            dictwriter.writerow([list[0], list[2], list[4]])