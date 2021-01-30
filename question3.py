
import maze_helper

def dfs (maze, position, explored = []):
    explored.append(position)
    for i in maze_helper.get_adjacent_positions(maze,position):  
        loco = maze_helper.symbol_at(maze,i) 
        #checks the validity of the coords in explored[]
        if (loco == "X"):
            explored.append(i)
            path = []
            path.append(i)
            count = 0
            max = len(explored)
            for x in range (max-1,0,-1):
                for j in maze_helper.get_adjacent_positions(maze,explored[x]):
                    if (j == path[count]):
                        path.append(explored[x])
                        count+= 1
                        break
            for j in path:
                maze_helper.add_walk_symbol(maze,j)
            maze_helper.print_maze(maze)
        #continues the dfs search
        if (i not in explored):
            dfs(maze,i,explored)
def main():
    #declare the starting the position here
    position = 5,0
    maze = maze_helper.sample_maze()
    dfs(maze,position,[])
if __name__ == "__main__":
    main()