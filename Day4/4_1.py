import re

with open("data/4_1.txt", "r") as f:
    content = f.read()

content = [line.split() for line in content.split("\n\n")]


valid_data = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def validation(passport):
    validation_list = []
    validation_list.append(validate_byr(passport.get("byr")))
    validation_list.append(validate_iyr(passport.get("iyr")))
    validation_list.append(validate_eyr(passport.get("eyr")))
    validation_list.append(validate_hgt(passport.get("hgt")))
    validation_list.append(validate_hcl(passport.get("hcl")))
    validation_list.append(validate_ecl(passport.get("ecl")))
    validation_list.append(validate_pid(passport.get("pid")))
    return all(validation_list)

def validate_byr(year):
    return 1920 <= int(year) <= 2002

def validate_iyr(year):
    return 2010 <= int(year) <= 2020

def validate_eyr(year):
    return 2020 <= int(year) <= 2030

def validate_hgt(height):
    if str(height).endswith("cm"):
        return 150 <= int(height[:-2]) <= 193
    elif str(height).endswith("in"):
        return 59 <= int(height[:-2]) <= 76
    else:
        return False

def validate_hcl(hairColor):
    if str(hairColor).startswith("#"):
        return re.match(r"^[0-9a-f]{6}$", hairColor[1:])
    else:
        return False
        
def validate_ecl(eyeColor):
    eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return eyeColor in eye_colors

def validate_pid(passID):
    return re.match(r"^[0-9]{9}$", passID)

def simplePassportValidator():
    nbr_of_valid_passports = 0
    for line in content:
        passport = {}
        for info in line:
            key, value = info.split(":")
            passport[key] = value

        if all (key in passport for key in valid_data):
            nbr_of_valid_passports += 1
    return nbr_of_valid_passports

def strictPassportValidator():
    nbr_of_valid_passports = 0
    for line in content:
        passport = {}
        for info in line:
            key, value = info.split(":")
            passport[key] = value

        if all (key in passport for key in valid_data) and validation(passport):
            nbr_of_valid_passports += 1
    return nbr_of_valid_passports


print("Valid on simple validator: " + str(simplePassportValidator()))
print("Valid on Strict validator: " + str(strictPassportValidator()))