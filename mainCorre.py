import random
import time

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Creo la clase persona para poder darle atributos al jugador.
class persona():
    def __init__(self, nombre, vida, viviendo, cansancio):
        self.Nombre = nombre
        self.Vida = vida
        self.Viviendo = viviendo
        self.Cansancio = cansancio

    def estado(self):
        print("Nombre:", self.Nombre,"\nVida:", self.Vida,"%\nSigue vivo:", self.Viviendo,"\nCansancio:",(10*self.Cansancio),"%")
    
    def check(self):

        if self.Cansancio >= 10:
            self.Vida = self.Vida - 25
            self.Cansancio = 10
        elif self.Cansancio < 0:
            self.Cansancio = 0
        
        if self.Viviendo == False:
            self.Vida = 0
        elif self.Vida == 0:
            self.Viviendo = False
        elif self.Vida > 100:
            self.Vida = 100 
        
        if self.Viviendo == True:
            if self.Cansancio >= 9 and self.Vida <= 25:
                print("Estas muy herido y cansado...")
            elif self.Cansancio >= 9 and self.Vida > 25:
                print("Estas muy cansado...")
            elif self.Cansancio < 9 and self.Vida <= 25:
                print("Estas muy herido...")

            if self.Cansancio >= 9 or self.Vida <= 25:
                time.sleep(1)
                print("Tienes que encontrar un poblado pronto o moriras...")    

            print("Te quedan",self.Vida,"% ","de vida.\nTu nivel de cansancio es",(10*self.Cansancio),"%\n")

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Funcion para narrar la introduccion del juego
def intro():
    time.sleep(1)
    print("\nUn virus sin identificar se empieza a propagar por el mundo, \nlos primeros infectados empiezan a morir y a las pocas horas \nregresan a la vida atacando a todo aquel que encuentren a su paso. \nNadie estaba preparado para algo parecido...")
    time.sleep(8)
    print("\nTe persigue una horda de zombies, trata de escapar de ellos, \npero cuidado! no todos los caminos conducen a buen destino...\nVeamos que tan lejos puedes acompañar a",romualdo.Nombre,"sin que muera...")
    time.sleep(8)
    print("\nFrente a ti tienes 2 caminos")

    opciones() # Llamo a la funcion que muestras las opciones disponibles de camino

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Defino dos diccionarios para limpiar un poco el codigo de las funciones caminoAleatorio(), sospechaCamino(), buffsCamino() y sigueVivo()
# Diccionario para los caminos
diccionarioCaminos =   {"Camino_1":"terminas en el mar, todo parece tranquilo pero un grupo de piratas \nte encuentran y te llevan prisionero en su barco... A los pocos \ndías mueres de hambre...\n",
                        "Camino_2":"te topas con dos refugiados y una pequeña fogata a la orilla del \ncamino. Te convidan de su comida y te ayudan con tus heridas.\n",
                        "Camino_3":"llegas a una cascada de 15 metros! Te esfuerzas por escalarla y \ndesde arriba observas unos animales en el bosque... Apuras el paso \ny llegas a otro cruce.\n",
                        "Camino_4":"te ataca una manada de lobos hambrientos! Corres por tu vida pero \nlogran morderte un poco.\n",
                        "Camino_5":"te encuentras un campamento de canivales! Logras escapar a través \ndel bosque pero sufriste heridas.\n",
                        "Camino_6":"llegas a un pequeño arroyo, aprovechas para limpiarte las heridas \ny beber un poco de agua antes de continuar con el viaje.\n",
                        "Camino_7":"te encuentras un transehunte delirante que asegura haber visto \npiratas... Sigues tu camino y llegas un nuevo cruce.\n",
                        "Camino_8":"llegas a un poblado! Un habitante te invita a pasar la noche \nen el granero de su casa, te da alimentos, cura tus heridas y te \npermite darte una ducha antes de dormir.\nAl día siguientes continuas tu viaje.\n",
                        "Camino_9":"termina en un precipicio! Puedes ver que del otro lado hay un \npueblo, pero el puente que cruza hasta el otro lado esta roto, \nlos zombies te alcanzan y mueres...\n",
                        "Camino_10":"resulta ser un sendero tranquilo que te lleva a un nuevo cruce.\n",
                       }

