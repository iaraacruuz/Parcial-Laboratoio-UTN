
from os import system

system("cls")

import re
import csv


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
    contador=0

    for linea in archivo_pokemon:
        contador+=1
        columna = linea.split(",")
        habilidades = columna[5]
        habilidades = habilidades.replace('Ninguna','').strip() 
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
    if contador !=0:
        print("Lista de pokemones del archivo CSV creada exitosamente.")
    else:
        print("Lista de pokemones del archivo CSV  no se creo.")
    return lista



# 2:Listar cantidad por tipo: mostrará todos los tipos indicando la cantidad de
# pokemones que corresponden a ese tipo.

def cantidad_por_tipo(lista_pokemones: list) -> dict:
    '''
        Brief: La función cuenta la cantidad de pokémones por tipo.
        Parámetros:
        lista_pokemones (lista): Una lista de diccionarios de pokémones. Cada diccionario representa
        un pokemon y tiene una clave llamada 'tipo' que contiene una cadena de texto con uno o varios 
        tipos separados por '/'.
        Retorno: Un diccionario que muestra la cantidad de pokemones por tipo. Las claves del diccionario son los tipos y
        los valores son las cantidades correspondientes de pokémones de cada tipo.
    '''

    cantidad_por_tipo = {}
    for pokemon in lista_pokemones:
        tipos = pokemon['Tipo'].split('/')
        for tipo in tipos:
            tipo_minuscula = tipo.lower()
            if tipo_minuscula in cantidad_por_tipo:
                cantidad_por_tipo[tipo_minuscula] += 1
            else:
                cantidad_por_tipo[tipo_minuscula] = 1

    cantidad_por_tipo_combinado = {}
    for tipo, cantidad in cantidad_por_tipo.items():
        tipo_combined = next((t for t in cantidad_por_tipo_combinado.keys() if t.lower() == tipo.lower()), tipo)
        if tipo_combined in cantidad_por_tipo_combinado:
            cantidad_por_tipo_combinado[tipo_combined] += cantidad
        else:
            cantidad_por_tipo_combinado[tipo_combined] = cantidad

    return cantidad_por_tipo_combinado

# #3. Listar pokemones por tipo: mostrará cada tipo indicando el nombre y poder
# # de ataque de cada pokemon que corresponde a ese tipo.

def listar_pokemones_por_tipo(lista_pokemones: list):
    '''
        Brief: La función lista los pokémones por tipo, mostrando el nombre y el poder de ataque de cada pokémon
        que corresponde a ese tipo.
        Parámetros:
        lista_pokemones: Una lista de diccionarios de pokémones. Cada diccionario representa un pokemon.
        Retorno: La función no retorna ningún valor, imprime en la salida la lista de pokemones por tipo.
    '''
    cantidad_por_tipo_dict = cantidad_por_tipo(lista_pokemones)  
    tipos = set(cantidad_por_tipo_dict.keys()) 
    for tipo in tipos:
        print(f"{tipo.capitalize()}:")
        for pokemon in lista_pokemones:
            if any(p_type.lower() == tipo.lower() for p_type in pokemon['Tipo'].split('/')):
                print(f"- {pokemon['Nombre']} ({pokemon['Poder de Ataque']})")
        print()

# 4. Listar pokemones por habilidad: el usuario ingresa la descripción de una
# habilidad y el programa deberá mostrar nombre, tipo y promedio de poder
# entre ataque y defensa.

def listar_pokemones_por_habilidad(habilidad:str, lista_pokemones):
    '''
        Brief: La función busca pokemones por habilidad y muestra en pantalla sus nombres, tipos y promedio de poder.
        Parámetros:
        habilidad (str): La habilidad que se va a buscar en los pokemones.
        lista_pokemones (list): Una lista de diccionarios de pokemones. Cada diccionario representa un pokémon.
        Retorno: Esta función no retorna nada, solo imprime por pantalla los nombres, tipos y promedio de poder
        de los pokemones que tienen la habilidad indicada. Si no se encuentran pokemones con esa habilidad, imprime un mensaje indicándolo.
    '''
    habilidad = habilidad.lower() #convertir a minusculas
    encontrado = False
    for pokemon in lista_pokemones:
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

