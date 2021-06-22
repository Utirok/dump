import json
with open(r'C:\Users\Фёдор\PycharmProjects\dump\RomeoAndJuliet.json', encoding='utf-8') as file:
    shakespeare = json.load(file)
    allcharacters = []
    phrases_number = 0
    talkative_character = ''
    for act in shakespeare['acts']:
        for scene in act['scenes']:
            for action in scene['action']:
                allcharacters.append(action['character'])
    for character in allcharacters:
        if allcharacters.count(character) > phrases_number:
            phrases_number = allcharacters.count(character)
            talkative_character = character
print(talkative_character)