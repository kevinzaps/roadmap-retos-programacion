"""
funciones definidas por el usuario   
"""

# funcion simple

def greet():
    print("Hola, Python!")

greet()

# funcion con retorno

def return_greet():
    return "Hola, Phyton!"

print(return_greet())

# funcion con un argumento

def arg_greet(name):
    print(f"hola, {name}!")

arg_greet("brais")

# funcion con argumentos

def args_greet(greet, name):
    print(f"{greet}, {name}!")


args_greet("hola", "brais")
args_greet(name="brais", greet="hola")

# funciones con un argumento predeterminado

def default_arg_greet(name="phyton"):
    print(f"hola, {name}!")

default_arg_greet("brais")
default_arg_greet()

# con argumentos y retorno

def return_args_greet(greet, name):
    return f"{greet}, {name}!"


print(return_args_greet("hi", "brais"))


#funciones con retorno de varios valores

def multiple_return_greet():
    return "hola", "phyton"


greet, name = multiple_return_greet()
print(greet)
print(name)

# con un numero variable de argumentos

def variable_args_greet(*names):
    for name in names:
        print(f"hola, {name}!")

variable_args_greet("kevin", "montes", "robin")

# con un numero variable de argumentos con palabra clave

def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"hola, {value} ({key})!")

variable_key_arg_greet(
    language="phyton",
    name="brais",
    alias="mouredev"
)

"""
funciones dentro de funciones
"""

def outer_fuction():
    def inner_fuction():
        print("funcion interna: Hola, phyton !")
    inner_fuction()

outer_fuction()


"""
funciones de lenguaje (built-in)
"""

print(len("kevinzap"))
print(type(5214))
print("kevinzap".upper())

"""
variables locales y globales
"""

global_variable = "phyton"

print(global_variable)

def hello_phyton():
    
    print(f"hello, {global_variable}!")

hello_phyton()


global_variable = "phyton"

print(global_variable)

def hello_phyton():
    local_var = "hola"
    print(f"{local_var}, {global_variable}")


print(global_variable)
#print(local_var) no se puede acceder desde fuera de la funcion

hello_phyton()

"""
extra
"""
