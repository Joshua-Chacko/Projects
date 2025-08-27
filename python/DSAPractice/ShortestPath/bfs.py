# parse the maze.txt file to get the grid
# parse the maze.txt file to create paths that check if its walkable or not

def print_grid(filename):
    with open(filename, 'r') as file:
        for line in file:
            clean_line = line.rstrip('\n')
            print(clean_line)

def parse_ascii_maze(filename):
    bool_grid = []
    with open(filename, 'r') as file:
        char_map = {'#': 1, ' ': 0, 'S': 2, 'E': 3, '.': 0}
        int_grid = []
        start_pos = None
        end_pos = None
        
        for r, line in enumerate(file):
            row = []
            for c, char in enumerate(line):
                value = char_map.get(char, 0)
                row.append(value)
                
                # Track special positions
                if char == 'S':
                    start_pos = (r, c)
                elif char == 'E':
                    end_pos = (r, c)
            int_grid.append(row)
    return int_grid, start_pos, end_pos

def bfs(grid, start, end):
    if not grid or not start or not end:
        return None, 0
    
    row, col = len(grid), len(grid[0])

    # goes throuhg every 


    


def main():
    print_grid(filename='maze.txt')
    grid, start, end = parse_ascii_maze(filename='maze.txt')
    bfs(grid, start, end)


if __name__ == '__main__':
    main()