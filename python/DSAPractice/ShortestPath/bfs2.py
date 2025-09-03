from collections import deque
import time

def print_grid(filename, grid) -> None:
    """ Print the Grid by reading the txt file """
    if filename is not None:
        print(f"================ {filename} ================")
        with open(filename, 'r') as file:
            for line in file:
                print(line.rstrip('\n'))
        print(f"================{(len(filename)+2) * "="}================")
    else:
        # Fixed: properly format the grid without quotes
        for row in grid:
            print(''.join(str(cell) for cell in row))
        print(f"================={(len(grid) + 2) * "="}=================")


def parse_gird(filename):
    """ Parse through the txt file creating a  2x2 grid that represent:
            - Walkable areas 
            - none Walkable areas 
            - the start
            - ending positions """
    with open(filename, 'r') as file:
        char_map = {'#': 1, ' ': 0, 'S': 0, 'E': 0}
        int_grid = []
        start_pos = None
        end_pos = None

        lines = file.readlines()
        for row, line in enumerate(lines):
            rows = []
            for col, char in enumerate(line):
                if char == "\n":
                    continue
                value = char_map.get(char, 0)
                rows.append(value)
                if char == 'S':
                    start_pos = (row, col)
                elif char == 'E':
                    end_pos = (row, col)
            int_grid.append(rows)
    

    return int_grid, start_pos, end_pos

def return_grid(grid, char_map):
    int_grid = []

    for line in grid:
        rows = []
        for char in line:
            if char == "\n":
                continue
            value = char_map.get(char, 0)
            rows.append(value)
        int_grid.append(rows)
    return int_grid

def bfs(grid, start_pos, end_pos):
    """ given the parse_grids grid, start, and end position:
            - traverse the grid from start to end
            - keep track of the shortest distance
            - show the path on the grid """
    
    char_map = {1: '#', 0: ' ', '*': '*'}
    # create a moves that goes through all the motions up, down, left, and right
    moves = [[1,0], [0,1], [-1,0], [0,-1]]
    # create the start position (x,y) and end position (x,y)
    start_x, start_y = start_pos
    
    end_x, end_y = end_pos
    # find the rows and cols for verifying if over the grid axis
    rows, cols = len(grid), len(grid[0])
    # vistied and a distance tracker both 2x2 arrays one keeps track of True or false the other is all 0
    visited = [[False] * cols for i in range(rows)]
    distance = [[0] * cols for i in range(rows)]
    # create a queue that will be our current position
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = True
    # while loop until the queue is empty
    while len(queue):
        # (x,y) pop the current position from the queue 
        x,y = queue.popleft()
        # iterate through the moves 
        for dx, dy in moves:
        # check if the moves + curr position is out of bounds check if in visited and if its a walkable position
            new_x, new_y = x+dx, y+dy
            if 0 <= new_x < rows and 0 <= new_y < cols and not visited[new_x][new_y] and grid[new_x][new_y] == 0:
            # if it is it will append the new position, add to visited, and increment count to the distance 
                queue.append((new_x, new_y))
                visited[new_x][new_y] = True
                distance[new_x][new_y] = distance[x][y] + 1
    
    def backtracking():
        print(f"End position distance: {distance[end_x][end_y]}\n")
                
        curr_x, curr_y = end_x, end_y
        grid[curr_x][curr_y] = "*"
        
        while curr_x != start_x or curr_y != start_y:
            curr_distance = distance[curr_x][curr_y]
            found_next = False
            
            for dx, dy in moves:
                new_x = curr_x + dx
                new_y = curr_y + dy
                
                if (0 <= new_x < rows and 0 <= new_y < cols):
                    if distance[new_x][new_y] == curr_distance - 1:
                        curr_x, curr_y = new_x, new_y
                        grid[curr_x][curr_y] = "*"
                        found_next = True
                        break
            
            if not found_next:
                print("No valid neighbor found!")
                break
        
        return return_grid(grid, char_map)

    # return distance[end_pos] if visited[end] else -1
    return distance[end_x][end_y] if visited[end_x][end_y] else -1, backtracking()



def main() -> None:
    """ Initializes each function and prints the shortest path and final grid """
    mazes = ["maze.txt", "maze1.txt", "maze2.txt", "maze3.txt", "maze4.txt"]
    for filename in mazes:
        print_grid(filename, None)
        maze, start_pos, end_pos = parse_gird(filename)
        print_grid(None, maze)
        shortest_path, maze = bfs(maze, start_pos, end_pos)
        if shortest_path != -1:
            print_grid(None, maze)
            print(f"\nlength of the shortest path for {filename} = {shortest_path}\n")
        else:
            print_grid(None, maze)
            print(f"There is no path from start to end position")


if __name__ == '__main__':
    main()