# Example 1: Using a for loop to iterate over a list
print("For loop")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit,end=' ')


print('\n\n')

# Example 2: Using a while loop to print numbers from 1 to 5
print("\nwhile loop")
i = 1
while i <= 5:
    print(i, end = ' ')
    i += 1  # Increment i by 1
    
print("\n range loop")
for i in range(1,11):
    print(i,end=' ')