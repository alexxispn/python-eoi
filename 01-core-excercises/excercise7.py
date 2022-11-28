entry = input("Introduce una entrada: ") or "//1.1.1.1/eoi/python/hola"
entry = entry.lstrip('/')
entry = entry.split('/')
equipo = entry[0]
ruta = '/'.join(entry[1:])
print(f"{equipo=}; {ruta=}")

