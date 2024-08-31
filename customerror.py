a = input("Enter any value bw 5 and 9 :")
if a == "quit":
    print("the problem stopped")
elif a<"5" or a>"9":
    raise ValueError("value should be 5 and 9 ")
else:
    print("the number is bw 5 - 9")