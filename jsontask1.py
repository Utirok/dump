import json
with open('dictionary_new.json', 'w') as to_write:
    with open(r'C:\Users\Фёдор\PycharmProjects\dump\wikidata_1000.json', encoding='utf-8') as file:
        dictionary = dict()
        for str in file:
            data = json.loads(str)
            try:
                dictionary[data["label"]["value"]] = data["description"]["value"]
            except KeyError:
                dictionary[data['label']["value"]] = None
    json.dump(dictionary, to_write, ensure_ascii=False, indent=4)