# Diccionario para las pistas de los caminos
diccionarioPistas =    {"Pista_1":"desemboca en un pequeño arroyo",
                        "Pista_2":"conduce a un pequeño poblado",
                        "Pista_3":"desemboca en un pequeño arroyo",
                        "Pista_4":"es un sendero tranquilo",
                        "Pista_5":"conduce a un pequeño poblado",
                        "Pista_6":"desemboca en un pequeño arroyo",
                        "Pista_7":"es un sendero tranquilo",
                        "Pista_8":"conduce a un pequeño poblado",
                        "Pista_9":"conduce a un pequeño poblado",
                        "Pista_10":"es un sendero tranquilo",
                       }

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Funcion que devuelve de manera aleatoria uno de los 10 caminos posibles
def caminoAleatorio():

    caminoRandom = random.randint(1,10)

    if caminoRandom == 1:
        return "Camino_1"
    elif caminoRandom == 2:
        return "Camino_2"
    elif caminoRandom == 3:
        return "Camino_3"
    elif caminoRandom == 4:
        return "Camino_4"
    elif caminoRandom == 5:
        return "Camino_5"
    elif caminoRandom == 6:
        return "Camino_6"
    elif caminoRandom == 7:
        return "Camino_7"
    elif caminoRandom == 8:        
        return "Camino_8"
    elif caminoRandom == 9:
        return "Camino_9"
    elif caminoRandom == 10:
        return "Camino_10"
    else:
        return "Verificar porque algo anda mal... caminoAleatorio()"

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Funcion que devuelve pistas sobre los caminos generados aleatoriamente
def sospechaCamino(sospecha):

    if sospecha == "Camino_1":
        return "Pista_1"
    elif sospecha == "Camino_2":
        return "Pista_2"
    elif sospecha == "Camino_3":
        return "Pista_3"
    elif sospecha == "Camino_4":
        return "Pista_4"
    elif sospecha == "Camino_5":
        return "Pista_5"
    elif sospecha == "Camino_6":
        return "Pista_6"
    elif sospecha == "Camino_7":
        return "Pista_7"
    elif sospecha == "Camino_8":
        return "Pista_8"
    elif sospecha == "Camino_9":
        return "Pista_9"
    elif sospecha == "Camino_10":
        return "Pista_10"
    else:
        return "Verificar porque algo anda mal... sospechaCamino()"

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Funcion que devuelve los daños o curaciones de los caminos generados aleatoriamente
def buffsCamino(buffs):

    if buffs == "Camino_1":
        romualdo.Cansancio = 10
        return -100
    elif buffs == "Camino_2":
        romualdo.Cansancio = romualdo.Cansancio - 2
        return 5
    elif buffs == "Camino_3":
        romualdo.Cansancio = romualdo.Cansancio + 2
        return 0
    elif buffs == "Camino_4":
        romualdo.Cansancio = romualdo.Cansancio + 3
        return -20
    elif buffs == "Camino_5":
        romualdo.Cansancio = romualdo.Cansancio + 4
        return -25
    elif buffs == "Camino_6":
        romualdo.Cansancio = romualdo.Cansancio - 1
        return 0
    elif buffs == "Camino_7":
        romualdo.Cansancio = romualdo.Cansancio + 1
        return 0
    elif buffs == "Camino_8":
        romualdo.Cansancio = 0
        return 100
    elif buffs == "Camino_9":
        romualdo.Cansancio = 10
        return -100
    elif buffs == "Camino_10":
        romualdo.Cansancio = romualdo.Cansancio + 1
        return 0
    else:
        return "Verificar porque algo anda mal... buffsCamino()"

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Funcion que devuelve si romualdo continua con vida o no
def sigueVivo(vive):

    if vive == "Camino_1":       
        return False
    elif vive == "Camino_2":
        return True
    elif vive == "Camino_3":
        return True
    elif vive == "Camino_4":
        return True
    elif vive == "Camino_5":
        return True
    elif vive == "Camino_6":
        return True
    elif vive == "Camino_7":
        return True
    elif vive == "Camino_8":        
        return True 
    elif vive == "Camino_9":
        return False
    elif vive == "Camino_10":
        return True
    else:
        return "Verificar porque algo anda mal... sigueVivo()"

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Funcion para que el jugador elija un camino 
def eleccion():

    camino = ""
    letras = 0

    # Loop para que el jugador elija un camino, solo sale del loop si elige 1 o 2
    # El try-except es para evitar que el programa caiga si ingresa una letra
    while camino != 1 and camino != 2:
        try:
            camino = int(input("\n¿Camino 1 o camino 2?: "))
            time.sleep(2)
        except ValueError:
            print("\n¡ATENCION!\nNo se pueden ingresar letras.\nPor favor vuelve a intentarlo.")
            letras = letras + 1
            if letras >= 3:
                print("\nLos caracteres permitidos son el numero 1 y el numero 2.\nPor favor vuelve a intentarlo.")
    return camino

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Funcion que nos muestra las opciones de camino disponibles para elegir, con pistas
def opciones():
    if diccionarioPistas[sospechaUno] == diccionarioPistas[sospechaDos]:
        print(" El camino 1 parecen que",diccionarioPistas[sospechaUno],", y el camino 2... Tambien!") # Muestra si ambas pistas son iguales 
        time.sleep(1)
        print("\nElige con cuidado, tu vida depende de ello...")
    else:
        print(" 1. Este camino parece que",diccionarioPistas[sospechaUno]) # Muestra una pista de lo que parece que hay en el camino 1 
        print(" 2. Este camino parece que",diccionarioPistas[sospechaDos]) # Muestra una pista de lo que parece que hay en el camino 2
        time.sleep(1)
        print("\nElige con cuidado, tu vida depende de ello...")

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Funcion que nos muestra el mensaje de finalización del juego
def mensajeFin():

    time.sleep(2)
    print (romualdo.Nombre,"logró recorrer",distanciaRecorrida,"kms antes de morir.")
    time.sleep(1)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GAME OVER MI CIELA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Declaración de variables y estados iniciales