def listar_pokemones_ordenados(lista_pokemones):
    '''
    Brief: Esta función recibe la lista de pokemones que contiene información sobre los pokémon, 
    los ordena por poder de ataque y nombre, y los imprime en la consola en orden ascendente.
    Parámetros:
    path (str): la ruta del archivo que contiene información sobre los pokémon.
    Retorna: No retorna nada. La función simplemente imprime información en la consola.
    '''
    for i in range(len(lista_pokemones)-1):
        for j in range(i+1, len(lista_pokemones)):
            if lista_pokemones[i]["Poder de Ataque"].isdigit() and lista_pokemones[j]["Poder de Ataque"].isdigit():
                if int(lista_pokemones[i]["Poder de Ataque"]) > int(lista_pokemones[j]["Poder de Ataque"]):
                    lista_pokemones[i], lista_pokemones[j] = lista_pokemones[j], lista_pokemones[i]
                elif int(lista_pokemones[i]["Poder de Ataque"]) == int(lista_pokemones[j]["Poder de Ataque"]):
                    if lista_pokemones[i]["Nombre"] > lista_pokemones[j]["Nombre"]:
                        lista_pokemones[i], lista_pokemones[j] = lista_pokemones[j], lista_pokemones[i]
    for pokemon in lista_pokemones:
        print(f"Nombre: {pokemon['Nombre']}, Tipo: {pokemon['Tipo']}, Poder de Ataque: {pokemon['Poder de Ataque']}, Poder de Defensa: {pokemon['Poder de Defensa']}")



# 6. Guardar Json: Generará un archivo de tipo Json con los pokemones de un
# tipo específico (lo ingresa el usuario). En el mismo se guardará el nombre del
# pokemon, el mayor valor entre los puntos de ataque y defensa, y por último el
# tipo de poder. Por ejemplo:
import json
def guardar_json(tipo:str, lista_pokemones):
    '''
        Brief: Genera un archivo JSON con los pokemones de un tipo especifico.
        Parámetros:
        tipo (str): Es el tipo especifico de pokemones que se desea guardar en el archivo JSON.
        lista_pokemones (list): Una lista de diccionarios de pokemones que contiene la información de cada uno.
        Retorno: La función retorna la ruta del archivo JSON si se guarda correctamente, o None si no hay pokemones del
        tipo especificado en el archivo CSV. En caso de que no se pueda guardar el archivo JSON, la función levantaría una excepción.
    '''

    pokemon_tipo=[]
      # Conjunto para almacenar nombres de Pokémon ya agregados

    contador=0
    for pokemon in lista_pokemones:
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

    ruta_archivo = os.path.join(os.getcwd(), f"{tipo}.json")  
    with open(ruta_archivo, "w") as archivo:
        json.dump(pokemon_tipo, archivo, indent=4)
    return ruta_archivo



#7 Leer Json: permitirá mostrar un listado con los pokemones guardados en el
# archivo Json de la opción 5.

import json
import os
def leer_json( tipo) -> list:
    '''
        Brief: Lee un archivo JSON y muestra un listado de los pokemones guardados.
        Parametros:
        tipo (str): La ruta del archivo JSON que se desea leer.
        Retorno: Retorna una lista de diccionarios que representa los pokemones guardados en el archivo JSON.
    
    '''
    with open(tipo, 'r', encoding='utf-8') as archivo:
        diccionario_pokemones = json.load(archivo)
    return diccionario_pokemones


# A. Agregar pokemon: el usuario ingresará los datos de un pokemon, y el mismo se agregará a la lista, siempre y cuando este ya no esté cargado.
def agregar_pokemon(lista_pokemones):
    '''
        Brief: Agrega un nuevo pokémon a la lista de pokemones.
        Parametros:
        lista_pokemones (list): La lista de diccionarios de pokemones donde se agregarán los datos del nuevo pokémon.
        Retorno: Retorna la lista de pokemones actualizada con el nuevo pokémon agregado, o None si el pokemon ya esta
        en la lista o si se produce un error al ingresar los datos.
    '''
    numero = input("Ingrese el número de Pokédex: ")
    
    for pokemon in lista_pokemones:
        if pokemon["N° Pokedex"] == numero.zfill(3):
            print("El Pokémon ya está en la lista")
            return None


    nombre = input("Ingrese el nombre del Pokémon: ")

    for pokemon in lista_pokemones:
        if pokemon['Nombre'] == nombre:
            print("Error: el Pokémon ya existe en la lista.")
            return None
        
    tipo = input("Ingrese el tipo de Pokémon: ")
    poder_ataque = input("Ingrese el poder de ataque: ")
    while not poder_ataque.isdigit():
        print("Error: debe ingresar un valor numérico.")
        poder_ataque = input("Ingrese el poder de ataque del Pokémon que quiere agregar: ")
    poder_defensa = input("Ingrese el poder de defensa que quiere agregar: ")
    while not poder_defensa.isdigit():
        print("Error: debe ingresar un valor numérico.")
        poder_defensa = input("Ingrese el poder de defensa que quiere agregar: ")
    habilidades = input("Ingrese las habilidades del Pokémon, separadas por comas:")
    habilidades = [habilidad.strip() for habilidad in habilidades.split(",")]

    nuevo_pokemon = {
        "N° Pokedex": numero,
        "Nombre": nombre,
        "Tipo": tipo,
        "Poder de Ataque": poder_ataque,
        "Poder de Defensa": poder_defensa,
        "Habilidades": habilidades
    }


    lista_pokemones.append(nuevo_pokemon)
    print("Se ha agregado el nuevo pokémon")

    return lista_pokemones


    
   
