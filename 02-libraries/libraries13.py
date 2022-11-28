import os

import arrow

for fn in os.listdir():
    print(fn, arrow.get(os.path.getmtime(fn)).humanize())



