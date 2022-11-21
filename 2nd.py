# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.    
           
x = input('X = ')
y = input('Y = ')
z = input('Z = ')

print(not (x or y or z) == (not(x) and not(y) and not(z)))