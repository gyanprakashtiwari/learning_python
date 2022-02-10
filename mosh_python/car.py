




#HOW TO HANDLE ERRORS IN PYTHON 
# try:
#     age = int(input("Age : "))
#     print(age)
# except:
#     print("hai ram!")



# numbers = [5,2,5,2,2]

# for i in numbers:
#     for j in range(i):
#         print('X',end = "")
#     print("")



# for item in "python":
#     print(item)

# for item in range(5,10,2):
#     print(item)

# prices = [10,20,30]

# ans = 0

# for price in prices:
#     ans += price
# print(ans)





# THE CAR GAME!!
# is_start = False

# while True:
#     response = str(input("> "))
#     if (response.lower() == "help"):
#         print("start - to start the car")
#         print("stop - to stop the car")
#         print("quit - to exit")
#     elif response.lower()== "start":
#         if is_start:
#             print("Car has Already Started")
#         else:
#             is_start = True
#             print("Car started, Ready to Go!")
#     elif response.lower() == "stop":
#         if (not is_start):
#             print("Car has Already stopped..")
#         else:
#             is_start = False
#             print("Car Stopped.")
#     elif response.lower() == "quit":
#         break
#     else:
#         print("I don't understand that...")