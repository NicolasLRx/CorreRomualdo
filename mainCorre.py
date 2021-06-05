import random
import time
from typing import Tuple

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Creo la clase persona para poder darle atributos al jugador.
class persona():
    def __init__(self, nombre, vida, viviendo, cansancio, hambre):
        self.Nombre = nombre
        self.Vida = vida
        self.Viviendo = viviendo
        self.Cansancio = cansancio
        self.Hambre = hambre

    def estado(self):
        print("Nombre:", self.Nombre,"\nVida:", self.Vida,"%\nSigue vivo:", self.Viviendo,"\nCansancio:",self.Cansancio,"%","\nHambre:",self.Hambre,"%")

    def check(self):

        if self.Cansancio >= 75 or self.Hambre >= 75:
            self.Vida = self.Vida - 10

        if self.Cansancio < 0:
            self.Cansancio = 0
        elif self.Cansancio > 100:
            self.Cansancio = 100

        if self.Hambre > 100:
            self.Hambre = 100
        elif self.Hambre < 0:
            self.Hambre = 0

        if self.Viviendo == False:
            self.Vida = 0
        elif self.Vida == 0:
            self.Viviendo = False
            print("Tu vida llego a 0...\n")
        elif self.Vida > 100:
            self.Vida = 100

        if self.Viviendo == True:
            if self.Cansancio >= 75 and self.Vida <= 25 and self.Hambre >= 75:
                print("Estas muy cansado, herido y hambriento...")
            elif self.Cansancio >= 75 and self.Vida > 25 and self.Hambre < 75:
                print("Estas muy cansado...")
            elif self.Cansancio < 75 and self.Vida <= 25 and self.Hambre < 75:
                print("Estas muy herido...")
            elif self.Cansancio < 75 and self.Vida > 25 and self.Hambre >= 75:
                print("Estas muy hambriento...")
            elif self.Cansancio >= 75 and self.Vida <= 25 and self.Hambre < 75:
                print("Estas muy cansado y herido...")
            elif self.Cansancio >= 75 and self.Vida > 25 and self.Hambre >= 75:
                print("Estas muy cansado y hambiriento...")
            elif self.Cansancio < 75 and self.Vida <= 25 and self.Hambre >= 75:
                print("Estas muy herido y hambriento...")

            if self.Cansancio >= 75 or self.Vida <= 25 or self.Hambre >= 75:
                time.sleep(1)
                print("Tienes que encontrar un poblado pronto o moriras...")

            print("Te quedan",self.Vida,"% ","de vida.\nTu nivel de cansancio es",(self.Cansancio),"%","\nTu nivel de hambre es",self.Hambre,"%\n")

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Funcion para narrar la introduccion del juego
def intro():
    time.sleep(3)
    print("A fines del 2019 un virus sin identificar se empieza a propagar China y luego por el")
    time.sleep(2)
    print("mundo. El caos y la desesperación invaden a toda la humanidad, que pronto se ve")
    time.sleep(2)
    print("encerrada en cuarentena. Luego de 1 año parecía que los científicos habían desarrollado")
    time.sleep(2)
    print("una vacuna para evitar que la gente siga muriendo, todo iba bien hasta que el virus muto")
    time.sleep(2)
    print("en una cepa muy contagiosa y poco mortal, que permaneció latente por varios años.\n")
    time.sleep(3)
    print("Ya casi todos habían recuperado sus antiguas vidas, la gente empezaba a olvidar los")
    time.sleep(2)
    print("barbijos y el alcohol en gel, y fue ahí cuando, por sorpresa, muchos empezaron a morir y")
    time.sleep(2)
    print("a las pocas horas regresaban a la vida atacando a todo aquel que encuentren a su paso.\n")
    time.sleep(3)
    print("Nadie estaba preparado para algo parecido...\n")
    time.sleep(3)
    print("Las pocas personas que nunca se contagiaron no tuvieron mas remedio que huir,")
    time.sleep(2)
    print("esconderse, aislarse en lugares remotos. Mientras el mundo quedaba a merced de los")
    time.sleep(2)
    print("caminantes.\n")
    time.sleep(3)
    print("Hoy, luego de casi 2 años después, te encuentras en algún lugar de Sudamérica y te")
    time.sleep(2)
    print("persigue una horda de zombies. Trata de escapar de ellos, eligiendo caminos que te")
    time.sleep(2)
    print("lleven a un lugar seguro ¡pero cuidado! Algunos conducen a la perdición... Veamos qué")
    time.sleep(2)
    print("tan lejos puedes acompañar a sin que muera...\n")
    time.sleep(3)
    print("Frente a ti tienes 2 caminos")

    opciones() # Llamo a la funcion que muestras las opciones disponibles de camino

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Defino dos diccionarios para limpiar un poco el codigo de las funciones caminoAleatorio(), sospechaCamino(), buffsCamino() y sigueVivo()
# Diccionario para los caminos
diccionarioCaminos =   {"Camino_1":"terminas a la orilla del mar, todo parece tranquilo pero un grupo de piratas te encuentran\ny te llevan prisionero en su barco como esclavo, hasta que eventualmente\nse cansan de ti y te arrojan por la borda lejos de la costa. Te conviertes en el almuerzo\nde los tiburones…\n",
                        "Camino_2":"te topas con dos refugiados y una pequeña fogata a la orilla del camino. Te convidan de\nsu comida y te ayudan con tus heridas.\n",
                        "Camino_3":"llegas a una cascada de unos 15 metros de alto! Buscas por donde puedes escalar, hasta\nque encuentras una cuerda colgando por el borde de unas piedras. Te esfuerzas para\nlograr subir y desde arriba observas unos animales en el bosque... Apuras el paso y llegas\na otro cruce.\n",
                        "Camino_4":"te ataca una manada de lobos hambrientos que corren para comerte! Corres por tu\nvida y te salvas trepando en un árbol. Luego de unas horas de esperar, los lobos se van\ny logras huir solo con algunas mordidas y rasguños.\n",
                        "Camino_5":"te encuentras un campamento de caníbales! Logras escapar a través del bosque, pero\nsufriste heridas.\n",
                        "Camino_6":"te encuentras un transeúnte delirante y herido que asegura haber visto piratas\nasaltando un pueblo cercano. Intentas averiguar donde esta ese poblado, pero el\nhombre se desmaya. Sigues tu camino y llegas un nuevo cruce.\n",
                        "Camino_7":"llegas a un pequeño arroyo, aprovechas para limpiarte las heridas, descansar y beber un\npoco de agua antes de continuar con el viaje.\n",
                        "Camino_8":"resulta ser un camino tranquilo y sin complicaciones, incluso logras comer algo a la\nsombra de un árbol. Luego de una siestita continuas retomas el viaje y llegas a un nuevo\ncruce.\n",
                        "Camino_9":"llegas a un poblado! Un habitante te invita a pasar la noche en el granero de su casa, te\nda alimentos, cura tus heridas y te permite darte una ducha antes de dormir. Al día\nsiguientes continuas tu viaje.\n",
                        "Camino_10":"a medio camino te encuentras con un perro que se acerca buscando comida, lo\nacaricias y notas una chapita con el nombre Bartolo. Te acompaña un tramo del\nrecorrido, luego se mete corriendo al bosque... Llegas a un nuevo cruce.\n",
                        "Camino_11":"terminas a la orilla del mar, observas a unos metros de la costa un barco pirata! Logras\nesconderte detrás de unas grandes piedras y los piratas no te ven. Pero tienes que\nesperar bastante tiempo hasta que se van los malvivientes, terminas muy cansado y\nhambriento.\n",
                        "Camino_12":"termina en el borde de un precipicio! Puedes ver que del otro lado hay un pueblo, pero\nel puente que cruza hasta el otro lado está roto, intentas volver por donde viniste, pero\nte topas con un grupo numeroso de zombies y no logras escapar…\n",
                        "Camino_13":"mientras caminas sientes que alguien te esta siguiendo, notas que hay alguien en las\ncercanías, pero no logras ver donde está. Intentas hacerte el distraído y seguir tu\ncamino, pero de repente caes en una trampa, un pozo de unos 3 metros de profundidad.\nEntonces aparecen las personas que te perseguían, ¡caníbales! Terminas atado a un\npalo, girando sobre una fogata…\n",
                        "Camino_14":"a medio camino te encuentras con un perro que se acerca buscando comida, lo\nacaricias y notas una chapita con el nombre Freddy. Te acompaña un tramo del\nrecorrido, luego se mete corriendo al bosque... Llegas a un nuevo cruce.\n",
                        "Camino_15":"a medio camino te encuentras con un perro que se acerca buscando comida, lo\nacaricias y notas una chapita con el nombre Capitán. Te acompaña un tramo del\nrecorrido, luego se mete corriendo al bosque... Llegas a un nuevo cruce.\n",
                        "Camino_16":"te encuentras un transeúnte delirante y herido que asegura haber visto piratas\nasaltando un pueblo cercano. Intentas averiguar donde esta ese poblado, pero el\nhombre se desmaya. Sigues tu camino y llegas un nuevo cruce.\n",
                        "Camino_17":"te topas con una familia de viajeros descansando al lado de una fogata. Te invitan un\npoco de comida y te cuentan que escaparon de un pueblo que fue devastado por los\n¡caníbales! Luego de comer sigues tu camino y llegas a un nuevo cruce.\n",
                        "Camino_18":"te topas con dos refugiados y una pequeña fogata a la orilla del camino. Pero creen que\neres parte de un grupo de ladrones de comida y te amenazan con un cuchillo para que\nte vayas. No discutes y sigues camino hasta que encuentras otro cruce.\n",
                        "Camino_19":"te encuentras un borracho que te confunde con su hermano. Acompañas al hombre un\ntramo del camino hasta que encuentras a otro borracho durmiendo a la sobra de un\nárbol… no caben dudas, es su hermano. Los dejas durmiendo uno al lado del otro y\nsigues tu camino hasta llegar a un nuevo cruce.\n",
                       }

