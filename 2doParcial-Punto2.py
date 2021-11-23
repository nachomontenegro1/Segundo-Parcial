# Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos
# necesarios para resolver las tareas, listadas a continuación:
# 1. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servidor, router, switch, impresora;
# 2. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook: Red
# Hat, Debian, Arch;
# 3. encontrar el camino más corto para enviar a imprimir un documento desde la pc:
# Debian y Red Hat, hasta el servidor “MongoDB”;
# 4. encontrar el árbol de expansión mínima;
# 5. la impresora esta temporalmente fuera de linea por mantenimiento, quítela del grafo y
# realice un barrido en profundidad para corroborar que efectivamente fue borrada;
# 6. debe utilizar un grafo no dirigido.

from grafo import Grafo

redes= Grafo (dirigido= False)

redes.insertar_vertice('Switch 1', data = 'Switch')
redes.insertar_vertice('Switch 2', data = 'Switch')
redes.insertar_vertice('Router 1', data = 'Router')
redes.insertar_vertice('Router 2', data = 'Router')
redes.insertar_vertice('Router 3', data = 'Router')
redes.insertar_vertice('Debian', data = 'Notebook')
redes.insertar_vertice('Red Hat', data = 'Notebook')
redes.insertar_vertice('Arch', data = 'Notebook')
redes.insertar_vertice('Fedora', data = 'PC')
redes.insertar_vertice('Guarani', data = 'Servidor')
redes.insertar_vertice('MongoDB', data = 'Servidor')
redes.insertar_vertice('Impresora', data = 'Impresora')
redes.insertar_vertice('Ubuntu', data = 'PC')
redes.insertar_vertice('Mint', data = 'PC')
redes.insertar_vertice('Manjaro', data = 'PC')
redes.insertar_vertice('Parrot', data = 'PC')


redes.insertar_arista(17, 'Switch 1', 'Debian')
redes.insertar_arista(18, 'Switch 1', 'Ubuntu')
redes.insertar_arista(22, 'Switch 1', 'Impresora')
redes.insertar_arista(80, 'Switch 1', 'Mint')
redes.insertar_arista(29, 'Switch 1', 'Router 1')
redes.insertar_arista(37, 'Router 1', 'Router 2')
redes.insertar_arista(43, 'Router 1', 'Router 3')
redes.insertar_arista(50, 'Router 2', 'Router 3')
redes.insertar_arista(25, 'Router 2', 'Red Hat')
redes.insertar_arista(9, 'Router 2', 'Guarani')
redes.insertar_arista(61, 'Switch 2', 'Router 3')
redes.insertar_arista(40, 'Switch 2', 'Manjaro')
redes.insertar_arista(12, 'Switch 2', 'Parrot')
redes.insertar_arista(5, 'Switch 2', 'MongoDB')
redes.insertar_arista(56, 'Switch 2', 'Arch')
redes.insertar_arista(3, 'Switch 2', 'Fedora')


# Punto2 //Barrido en profundidad y amplitud desde la tres notebooks: Red Hat, Debian, Arch//
pos = redes.buscar_vertice('Red Hat')

print('Barrido en profundidad y amplitud desde Red Hat:')
redes.barrido_profundidad(pos)
redes.marcar_no_visitado()
print()
redes.barrido_amplitud(pos)
redes.marcar_no_visitado()
print()
pos = redes.buscar_vertice('Debian')
print('Barrido en profundidad y amplitud desde Debian:')
redes.barrido_profundidad(pos)
redes.marcar_no_visitado()
print()
redes.barrido_amplitud(pos)
redes.marcar_no_visitado()
print()
pos = redes.buscar_vertice('Arch')
print('Barrido en profundidad y amplitud desde Arch:')
redes.barrido_profundidad(pos)
redes.marcar_no_visitado()
print()
redes.barrido_amplitud(pos)
redes.marcar_no_visitado()
print()

# Punto3 //Encontrar el camino más corto para enviar a imprimir un documento desde la pc: Debian y Red Hat, hasta el servidor “MongoDB”//

redes.camino_mas_corto('Debian', 'MongoDB')
print()
redes.camino_mas_corto('Red Hat', 'MongoDB')
print()

# Punto4 //Encontrar el árbol de expansión mínima//
redes.arbol_expansion_minimo()
print()


# Punto5 //La impresora esta temporalmente fuera de linea por mantenimiento, quítela del grafo y realice un barrido en profundidad para corroborar que efectivamente fue borrada//
redes.eliminar_vertice('Impresora')
redes.barrido_profundidad(0)

