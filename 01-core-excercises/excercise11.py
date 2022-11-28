player_one = input("Jugador uno. Escribe piedra, papel o tijeras: ").lower()
player_two = input("Jugador dos. Escribe piedra, papel o tijeras: ").lower()
paper = ["papel", "paper", 1]
rock = ["piedra", "rock", 2]
scissors = ["tijeras", "scissors", 3]
options_allowed = paper + rock + scissors

if (player_one in options_allowed) and (player_two in options_allowed):
    if player_one == player_two:
        print("Empate")
    elif (player_one in paper) and (player_two in rock) or \
            (player_one in rock) and (player_two in scissors) or \
            (player_one in scissors) and (player_two in paper):
        print("Gana jugador uno")
    else:
        print("Gana jugador dos")
else:
    print("Alguna de las opciones no es válida")
