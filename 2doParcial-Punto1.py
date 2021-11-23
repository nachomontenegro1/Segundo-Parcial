# El encargado de Jurassic World nos solicita que desarrollemos un algoritmo que nos permita
# resolver los siguientes requerimientos:
# 1. almacenar los datos de los distintos dinosaurios que hay en la isla, de cada uno se
# conoce su nombre, código de cinco dígitos y zona de ubicación (un dígito y un carácter
# por ejemplo 7A), existen varios dinosaurios con el mismo nombre pero sus códigos son
# distintos, los códigos no pueden ser repetidos (tenga cuidado);
# 2. se deben almacenar los datos en dos arboles uno ordenado por nombre y otro por
# código;
# 3. realizar un barrido en orden del árbol ordenado por nombre;
# 4. mostrar toda la información del dinosaurio 792;
# 5. mostrar toda la información de todos los T-Rex que hay en la isla;
# 6. modificar el nombre del dinosaurio en Sgimoloch en ambos arboles porque esta mal
# cargado, su nombre correcto es Stygimoloch;
# 7. mostrar la ubicación de todos los Raptores que hay en la isla;
# 8. contar cuantos Diplodocus hay en el parque;
# 9. debe cargar al menos 15 elementos.


from arbol_binario import Arbol

datos = [
    {'Nombre': 'T-Rex', 'Codigo': 45790,'Zona':'8A'},
    {'Nombre': 'Triceratops', 'Codigo': 12785,'Zona':'3C'},
    {'Nombre': 'Diplodocus', 'Codigo': 23689,'Zona':'9S'},
    {'Nombre': 'T-Rex', 'Codigo': 13545,'Zona':'3D'},
    {'Nombre': 'Velociraptor', 'Codigo': 792,'Zona':'7Z'},
    {'Nombre': 'Estegosaurio', 'Codigo': 32456,'Zona':'5F'},
    {'Nombre': 'Velociraptor', 'Codigo': 99875,'Zona':'7D'},
    {'Nombre': 'Sgimoloch', 'Codigo': 23134,'Zona':'2A'},
    {'Nombre': 'Anquilosaurio', 'Codigo': 80802,'Zona':'1Z'},
    {'Nombre': 'Protoceratops', 'Codigo': 10203,'Zona':'2D'},
    {'nombre':'Amargasaurio', 'codigo': 46788, 'Zona': '4S'},
    {'nombre':'Braquiosaurio', 'codigo': 65782, 'Zona': '9E'},
    {'nombre':'T-Rex', 'codigo': 14412, 'Zona': '8A'},
    {'nombre':'Gallimimo', 'codigo': 12986, 'Zona': '4R'},
    {'nombre':'Espinosaurio', 'codigo': 19213, 'Zona': '9Q'},
    {'Nombre': 'Velociraptor', 'Codigo': 56432,'Zona':'8K'},

]

nombre_dinos= Arbol()
codigo_dinos= Arbol()

for dinosaurio in datos:
    nombre_dinos = nombre_dinos.insertar_nodo(dinosaurio['nombre'], dinosaurio) 

for dinosaurio in datos:
    codigo_dinos = codigo_dinos.insertar_nodo(dinosaurio['codigo'], dinosaurio)

#Punto 3 //Barrido en orden del árbol ordenado por nombre//
nombre_dinos.inorden()

#Punto 4 //Información del Dinosaurio Cod. 792//
print ('Información del Dinosaurio Código Nro 792: ')
codigo_dinos.mostrar_informacion_codigo(792)

#Punto 5 //Información de todos los T-Rex hallados//
print ('Información de todos los T-Rex de la Isla: ')
nombre_dinos.mostrar_informacion_nombre

#Punto 6 //Modificar Nombre de Sgimoloch a Stygimoloch//
buscado = input ('Ingrese el nombre del dinosaurio a modificar: ').capitalize() 
nombre_dinos.busqueda_proximidad(buscado)
print ()
buscado = input('De la lista anterior, escriba el nombre completo del dinosaurio a modificar: ').capitalize()
print()
pos = nombre_dinos.busqueda(buscado)
if (pos):
    nuevo_nombre = input('Ingrese el nuevo nombre: ').capitalize()
    nombre, dinosaurio = nombre_dinos.eliminar_nodo(buscado)
    dinosaurio['nombre'] = nuevo_nombre
    arbol = nombre_dinos.insertar_nodo(nuevo_nombre, dinosaurio)
    print()
    nombre_dinos.inorden()
    print()
    codigo_dinos.inorden()
print()


#Punto7 //Ubicación de los Velociraptores de la isla//
print ('Ubicación de todos los Velociraptores: ')
nombre_dinos.mostrar_ubicacion_dinosaurio('Velociraptor')

#Punto8 //Cantidad de Diplodocus en la isla//
contador= nombre_dinos.contar_ocurrencias_dinosaurios('Diplodocus')
print ('En la isla hay ',contador,' Diplodocus en total.')
