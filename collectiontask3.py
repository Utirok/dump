import collections
import json

with open(r'C:\Users\Фёдор\PycharmProjects\dump\RomeoAndJuliet.json', encoding='utf-8') as file:
    shakespeare = json.load(file)
    counter = collections.Counter()
    for act in shakespeare["acts"]:
        for scene in act["scenes"]:
            for actions in scene["action"]:
                counter[actions["character"]] = counter[actions["character"]] + 1
    print(counter)
