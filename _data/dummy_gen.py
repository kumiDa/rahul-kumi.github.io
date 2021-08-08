import os
import json
from faker import Faker

file_name = os.path.abspath("til.json")
fake = Faker()

data = []

for _ in range(10):
    entry = {}
    entry["date"] = fake.date()
    entry["items"] = []
    for _ in range(2):
        item = {}
        item["url"] = fake.url()
        item["title"] = fake.sentence()
        item["tags"] = fake.words()
        entry["items"].append(item)
    data.append(entry)

with open(file_name, 'w') as fp:
    json.dump(data, fp)