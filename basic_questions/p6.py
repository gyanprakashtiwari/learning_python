from signal import valid_signals


values = input("Enter some numbers separated by comma\n")

values = values.split(",")
t = tuple(values)

print("List: ",values)
print ("Tuple: ",t)