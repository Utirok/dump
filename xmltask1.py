import xml.etree.ElementTree as tree
with open(r'C:\Users\Фёдор\PycharmProjects\dump\annot.opcorpora.no_ambig.xml', encoding='utf-8') as corp:
    with open('sentences_list.txt', 'w', encoding='utf-8') as new_one:
        tree = tree.parse(corp)
        root = tree.getroot()
        for it in root.iter('source'):
            new_one.write(it.text + '\n')