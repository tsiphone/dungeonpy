import numpy as np

rng = np.random.default_rng()
terrain = rng.integers(low=0, high=100, size=100)

map = terrain.reshape(10, 10)

screen = np.full(map.shape, ".", dtype="<U1")
screen[map < 5] = "$"
screen[map >= 75] = "#"

player_y, player_x = 5, 5
screen[player_y, player_x] = "@"

points = 0

def draw():
    print("\n" + "=" * 25)
    print("+" + "---" * 10 + "+")
    for row in screen:
        print("| " + " ".join(row) + " |")
    print("+" + "---" * 10 + "+")
    print(f"Gold levered: {points} | Walls in map: {np.sum(screen == '#')}")
    print(f"Controls: [W] up | [S] down | [A] left | [D] right | [Q] exit")

while True:
    draw()
    action = input("Movement (W/A/S/D + Enter: ").strip().lower()
    if action == "q":
        print("Quitting...")
        break

    new_y, new_x = player_y, player_x

    if action == "w":
        new_y -= 1
    elif action == "s":
        new_y += 1
    elif action == "a":
        new_x -= 1
    elif action == "d":
        new_x += 1
    else:
        print("Forbidden key, use W,A,S or D")
        continue

    if not (0 <= new_y < 10 and 0 <= new_x < 10):
        print("Invalid coordinates")
        continue

    destiny = screen[new_y, new_x]

    if destiny == "#":
        print("There is a wall in your path, cannot pass")
        continue
    if destiny == "$":
        points += 1
        print("Treasure!!!")

    screen[player_y, player_x] = " "
    player_y, player_x = new_y, new_x
    screen[player_y, player_x] = "@"





