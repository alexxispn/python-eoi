yes_answers = ["yes", "y", "sí", "si"]
can_fly = input("¿Puede volar? ").lower() in yes_answers
is_human = input("¿Es humano? ").lower() in yes_answers
has_mask = input("¿Tiene máscara? ").lower() in yes_answers

if can_fly and is_human:
    if has_mask:
        print("es Ironman")
    else:
        print("es Captain Marvel")
elif can_fly and not is_human:
    if has_mask:
        print("es Ronan Accuser")
    else:
        print("es Vision")
elif not can_fly and is_human:
    if has_mask:
        print("es Spiderman")
    else:
        print("es Hulk")
else:
    if has_mask:
        print("es Black Bolt")
    else:
        print("es Thanos")
