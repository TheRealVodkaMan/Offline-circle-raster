import math


def setup_grid(grid, grid_size):
    for j in range(0,int(grid_size)):
        sub_grid = [0]*int(grid_size)

        for i in range(0, int(grid_size)):
            sub_grid[i] = 0

        grid.append(sub_grid)


def setup_grid_serial(grid0, grid1, grid_size):
    for j in range(0,int(grid_size)):
        sub_grid0 = [0]*int(grid_size)
        sub_grid1 = [0]*int(grid_size)

        for i in range(0, int(grid_size)):
            sub_grid0[i] = 0
            sub_grid1[i] = 0

        grid0.append(sub_grid0)
        grid1.append(sub_grid1)


def draw_circle(grid, dia, grid_size):
    grid_offset = round((grid_size - dia)/2)
    radius = math.floor(dia/2)

    if(dia % 2 == 0):
        circle_offset = 0.5
    else:
        circle_offset = 0

    for j in range(0, grid_size):
        for i in range(0, grid_size):
            grid[j][i] = 0

    for j in range(0, int(dia)):
        for i in range(0, int(dia)):
            if ((i-radius+circle_offset)**2 + (j-radius+circle_offset)**2) < math.pow(dia/2,2):
                grid[j+grid_offset][i+grid_offset] = 1
            else:
                grid[j+grid_offset][i+grid_offset] = 0


def print_grid(grid, grid_size):
    for j in range(0, int(grid_size)):
        for i in range(0, int(grid_size)):
            print(grid[j][i], end="")

            if(i == int(grid_size)-1):
                print("")

#test_grid = []

#setup_grid(test_grid, 25)
#draw_circle(test_grid, 10, 25)
#print_grid(test_grid, 25)