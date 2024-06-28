# 5 while true ventas
import os
from datetime import datetime
import pyfiglet
os.system("cls")

folio=10020
#folio= numero de venta
#10 productos
#investigar con python como saco la fecha de sistema
productos=[
            
        ]

#es un numero correlativo(folio=folio+1)
#si stock es 0 mostrar que no quedan mas o error.
#folio, fecha, id, cantidad, total
ventas=[
        

        ]


archivo="productos.txt"
def cargar_prod(archivo):
    # Lista para almacenar los datos
    lista_datos = []   

    # Abrimos el archivo en modo lectura  r Read
    with open(archivo, 'r') as file:
        # Leemos cada línea del archivo
       
        for linea in file:
            
            linea = linea.strip()
            
            datos = linea.split(',')

            lista_datos.append(datos)

    return lista_datos
def imprimir_datos(lista_datos):
    for i in range (0,len(lista_datos),10):
        print(f"{lista_datos[i]}, {lista_datos[i+1]}, {lista_datos[i+2]}, {lista_datos[i+3]}, {lista_datos[i+4]}, {lista_datos[i+5]}, {lista_datos[i+6]}, {lista_datos[i+7]}, {lista_datos[i+8]}, {lista_datos[i+9]}")

archivo_2="ventas_prod.txt"
def cargar_ventas(archivo_2):
    # Lista para almacenar los datos
    lista_datos = []   

    # Abrimos el archivo en modo lectura  r Read
    with open(archivo_2, 'r') as file:
        # Leemos cada línea del archivo
       
        for linea in file:
            
            linea = linea.strip()
            
            datos = linea.split(',')

            lista_datos.append(datos)

    return lista_datos
def imprimir_datos(lista_datos):
    for i in range (0,len(lista_datos),5):
        print(f"{lista_datos[i]}, {lista_datos[i+1]}, {lista_datos[i+2]}, {lista_datos[i+3]}, {lista_datos[i+4]}")
#Menu principal
def validar_opcion():
    while True:
        opcion = input("Ingrese una opción: ")
        try:
            opcion = int(opcion)
            if opcion <= 5:
                return opcion
            else:
                print("Opción inválida. Por favor, ingrese un número entre 1 y 5.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")
#Validar id de Centas
def validate_id():
    while True:
        idprd = input("Ingrese Id de producto (o 'S' para salir): ")
        if idprd.upper() == 'S':
            return None
        if len(idprd) == 4:
            sw = 0
            for a in productos:
                if a[0] == idprd:
                    sw = 1
                    break
            if sw == 1:
                return idprd
            else:
                print("Error: El ID no existe. Intente nuevamente.")
        else:
            print("Error: El ID debe tener exactamente 4 caracteres. Intente nuevamente.")
#Validar cantidades Ventas
def validar_cantidad(stock):
    while True:
        try:
            cantidad = int(input("Ingrese cantidad a comprar: "))
            if cantidad > 0 and cantidad <= stock:
                return cantidad
            elif cantidad <= 0:
                print("Error: La cantidad debe ser mayor a 0.")
            else:
                print("Error: La cantidad no puede ser mayor al stock disponible.")
        except ValueError:
            print("Error: La entrada debe ser un número. Intente nuevamente.")
#Validar respuesta de ventas

def validar_respuesta():
    while True:
        respuesta = input("Desea comprarlo (SI/s o NO/n): ").strip().lower()
        if respuesta in ["si", "s"]:
            return "si"  # Retorna 'si' explícitamente
        elif respuesta in ["no", "n"]:
            return "no"  # Retorna 'no' explícitamente
        else:
            print("Respuesta inválida. Por favor, ingresa (SI o NO.")

def validar_respuesta2():
    while True:
        respuesta_otro_pr = input("Dsesea comprar otro producto (SI/s o NO/n): ").strip().lower()
        if respuesta_otro_pr in ["si", "s"]:
            return "si" 
        elif respuesta_otro_pr in ["no", "n"]:
            return "no"  
        else:
            print("Respuesta inválida. Por favor, ingresa SI/s o NO/n.")  

