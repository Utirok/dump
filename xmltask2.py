import xml.etree.ElementTree as tree
tree = tree.parse(r'C:\Users\Фёдор\PycharmProjects\dump\annot.opcorpora.no_ambig.xml')
root = tree.getroot()
with open('plural_nouns.txt', 'w', encoding='utf-8') as new_one:
    for it in root.iter('token'):
        dump = []
        for teg_g in it.iter('g'):
            dump.append(teg_g.get('v'))
        if 'NOUN' in dump:
            if 'plur' in dump:
                new_one.write(it.get('text') + '\n')