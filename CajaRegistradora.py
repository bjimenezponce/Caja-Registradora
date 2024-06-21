continuar = True
productos = []  # lista vacia para que se llene con los elementos que se solicitan mas abajo
# El iva es el valor de impuesto al valor agregado que es el 19%
Iva = 0.19

respuesta = "si"
acumuladoItems = 0
#comenzamos el ciclo para el ingreso de los productos y precios
while respuesta == "si":
    # se pide que ingrese el nombre del producto
    NombreP = input("ingrese el nombre de su producto ")
    # cantidad de productos que desea
    Cantidad = int(input("ingrese la cantidad de productos "))
    # esta linea de comandos es para poder guardar los nombres de cada producto
    productos.append(NombreP)
    # En esta linea pedimos ingresar el precio del producto pedido anteriormente
    Precio = int(input("¿cual es el precio Unitario de su producto? "))
    # valor a mostrar real de productos, multimplica el precio de los producto x la cantidad de ellos
    PrecioR = Precio * Cantidad

    acumuladoItems = acumuladoItems + PrecioR

    # ImprimirProducto(NombreP,Precio) # aqui se fijan nombre y precio como parametros
    print("Producto: " + NombreP + "\n Precio: " + str(PrecioR))

    respuesta= input(" ¿Desea ingresar mas articulos? > (si - no) ")
    if respuesta == "no":
        Total_iva = int(acumuladoItems * 1.19) # En este apartado el 1.19 es el valor del iva mas el 100% mas el 19% del iva
        print ("El total a pagar es: ", Total_iva)
        print ("El IVA de su compra es: ", acumuladoItems * Iva )
        Pago = int(input("Ingrese el pago "))
        
    if Pago < Total_iva:
        Pago = int(input ("EL monto a pagar debe ser igual o superior, ingrese nuevamente ")) 
else:  vuelto = Pago - Total_iva
print ("tu vuelto es: ", vuelto) # el vuelto es calculado a partir del total_iva que seria el total final a pagar menos el pago monto que ingresa el usuario para pagar los productos que lleva   
print (" que tengas un buen dia te estaremos esperando ;)" )
input()