#Menu Reporte
def validar_opcion_op():
    while True:
        try:
            op = int(input("Ingrese una opción (1-4): "))
            if 1 <= op <= 4:
                return op
            else:
                print("Error: La opción debe ser entre 1 y 4.")
        except ValueError:
            print("Error: Debe ingresar un número.")
# Validar Fechas
def validar_fecha(fecha):
    partes = fecha.split("-")
    if len(partes) != 3:
        return False
    dia, mes, año = partes
    if not (dia.isdigit() and mes.isdigit() and año.isdigit()):
        return False
    dia, mes, año = int(dia), int(mes), int(año)
    if not (1 <= dia <= 31 and 1 <= mes <= 12 and año > 2000):
        return False
    return True
#Validar Menu Mantenedores
def validar_opcion_op3():
    while True:
        try:
            op3 = int(input("Ingrese una opción (1-6): "))
            if 1 <= op3 <= 6:
                return op3
            else:
                print("Error: La opción debe ser entre 1 y 6.")
        except ValueError:
            print("Error: Debe ingresar un número.")
# Validar id de Agregar
def validar_id(id):
    if len(id) != 4:
        print("El ID debe tener 4 caracteres")
        return False
    for producto in productos:
        if producto[0] == id:
            print("El ID ya existe")
            return False
    return True
#Validar tex vacio Agregar
def validar_texto(texto):
    if texto.strip() == "":
        print("El campo no puede estar vacío")
        return False
    return True
#Validar cantidades no sean menmos de 0 Agregar
def validar_numero(numero, minimo=0):
    if numero < minimo:
        print(f"El número debe ser mayor o igual que {minimo}")
        return False
    return True
#Validar
def validate_id():
    while True:
        idprd = input("Ingrese Id de producto (o 'S' para salir): ")
        if idprd.upper() == 'S':
            return None
        if len(idprd) == 4:
            sw = 0
            for a in productos:
                if a[0] == idprd:
                    sw = 1
                    break
            if sw == 1:
                return idprd
            else:
                print("Error: El ID no existe. Intente nuevamente.")
        else:
            print("Error: El ID debe tener 4 caracteres. Intente nuevamente...")

opcion=0
fecha=datetime.now().strftime("%d-%m-%Y")
print(pyfiglet.figlet_format("""Ventas de Polerones"""))
print("                     Autores: Benjamin Venegas Carreño")
                                
