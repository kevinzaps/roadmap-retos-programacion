"""
Operadores  
"""

#operadores aritmeticos
print(f"suma: 10 + 3 = {10 + 3}")
print(f"resta: 10 - 3 = {10 - 3}")
print(f"multiplicacion: 10 * 3 = {10 * 3}")
print(f"division: 25 / 4 = {25 / 4}")
print(f"modulo : 25 % 4 = {25 % 4}")
print(f"exponente: 10 ** 3 = {10 ** 3}")
print(f"division entera: 10 // 3 = {10 // 3}")

# operadores de comparacion
print(f"igualdad: 10 == 3 es {10 == 3}")
print(f"desigualdad: 10 != 3 es {10 != 3}")
print(f"mayor que: 10 > 3 es {10 > 3}")
print(f"menor que: 10 < 3 es {10 < 3}")
print(f"mayor o igual que: 10 >= 10 es {10 >= 10}")
print(f"menor o igual que: 10 <= 3 es {10 <= 3}")

# operador logico
# para ser verdadero ambos deben ser verdaderos
print(f"AND &&: 10 + 3 == 13 AND 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")
# SI SE CUMPLE 1 DE LA DOS SERA VERDADERO 
print(f"or ||: 10 + 3 == 13 or 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 4}")
print(f"NOT !: 10 + 3 == 14 es {not 10 + 3 == 14}")

#operadores de asignacion
my_number = 11 # asignacion
print(my_number)
my_number += 1 #suma y asignacion
print(my_number)
my_number -= 1 # resta y asignacion
print(my_number)
my_number *= 2 # multiplicacion y asignacion    
print(my_number)
my_number /= 2 # division y asignacion
print(my_number)
my_number %= 2 # modulo y asignacion
print(my_number)
my_number **= 1 # exponente y asignacion
print(my_number)
my_number //= 1
print(my_number)

# Operadores de identidad
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")

#operadores de pertenencia
print(f" 'u' in 'mouredev' = {'u' in 'mouredev'}")
print(f" 'b' not in 'mouredev' = {'b' not in 'mouredev'} ")

# operadores de bit
a = 10 # 1010   
b = 3 # 0011
print(f"AND: 10 & 3 = {10 & 3}") # 0010
print(f"OR: 10 | 3 = {10 | 3}") # 1011  
print(f"XOR: 10 ^ 3 = {10 ^ 3}") # 1001
print(f"NOT: ~10 = {~10}") # -11
print(f"desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") # 0010
print(f"desplazamiento a la izquierda: 10 << 2 = {10 << 2}") # 101000

"""
estructuras de control
"""

#condicionales

my_string = "kevin" 
if my_string == "kevin":
    print("my_string es 'kevin'")
elif my_string == "zapata":
    print("my_string es 'zapata'")
else:
    print("my_string no es ni 'kevin' ni 'zapata'")

# iterativas

for i in range(11):
    print(i)

i = 15

while i >= 5:
    print(i)
    i -= 1

    #manejo de exepciones

try:
    print(10 / 1)
except:
    print("se ha producido una error")
finally:
    print("Ha finalizado el manejo de exepciones")


"""
extra
"""

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)