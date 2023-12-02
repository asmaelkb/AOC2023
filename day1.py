
sum = 0

f = open("day1.txt")

numbers = ["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty"]

def match_with(line):
    for i in range(len(numbers)):
        line = line.replace(numbers[i], str(i+1))

    return line

# for line in f:
#     liste = []
#     new_line = match_with(line)
#     for lettre in new_line:
#         if (lettre.isdigit()):
#             liste.append(lettre)
#     print(line + " ---> " + new_line)
#     sum += int(liste[0] + liste[len(liste) - 1])
#     liste = []

# print(sum)

# Last number : lire backward
# On lit jusqu'à trouver un élément de numbers, et on le remplace

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
        

for line in f:
    first = find_first(line)
    last = find_last(line)
    res = first + last
    sum += int(res)

print(sum)