import re
import math

def solve(sudo): 
    zero = None
    for i in range(len(sudo)):
        for j in range(len(sudo[0])):
            if sudo[i][j] == 0:
                zero = (i, j) 
    if not zero:
        return True
    else:
        r, c = zero
    for num in range(1,10):
        if check(sudo, num, (r,c)):
            sudo[r][c] = num
            if solve(sudo):
                return True
            sudo[r][c] = 0
    return False

def check(sudo, num, p):
    #check row
    for r in range(len(sudo)):
        if num == sudo[p[0]][r] and p[1] != r:
            return False
    #check column
    for r in range(len(sudo)):
        if num == sudo[r][p[1]] and p[0] != r:
            return False
    #check grid
    gridSize = int(math.sqrt(len(sudo[0])))
    grid_x = p[1] // gridSize
    grid_y = p[0] // gridSize
    for gr in range(gridSize * grid_y, gridSize * grid_y + 3):
        for gc in range(gridSize * grid_x, gridSize * grid_x + 3):
            if sudo[gr][gc] == num and p != (gr, gc):
                return False
    return True

f = open('sudoku.txt', 'r') 
splitting = re.split(r"Grid \d{1,}\n", f.read())
eachSudo = splitting[1:]
sum = 0
for index, s in enumerate(eachSudo):
    sudo = []
    for line in s.splitlines():
        sudo.append(list(map(int, list(line))))
    solve(sudo)
    # print sum of first 3 digit
    threeDigit = int(''.join(map(str, sudo[0][:3])))
    sum += threeDigit
    print('Grid', str(index + 1) , ': ', str(threeDigit))

print('total: ', sum)
print('Hello, I am Ching. Thank you for giving me this opportunity to do this test.')
print('I have to confess that I\'ve done lot of search in StackOverflow and google and even ask my friend how to do in order to finish this test. ')
print('I understand that this is not a ethnic and easy-acceptable behaviour, so nevertheless, thank you for this opportunity for me to learn more about python :)')
