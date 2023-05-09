from os import system

system("cls")

import re


def pokemones_csv(path:str)->list:
    '''
    Brief: Lee un archivo CSV con información de Pokemones y retorna una lista de diccionarios
    con los datos de cada uno.
    Parametros:
    path: string que indica la ubicación del archivo CSV.
    Retorna: lista de diccionarios, donde cada diccionario representa un Pokemon y contiene las 
    siguientes claves: nro de pokedex, nombre, tipo, poder de ataque y defensa y habilidades.
    
    '''

    lista=[]
    archivo_pokemon= open(path, "r")
    for linea in archivo_pokemon:
        columna = linea.split(",")
        habilidades = columna[5]
        habilidades = habilidades.replace('Ninguna','').strip() # Remover "Ninguna" de la lista de habilidades
        habilidades = habilidades.split(',')
        pokemon = {
            "N° Pokedex": columna[0].zfill(3),
            "Nombre": columna[1],
            "Tipo": columna[2],
            "Poder de Ataque": columna[3],
            "Poder de Defensa": columna[4],
            "Habilidades": habilidades 
        }
        lista.append(pokemon)
    
    archivo_pokemon.close()
    return lista

   



#2:Listar cantidad por tipo: mostrará todos los tipos indicando la cantidad de
# pokemones que corresponden a ese tipo.
def cantidad_por_tipo(path:str):
    '''
    Brief: la función cantidad_por_tipo toma como entrada la ruta de un archivo CSV que contiene
    información de pokemones y devuelve un diccionario con la cantidad de pokemones por tipo.
    Parámetros:
    path: una cadena de caracteres que representa la ruta del archivo CSV a procesar.
    Retorna: un diccionario donde las claves son los tipos de los pokemones encontrados en el archivo CSV 
    y los valores son las cantidades de pokemones correspondientes a cada tipo.
    
    '''
    pokemones= pokemones_csv(path)
    cantidad_por_tipo= {}
    for pokemon in pokemones:
        tipos = pokemon['Tipo'].split('/')
        for tipo in tipos:
            if tipo in cantidad_por_tipo:
                cantidad_por_tipo[tipo] += 1
            else:
                cantidad_por_tipo[tipo] = 1

    return cantidad_por_tipo




#3. Listar pokemones por tipo: mostrará cada tipo indicando el nombre y poder
# de ataque de cada pokemon que corresponde a ese tipo.


def listar_pokemones_por_tipo(path:str):
    '''
    Esta funcion hace lo siguiente:
    Brief: Crea una lista de pokemones por el tipo.
    Parametros:
    Path: la ruta del archivo csv , que contiene info
    de los pokemones, y es del tipo str.
    Luego se recorre con un for los tipos
    Retorna: simplemente imprime por la consola la lista de
    Pokemones agrupados por tipo. Y al llamar la funcion los muestra.
    
    '''
    pokemones = pokemones_csv(path)
    cantidad_por_el_tipo = cantidad_por_tipo(path)
    tipos = set(cantidad_por_el_tipo.keys()) 
    for tipo in tipos:
        print(f"{tipo}:")
        for pokemon in pokemones:
            if tipo in pokemon["Tipo"].split('/'):
                print(f"- {pokemon['Nombre']} ({pokemon['Poder de Ataque']})")
        print()




# 4. Listar pokemones por habilidad: el usuario ingresa la descripción de una
# habilidad y el programa deberá mostrar nombre, tipo y promedio de poder
# entre ataque y defensa.

def listar_pokemones_por_habilidad(path:str, habilidad:str):
    '''
    Brief: listar_pokemones_por_habilidad
    Parámetros: 
    path es la ruta del archivo CSV que contiene los datos de los pokemones, y habilidad
    es la habilidad que se va a buscar en los pokemones.
    Retorna: esta función no retorna nada, simplemente imprime por pantalla los nombres, tipos y promedio
    de poder de los pokemones que tienen la habilidad indicada. Si no se encuentran pokemones con esa habilidad, 
    imprime un mensaje indicándolo.
    '''
    pokemones = pokemones_csv(path)
    habilidad = habilidad.lower() # Convertir a minúsculas
    encontrado = False
    for pokemon in pokemones:
        habilidades = pokemon['Habilidades']
        for cada_habilidad in habilidades:
            if re.search(habilidad, cada_habilidad.lower()): 
                poder_total = int(pokemon['Poder de Ataque']) + int(pokemon['Poder de Defensa'])
                promedio = poder_total / 2
                print(f"Nombre: {pokemon['Nombre']}, Tipo: {pokemon['Tipo']}, Promedio: {promedio}")
                encontrado = True
    if not encontrado:
        print("No se encontraron pokemones con la habilidad indicada.")


