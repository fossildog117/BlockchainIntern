import random as r

width = height = 50
maze = [[0 for i in range(width)] for j in range(height)]
wasHere = [[False for i in range(width)] for j in range(height)]
shortestPath = [[False for i in range(width)] for j in range(height)]

startX = startY = 1
endX = 48
endY = 48


def solveMaze(x, y):
    if x is endX and y is endY:
        return True

    if maze[x][y] is 'w' or wasHere[x][y] is True:
        return False

    wasHere[x][y] = True

    if x is not 0:
        if solveMaze(x - 1, y) is True:
            shortestPath[x][y] = True
            return True

    if x is not width - 1:
        if solveMaze(x + 1, y) is True:
            shortestPath[x][y] = True
            return True

    if y is not 0:
        if solveMaze(x, y - 1) is True:
            shortestPath[x][y] = True
            return True

    if y is not height - 1:
        if solveMaze(x, y + 1) is True:
            shortestPath[x][y] = True
            return True

    return False


def printMaze():
    for i in range(width):
        for j in range(height):
            print maze[i][j],
        print ""
    print ""


def generateMaze():
    for x in range(width):
        for y in range(height):
            if x is 0 or y is 0 or x is width - 1 or y is height - 1:
                maze[x][y] = 'w'
            else:
                z = r.randint(0, 3)
                if z is 0:
                    maze[x][y] = 'w'
                else:
                    maze[x][y] = ' '

    maze[startX][startY] = 's'
    maze[endX][endY] = 'e'
    printMaze()


if __name__ == '__main__':
    generateMaze()
    solveMaze(startX, startY)

    for i in range(width):
        for j in range(height):
            if shortestPath[i][j] is True:
                maze[i][j] = '*'

    maze[startX][startY] = 's'

    printMaze()


