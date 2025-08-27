
def floodFill(grid, x, y, old_color, new_color):
    if old_color == new_color: # there won't be any changes
        return grid
    if (x < 0 or x >= len(grid)) or (y < 0 or y >= len(grid[0])): # checks if its beyond the grid
        return
    
    if grid[x][y] == old_color:
        grid[x][y] = new_color

        floodFill(grid, x-1, y, old_color, new_color) # to the left
        floodFill(grid, x+1, y, old_color, new_color) # to the right
        floodFill(grid, x, y+1, old_color, new_color) # to the down
        floodFill(grid, x, y-1, old_color, new_color) # to the left

    return grid




def main():
    grid = [
        [1, 1, 1, 2, 2],
        [1, 1, 0, 2, 0],
        [1, 0, 0, 2, 2],
        [0, 0, 2, 2, 2],
        [0, 2, 2, 1, 1]
    ]
    rows = 0
    column = 0
    old_color = 0
    new_color = 1

    for row in grid:
        print(' '.join(str(cell) for cell in row))
    print()
    
    grid = floodFill(grid, rows, column, old_color, new_color)


    for row in grid:
        print(' '.join(str(cell) for cell in row))
    print()

if __name__ == "__main__":
    main()