import re

def readFile():
    with open("day4/input.txt", "r") as file:
        return [line.rstrip() for line in file] + [""] # added empty line for looping purposes


def part1():
    data = readFile()

    passport = ""
    valid = 0
    for line in data:
        if line == "": # if blank check validity of current passport
            if len(re.findall('ecl|pid|eyr|hcl|byr|iyr|hgt', passport)) == 7:
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
            byr = re.search('byr:(19[2-9][0-9]|200[0-2])', passport)
            iyr = re.search('iyr:(201[0-9]|2020)', passport)
            eyr = re.search('eyr:(202[0-9]|2030)', passport)
            hgt = re.search('hgt:(1[5-8][0-9]|19[0-3])cm|hgt:(59|6[0-9]|7[0-6])in', passport)
            hcl = re.search('hcl:(#[a-f0-9]{6}\\b)', passport)
            ecl = re.search('ecl:(amb|blu|brn|gry|grn|hzl|oth)', passport)
            pid = re.search('pid:(\\d{9}\\b)', passport)

            if byr != None and iyr != None and eyr != None and hgt != None and hcl != None and ecl != None and pid != None:
                valid += 1
            passport = ""
            continue
        passport += (" " + line)
    print(valid)

part1()
part2()


