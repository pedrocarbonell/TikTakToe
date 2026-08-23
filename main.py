
grid = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]


# First lets print the grid

def print_grid(grid):
    for row in grid:
        for i, col in enumerate(row):
            if i < 2:
                print(col, end=" | ")
            else:
                print(col)

print_grid(grid)
# Lets check if there's a winner

def winner_check(grid):
    # Horizontal check
    for row in grid:
        x = 0
        o = 0
        for col in row:
            if col == "X":
                x += 1
            if col == "O":
                o += 1
        if x == 3:
            return "X"
        if o == 3:
            return "O"
    # Vertical Check
    vertical_grid = list(zip(*grid))

    for row in vertical_grid:
        x = 0
        o = 0
        for col in row:
            if col == "X":
                x += 1
            if col == "O":
                o += 1
        if x == 3:
            return "X"
        if o == 3:
            return "O"

    # Diagonal Check
    if grid[0][0] == grid[1][1] == grid[2][2] != " ":
        return grid[0][0]
    elif grid[0][2] == grid[1][1] == grid[2][0] != " ":
        return grid[0][2]
    else:
        return None

def play_game():
    while True:
        # X plays
        player_turn("X")
        if winner_check(grid) == "X":
            print("X Wins")
            return

        player_turn("O")
        if winner_check(grid) == "O":
            print("O Wins")
            return

def player_turn(player: str):
    while True:
        X_row = int(input(f"{player} di tu fila: "))
        X_column = int(input(f"{player} di tu columna: "))
        if X_row > 2 or X_column >2:
            print("Select values between 0 and 2")
            continue
        if grid[X_row][X_column] == " ":
            grid[X_row][X_column] = player
            print_grid(grid)
            return False
        else:
            print("Cell already played, play again")
            return True

play_game()