# B. Guardar datos de los pokemones en csv:


def guardar_pokemon_en_csv(pokemon, path):
    '''
        Brief: Guarda los datos de un pokémon en un archivo CSV.
        Parametros:
        pokemon (dict): Un diccionario con los datos del pokemon que se desea guardar.
        path (str): La ruta del archivo CSV donde se guardaran los datos
    '''
    with open(path, mode="a", newline="", encoding="UTF-8") as archivo_csv:
        habilidades_str = ', '.join(pokemon["Habilidades"])
        fila = f'{pokemon["N° Pokedex"]},{pokemon["Nombre"]},{pokemon["Tipo"]},{pokemon["Poder de Ataque"]},{pokemon["Poder de Defensa"]},{habilidades_str}\n'
        archivo_csv.write(fila)

    print("Los datos del pokemon se han guardado en el archivo CSV.")




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
    lista_pokemones_aprobada = False
    
    while True:
        respuesta= menu_principal()
        if respuesta.isdigit() and 1 <= int(respuesta) <= 9:
                match respuesta:
                    case "1":
                        lista_pokemones=  pokemones_csv("pokemones.csv")
                        lista_pokemones_aprobada= True

                    case "2":
                        if lista_pokemones_aprobada:
                            cantidad_por_tipo_dict = cantidad_por_tipo(lista_pokemones)  
                            for tipo, cantidad in cantidad_por_tipo_dict.items():
                                print(f"{tipo}: {cantidad}")
                        else:
                            print("No se cargó la lista de pokemon")
                    case "3":

                        if lista_pokemones_aprobada:
                            listar_pokemones_por_tipo(lista_pokemones)
                        else:
                            print("No se cargo la lista de pokemones correctamente.Por favor solicita la opcion 1 otra vez")

                    case "4":
                        if lista_pokemones_aprobada:
                            habilidad = input("Ingresa la habilidad,acuerdese de poner el tilde si es que corresponde: ")
                            listar_pokemones_por_habilidad(habilidad, lista_pokemones)
                        else:
                            print("No se cargo la lista de pokemones correctamente.Por favor solicita la opcion 1 otra vez")
                    case "5":
                        if lista_pokemones_aprobada:
                            listar_pokemones_ordenados(lista_pokemones)
                        else:
                            print("No se cargo la lista de pokemones correctamente.Por favor solicita la opcion 1 otra vez")
                    case "6":
                        if lista_pokemones_aprobada:
                            tipo = input("Ingrese el tipo de pokemon a guardar en el archivo JSON: ")
                            guardar_json( tipo, lista_pokemones)
                        else:
                            print("No se cargo la lista de pokemones correctamente.Por favor solicita la opcion 1 otra vez")

                    case "7":

                            if lista_pokemones_aprobada:
                                    tipo = input("Ingrese el tipo de archivo JSON que desea leer: ")
                                    ruta_archivo_json = guardar_json(tipo, lista_pokemones) 
                                    lista_pokemones_json = leer_json(ruta_archivo_json)  
                                    
                                    print(json.dumps(lista_pokemones_json, indent=4, ensure_ascii = False))
                            else:
                                print("No se cargó la lista de pokemones")
      

                    case "8":

                        if lista_pokemones_aprobada:
                            lista_pokemones = pokemones_csv('pokemones.csv')
                            nuevo_pokemon = agregar_pokemon(lista_pokemones,)
                            if nuevo_pokemon is not None:
                                guardar_pokemon_en_csv(lista_pokemones[-1], "pokemones.csv")
                        else:
                            print("No se cargo la lista de pokemones correctamente.Por favor solicita la opcion 1 otra vez")
                    case "9":
                        break
        else:
            print("ERROR, OPCION INEXISTENTE, VUELVA A INGRESAR OTRA VEZ UNA OPCION DEL 1 AL 9")
opciones()

