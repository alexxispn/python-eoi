def valid_number(lim_inferior: int = 2, lim_superior: int = 5) -> bool:
    entry = int(input("Introduce un número: "))
    return lim_inferior <= entry <= lim_superior


print(valid_number(0, 100))
