import os
from datetime import datetime

for filename in os.listdir():
    ts_modification = os.path.getmtime(filename)
    file_modification = datetime.fromtimestamp(ts_modification)
    now = datetime.now()
    ts_difference = now - file_modification
    is_recent = ts_difference.days < 1
    print(f'{filename} was modified {ts_difference.days} days ago and'
          f' is {"recent" if is_recent else "old"}')