# #5:Listar pokemones ordenados: mostrará todos los datos de los pokemones
# # ordenados por poder de ataque y en caso de coincidir en el valor, por nombre
# de la A-Z.

def listar_pokemones_ordenados(path:str):
    '''
    Brief: Esta función recibe una ruta de archivo (path) que contiene información sobre los pokémon, 
    los ordena por poder de ataque y nombre, y los imprime en la consola en orden ascendente.
    Parámetros:
    path (str): la ruta del archivo que contiene información sobre los pokémon.
    Retorna: No retorna nada. La función simplemente imprime información en la consola.
    '''
    pokemones = pokemones_csv(path)
    for i in range(len(pokemones)-1):
        for j in range(i+1, len(pokemones)):
            if pokemones[i]["Poder de Ataque"].isdigit() and pokemones[j]["Poder de Ataque"].isdigit():
                if int(pokemones[i]["Poder de Ataque"]) > int(pokemones[j]["Poder de Ataque"]):
                    pokemones[i], pokemones[j] = pokemones[j], pokemones[i]
                elif int(pokemones[i]["Poder de Ataque"]) == int(pokemones[j]["Poder de Ataque"]):
                    if pokemones[i]["Nombre"] > pokemones[j]["Nombre"]:
                        pokemones[i], pokemones[j] = pokemones[j], pokemones[i]
    for pokemon in pokemones:
        print(f"Nombre: {pokemon['Nombre']}, Tipo: {pokemon['Tipo']}, Poder de Ataque: {pokemon['Poder de Ataque']}, Poder de Defensa: {pokemon['Poder de Defensa']}")



# 6. Guardar Json: Generará un archivo de tipo Json con los pokemones de un
# tipo específico (lo ingresa el usuario). En el mismo se guardará el nombre del
# pokemon, el mayor valor entre los puntos de ataque y defensa, y por último el
# tipo de poder. Por ejemplo:
import json
def guardar_json(path:str, tipo:str):
    '''
    Brief: esta funcion recibe una ruta del archivo (path), que contiene la informacion sobre los pókemon,
    y tipo: que es un string que luego sera utilizado para reemplazar el tipo que se desea buscar en el archivo csv.
    Retorna:
    La función retorna el string tipo si se guardo correctamente el archivo JSON o None si no hay pokemones del tipo
    especificado en el archivo CSV. En caso de que no se pueda guardar el archivo JSON, la función levantaría una excepción.
    
    '''

    pokemones= pokemones_csv(path)
    pokemon_tipo=[]
    contador=0
    for pokemon in pokemones:
        if pokemon["Tipo"].lower() == tipo.lower():
            contador +=1
            poder_ataque = int(pokemon["Poder de Ataque"])
            poder_defensa = int(pokemon["Poder de Defensa"])
            if poder_ataque > poder_defensa:
                max_puntos = poder_ataque
                tipo_puntos_a_mostrar= "Ataque"
            elif poder_ataque< poder_defensa:
                max_puntos = poder_defensa
                tipo_puntos_a_mostrar= "Defensa"
            else:
                max_puntos = poder_defensa
                tipo_puntos_a_mostrar= "Ambos"
            pokemon_tipo.append({
                "Nombre": pokemon["Nombre"],
                "Mayor Puntos": max_puntos,
                "Tipo de Poder": tipo_puntos_a_mostrar
            })
    if contador == 0:
        print(f"No hay pokemones del tipo '{tipo}' en el archivo CSV")
        return

    with open(f"{tipo}.json", "w") as archivo:
        json.dump(pokemon_tipo, archivo, indent=4)
    return tipo


# 6 parte dos:

def leer_el_archivo_json(tipo:str):
    '''
    Brief: Esta función tiene como objetivo leer un archivo JSON que contiene información de los pokemones de un
    cierto tipo.
    Parámetros:
    tipo: una cadena de texto que representa el nombre del archivo JSON a leer. Si la extensión ".json" no está presente
    en el nombre, la función la agregara automáticamente.
    Retorna: una lista de diccionarios que contiene información de los pokemones del tipo especificado en el archivo JSON
    '''
    if "." not in tipo:
        tipo += ".json"
    with open(tipo, "r", encoding='utf-8') as archivo:
        datos_pokemones = json.load(archivo)
    return datos_pokemones




