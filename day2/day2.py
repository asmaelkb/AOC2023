
file = open("day2.txt")

ref_bag = {"red": 12, "green": 13, "blue": 14}

def match(element, bag):
    op = element.split(" ")
    number = int(op[0])
    color = op[1]
    bag[color] = max(number, bag[color])

    return bag


# PART1
def verif(bag):
    for i in ["red", "green", "blue"]:
        if (bag[i] > ref_bag[i]):
            return False
    return True


sum = 0
for line in file:
    bag = {"red": 0, "green": 0, "blue": 0}

    ### PART 1
    # nb_game = int(line.split(":")[0])

    after = line.split(": ")[1]
    after = after.split("\n")[0]
    after = after.split("; ")

    for i in range (len(after)):
        after[i] = after[i].split(", ")
        for k in range(len(after[i])):
            bag = match(after[i][k], bag)
    
    ### PART 1
    # if (verif(bag)):
    #     sum += nb_game
    
    ### PART 2
    sum += (bag["red"] * bag["green"] * bag["blue"])

print(sum)
