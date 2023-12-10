from flask import Flask
from flask import render_template, request
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'vorx'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306

mysql.init_app(app) 

if __name__ == '__main__':
    app.run(port=3306, debug=True)













"""def cargar_productos():
    try:
        with open("productos.json", "r") as archivo:
            productos = json.load(archivo)
    except FileNotFoundError:
        productos = []
    return productos


def guardar_productos(productos):
    with open("productos.json", "w") as archivo:
        json.dump(productos, archivo, indent=4)


def mostrar_menu():
    print("\n")
    print("---------------VORX---------------")
    print("Bienvenido al Sistema de Gestión de Stock")
    print("\n")
    print("1. Gestionar productos")
    print("2. Mostrar reportes")
    print("3. Salir")
    print("\n")


def gestionar_productos(productos):
    while True:
        print("\n--- Gestionar productos ---")
        print("1. Ingresar un nuevo producto")
        print("2. Modificar un producto")
        print("3. Eliminar un producto")
        print("4. Volver al menú principal")
        print("\n")

        opcion = input("Ingrese una opción: ")
        print("\n")

        if opcion == "1":
            ingresar_producto(productos)
        elif opcion == "2":
            modificar_producto(productos)
        elif opcion == "3":
            eliminar_producto(productos)
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")


def ingresar_producto(productos):
    codigo = input("Ingrese el código del producto: ")
    if codigo in [producto["codigo"] for producto in productos]:
        print("El código ya existe. No se puede ingresar el producto.")
        return

    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese la cantidad en stock: "))

    producto = {"codigo": codigo, "nombre": nombre,
                "precio": precio, "stock": stock}
    productos.append(producto)
    guardar_productos(productos)
    print("Producto ingresado correctamente.")


def modificar_producto(productos):
    codigo = input("Ingrese el código del producto a modificar: ")
    producto_encontrado = None

    for producto in productos:
        if producto["codigo"] == codigo:
            producto_encontrado = producto
            break

    if producto_encontrado is None:
        print("Producto no encontrado.")
        return

    nombre = input(
        "Ingrese el nuevo nombre del producto (dejar en blanco para no modificar): ")
    if nombre:
        producto_encontrado["nombre"] = nombre

    precio = input(
        "Ingrese el nuevo precio del producto (dejar en blanco para no modificar): ")
    if precio:
        producto_encontrado["precio"] = float(precio)

    stock = input(
        "Ingrese la nueva cantidad en stock (dejar en blanco para no modificar): ")
    if stock:
        producto_encontrado["stock"] = int(stock)

    guardar_productos(productos)
    print("Producto modificado correctamente.")


def eliminar_producto(productos):
    codigo = input("Ingrese el código del producto a eliminar: ")
    producto_encontrado = None

    for producto in productos:
        if producto["codigo"] == codigo:
            producto_encontrado = producto
            break

    if producto_encontrado is None:
        print("Producto no encontrado.")
        return

    productos.remove(producto_encontrado)
    guardar_productos(productos)
    print("Producto eliminado correctamente.")


def mostrar_reportes(productos):
    print("\n--- Reportes ---")
    print("1. Mostrar todos los productos")
    print("2. Mostrar productos con bajo stock")
    print("3. Volver al menú principal")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        mostrar_todos_los_productos(productos)
    elif opcion == "2":
        mostrar_productos_bajo_stock(productos)
    elif opcion == "3":
        return
    else:
        print("Opción inválida. Por favor, intente nuevamente.")


def mostrar_todos_los_productos(productos):
    print("\n--- Todos los productos ---")
    for producto in productos:
        print(f"Código: {producto['codigo']}")
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: {producto['precio']}")
        print(f"Stock: {producto['stock']}")
        print("--------------------")


def mostrar_productos_bajo_stock(productos):
    print("\n--- Productos con bajo stock ---")
    for producto in productos:
        if producto["stock"] < 10:
            print(f"Código: {producto['codigo']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: {producto['precio']}")
            print(f"Stock: {producto['stock']}")
            print("--------------------")


def main():
    productos = cargar_productos()

    while True:
        mostrar_menu()

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            gestionar_productos(productos)
        elif opcion == "2":
            mostrar_reportes(productos)
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")


if __name__ == "__main__":
    main()"""
