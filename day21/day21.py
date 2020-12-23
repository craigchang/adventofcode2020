import re
import functools

def common(a, b):
    return list(set(a) & set(b))

def readFile():
    recipes = [] # list of recipes
    allergenDict = dict() # allergen to list of recipes map
    with open("day21/input.txt", "r") as file:
        for line in file:
            ingredients = line.split(" (")[0].split(" ")
            allergens = re.search("\(contains (.*)\)", line)[1].split(", ")
            recipes.append(ingredients)
            for a in allergens:
                if (a not in allergenDict):
                    allergenDict[a] = []
                allergenDict[a].append(ingredients)
    return recipes, allergenDict

def main():
    recipesList, allergenDict = readFile()
    ingredientAllergenMap = dict() # ingredient to allergen map

    while(len(allergenDict) != len(ingredientAllergenMap)):
        for allergen, recipes in allergenDict.items():
            commonList = []

            if len(recipes) == 1: # the common list will be the ingredients
                commonList = recipes[0] 
            else: # find common ingredients between recipes where allergen is found
                for r in recipes: 
                    commonList = r if len(commonList) == 0 else list(set(commonList) & set(r))

            if len(commonList) == 1: # if 1 common ingredient found
                ingredientAllergenMap[commonList[0]] = allergen
            elif len(commonList) > 1:
                leftover = [c for c in commonList if c not in ingredientAllergenMap]
                if len(leftover) == 1:
                    ingredientAllergenMap[leftover[0]] = allergen

    # part 1
    nonAllergen = sum([1 for r in recipesList for ingredient in r if ingredient not in ingredientAllergenMap])
    print(nonAllergen)

    # part 2
    canonicalDangerousList = { k: v for k, v in sorted(ingredientAllergenMap.items(), key=lambda item: item[1]) }
    print( ",".join(canonicalDangerousList) )

main()