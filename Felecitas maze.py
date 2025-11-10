# Maze Game
# Author: Felecitas
# Date: November 2025
# Description: Simple text-based maze game for Git branching project.

print("=== Maze Game Instructions ===")
print("W - move up")
print("A - move left")
print("S - move down")
print("D - move right")
print("===============================")

print("Welcome to Felecitas’s Maze!\n")

maze = [
    ["#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#"],
    ["#", " ", "#", "E", " ", " ", "#"],
    ["#", " ", " ", " ", "#", " ", "#"],
    ["#", "S", "#", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#"]
]

player_row, player_col = 5, 1

def display_maze():
    for r in range(len(maze)):
        for c in range(len(maze[r])):
            if r == player_row and c == player_col:
                print("P", end=" ")
            else:
                print(maze[r][c], end=" ")
        print()
    print()

while True:
    display_maze()
    move = input("Enter your move (W/A/S/D): ").strip().upper()

    if move not in ["W", "A", "S", "D"]:
        print("Invalid move! Please use W, A, S, or D.\n")
        continue

    new_row, new_col = player_row, player_col

    if move == "W":
        new_row -= 1
    elif move == "S":
        new_row += 1
    elif move == "A":
        new_col -= 1
    elif move == "D":
        new_col += 1

    if maze[new_row][new_col] == "#":
        print("You hit a wall. Try a different direction.\n")
    elif maze[new_row][new_col] == "E":
        print("Congratulations! You reached the exit of Felecitas’s Maze.")
        break
    else:
        player_row, player_col = new_row, new_col
