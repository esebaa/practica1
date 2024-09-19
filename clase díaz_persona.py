#PRACTICA CALIFICADA NÚMERO 1 TALLER DE PROGRAMACIÓN I
#Apellidos y Nombres: Díaz Nieves Emanuel Sebastian
#Código:202410467

#Problema 1) Escriba el código Python para representar las clases y lógica del siguiente diagrama. Escriba también las pruebas unitarias con unittest.
#19/09/2024

class Díaz_Persona:

    nombre = ''
    apellidos = ''
    calorias = 0

    def caminar(self):
        self.calorias +=0

per1 = Díaz_Persona()

print(per1.nombre + ', ' + per1.apellidos + ', calorias: ' + str(per1.calorias))

per1.nombre = 'Emanuel'
per1.apellidos = 'Díaz Nieves'
per1.calorias = 5000


per1.calorias_consumidas =

per1.caminar()
print(per1.nombre + ', ' + per1.apellidos + ', calorias: ' + str(per1.calorias))