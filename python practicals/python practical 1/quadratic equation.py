#5.Python program to solve quadratic equation
a = 2
b = 3
c = 4
import cmath
d = (b**2)-(4*a*c)
ans = cmath.sqrt(d)
x = (-b+ans)/2*a
y = (-b-ans)/2*a
print("The solution are ",(x,y))