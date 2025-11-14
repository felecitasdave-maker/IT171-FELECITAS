dave_x, dave_y = 0, 0
felicitas_x, felicitas_y = 0, 0


treasure_x = 3
treasure_y = 2


game_running = True

print("Welcome to {lastname}'s Maze")
print("Players: Dave and Felicitas")
print("Use 'up', 'down', 'left', 'right' to move, or 'quit' to stop playing.\n")


def move_player(name, x, y):
    move = input(f"{name}'s move (up/down/left/right/quit): ").lower().strip()
    if move == "w":
        y += 1
    elif move == "s":
        y -= 1
    elif move == "a":
        x -= 1
    elif move == "d":
        x += 1
    elif move == "quit":
        print(f"{name} quit the game.")
        return x, y, False
    else:
        print("Invalid input! Use 'up', 'down', 'left', 'right', or 'quit'.")
        return x, y, True
    return x, y, True

while game_running:
    
    dave_x, dave_y, still_playing = move_player("Dave", dave_x, dave_y)
    if not still_playing:
        break
    print(f"Dave's position: ({dave_x}, {dave_y})")

    
    if dave_x == treasure_x and dave_y == treasure_y:
        print("Dave found the treasure! Dave wins!")
        break

   
    felicitas_x, felicitas_y, still_playing = move_player("Felicitas", felicitas_x, felicitas_y)
    if not still_playing:
        break
    print(f"Felicitas's position: ({felicitas_x}, {felicitas_y})")

   
    if felicitas_x == treasure_x and felicitas_y == treasure_y:
        print("Felicitas found the treasure! Felicitas wins!")
        break
