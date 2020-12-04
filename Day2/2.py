f = open("data/2_1.txt", "r")
content = f.readlines()
content = [line.strip().replace(":", "").split(",") for line in content]
f.close()

def pwdCheckerSledRental():
    count = 0
    for x in content:
        for y in x:
            charCounter = 0
            data = y.split(" ")
            charRange = data[0]
            charRange = charRange.split("-")
            charMin = charRange[0]
            charMax = charRange[1]
            charToExist = data[1]
            pwd = data[2]
            
            for i in pwd:
                if i == charToExist:
                    charCounter += 1
            if charCounter >= int(charMin) and charCounter <= int(charMax):
                count += 1
    print("The amount of correct passwords are: " + str(count))

def pwdChecker():
    count = 0
    for x in content:
        for y in x:
            data = y.split(" ")
            charRange = data[0]
            charRange = charRange.split("-")
            pos1 = charRange[0]
            pos2 = charRange[1]
            charToExist = data[1]
            pwd = data[2]

            if (bool(pwd[int(pos1)-1] == charToExist) ^ bool(pwd[int(pos2)-1] == charToExist)):
                count += 1

    print("The amount of correct passwords are: " + str(count))

pwdCheckerSledRental()
pwdChecker()