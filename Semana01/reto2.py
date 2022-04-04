personas = []

# Cantidad de personas que van a ingresar
numero_personas = int(input("Cuantas personas van a entrar? "))

# Establece los datos de las personas en el array "personas"
for i in range(numero_personas):
  nombre = input("Ingrese su nombre: ")
  dni = int(input("Ingrese su dni: "))
  nacimiento = int(input("Ingrese su fecha de nacimiento aaaa/mm/dd: "))
  persona = {
    "nombre": nombre,
    "dni" : dni,
    "nacimiento": nacimiento
    }
  personas.append(persona)

# Ordena el array "personas" de menor a mayor segun la la fecha de nacimiento
personas = sorted(personas, key = lambda i: i['nacimiento'])

# Muestra las los dicts por orden de año de nacimiento
for persona in personas:
  print(persona)