#!/Users/wakita/.venvs/web/bin/python3

import json
from pathlib import Path
import re

import pandas as pd

ROOT = Path(__file__).parent.parent
GSHEETS = sorted(ROOT.joinpath('etc').glob('y*.xlsx'))

def convert():
  years = {}
  for path in GSHEETS:
    year = path.name[1:-5]
    book = pd.read_excel(path, sheet_name=None)
    tables = {}
    for title, sheet in book.items():
      tables[title] = json.loads(sheet.to_json(orient='records', force_ascii=False))
    years[year] = tables
  with open(ROOT.joinpath('_data', 'classes.json'), 'w') as classes_json:
    json.dump(years, classes_json, ensure_ascii=False, indent=2)

if __name__ == '__main__':
  convert()

# vi: ft=python sw=2
