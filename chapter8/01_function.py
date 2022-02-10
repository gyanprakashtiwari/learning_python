def percent(marks):
    s = sum(marks)/(len(marks)*100)
    s*=100
    return s


marks = [60,40,45,80]
print(percent(marks))
