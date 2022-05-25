print("\t\t\t:·PYTHON-VET by J.A. Hernández·:")
print("\n:·Nuestra misión es brindarle la mejor experiencia en consulta veterinaria·:")
print("_____________________________________________________________________________")

var1 = input("\nNombre del MV: ")
var2 = input("\nNombre del propietario: ")
var3 = input("\nNombre del paciente: ")

print(f"\nBienvenido a consulta, MV {var1}.")
print(f"\nUsted está atendiendo a: {var2} y a su mascota {var3}.")

print(f"\nPongamos al día la historia clínica de {var3}.")
consulta = input(f"\n¿{var3} viene por un control médico o es su primera consulta?: ")
print(f"\n¡De acuerdo! Ayudaremos a {var3} en su {consulta}.")
    
    # En el menú de especies se muestran las especies de animales para consulta

print("\n:Menú:\n")
tipo = {1:"1. Perro", 2:"2. Gato", 3:"3. Mamífero",
        4:"4. Ave", 5:"5. Reptil"}
for value in tipo:
    print(tipo[value])
tipo = int(input("\nIntroduzca el tipo de paciente a tratar: "))

try:
    if tipo == 1:
        print("\nHa seleccionado: Perro")
        raza = input("\nIntroduzca la raza del animal: ")
        print(f"\nUsted ha indicado que {var3} es un perro de raza {raza}.")
    elif tipo == 2:
        print("\nHa seleccionado: Gato")
        raza = input("\nIntroduzca la raza del animal: ")
        print(f"\nUsted ha indicado que {var3} es un gato de raza {raza}.")
    elif tipo == 3:
        print("\nHa seleccionado: Mamífero")
        especie = input("\nIntroduzca la especie del animal: ")
        print(f"\nUsted ha indicado que {var3} es un mamífero de la especie {especie}.")
    elif tipo == 4:
        print("\nHa seleccionado: Ave")
        especie = input("\nIntroduzca la especie del animal: ")
        print(f"\nUsted ha indicado que {var3} es un ave de la especie {especie}.")
    elif tipo == 5:
        print("\nHa seleccionado: Reptil")
        especie = input("\nIntroduzca la especie del animal: ")
        print(f"\nUsted ha indicado que {var3} es un reptil de la especie {especie}.")
    else:
        print("\n¡Ha ocurrido un error! Por favor, seleccione un tipo de paciente del menú.")
        print("No ha definido la especie del paciente a evaluar.")
        print("El registro del paciente está incompleto y no es posible brindar un diagnóstico correcto.")
except:
    pass
           
    # Ahora se muestran las variables donde se guardarán las
    # constantes fisiológicas del paciente, que se pedirán en la anamnesis

