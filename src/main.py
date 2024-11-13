import pandas as pd
import json
from scrape import scrape_and_parse
from scoring import find_top_10_events

input_path = 'src/input_json.json'

with open(input_path) as f:
    data = json.load(f)
json_str = json.dumps(data)
df = pd.json_normalize(data)


events = scrape_and_parse(df.at[0, 'industry'])


top_10_list = find_top_10_events(request=json_str, list=events)
with open('output.json', 'w') as f:
    json.dump(top_10_list, f, indent=4)