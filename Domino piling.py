def domino(x,y):
   return (x*y)//2


user_input = input()
width_and_height = user_input.split(" ")
x=int(width_and_height[0])
y=int(width_and_height[1])

print(domino(x,y))
