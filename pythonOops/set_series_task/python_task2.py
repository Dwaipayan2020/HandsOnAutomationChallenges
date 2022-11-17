even = []
odd = []
ip = input("Enter a number...\n")
listOfNum = range(int(ip))
func_y = lambda x: even.append(x) if x % 2 == 0 else odd.append(x)

[func_y(x) for x in listOfNum]

print("Even numbers::", even)
print("Odd numbers::", odd)