if tipo == 1 or tipo == 2 or tipo == 3 or tipo == 4 or tipo == 5:
    try:
        sexo = input(f"\nAhora indique el sexo de {var3} (M/H): ")
        print(f"\nEl sexo de {var3} es {sexo}.")
   
        edad = float(input(f"\nAhora indique la edad de {var3} (años): "))
        if edad == 1:
            print(f"\n{var3} tiene {edad} año de edad.")
        else:
            print(f"\n{var3} tiene {edad} años de edad.")

        peso = float(input(f"\nAhora indique el peso de {var3} (kilogramos): "))
        if peso == 1:
            print(f"\n{var3} pesa {peso} kilogramo.")
        else:
            print(f"\n{var3} pesa {peso} kilogramos.")

        temperatura = float(input(f"\nAhora indique la temperatura de {var3} (ºC): "))
        print(f"\nLa temperatura de {var3} es de {temperatura} ºC.")
        if tipo == 1:
            if temperatura < 37.5:
                print(f"-> Advertencia: La Tº de {var3} se encuentra por debajo del parámetro normal.")
            elif temperatura > 39.2:
                print(f"-> Advertencia: La Tº de {var3} se encuentra por encima del parámetro normal.")
            else:
                print(f"-> La Tº de {var3} se encuentra dentro del rango normal.")
        elif tipo == 2:
            if temperatura < 38:
                print(f"-> Advertencia: La Tº de {var3} se encuentra por debajo del parámetro normal.")
            elif temperatura > 39.2:
                print(f"-> Advertencia: La Tº de {var3} se encuentra por encima del parámetro normal.")
            else:
                print(f"-> La Tº de {var3} se encuentra dentro del rango normal.")
        else:
            print("\nNo contamos actualmente con registros para esta especie.")
            print("Se recomienda un diagnóstico especializado.")
        
        pulso = int(input(f"\nAhora indique el pulso de {var3} (ppm): "))
        print(f"\n{var3} tiene aproximadamente unas {pulso} pulsaciones por minuto.")
        if tipo == 1:
            if pulso < 60:
                print(f"-> Advertencia: El ppm de {var3} se encuentra por debajo del rango normal.")
            elif pulso > 180:
                print(f"-> Advertencia: El ppm de {var3} se encuentra por encima del rango normal.")
            else:
                print(f"-> El ppm de {var3} se encuentra dentro del rango normal.")
        elif tipo == 2:
            if pulso < 140:
                print(f"-> Advertencia: El ppm de {var3} se encuentra por debajo del rango normal.")
            elif pulso > 220:
                print(f"-> Advertencia: El ppm de {var3} se encuentra por encima del rango normal.")
            else:
                print(f"-> El ppm de {var3} se encuentra dentro del rango normal.")
        else:
            print("\nNo contamos actualmente con registros para esta especie.")
            print("Se recomienda un diagnóstico especializado.")

        fc = int(input(f"\nAhora indique la frecuencia cardíaca de {var3} (lpm): "))
        print(f"\nLa frecuencia cardíaca de {var3} es de {fc} latidos por minuto.")
        if tipo == 1:
            if fc < 60:
                print(f"-> Advertencia: La FC de {var3} se encuentra por debajo del rango normal.")
            elif fc > 180:
                print(f"-> Advertencia: La FC de {var3} se encuentra por encima del rango normal.")
            else:
                print(f"-> La FC de {var3} se encuentra dentro del rango normal.")
        elif tipo == 2:
            if fc < 140:
                print(f"-> Advertencia: La FC de {var3} se encuentra por debajo del rango normal.")
            elif fc > 220:
                print(f"-> Advertencia: La FC de {var3} se encuentra por encima del rango normal.")
            else:
                print(f"-> La FC de {var3} se encuentra dentro del rango normal.")
        else:
            print("\nNo contamos actualmente con registros para esta especie.")
            print("Se recomienda un diagnóstico especializado.")

        fr = int(input(f"\nAhora indique la frecuencia respiratoria de {var3} (rpm): "))
        print(f"\nLa frecuencia respiratoria de {var3} es de {fr} respiraciones por minuto.")
        if tipo == 1:
            if fr < 10:
                print(f"-> Advertencia: La FR de {var3} se encuentra por debajo del rango normal.")
            elif fr > 30:
                print(f"-> Advertencia: La FR de {var3} se encuentra por encima del rango normal.")
            else:
                print(f"-> La FR de {var3} se encuentra dentro del rango normal.")
        elif tipo == 2:
            if fr < 20:
                print(f"-> Advertencia: La FR de {var3} se encuentra por debajo del rango normal.")
            elif fr > 42:
                print(f"-> Advertencia: La FR de {var3} se encuentra por encima del rango normal.")
            else:
                print(f"-> La FR de {var3} se encuentra dentro del rango normal.")
        else:
            print("\nNo contamos actualmente con registros para esta especie.")
            print("Se recomienda un diagnóstico especializado.")

        tpc = float(input(f"\nAhora indique el tiempo de perfusión capilar de {var3} (segundos): "))
        if tpc <= 1:
            print(f"\nEl tiempo de pefusión capilar de {var3} es menor a 1 segundo.")
            print(f"-> El TPC de {var3} se encuentra dentro del rango normal.")
        elif tpc <= 2:
            print(f"\nEl tiempo de perfusión capilar de {var3} es menor a 2 segundos.")
            print(f"-> El TPC de {var3} se encuentra dentro del rango normal.")
        else:
            print(f"\nEl tiempo de perfusión capilar de {var3} es mayor a 2 segundos.")
            print(f"-> Advertencia: El TPC de {var3} se encuentra por encima del parámetro normal.")

        print("\nLa historia clínica ha sido actualizada exitosamente...")
    except:
        pass

    # Una vez tomadas las constantes fisiológicas del paciente, se continuará
    # a preguntar información clave que pueda aportar un mejor entendimiento
    # para el diagnóstico definitivo

print("\n|--------------------------------------|")

motivo = input("\nSeñale el motivo de la consulta: ")
evolucion = input("\n¿Cómo ha evolucionado la enfermedad?: ")
apetito = input("\nEstado del apetito: ")
comportamiento = input("\nEstado actual de su comportamiento: ")
print(f"\nBreve anamnesis de {var3}:")
print(f"Motivo de la consulta: {motivo}.")
print(f"Evolución de la enfermedad: {evolucion}.")
print(f"Estado del apetito: {apetito}.")
print(f"Estado del comportamiento: {comportamiento}.")
print("\nLa historia clínica ha sido actualizada exitosamente...")

    # Ahora se realizará el examen físico del paciente

print("\n|--------------------------------------|")
print(f"\nExamen físico de {var3}:\n")

try:
    print("Condición Corporal ->")
    cc = {1:"1. Muy delgado", 2:"2. Delgado", 3:"3. Peso ideal",
          4:"4. Sobrepeso", 5:"5. Obeso"}
    for value in cc:
        print(cc[value])
    cc = int(input(f"\nIndique cuál es la condición corporal de {var3}: "))
    if tipo == 1:
        if cc == 1:
            print(f"\n{var3} se encuentra en una condición corporal muy delgada.")
        elif cc == 2:
            print(f"\n{var3} se encuentra en una condición corporal delgada.")
        elif cc == 3:
            print(f"\n{var3} se mantiene en su peso ideal.")
        elif cc == 4:
            print(f"\n{var3} tiene un sobrepeso considerable.")
        elif cc == 5:
            print(f"\n{var3} tiene un alto grado de obesidad.")
        else:
            print(f"\n¡Ha ocurrido un error! Valor incorrecto.")
    elif tipo == 2:
        if cc == 1:
            print(f"\n{var3} se encuentra en una condición corporal muy delgada.")
        elif cc == 2:
            print(f"\n{var3} se encuentra en una condición corporal delgada.")
        elif cc == 3:
            print(f"\n{var3} se mantiene en su peso ideal.")
        elif cc == 4:
            print(f"\n{var3} tiene un sobrepeso considerable.")
        elif cc == 5:
            print(f"\n{var3} tiene un alto grado de obesidad.")
        else:
            print(f"\n¡Ha ocurrido un error! Valor incorrecto.")
    else:
        print("\nNo contamos actualmente con registros para esta especie.")
        print("Se recomienda un diagnóstico especializado.")
        
    print("\nLa historia clínica ha sido actualizada exitosamente...")
except:
    pass

print("\n¡Gracias por su colaboración!")
