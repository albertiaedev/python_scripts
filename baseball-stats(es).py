print("|::-MUÉSTRANOS TUS ESTADÍSTICAS DE BÉISBOL-::|")

jugador = input("\nIngrese el nombre del jugador: ")
equipo = input("\nIngrese el nombre del equipo: ")
posicion = input("\nIngrese la posición que juega: ")

print("\n|::-Menú de estadísticas-::|\n")
stat = {1:'1.Bateo.', 2:'2.Pitcheo.', 3:'3.Fildeo.'}
for value in stat:
    print(stat[value])
stat = int(input("\nSeleccione las estadísticas a calcular: "))

if stat == 1:
    print("\n|::-Estadísticas de bateo-::|\n")
    batting = {1:'1.AVG.', 2:'2.SLG.', 3:'3.OBP.', 4:'4.Salir.'}
    for value in batting:
        print(batting[value])
    batting = int(input("\nSeleccione una estadística de bateo: "))
    # Calculemos las estadísticas de bateo
    if batting == 1:
        print("\nPromedio de bateo (AVG)->")
        AB = int(input('\nIndique la cantidad de turnos al bate: '))
        H = int(input('\nIndique la cantidad de hits conectados: '))
        AVG = H/AB # Promedio de bateo
        print(f"\nEl promedio de bateo de {jugador} es: {AVG:.3f}")
    elif batting == 2:
        print("\nPromedio de slugging (SLG)->")
        AB = int(input('\nIndique la cantidad de turnos al bate: '))
        H1 = int(input('\nIndique la cantidad de sencillos conectados: '))
        H2 = int(input('\nIndique la cantidad de dobles conectados: '))
        H3 = int(input('\nIndique la cantidad de triples conectados: '))
        HR = int(input('\nIndique la cantidad de jonrones conectados: '))
        SLG = (H1+(H2*2)+(H3*3)+(HR*4))/AB # Promedio de slugging
        print(f"\nEl promedio de slugging de {jugador} es: {SLG:.3f}")
    elif batting == 3:
        print("\nPorcentaje de bases alcanzadas (OBP)->")
        AB = int(input('\nIndique la cantidad de turnos al bate: '))
        H = int(input('\nIndique la cantidad de hits conectados: '))
        BB = int(input('\nIndique la cantidad de bases por bolas recibidas: '))
        HBP = int(input('\nIndique la cantidad de veces que el bateador fue golpeado por la pelota: '))
        SAC_FLY = int(input('\nIndique la cantidad de elevados de sacrificio: '))
        OBP = (H+BB+HBP)/(AB+BB+HBP+SAC_FLY) # Porcentaje de bases alcanzadas
        print(f"\nEl porcentaje de bases alcanzadas de {jugador} es: {OBP:.3f}")
    elif batting == 4:
        salir = int(input("\n¿Seguro que desea salir?\n[Presione 0 para salir] -> "))
        if salir == 0:
            print("\nNos vemos pronto con mejores números al bate...")
        else:
            print("\nReinicie el sistema...")
    else:
        print("\nHa ocurrido un error.")
        print("\nNo se reconoce esta acción.")
elif stat == 2:
    print("\n|::-Estadísticas de pitcheo-::|\n")
    pitching = {1:'1.ERA.', 2:'2.WHIP.', 3:'3.WP.', 4:'4.Salir.'}
    for value in pitching:
        print(pitching[value])
    pitching = int(input("\nSeleccione una estadística de pitcheo: "))
    # Calculemos las estadísticas de pitcheo
    if pitching == 1:
        print("\nEfectividad (ERA)->")
        IL = float(input("\nIndique la cantidad de innings lanzados: "))
        CP = int(input("\nIndique la cantidad de carreras permitidas: "))
        ERA = (CP*9)/(IL) # Efectividad
        print(f"\nLa efectividad de {jugador} es: {ERA:.2f}")
    elif pitching == 2:
        print("\nPorcentaje de bases concedidas (WHIP)->")
        IL = float(input("\nIndique la cantidad de innings lanzados: "))
        H = int(input("\nIndique la cantidad de hits permitidos: "))
        BB = int(input("\nIndique la cantidad de bases por bolas otorgadas: "))
        WHIP = (H+BB)/(IL) # Porcentaje de bases concedidas
        print(f"\nEl porcentaje de bases concedidas de {jugador} es: {WHIP:.2f}")
    elif pitching == 3:
        print("\nPorcentaje de juegos ganados (WP)->")
        JG = int(input("\nIndique el total de juegos ganados: "))
        JD = int(input("\nIndique el total de juegos decididos: "))
        WP = JG/JD # Porcentaje de juegos ganados
        print(f"\nEl porcentaje de juegos ganados de {jugador} es: {WP:.2f}")
    elif pitching == 4:
        salir = int(input("\n¿Seguro que desea salir?\n[Presione 0 para salir] -> "))
        if salir == 0:
            print("\nNos vemos pronto con mejores números en el montículo...")
        else:
            print("\nReinicie el sistema...")
    else:
        print("\nHa ocurrido un error.")
        print("\nNo se reconoce esta acción.")
elif stat == 3:
    print("\n|::-Estadísticas de fildeo-::|\n")
    fielding = {1:'FA.', 2:'2.Salir.'}
    for value in fielding:
        print(fielding[value])
    fielding = int(input("\nSeleccione una estadística de fildeo: "))
    # Calculemos las estadísticas de fildeo
    if fielding == 1:
        print("\nPromedio de fildeo (FA)->")
        OUT = int(input("\nIndique la cantidad de jugadores sacados out:"))
        A = int(input("\nIndique la cantidad de asistencias realizadas:"))
        E = int(input("\nIndique la cantidad de errores realizados:"))
        FA = (OUT+A)/(OUT+A+E) # Promedio de fildeo
        print(f"\nEl promedio de fildeo de {jugador} es: {FA:.3f}")
    elif fielding == 2:
        salir = int(input("\n¿Seguro que desea salir?\n[Presione 0 para salir] -> "))
        if salir == 0:
            print("\nNos vemos pronto con mejores números en el diamante...")
        else:
            print("\nReinicie el sistema...")
    else:
        print("\nHa ocurrido un error.")
        print("\nNo se reconoce esta acción.")
else:
    print("\nHa ocurrido un error.")
    print("\nNo hay estadísticas para calcular.")
