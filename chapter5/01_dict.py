myDict = {
    "Fast" : "In a quick manner",
    "gyan" : "a cp guy",
    "anotherdict" : {"gyan" : "player"}
}

# print(myDict["anotherdict"]['gyan'])

# prints the list of all keys

# print(myDict.keys())
# prints list of all values
# print(myDict.values())
# print all key value pairs

# print(myDict)
# updates dict by adding the provided key value pair/pairs
myDict.update({"ehh":"hoo"})
print(myDict.get("gyan")) # gives null if key is not present in dict
# myDict["golu"] --> this give error but using .get doesn't give error

