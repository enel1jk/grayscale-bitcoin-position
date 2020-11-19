#%%
import json
from datetime import date

with open('candles.json', 'r') as f:
    candles = json.load(f)
    prices = {}
    for k in candles:
        d = date.fromtimestamp(int(k[0])).strftime("%Y%m%d")
        prices[d] = k[4]

with open('aum.csv') as f:
    aum_lines = f.readlines()
with open('aum.csv', 'w') as f:
    for line in aum_lines:
        line = line.strip('\n')
        date = line.split('\t')[0]
        price = prices[date]
        f.write(f"{line}\t{price}\n")
        print(f"{line}\t{price}")
