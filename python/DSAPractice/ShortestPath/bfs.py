from collections import deque

def print_grid(filename):
    with open(filename, 'r') as file:
        for line in file:
            clean_line = line.rstrip('\n')
            print(clean_line)

def parse_ascii_maze(filename):
    with open(filename, 'r') as file:
        char_map = {'#': 1, ' ': 0, 'S': 0, 'E': 0, '.': 0}
        int_grid = []
        start_pos = None
        end_pos = None
        
        # First pass: read all lines to find max width
        lines = file.readlines()
        max_width = max(len(line.rstrip('\n')) for line in lines) if lines else 0
        
        for r, line in enumerate(lines):
            line = line.rstrip('\n')
            row = []
            
            # Pad line to max_width to ensure rectangular grid
            line = line.ljust(max_width)
            
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
    moves = [[1,0],[0,1],[-1,0],[0,-1]]
    if not grid or not start or not end:
        return None
    
    row, col = len(grid), len(grid[0])
    
    # Debug: Check grid dimensions
    print(f"Grid dimensions: {row} rows x {col} cols")
    print(f"Start: {start}, End: {end}")
    
    # Verify all rows have same length
    for i, grid_row in enumerate(grid):
        if len(grid_row) != col:
            print(f"Warning: Row {i} has length {len(grid_row)}, expected {col}")
    
    dist = [[0] * col for i in range(row)]
    vist = [[False] * col for i in range(row)]
    start_x, start_y = start
    end_x, end_y = end
    q = deque()
    q.append((start_x, start_y))
    vist[start_x][start_y] = True
    
    while len(q):
        x, y = q.popleft()
        for dx, dy in moves:
            new_x = dx + x
            new_y = dy + y
            if (new_x >= 0 and new_x < row and new_y >= 0 and new_y < col 
                and not vist[new_x][new_y] and grid[new_x][new_y] == 0):
                q.append((new_x, new_y))
                vist[new_x][new_y] = True
                dist[new_x][new_y] = dist[x][y] + 1
    
    if not vist[end_x][end_y]:
        return -1
    else:
        return dist[end_x][end_y]

def main():
    list_maze = ["maze.txt", "maze1.txt", "maze2.txt", "maze3.txt", "maze4.txt"]
    for i, maze_file in enumerate(list_maze):
        try:
            print(f"\n--- Processing {maze_file} ---")
            print_grid(filename=maze_file)
            grid, start, end = parse_ascii_maze(filename=maze_file)
            
            if start is None:
                print("Error: No start position 'S' found!")
                continue
            if end is None:
                print("Error: No end position 'E' found!")
                continue
                
            result = bfs(grid, start, end)
            print(f"Result: {result}")
            
        except FileNotFoundError:
            print(f"File {maze_file} not found, skipping...")
        except Exception as e:
            print(f"Error processing {maze_file}: {e}")
            import traceback
            traceback.print_exc()

if __name__ == '__main__':
    main()