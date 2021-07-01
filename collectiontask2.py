import json
import collections

with open(r'C:\Users\Фёдор\PycharmProjects\dump\RomeoAndJuliet.json', encoding='utf-8') as file:
    shakespeare = json.load(file)
    dict = collections.defaultdict(list)
    for act in shakespeare["acts"]:
        for scene in act["scenes"]:
            for actions in scene["action"]:
                dict[actions["character"]].append(actions["says"])
    print(dict)