#7 Leer Json: permitirá mostrar un listado con los pokemones guardados en el
# archivo Json de la opción 5.

def leer_json_de_pokemones_ordenados()->list:
    '''
    Tiene como objetivo leer un archivo csv que contiene la infor de los pokemones, ordenarla alfabeticamente
    por nombre y guardarla. No recibe parametros ni retorna nada. Su función es simplemente mostrar en pantalla el
    contenido del archivo JSON generado y un mensaje indicando que se creo correctamente el archivo
    '''
    pokemones_ordenados= listar_pokemones_ordenados("pokemones.csv")
    with open("pokemones_ordenados.json", 'w', encoding='utf-8') as archivo:
            json.dump(pokemones_ordenados, archivo)
    print(json.dumps(pokemones_ordenados))
    print("El archivo pokemones_ordenados.json fue creado exitosamente.")




# A. Agregar pokemon: el usuario ingresará los datos de un pokemon, y el mismo se agregará a la lista, siempre y cuando este ya no esté cargado.
def agregar_pokemon(path):
    pokemones= pokemones_csv(path)
    numero= input("Ingrese el numero de Pokedex, si tiene ceros delante respetelos: ")
    nombre= input(" Ingrese el nombre del Pokemon: ")
    tipo= input("Ingrese el tipo de Pokemon: ")
    poder_ataque= input("Ingrese el poder de ataque:")
    poder_defensa= input("Ingrese el poder de defensa:")
    habilidades= input("Ingrese las habilidades del pokemon, separadas por comas:")
    habilidades= habilidades.split(",")
    habilidades = [habilidad.strip() for habilidad in habilidades]
    for pokemon in pokemones:
        if pokemon["Nombre"]== nombre:
            print("El pokemon ya esta en la lista")
            return
        nuevo_pokemon={
            "N° Pokedex": numero,
            "Nombre": nombre,
            "Tipo": tipo,
            "Poder de Ataque": poder_ataque,
            "Poder de Defensa": poder_defensa,
            "Habilidades": habilidades 
        }
        pokemones.append(nuevo_pokemon)
    print("Ya se cargo el nuevo pokemon")
    return pokemones





# B. Guardar datos de los pokemones en csv:
import csv
def guardar_los_poke_en_csv(pokemones:list):
        with open("pokemones.csv", mode= "a", encoding="utf-8") as archivo_csv:
            archivo_csv.write("N° Pokedex, Nombre, Tipo, Poder de Ataque, Poder de Defensa, Habilidades \n")
            for pokemon in pokemones:
                linea= ','.join([pokemon["N° Pokedex"], pokemon["Nombre"], pokemon["Tipo"], pokemon["Poder de Ataque"], pokemon["Poder de Defensa"], ",".join(pokemon["Habilidades"])])
                archivo_csv.write(linea + "\n")



        








#8:
def imprimir_menu():
    print('''1- Mostrar los datos del archivo csv: 
    2- Mostrar listados la CANTIDAD por tipo: 
    3- Mostrar listados los pokemones por tipo:
    4- Mostrar listados los pokemones por HABILIDAD:
    5- Mostrar ordenados lo pokemones por 'poder de ataque': 
    6- Se crea un archivo JSON con el tipo que ingrese:
    7- Mostrar el archivo JSON que se creo: 
    8- Agregar Pokemon:
    9- Salir: ''')

def menu_principal():
    imprimir_menu()
    respuesta= input("INgrese una opcion: ")
    return respuesta

def opciones():
    while True:
        respuesta= menu_principal()
        match respuesta:
            case "1":
                lista_pokemones = pokemones_csv("pokemones.csv")
                for pokemon in lista_pokemones:
                            print(pokemon)
            case "2":
                print(cantidad_por_tipo("pokemones.csv"))
            case "3":
                print(listar_pokemones_por_tipo("pokemones.csv"))
            case "4":
                habilidad = input("Ingresa la habilidad,acuerdese de poner el tilde si es que corresponde: ")
                print(listar_pokemones_por_habilidad("pokemones.csv", habilidad))
            case "5":
                print(listar_pokemones_ordenados("pokemones.csv"))
            case "6":
                tipo = input("Ingrese el tipo de pokemon a guardar en el archivo JSON: ")
                nombre= guardar_json("pokemones.csv", tipo)
                datos_pokemones= leer_el_archivo_json(nombre)
                print(json.dumps(datos_pokemones, indent=4))

            case "7":
                leer_json_de_pokemones_ordenados()

            case "8":

                
                print(agregar_pokemon("pokemones.csv"))

            case "9":
                break
opciones()