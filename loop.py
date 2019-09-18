
'''
Write a simple script that demonstrate your understanding of loops in python   
'''
# Start with wile loop

i = 1
while i <= 7:
    print(i)
    i += 1
    if i == 4:
        break

# For Loop
x = (1, 2, "Python")
for i in x:
    print(i)

# Nested Loop
x = [1, 2, 3]
y = ["a", "b", "c"]
for i in x:
    for j in y:
        print(j, end="")
        print(i, end="") 