# Diccionario para las pistas de los caminos
diccionarioPistas =    {"Pista_1":"cruza un arroyo",
                        "Pista_2":"conduce a un pequeño poblado",
                        "Pista_3":"cruza un arroyo",
                        "Pista_4":"es un sendero tranquilo",
                        "Pista_5":"conduce a un pequeño poblado",
                        "Pista_6":"es un sendero tranquilo",
                        "Pista_7":"cruza un arroyo",
                        "Pista_8":"es un sendero tranquilo",
                        "Pista_9":"conduce a un pequeño poblado",
                        "Pista_10":"es un sendero tranquilo",
                        "Pista_11":"cruza un arroyo",
                        "Pista_12":"conduce a un pequeño poblado",
                        "Pista_13":"es un sendero tranquilo",
                        "Pista_14":"cruza un arroyo",
                        "Pista_15":"conduce a un pequeño poblado",
                        "Pista_16":"cruza un arroyo",
                        "Pista_17":"es un sendero tranquilo",
                        "Pista_18":"cruza un arroyo",
                        "Pista_19":"conduce a un pequeño poblado",
                       }

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Funcion que devuelve de manera aleatoria uno de los 10 caminos posibles
def caminoAleatorio():

    caminoRandom = random.randint(1,19)

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
    elif caminoRandom == 11:
        return "Camino_11"
    elif caminoRandom == 12:
        return "Camino_12"
    elif caminoRandom == 13:
        return "Camino_13"
    elif caminoRandom == 14:
        return "Camino_14"
    elif caminoRandom == 15:
        return "Camino_15"
    elif caminoRandom == 16:
        return "Camino_16"
    elif caminoRandom == 17:
        return "Camino_17"
    elif caminoRandom == 18:
        return "Camino_18"
    elif caminoRandom == 19:
        return "Camino_19"
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
    elif sospecha == "Camino_11":
        return "Pista_11"
    elif sospecha == "Camino_12":
        return "Pista_12"
    elif sospecha == "Camino_13":
        return "Pista_13"
    elif sospecha == "Camino_14":
        return "Pista_14"
    elif sospecha == "Camino_15":
        return "Pista_15"
    elif sospecha == "Camino_16":
        return "Pista_16"
    elif sospecha == "Camino_17":
        return "Pista_18"
    elif sospecha == "Camino_18":
        return "Pista_18"
    elif sospecha == "Camino_19":
        return "Pista_19"
    else:
        return "Verificar porque algo anda mal... sospechaCamino()"

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Funcion que devuelve si romualdo continua con vida o no
def sigueVivo(vive):

    # Se cansa 10 por camino normal
    # El hambre aumenta 10 por camino normal y mejora 10 si come un poco
    # El pueblo elimina todo el cansancio y el hambre, y restaura toda la vida

    if vive == "Camino_1":
        romualdo.Viviendo = False
        romualdo.Vida = 0 # Muere, los demas parametros no importan tanto
        #romualdo.Cansancio = 0
        #romualdo.Hambre = 0
        return False
    elif vive == "Camino_2":
        romualdo.Viviendo = True
        romualdo.Vida = romualdo.Vida + 10
        romualdo.Cansancio = romualdo.Cansancio - 10
        romualdo.Hambre = romualdo.Hambre - 10
        return True
    elif vive == "Camino_3":
        romualdo.Viviendo = True
        #romualdo.Vida = 0 # No disminuye la vida en este camino por ahora
        romualdo.Cansancio = romualdo.Cansancio + 40 # Se cansa 2 por cada metro escalado + 10 por el camino
        romualdo.Hambre = romualdo.Hambre + 10
        return True
    elif vive == "Camino_4":
        romualdo.Viviendo = True
        romualdo.Vida = romualdo.Vida - 20
        romualdo.Cansancio = romualdo.Cansancio + 20
        romualdo.Hambre = romualdo.Hambre + 10
        return True
    elif vive == "Camino_5":
        romualdo.Viviendo = True
        romualdo.Vida = romualdo.Vida - 20
        romualdo.Cansancio = romualdo.Cansancio + 20
        romualdo.Hambre = romualdo.Hambre + 10
        return True
    elif vive == "Camino_6":
        romualdo.Viviendo = True
        #romualdo.Vida = 0 # No disminuye la vida en este camino por ahora
        romualdo.Cansancio = romualdo.Cansancio + 10
        romualdo.Hambre = romualdo.Hambre + 10
        return True
    elif vive == "Camino_7":
        romualdo.Viviendo = True
        #romualdo.Vida = 0 # No disminuye la vida en este camino por ahora
        romualdo.Cansancio = romualdo.Cansancio - 10
        romualdo.Hambre = romualdo.Hambre - 10
        return True
    elif vive == "Camino_8":
        romualdo.Viviendo = True
        #romualdo.Vida = 0 # No disminuye la vida en este camino por ahora
        romualdo.Cansancio = romualdo.Cansancio - 10
        romualdo.Hambre = romualdo.Hambre - 10
        return True
    elif vive == "Camino_9":
        romualdo.Viviendo = True
        romualdo.Vida = 100
        romualdo.Cansancio = 0
        romualdo.Hambre = 0
        return False
    elif vive == "Camino_10":
        romualdo.Viviendo = True
        #romualdo.Vida = 0 # No disminuye la vida en este camino por ahora
        romualdo.Cansancio = romualdo.Cansancio + 10
        romualdo.Hambre = romualdo.Hambre + 10
        return True
    elif vive == "Camino_11":
        romualdo.Viviendo = True
        #romualdo.Vida = 0 # No disminuye la vida en este camino por ahora
        romualdo.Cansancio = romualdo.Cansancio + 30
        romualdo.Hambre = romualdo.Hambre + 50
        return True
    elif vive == "Camino_12":
        romualdo.Viviendo = False
        romualdo.Vida = 0 # Muere, los demas parametros no importan tanto
        #romualdo.Cansancio = 0
        #romualdo.Hambre = 0
        return True
    elif vive == "Camino_13":
        romualdo.Viviendo = False
        romualdo.Vida = 0 # Muere, los demas parametros no importan tanto
        #romualdo.Cansancio = 0
        #romualdo.Hambre = 0
        return True
    elif vive == "Camino_14":
        romualdo.Viviendo = True
        #romualdo.Vida = 0 # No disminuye la vida en este camino por ahora
        romualdo.Cansancio = romualdo.Cansancio + 10
        romualdo.Hambre = romualdo.Hambre + 10
        return True
    elif vive == "Camino_15":
        romualdo.Viviendo = True
        #romualdo.Vida = 0 # No disminuye la vida en este camino por ahora
        romualdo.Cansancio = romualdo.Cansancio + 10
        romualdo.Hambre = romualdo.Hambre + 10
        return True
    elif vive == "Camino_16":
        romualdo.Viviendo = True
        #romualdo.Vida = 0 # No disminuye la vida en este camino por ahora
        romualdo.Cansancio = romualdo.Cansancio + 10
        romualdo.Hambre = romualdo.Hambre + 10
        return True
    elif vive == "Camino_17":
        romualdo.Viviendo = True
        #romualdo.Vida = 0 # No disminuye la vida en este camino por ahora
        romualdo.Cansancio = romualdo.Cansancio - 10
        romualdo.Hambre = romualdo.Hambre - 10
        return False
    elif vive == "Camino_18":
        romualdo.Viviendo = True
        #romualdo.Vida = 0 # No disminuye la vida en este camino por ahora
        romualdo.Cansancio = romualdo.Cansancio + 10
        romualdo.Hambre = romualdo.Hambre + 10
        return True
    elif vive == "Camino_19":
        romualdo.Viviendo = True
        #romualdo.Vida = 0 # No disminuye la vida en este camino por ahora
        romualdo.Cansancio = romualdo.Cansancio + 10
        romualdo.Hambre = romualdo.Hambre + 10
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
        print("El camino 1 parecen que",diccionarioPistas[sospechaUno],", y el camino 2... Tambien!") # Muestra si ambas pistas son iguales
        time.sleep(1)
        print("\nElige con cuidado, tu vida depende de ello...")
    else:
        print("1. Este camino parece que",diccionarioPistas[sospechaUno]) # Muestra una pista de lo que parece que hay en el camino 1
        print("2. Este camino parece que",diccionarioPistas[sospechaDos]) # Muestra una pista de lo que parece que hay en el camino 2
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

romualdo = persona("Romualdo",100,True,0,25) # Defino de momento nombre, vida y estado de manera estatica al principio
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
        sigueVivo(caminoUno)
        time.sleep(2)
        romualdo.check() # Imprimo el estado del personaje
    elif unCamino == 2:
        distanciaRecorrida = distanciaRecorrida + 1
        print("\nElegiste el camino que parece que", diccionarioPistas[sospechaDos],"\ny", diccionarioCaminos[caminoDos])
        sigueVivo(caminoDos)
        time.sleep(2)
        romualdo.check() # Imprimo el estado del personaje

mensajeFin() # Mostramos el mensaje de fin