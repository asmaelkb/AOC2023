
ref_bag = {"red":12, "green":13, "blue":14}
file = open("day2.txt")
sum = 0

def match(element, bag):
    op = element.split(" ")
    number = int(op[0])
    color = op[1]
    bag[color] = max(number, bag[color])

    return bag


# 1ère étoile
def verif(bag): # bag1 trouvé, bag2 reference
    for i in ["red", "green", "blue"]:
        if (bag[i] > ref_bag[i]):
            return False
    return True


for line in file:
    bag = {"red": 0, "green":0, "blue":0}
    # 1ère étoile
    # nb_game = int(line.split(":")[0])

    after = line.split(": ")[1]
    after = after.split("\n")[0]
    after = after.split("; ")
    #print(after)
    for i in range (len(after)):
        after[i] = after[i].split(", ")
        for k in range(len(after[i])):
            bag = match(after[i][k], bag)
    
    sum += (bag["red"] * bag["green"] * bag["blue"])

print(sum)
    #print(after)
    
    # match(element, bag)