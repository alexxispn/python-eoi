import os
from datetime import datetime
from hashlib import md5

entry = "Perdón imposible, ejecutar prisionero"


# def hash_md5(text):
#     return f'text: {text} - hash: {md5(text.encode()).hexdigest()}'

def get_hash(file):
    with open(file, "rb") as f:
        m = md5(f.read())
        return m.hexdigest()


for fn in os.listdir():
    if os.path.isfile(fn):
        size = os.path.getsize(fn)
        hash_md5 = get_hash(fn)
        last_mod = datetime.fromtimestamp(os.path.getmtime(fn))
        print(f"{fn:<28} {size:>14} {last_mod.ctime():24} {hash_md5:<32}")
