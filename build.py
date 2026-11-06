#!/usr/bin/env python3
"""Update the embedded dataset without external dependencies."""
import json
from pathlib import Path
root = Path(__file__).resolve().parent
path = root / 'index.html'
html = path.read_text()
start = '<script id="homework-data" type="application/json">'
a = html.index(start) + len(start)
b = html.index('</script>', a)
data = json.loads((root / 'data.json').read_text())
path.write_text(html[:a] + json.dumps(data, ensure_ascii=False).replace('</', '<\\/') + html[b:])
print('index.html actualizado')
