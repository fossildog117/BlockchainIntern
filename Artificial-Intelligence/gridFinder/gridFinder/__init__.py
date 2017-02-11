def printMap(princess, bot, gridSize):
    for i in range (0, gridSize, 1):
        for j in range (0, gridSize, 1):
            if princess[0] is i and princess[1] is j:
                print "p",
            elif bot[0] is i and bot[1] is j:
                print "b",
            else:
                print "-",
        print ""
    print ""

def findPrincess(princess, bot, gridSize):

    while abs(princess[0] - bot[0] != 0):
        if bot[0] > princess[0]:
            bot[0] -= 1
        else:
            bot[0] += 1
        printMap(princess, bot, gridSize)

    while abs(princess[1] - bot[1]) != 0:
        if bot[1] > princess[1]:
            bot[1] -= 1
        else:
            bot[1] += 1
        printMap(princess, bot, gridSize)

if __name__ == '__main__':

    gridSize = 6
    princess = [4, 5]
    bot = [0, 0]

    printMap(princess, bot, gridSize)
    findPrincess(princess, bot, gridSize)

