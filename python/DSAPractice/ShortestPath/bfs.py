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
                    print(f"start position {r,c}")
                    start_pos = (r, c)
                elif char == 'E':
                    end_pos = (r, c)
            int_grid.append(row)
            
    return int_grid, start_pos, end_pos

def bfs_with_path(grid, start, end):
    """BFS that returns both distance and the actual path"""
    moves = [[1,0],[0,1],[-1,0],[0,-1]]
    if not grid or not start or not end:
        return None, None
    
    row, col = len(grid), len(grid[0])
    dist = [[0] * col for i in range(row)]
    vist = [[False] * col for i in range(row)]
    parent = [[None] * col for i in range(row)]  # Track where we came from
    
    start_x, start_y = start
    end_x, end_y = end
    q = deque()
    q.append((start_x, start_y))
    vist[start_x][start_y] = True
    
    while len(q):
        x, y = q.popleft()
        
        # If we reached the end, we can stop early (optional optimization)
        if (x, y) == end:
            break
            
        for dx, dy in moves:
            new_x = dx + x
            new_y = dy + y
            if (new_x >= 0 and new_x < row and new_y >= 0 and new_y < col 
                and not vist[new_x][new_y] and grid[new_x][new_y] == 0):
                q.append((new_x, new_y))
                vist[new_x][new_y] = True
                dist[new_x][new_y] = dist[x][y] + 1
                parent[new_x][new_y] = (x, y)  # Remember where we came from
    
    if not vist[end_x][end_y]:
        return -1, []  # No path found
    
    # Reconstruct path by backtracking from end to start
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parent[current[0]][current[1]]
    
    path.reverse()  # Reverse to get path from start to end
    return dist[end_x][end_y], path

def print_path_on_maze(filename, path):
    """Print the maze with the path marked"""
    with open(filename, 'r') as file:
        lines = [line.rstrip('\n') for line in file.readlines()]
    
    # Convert path to set for O(1) lookup
    path_set = set(path)
    
    print("\nMaze with path marked (*):")
    for r, line in enumerate(lines):
        output_line = ""
        for c, char in enumerate(line):
            if (r, c) in path_set and char not in ['S', 'E']:
                output_line += '*'
            else:
                output_line += char
        print(output_line)

def main():
    maze_file = "maze.txt"  # Test with one file first
    
    try:
        print(f"--- Processing {maze_file} ---")
        print("Original maze:")
        print_grid(filename=maze_file)
        
        grid, start, end = parse_ascii_maze(filename=maze_file)
        
        if start is None:
            print("Error: No start position 'S' found!")
            return
        if end is None:
            print("Error: No end position 'E' found!")
            return
            
        distance, path = bfs_with_path(grid, start, end)
        
        if distance == -1:
            print("No path found!")
        else:
            print(f"Shortest distance: {distance}")
            print(f"Path coordinates: {path}")
            print(f"Path length: {len(path)} steps")
            print_path_on_maze(maze_file, path)
            
    except FileNotFoundError:
        print(f"File {maze_file} not found!")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()