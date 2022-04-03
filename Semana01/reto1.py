import time

nombre = input("Ingrese su nombre ")
edad = int(input("Ingrese su edad "))

# Obtiene la hora actual
def get_hour():
  date = time.ctime()
  date = date.split()
  date_hour = date[3].split(":")
  hour = date_hour[0]
  return int(hour)

current_hour = get_hour()

if edad < 18:
  if current_hour <= 18:
    print(nombre + " debes realizar tus tareas.")
  else:
    print(nombre + " debes ir a dormir.")
else:
  print(nombre + " no estas obligado a hacer nada.")