os.system("pause")
os.system("cls")
while int(opcion) <= 5:
    os.system("cls")            
    print(f"""
                                        Fecha:{fecha}


                SISTEMA DE VENTAS
        --------------------------------
        1. Vender Productos
        2. Reportes.
        3. Mantenedores
        4. Administracion
        5. Salir

         """)
    opcion=validar_opcion()
    os.system("cls")
        
    match opcion:

        case 1:
            os.system("cls")
            print("""         
                        Vender Productos                 
                ---------------------------------      
                 """)
            print("\n")
            while True:
                    idprd = validate_id()
                    if idprd is None:
                            break
                    sw=0
                    for a in productos:
                            if a[0]==idprd:
                                sw=1 
                                print("Queda:",a[1]," ",a[2]," ",a[8]," ",a[9])
                                print("\n")
                                cantidad = validar_cantidad(int(a[8]))
                                tp=cantidad*int(a[9])
                                print("Total a pagar: ",tp)
                                print("\n")
                                respuesta = validar_respuesta()
                                if respuesta == "si":
                                    if int(a[8])>=cantidad:
                                        a[8]= int(a[8])-cantidad
                                        folio+=1
                                        fecha=datetime.now().strftime("%d-%m-%Y")
                                        ventas.append([folio,idprd,fecha,cantidad,tp])
                                        print("Compra Grabada, stock restante: ",a[8])
                                        os.system("pause")
                                        os.system("cls")
                                
                                        
                                        respuesta_otro_pr=validar_respuesta2()
                                        if respuesta_otro_pr=="si":
                                            opcion=1
                                        
                                        elif respuesta_otro_pr=="no":
                                            opcion=0
                                            
                                        else:
                                            print("Error: dato ingresado no es valido, intente nuevamente...")
                                    else:
                                        print("Error no hay suficiente stock.")
                                else:
                                    respuesta == "no"
                                    opcion=0
                    if sw==0:
                        print("Error, Id no existe...")            
                   
                        break
                    os.system("cls")
                   
                    
                    if opcion == 0:
                        break
            os.system("pause")
            os.system("cls")
        
        case 2:
            os.system("cls")
            op=0
            while op<=4:
                print("""
                                    REPORTES
                      ------------------------------------
                      1. General de ventas (con total)
                      2. Ventas por fecha especifica (con total)
                      3. Ventas por rango de fecha (con total)
                      4. Salir al menu principal

                      """)
                op = validar_opcion_op()
                os.system("cls")

                match op:
                    case 1:
                        print("\nGeneral de Ventas: ")
                        total_ventas = 0
                        if ventas:
                            for venta in ventas:
                                print(venta[0]," ",venta[1]," ",venta[2]," ",venta[3]," ",venta[4])
                                total_ventas += int(venta[4])
                            print("Total de ventas: ", total_ventas)
                        else:
                            print("No hay ventas para mostrar")
                        
                        os.system("pause")
                        os.system("cls")
                   

                    case 2:
                        while True:
                            print("Menú de opciones")
                            print("1. Buscar ventas por fecha")
                            print("2. Volver al menú anterior")
                            opcion = input("Ingrese una opción: ")
                            os.system("cls")

                            if opcion == "1":
                                fecha = input("Ingrese fecha a buscar (dd-mm-yyyy): ")
                                if validar_fecha(fecha):
                                    cv = 0
                                    total = 0

                                    for venta in ventas:
                                        if venta[2] == fecha:
                                            print(venta[0], " ", venta[1], " ", venta[2], " ", venta[4])
                                            cv += 1
                                            total += int(venta[4])

                                    if cv == 0:
                                        print("No hay ventas para mostrar")
                                    else:
                                        print("Total de ganancia por ventas: ", total)

                                    os.system("pause")
                                    os.system("cls")
                                else:
                                    print("Error: La fecha debe tener el formato dd-mm-yyyy y ser válida.")
                                    os.system("pause")
                                    os.system("cls")                            
                            elif opcion == "2":
                                break
                            else:
                                print("Error: Opción inválida. Intente nuevamente.")
                                os.system("pause")
                                os.system("cls")
                    case 3:
                            import datetime

                            while True:
                                os.system("cls")
                                total = 0
                                cv = 0

                                print("Ingrese rango de fechas para buscar ventas:")
                                print("1. Ingresar fechas")
                                print("2. Volver al menú anterior")
                                opcion = input("Ingrese una opción: ")
                                os.system("cls")

                                if opcion == "1":
                                    while True:
                                        fecha_inicio = input("Ingrese fecha de inicio (dd-mm-yyyy): ")
                                        try:
                                            fecha_inicio = datetime.datetime.strptime(fecha_inicio, "%d-%m-%Y")
                                            break
                                        except ValueError:
                                            print("Error: La fecha debe tener el formato dd-mm-yyyy.")
                                            os.system("pause")
                                            os.system("cls")

                                    while True:
                                        fecha_termino = input("Ingrese fecha de término (dd-mm-yyyy): ")
                                        try:
                                            fecha_termino = datetime.datetime.strptime(fecha_termino, "%d-%m-%Y")
                                            break
                                        except ValueError:
                                            print("Error: La fecha debe tener el formato dd-mm-yyyy.")
                                            os.system("pause")
                                            os.system("cls")

                                    for venta in ventas:
                                        fecha_venta = datetime.datetime.strptime(venta[2], "%d-%m-%Y")
                                        if fecha_inicio <= fecha_venta <= fecha_termino:
                                            print(f"Venta: {venta[0]}, Fecha: {venta[2]}, Monto: {venta[4]}")
                                            total += int(venta[4])
                                            cv += 1

                                    if cv == 0:
                                        print("No hay ventas para mostrar en este rango de fechas.")
                                    else:
                                        print("Total de ganancia por ventas: ", total)

                                    os.system("pause")
                                    os.system("cls")
                                elif opcion == "2":
                                    break
                                else:
                                    print("Error: Opción inválida. Intente nuevamente.")
                                    os.system("pause")
                                    os.system("cls")
                        
                        
                        
                        


                if op==4:
                    break
            
                                
                                    
                                    
                                
   #agregar .append                 


        case 3:
            os.system("cls")
            op3=0
            while op3<=6:
                print("""
                            MANTENEDOR DE PRODUCTOS
                    --------------------------------------
                    1. Agregar
                    2. Buscar
                    3. Eliminar
                    4. Modificar
                    5. Listar
                    6. Salir al menu principal

                     """)
                op3=validar_opcion_op3()

                match op3:
                    case 1:
                        os.system("cls")
                        print("\n Agregar Producto\n")
                        #agregar
                        print("Agregar datos a la Lista de Productos \n")
                        while True:
                            id = input("Ingrese el id del producto:  ")
                            if validar_id(id):
                                break
                        while True:
                            prod = input("Ingrese el producto: ")
                            if validar_texto(prod):
                                break
                        while True:
                            marca = input("Ingrese la marca del producto: ")
                            if validar_texto(marca):
                                break
                        while True:
                            color = input("Ingrese el color del producto: ")
                            if validar_texto(color):
                                break
                        while True:
                            genero = input("Indique si la prenda es de (Hombre, Mujer, Unisex): ")
                            if validar_texto(genero):
                                break
                        while True:
                            talla = input("Ingrese la talla de la prenda: ")
                            if validar_texto(talla):
                                break
                        while True:
                            material = input("Ingrese el material del Producto: ")
                            if validar_texto(material):
                                break
                        while True:
                            fabricante = input("Ingrese donde fue fabricado el producto: ")
                            if validar_texto(fabricante):
                                break
                        while True:
                            try:
                                stock = int(input("Ingrese el stock del producto: "))
                                if validar_numero(stock):
                                    break
                            except ValueError:
                                print("El stock debe ser un número")
                        while True:
                            try:
                                precio = int(input("Ingrese el precio del producto: "))
                                if validar_numero(precio):
                                    break
                            except ValueError:
                                print("El precio debe ser un número")

                        productos.append([id, prod, marca, color, genero, talla, material, fabricante, stock, precio])
                        os.system("pause")
                        os.system("cls")

                    case 2:
                        os.system("cls")
                        idprd = validate_id()
                        if idprd is None:
                            break
                        sw = 0
                        for a in productos:
                            if a[0] == idprd:
                                sw = 1
                                print(a[0], " ", a[1], " ", a[2], " ", a[3], " ", a[4], " ", a[5], " ", a[6], " ", a[7], " ", a[8], " ", a[9])
                                break
                        if sw == 0:
                            print("Id de prenda no existe...")
                        os.system("pause")
                        os.system("cls")
                        
                    case 3:
                        os.system("cls")
                        id=input("Ingrese un Id de producto a eliminar:  ")

                        
                        sw=0 #rut no encontrado  1 es rut encontrado
                        for i in range(len(productos)):
                            if productos[i][0]==id:
                                sw=1  #encontrado
                                productos.pop(i)
                                print("Producto Eliminado")
                                break #salir del ciclo
                                

                        if sw==0: print("Id de prenda no existe...")
                        os.system("pause")
                        os.system("cls")
                    case 4:
                            os.system("cls")
                            print("\n Modificar\n")
                            while True:
                                id = input("Ingrese un Id de prenda modificar:  ")
                                if id.strip()!= "":  # Check if the input is not blank
                                    break
                                else:
                                    print("Error: El Id no puede estar vacío. Intente nuevamente.")

                            sw=0 
                            for a in range(len(productos)):
                                if productos[a][0]==id:
                                    sw=1  #encontrado
                                    print("Id de producto encontrado en el indice ",a)
                                    
                                    
                                    print("\n")
                                    nuevo_producto = input("Ingrese el nuevo producto: ")
                                    while not validar_texto(nuevo_producto):
                                        nuevo_producto = input("Ingrese el nuevo producto: ")

                                    nueva_marca = input("Ingrese la marca: ")
                                    while not validar_texto(nueva_marca):
                                        nueva_marca = input("Ingrese la marca: ")

                                    nuevo_color = input("Ingrese el color: ")
                                    while not validar_texto(nuevo_color):
                                        nuevo_color = input("Ingrese el color: ")

                                    nuevo_gen = input("Ingrese si la prenda es de (Hombre,Mujer,Unisex): ")
                                    while not validar_texto(nuevo_gen):
                                        nuevo_gen = input("Ingrese si la prenda es de (Hombre,Mujer,Unisex): ")

                                    nueva_talla = input("Ingrese la talla: ")
                                    while not validar_texto(nueva_talla):
                                        nueva_talla = input("Ingrese la talla: ")

                                    nuevo_material = input("Ingrese el material: ")
                                    while not validar_texto(nuevo_material):
                                        nuevo_material = input("Ingrese el material: ")

                                    nuevo_fabricante = input("Ingrese el fabricante: ")
                                    while not validar_texto(nuevo_fabricante):
                                        nuevo_fabricante = input("Ingrese el fabricante: ")

                                    while True:
                                        try:
                                            nuevo_stock = input("Ingrese el stock del producto: ")
                                            if validar_texto(nuevo_stock):
                                                if validar_numero(int(nuevo_stock)):
                                                    nuevo_stock = int(nuevo_stock)
                                                    break
                                                else:
                                                    print("Error: El stock debe ser un número entero.")
                                            else:
                                                print("Error: El campo de stock no puede estar vacío.")
                                        except ValueError:
                                            print("El stock debe ser un numero...")
                                    while True:
                                        try:
                                            nuevo_precio = input("Ingrese el precio: ")
                                            if validar_texto(nuevo_precio):
                                                if validar_numero(int(nuevo_precio)):
                                                    nuevo_precio = int(nuevo_precio)
                                                    break
                                                else:
                                                    print("Error: El precio debe ser un número entero.")
                                            else:
                                                print("Error: El campo de precio no puede estar vacío.")
                                        except ValueError:
                                            print("El precio debe ser un numero...")
                                    productos[a][1]=nuevo_producto
                                    productos[a][2]=nueva_marca
                                    productos[a][3]=nuevo_color
                                    productos[a][4]=nuevo_gen
                                    productos[a][5]=nueva_talla
                                    productos[a][6]=nuevo_material
                                    productos[a][7]=nuevo_fabricante
                                    productos[a][8]=nuevo_stock
                                    productos[a][9]=nuevo_precio
                                    print("\n Listo! datos modificados")
                                    break #salir del ciclo
                                else:
                                    a = a + 10 #salta a cada rut
                            if sw==0: print("Id de producto no existe...")
                            os.system("pause")
                            os.system("cls")
                    case 5:
                        os.system("cls")
                        print("\n Listar Productos\n")
                        if productos:
                            for a in productos:
                            
                                print(a[0]," ",a[1]," ",a[2]," ",a[3]," ",a[4]," ",a[5]," ",a[6]," ",a[7]," ",a[8]," ",a[9])
                        else:
                            print("No hay productos para mostrar")   
                        os.system("pause")
                        os.system("cls")

                if op3==6:
                    break #sale del white y vuelve al while "principal"
        case 4:
            os.system("cls")
            op=0
            print("""
                            MENU ADMINISTRACION
                    --------------------------------
                    1. Cargar datos 
                    2. Respaldar datos (Grabar Actualizar)
                    3. Salir

                    """)
            op=int(input("Ingrese una opcion 1-3: "))

            if op==1:
              if not productos: #Se valida si la lista de productos esta vacia, en ese caso se cargan los productos y las ventas
                productos = cargar_prod(archivo)
                ventas = cargar_ventas(archivo_2)
                print("Datos cargados correctamente")
                os.system("pause")
              else:
                    print("Ya se realizo la carga") #Caso contrario se notifica al user que ya se hizo una carga.
                    os.system("pause")

            if op==2:
                
                with open(archivo, "w") as base: #Se reescribe el archivo y se guardan los datos de los productos actuales. 
                    for producto in productos:
                        base.write(f"{producto[0]},{producto[1]},{producto[2]},{producto[3]},{producto[4]},{producto[5]},{producto[6]},{producto[7]},{producto[8]},{producto[9]}\n")
                    for venta in ventas:
                        base.write(f"{venta[0]},{venta[1]},{venta[2]},{venta[3]},{venta[4]}\n")

            if op==3:
                
                
            
                if opcion==5:
                 break
                