import xml.etree.ElementTree as tree
tree = tree.parse(r'C:\Users\Фёдор\PycharmProjects\dump\annot.opcorpora.no_ambig.xml')
root = tree.getroot()
conjunction = 0
verb = 0
for it in root.iter('token'):
    if it.get('text') == 'может':
        dump = []
        for teg_g in it.iter('g'):
            dump.append(teg_g.get('v'))
        if "VERB" in dump:
            verb = verb + 1
        elif "CONJ" in dump:
            conjunction = conjunction + 1
print(verb, conjunction)