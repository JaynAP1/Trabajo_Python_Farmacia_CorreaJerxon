import json, os, datetime

Bol1=True
while Bol1==True:
    os.system("clear")

    with open("json/Compras.json", encoding="utf-8") as Compra:
        Compras=json.load(Compra)

    with open("json/Empleados.json", encoding="utf-8") as Empleado:
        Empleados=json.load(Empleado)
    
    with open("json/Medicamentos.json", encoding="utf-8") as Medicamento:
        Medicamentos=json.load(Medicamento)

    with open("json/Pacientes.json", encoding="utf-8") as Paciente:
        Pacientes=json.load(Paciente)
    
    with open("json/Proveedores.json", encoding="utf-8") as Proveedor:
        Proveedores=json.load(Proveedor)

    with open("json/Ventas.json", encoding="utf-8") as Venta:
        Ventas=json.load(Venta)

    print("====================================\n1).Vender.\n2).Comprar.\n3).Registros.\n4).Salir.\n====================================")
    Opcion1=str(input("Ingrese un numero para ir a la opcion deseada: "))

    if Opcion1 == "1":
        Bol2=True
        print("=====================")
        Contador=0
        for i in Medicamentos:
            Contador+=1
            print(Contador,").", i["nombre"])
        print("=====================")            

        Comparador=str(input("Ingrese el nombre del producto que desea: "))
        for y in Medicamentos:
            if Comparador == y["nombre"]:
                print("Has elegido el producto: ",y)
                Cantidad=int(input("Ingrese la cantidad que desea comprar: "))
                NombrePaciente=str(input("Ingrese el nombre del paciente: "))
                DireccionPaciente=str(input("Ingrese la direccion del paciente: "))
                PrecioTotal=Cantidad*y["precio"]
                Fecha=str(datetime.datetime.now())

                Ventas.append(
                {
                "fechaVenta": Fecha,
                "paciente": {
                    "nombre": NombrePaciente,
                    "direccion": DireccionPaciente
                },
                "empleado": {
                    "nombre": "Ana",
                    "cargo": "Vendedor"
                },
                "medicamentosVendidos": [
                    {
                        "nombreMedicamento": y,
                        "cantidadVendida": Cantidad,
                        "precio": PrecioTotal
                    }
                    ]
                }
                )

                with open("json/Ventas.json", "w") as Gventa:
                    json.dump(Ventas,Gventa)

            else:
                break


    elif Opcion1 == "2":
        print("Compras")
        input("")
    
    elif Opcion1 == "3":
        print("Registros")
        input("")
    
    elif Opcion1 == "4":
        print("Salir")
        input("")
        Bol1 = False