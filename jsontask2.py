import json
with open('romeo_dictionary.json', 'w') as new_one:
    with open(r'C:\Users\Фёдор\PycharmProjects\dump\RomeoAndJuliet.json', encoding='utf-8') as file:
        shakespeare = json.load(file)
        for act in shakespeare['acts']:
            for scene in act['scenes']:
                allcharacters = set()
                for characters in scene['action']:
                    allcharacters.add(characters['character'])
                new_one.write(json.dumps(list(allcharacters), ensure_ascii=False))
                new_one.write('\n')