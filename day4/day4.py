import re

REQUIRED_REGEX = "ecl|pid|eyr|hcl|byr|iyr|hgt"
BYR_REGEX = "(?=.*byr:(19[2-9][0-9]|200[0-2]))"
IYR_REGEX = "(?=.*iyr:(201[0-9]|2020))"
EYR_REGEX = "(?=.*eyr:(202[0-9]|2030))"
HGT_REGEX = "(?=.*(hgt:(1[5-8][0-9]|19[0-3])cm|hgt:(59|6[0-9]|7[0-6])in))"
HCL_REGEX = "(?=.*hcl:(#[a-f0-9]{6}\\b))"
ECL_REGEX = "(?=.*ecl:(amb|blu|brn|gry|grn|hzl|oth))"
PID_REGEX = "(?=.*pid:(\\d{9}\\b))"


def readFile():
    with open("day4/input.txt", "r") as file:
        return [line.rstrip() for line in file] + [""] # added empty line for looping purposes

def part1():
    data = readFile()

    passport = ""
    valid = 0
    for line in data:
        if line == "": # if blank check validity of current passport
            if len(re.findall(REQUIRED_REGEX, passport)) == 7:
                valid += 1
            passport = "" # start new passport check
            continue
        passport += (" " + line) # aggregate passport information
    print(valid)

def part2():
    data = readFile()

    passport = ""
    valid = 0
    for line in data:
        if line == "": # if blank check validity of current passport
            if re.search(BYR_REGEX + IYR_REGEX + EYR_REGEX + HGT_REGEX + HCL_REGEX + ECL_REGEX + PID_REGEX + ".*", passport):
                valid += 1
            passport = ""
            continue
        passport += (" " + line)
    print(valid)

part1()
part2()


