#La Empresa “Empire Inventory” necesita desarrollar un sistema de administración de
#productos para sus almacenes. Para cada producto se almacenará:
#• Nombre del producto.
#• Precio del producto.
#• Cantidad del producto.
#La información de los productos se almacenará en un arreglo bidimensional, donde cada fila
#representara un producto y las columnas contendrán los datos mencionados.
#Requerimientos:
#El sistema deberá constar de los siguientes puntos:
#1. Menú Principal: Mostrar un menú con las siguientes opciones disponibles:
#• Cargar producto/s.
#• Buscar producto.
#• Ordenar inventario.
#• Mostrar producto más caro y más barato.
#• Mostrar productos con precio mayor a 15000.
#• Salir
#2. Cargar inventario:
#• Desarrollar una función que permita al usuario ingresar los datos del o los
#productos en una matriz (nombre, precio, cantidad).
#• El sistema debe permitir al usuario ingresar la cantidad deseada de productos.
#3. Buscar producto:
#• Implementar un algoritmo de búsqueda que permita al usuario encontrar un
#producto específico por su nombre y muestre por pantalla todos los datos de
#ese producto (nombre, precio y cantidad).
#4. Ordenar inventario:
#• Utilizar un algoritmo de ordenamiento para ordenar los productos en función
#de su precio de manera ascendente y luego mostrar por pantalla los productos
#ordenados.
#5. Mostrar producto más caro:
#• Desarrollar una función que identifique y muestre el producto más caro del
#inventario.
#6. Mostrar producto más barato:
#• Desarrollar una función que identifique y muestre el producto más barato del
#inventario.
#Requisitos técnicos:
#▪ Utilizar funciones para cada una de las operaciones mencionadas.
#▪ Mantener una estructura de código limpia y bien comentada.
#▪ Si el usuario selecciona cualquier opción sin que existan productos registrados en el
#sistema, aparecerá un mensaje en pantalla notificando que no hay productos
#disponibles para la operación solicitada.
#Entrega del programa
#▪ La entrega se deberá realizar mediante el link al repositorio de GitHub.

inventario = [["Laptop", 500000.00, 10 ], ["Silla", 14000.00, 50], ["Libro", 12000.00, 100], ["Monitor", 70000.00, 30]]


def validar_int(a):
    if not a.isdigit():
        return False
    return True

#1. Menú Principal: Mostrar un menú con las siguientes opciones disponibles:
#• Cargar producto/s.
#• Buscar producto.
#• Ordenar inventario.
#• Mostrar producto más caro y más barato.
#• Mostrar productos con precio mayor a 15000.
#• Salir
def mostrar_menu ():
    a = input('''Menu principal:
    
    1 - Cargar producto/s.
    2 - Buscar producto.
    3 - Ordenar inventario.
    4 - Mostrar producto más caro y más barato.
    5 - Mostrar productos con precio mayor a 15000.
    6 - Salir 
    
    Opcion elegida: ''')
    return a


    

#2. Cargar inventario:
#• Desarrollar una función que permita al usuario ingresar los datos del o los
#productos en una matriz (nombre, precio, cantidad).
#• El sistema debe permitir al usuario ingresar la cantidad deseada de productos.
def agregar_producto_inventario (a, b, c):
    inventario.append([a, b, c])
    return

#3. Buscar producto:
#• Implementar un algoritmo de búsqueda que permita al usuario encontrar un
#producto específico por su nombre y muestre por pantalla todos los datos de
#ese producto (nombre, precio y cantidad).
def buscar_producto(a):
    for i in range(len(inventario)):
        producto = inventario[i][0]
        if a == producto:
            hay_producto = True
            print(inventario[i])
        else:
            hay_producto = False
    return hay_producto
        

#4. Ordenar inventario:
#• Utilizar un algoritmo de ordenamiento para ordenar los productos en función
#de su precio de manera ascendente y luego mostrar por pantalla los productos
#ordenados. 
def ordenar_inventario():
    print("No llegué a hacer esta funcion")
    


#5. Mostrar producto más caro:
#• Desarrollar una función que identifique y muestre el producto más caro del
#inventario.
def mostrar_prod_mascaro():
    producto = ""
    precio_caro = 0
    
    for i in range(len(inventario)):
        precio_producto = inventario[i][1]
        if precio_caro < precio_producto:
            precio_caro = precio_producto
            producto = inventario[i][0]
    return producto, precio_caro

#6. Mostrar producto más barato:
#• Desarrollar una función que identifique y muestre el producto más barato del
#inventario.
def mostrar_prod_masbarato():
    producto = ""
    precio_barato = inventario[0][1]
    
    for i in range(len(inventario)):
        precio_producto = inventario[i][1]
        if precio_barato > precio_producto:
            precio_barato = precio_producto
            producto = inventario[i][0]
        
    return producto, precio_barato

#• Mostrar productos con precio mayor a 15000.
def mostrar_prod_precio15000():
    for i in range(len(inventario)):
        producto = ""
        precio_mayor = 15000
        precio_producto = inventario[i][1]
        if precio_mayor < precio_producto:
            precio_mayor = precio_producto
            producto = inventario[i][0]
            print(producto, precio_mayor)
    return

entrar = True
while entrar:
    opcion = mostrar_menu()
    while not validar_int(opcion) and opcion not in [1, 2, 3, 4, 5, 6]:
        opcion = input("Caracter inválido, ingrese un numero entre 1 y 6: ")
        validar_int(opcion)
    opcion = int(opcion)
    match opcion:
        case 1: 
            nombre_producto = input("Ingrese el nombre del producto: ")
            precio_producto = input("Ingrese el precio del producto: ")
            while not validar_int(precio_producto):
                precio_producto = input("Caracter inválido, ingrese un dígito numérico: ")
                validar_int(precio_producto)
            precio_producto = int(precio_producto)
            cant_producto = input("Ingrese la cantidad de productos: ")
            while not validar_int(cant_producto):
                cant_producto = input("Caracter inválido, ingrese un dígito numérico: ")
                validar_int(cant_producto)
            cant_producto = int(cant_producto)
            agregar_producto_inventario(nombre_producto, precio_producto, cant_producto)
        case 2: 
            producto = input("Ingrese el nombre del producto que desea buscar: ")
            buscar_producto(producto)
            if not buscar_producto(producto):
                print("Producto no encontrado.")
        case 3: 
            ordenar_inventario
        case 4:
            mascaro_o_masbarato = input("Si desea buscar el producto mas caro ingrese 1, si desea buscar el mas barato ingrese 2: ")
            while not validar_int(mascaro_o_masbarato) and mascaro_o_masbarato not in [1, 2]:
                mascaro_o_masbarato = input("Caracter inválido, ingrese 1 o 2: ")
                validar_int(mascaro_o_masbarato)
            mascaro_o_masbarato = int(mascaro_o_masbarato)
            if mascaro_o_masbarato == 1:
                print (mostrar_prod_mascaro())
            elif mascaro_o_masbarato == 2:
                print (mostrar_prod_masbarato())
        case 5:
            print(mostrar_prod_precio15000())
        case 6:
            entrar = False
            print("Usted a salido del programa.")

