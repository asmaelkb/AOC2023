f = open("day3.txt")


row = 142
col = 142

def fill():
    tab = row*[[]]

    i = 1
    for line in f:
        if (i == row - 2):
            line = "."+line+"."
        else:
            line = "."+(line.replace("\n","."))

        tab[i] = list(line)
        i += 1

    tab[0] = col * ["."]
    tab[row - 1] = col * ["."]

    return tab


def is_part(number, i,j, size):
    coord = [(i, j-1), (i-1, j-1), (i+1, j-1), (i-1, j+size), (i, j+size), (i+1, j+size)]
    for k in range(size):
        coord.append((i-1, j+k))
        coord.append((i, j+k))
        coord.append((i+1, j+k))
    
    for (i,j) in coord:
        if (not(tab[i][j].isdigit()) and tab[i][j] != "."):
            return True

    

tab = fill()

sum = 0
indigit = False
for i in range(1, row-1):
    number = ""

    for j in range(1, col):

        # Case where there is a number
        if (tab[i][j].isdigit()):
            indigit = True
            number += tab[i][j]
        else:
            n = 0
        
            # Case when we were on the number, but not anymore
            if (indigit):
                n = len(number)
                number = int(number)

                if (is_part(number, i, j-n, n)):
                    sum += number
                
                indigit = False
        
            number = ""
        
print(sum)
        
    
