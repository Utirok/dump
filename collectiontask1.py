import json
import collections

with open(r'C:\Users\Фёдор\PycharmProjects\dump\RomeoAndJuliet.json', encoding='utf-8') as file:
    shakespeare = json.load(file)
    list = []
    for act in shakespeare["acts"]:
        for scene in act["scenes"]:
            for actions in scene["action"]:
                for saying in actions["says"]:
                    saying = saying.replace('!', '')
                    saying = saying.replace(':', '')
                    saying = saying.replace('?', '')
                    saying = saying.replace(',', '')
                    saying = saying.replace('-', '')
                    saying = saying.replace(';', '')
                    saying = saying.replace('.', '')
                phrase = saying.split(' ')
                for word in phrase:
                    list.append(word)
    twenty = collections.Counter(list)
    print('most common: \n' + str(twenty.most_common(20)))
    print('least common: \n' + str(twenty.most_common()[-21:-1]))