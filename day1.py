f = open("day1.txt")

numbers = ["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty"]

### PART 1

def match_with(line):
    for i in range(len(numbers)):
        line = line.replace(numbers[i], str(i+1))
    return line

sum = 0
for line in f:
    liste = []
    for lettre in line:
        if (lettre.isdigit()):
            liste.append(lettre)
    sum += int(liste[0] + liste[len(liste) - 1])

print(sum)

### PART 2 

# We read the line in order to find the first number (written in number or in letter)
def find_first(line):
    mot = ""
    for element in line:
        if (element.isdigit()):
            return element
        else:
            mot += element
        
        tmp = match_with(mot)
        if (tmp != mot):
            for lettre in tmp:
                if (lettre.isdigit()):
                    return lettre
        

# We read the line backward in order to find the last number (written in number or in letter)
def find_last(line):
    mot = ""
    
    for i in range(len(line)-1, 0, -1):
        element = line[i-1]
  
        if (element.isdigit()):
            return element
        else:
            mot = element + mot
        
        tmp = match_with(mot)
 
        if (tmp != mot):
            for lettre in tmp:
                if (lettre.isdigit()):
                    return lettre
        
sum = 0
for line in f:
    first = find_first(line)
    last = find_last(line)
    res = first + last
    sum += int(res)

print(sum)