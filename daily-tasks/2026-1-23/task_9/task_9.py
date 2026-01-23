# task 9: Write a Python program to convert a dictionary into a JSON string and save it to a file.

import json

def convert_to_json_and_save(dict, filepath):
    json_data = json.dumps(dict)
    with open(filepath, "w", encoding='utf-8') as f:
        f.write(json_data)


demo_dict = {
    "name": 'aryan bhattarai',
    'age': '22',
    'college': 'kantipur engineering college'
}

convert_to_json_and_save(demo_dict, 'test.json')