
 
def obtenedor_palabras():
    
    archivo = open("palabras.txt", "r")
    palabras = archivo.readline()
    return palabras.upper()
    
def jugar(palabras):
    completado_palabras = "_" * len(palabras)
    adivinadas = False
    letras_adivinadas = []
    palabras_adivinadas = []
    intentos = 3
    print("Ha empezado el juego!!!")
    print(munequito_ahorcado)
    print(completado_palabras)
    print("\n")

    while not adivinadas and intentos > 0:
        adivina = input("adivina la palabra ").upper()
        if len(adivina) == 1 and adivina.isalpha():
            if adivina in palabras_adivinadas:
                print("adivinaste la letra", adivina)
            elif adivina not in palabras:
                print (adivina, "no esta en la palabra")
                intentos -= 1
                palabras_adivinadas.append(adivina)
            else:
                print("Excelente ", adivina, " esta en la palabra!")
                palabras_adivinadas.append(adivina)
                palabra_como_lista = list(completado_palabras)
                indices = [i for i, letra in enumerate(palabras) if letra == adivina]
                for index in indices:
                    palabra_como_lista[index] = adivina
                completado_palabras = "".join(palabra_como_lista)
                if "_" not in completado_palabras:
                    adivinadas = True

        elif len(adivina) == len(palabras) and adivina.isalpha():
            if adivina in palabras_adivinadas:
                print("Acabas de adivinar la palabra", adivina)
            elif adivina != palabras:
                print(adivina, "no es la palabra.")
                intentos -= 1
                palabras_adivinadas.append(adivina)
            else:
                adivinadas = True
                completado_palabras = palabras

        else:
            print("intento fallido")
        
        print(munequito_ahorcado(intentos))
        print(completado_palabras)
        print("\n")

    if adivinadas:
        print("Felicidades, adivinaste la palabra")
    else:
        print("Lo siento, se acabaron los intentos. La palabra era " + palabras + ". Vuelve a jugar!")


def munequito_ahorcado(intentos):
    estados = [  
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return estados[intentos]

def principal():
    palabras = obtenedor_palabras()
    jugar(palabras)
    while input("Jugar otra vez? (si/no) ").upper == "SI":
        palabras = obtenedor_palabras()
        jugar(palabras)
    
if __name__ == "__principal__":
    principal()