distanciaRecorrida = 0 # Empezamos en 0 por ahora je

# Este for es solo para generar 50 espacios vacíos antes de arrancar el programa...
for i in range(50):
    print("\n")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CORRE ROMUALDO ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

romualdo = persona("Romualdo",100,True,0) # Defino de momento nombre, vida y estado de manera estatica al principio
#romualdo.estado() # Funcion estado de la persona, solo para ver como anda...

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Parte principal del programa
while romualdo.Viviendo:

    caminoUno = caminoAleatorio() # Asigno uno de los posibles caminos a la opcion 1 de forma aleatoria
    sospechaUno = sospechaCamino(caminoUno) # Asigno una pista para mostrar en funcion del camino generado para la opcion 1
    
    caminoDos = caminoAleatorio() # Asigno uno de los posibles caminos a la opcion 2 de forma aleatoria
    sospechaDos = sospechaCamino(caminoDos) # Asigno una pista para mostrar en funcion del camino generado para la opcion 2
    
    if distanciaRecorrida == 0:
        intro() # Llamo a la introduccion
        unCamino = eleccion() # Llamo a la funcion para que el usuario elija un camino
    else:
        opciones() # Llamo la funcion para mostrar las opciones de camino
        unCamino = eleccion() # Llamo la funcion para que el usuario elija un camino

    # En base a lo que elige el jugador, muestra un camino o el otro
    if unCamino == 1:
        distanciaRecorrida = distanciaRecorrida + 1
        print("\nElegiste el camino que parece que", diccionarioPistas[sospechaUno],"\ny", diccionarioCaminos[caminoUno])
        time.sleep(4)
        romualdo.Vida = romualdo.Vida + buffsCamino(caminoUno) # Asigno un buff o debuff para el camino 1
        romualdo.Viviendo = sigueVivo(caminoUno) # Definimos si Romualdo sigue vivo o no con el camino 1
        #romualdo.Cansancio = romualdo.Cansancio + 1 # Con cada camino recorrido Romualdo se va cansando
        romualdo.check() # Imprimo el estado del personaje
    elif unCamino == 2:
        distanciaRecorrida = distanciaRecorrida + 1
        print("\nElegiste el camino que parece que", diccionarioPistas[sospechaDos],"\ny", diccionarioCaminos[caminoDos])
        time.sleep(4)
        romualdo.Vida = romualdo.Vida + buffsCamino(caminoDos) # Asigno un buff o debuff para el camino 2
        romualdo.Viviendo = sigueVivo(caminoDos) # Definimos si Romualdo sigue vivo o no con el camino 2
        #romualdo.Cansancio = romualdo.Cansancio + 1 # Con cada camino recorrido Romualdo se va cansando
        romualdo.check() # Imprimo el estado del personaje

mensajeFin() # Mostramos el mensaje de fin