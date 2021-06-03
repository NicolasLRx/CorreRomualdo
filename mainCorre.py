import random
import time

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Creo la clase persona para poder darle atributos al jugador.
class persona():
    def __init__(self, nombre, vida, viviendo):
        self.Nombre = nombre
        self.Vida = vida
        self.Viviendo = viviendo

    def estado(self):
        print("Nombre:",self.Nombre,"\nVida:",self.Vida,"\nSigue vivo:",self.Viviendo)
    
    def check(self):

        if self.Viviendo == False:
            self.Vida = 0
        elif self.Vida == 0:
            self.Viviendo = False
        elif self.Vida > 100:
            self.Vida = 100 

        print("\nTe quedan",self.Vida,"puntos de vida.")

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

# Funcion que devuelve de manera aleatoria uno de los 10 caminos posibles
def caminoAleatorio():

    caminoRandom = random.randint(1,10)

    if caminoRandom == 1:
        romualdo.Viviendo = False
        return "terminas en el mar,\ntodo parece tranquilo pero un grupo de piratas te encuentran y te llevan prisionero en su barco... \nA los pocos días mueres de hambre..."
    elif caminoRandom == 2:
        romualdo.Viviendo = True
        return "te topas con dos refugiados y una pequeña fogata a la orilla del camino.\nTe convidan de su comida y te ayudan con tus heridas."
    elif caminoRandom == 3:
        romualdo.Viviendo = True
        return "llegas a una cascada de 15 metros!\nTe esfuerzas por escalarla y desde arriba observas unos animales en el bosque...\nApuras el paso y llegas a otro cruce"
    elif caminoRandom == 4:
        romualdo.Viviendo = True
        return "te ataca una manada de lobos hambrientos!\nCorres por tu vida pero logran morderte un poco.\nTienes que encontrar un poblado pronto o moriras...\n"
    elif caminoRandom == 5:
        romualdo.Viviendo = True
        return "te encuentras un campamento de canivales!\nlogras escapar a través del bosque pero sufriste heridas.\nTienes que encontrar un poblado pronto o moriras...\n"
    elif caminoRandom == 6:
        romualdo.Viviendo = True
        return "llegas a un pequeño arroyo, \naprovechas para limpiarte las heridas y beber un poco de agua antes de continuar con el viaje."
    elif caminoRandom == 7:
        romualdo.Viviendo = True
        return "te encuentras un transehunte delirante que asegura haber visto piratas...\nSigues tu camino y llegas un nuevo cruce"
    elif caminoRandom == 8:        
        romualdo.Viviendo = True
        return "llegas a un poblado!\nUn habitante te invita a pasar la noche en el granero de su casa,\nte da alimentos, cura tus heridas y te permite darte una ducha antes de dormir.\nAl día siguientes continuas tu viaje."
    elif caminoRandom == 9:
        romualdo.Viviendo = False
        return "termina en un precipicio!\nPuedes ver que del otro lado hay un pueblo, pero el puente que cruza hasta el otro lado esta roto,\nlos zombies te alcanzan y mueres...\n"
    elif caminoRandom == 10:
        return "resulta ser un sendero tranquilo que te lleva a un nuevo cruce."
    else:
        return "algo anda mal guacho"

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Funcion que devuelve pistas sobre los caminos generados aleatoriamente
def sospechaCamino(sospecha):

    if sospecha == "terminas en el mar,\ntodo parece tranquilo pero un grupo de piratas te encuentran y te llevan prisionero en su barco... \nA los pocos días mueres de hambre...":
        return "desemboca en un pequeño arroyo"
    elif sospecha == "te topas con dos refugiados y una pequeña fogata a la orilla del camino.\nTe convidan de su comida y te ayudan con tus heridas.":
        return "conduce a un pequeño poblado"
    elif sospecha == "llegas a una cascada de 15 metros!\nTe esfuerzas por escalarla y desde arriba observas unos animales en el bosque...\nApuras el paso y llegas a otro cruce":
        return "desemboca en un pequeño arroyo"
    elif sospecha == "te ataca una manada de lobos hambrientos!\nCorres por tu vida pero logran morderte un poco.\nTienes que encontrar un poblado pronto o moriras...\n":
        return "es un sendero tranquilo"
    elif sospecha == "te encuentras un campamento de canivales!\nlogras escapar a través del bosque pero sufriste heridas.\nTienes que encontrar un poblado pronto o moriras...\n":
        return "conduce a un pequeño poblado"
    elif sospecha == "llegas a un pequeño arroyo, \naprovechas para limpiarte las heridas y beber un poco de agua antes de continuar con el viaje.":
        return "desemboca en un pequeño arroyo"
    elif sospecha == "te encuentras un transehunte delirante que asegura haber visto piratas...\nSigues tu camino y llegas un nuevo cruce":
        return "es un sendero tranquilo"
    elif sospecha == "llegas a un poblado!\nUn habitante te invita a pasar la noche en el granero de su casa,\nte da alimentos, cura tus heridas y te permite darte una ducha antes de dormir.\nAl día siguientes continuas tu viaje.":
        return "conduce a un pequeño poblado"
    elif sospecha == "termina en un precipicio!\nPuedes ver que del otro lado hay un pueblo, pero el puente que cruza hasta el otro lado esta roto,\nlos zombies te alcanzan y mueres...\n":
        return "conduce a un pequeño poblado"
    elif sospecha == "resulta ser un sendero tranquilo que te lleva a un nuevo cruce.":
        return "es un sendero tranquilo"
    else:
        return "algo anda mal guacho"

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Funcion que devuelve los daños o curaciones de los caminos generados aleatoriamente
def buffsCamino(buffs):

    if buffs == "terminas en el mar,\ntodo parece tranquilo pero un grupo de piratas te encuentran y te llevan prisionero en su barco... \nA los pocos días mueres de hambre...":
        return -100
    elif buffs == "te topas con dos refugiados y una pequeña fogata a la orilla del camino.\nTe convidan de su comida y te ayudan con tus heridas.":
        return 5
    elif buffs == "llegas a una cascada de 15 metros!\nTe esfuerzas por escalarla y desde arriba observas unos animales en el bosque...\nApuras el paso y llegas a otro cruce":
        return 0
    elif buffs == "te ataca una manada de lobos hambrientos!\nCorres por tu vida pero logran morderte un poco.\nTienes que encontrar un poblado pronto o moriras...\n":
        return -5
    elif buffs == "te encuentras un campamento de canivales!\nlogras escapar a través del bosque pero sufriste heridas.\nTienes que encontrar un poblado pronto o moriras...\n":
        return -10
    elif buffs == "llegas a un pequeño arroyo, \naprovechas para limpiarte las heridas y beber un poco de agua antes de continuar con el viaje.":
        return 0
    elif buffs == "te encuentras un transehunte delirante que asegura haber visto piratas...\nSigues tu camino y llegas un nuevo cruce":
        return 0
    elif buffs == "llegas a un poblado!\nUn habitante te invita a pasar la noche en el granero de su casa,\nte da alimentos, cura tus heridas y te permite darte una ducha antes de dormir.\nAl día siguientes continuas tu viaje.":
        return 100
    elif buffs == "termina en un precipicio!\nPuedes ver que del otro lado hay un pueblo, pero el puente que cruza hasta el otro lado esta roto,\nlos zombies te alcanzan y mueres...\n":
        return -100
    elif buffs == "resulta ser un sendero tranquilo que te lleva a un nuevo cruce.":
        return 0
    else:
        return "algo anda mal guacho"

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Funcion que devuelve si romualdo continua con vida o no
def sigueVivo(vive):

    if vive == "terminas en el mar,\ntodo parece tranquilo pero un grupo de piratas te encuentran y te llevan prisionero en su barco... \nA los pocos días mueres de hambre...":       
        return False
    elif vive == "te topas con dos refugiados y una pequeña fogata a la orilla del camino.\nTe convidan de su comida y te ayudan con tus heridas.":
        return True
    elif vive == "llegas a una cascada de 15 metros!\nTe esfuerzas por escalarla y desde arriba observas unos animales en el bosque...\nApuras el paso y llegas a otro cruce":
        return True
    elif vive == "te ataca una manada de lobos hambrientos!\nCorres por tu vida pero logran morderte un poco.\nTienes que encontrar un poblado pronto o moriras...\n":
        return True
    elif vive == "te encuentras un campamento de canivales!\nlogras escapar a través del bosque pero sufriste heridas.\nTienes que encontrar un poblado pronto o moriras...\n":
        return True
    elif vive == "llegas a un pequeño arroyo, \naprovechas para limpiarte las heridas y beber un poco de agua antes de continuar con el viaje.":
        return True
    elif vive == "te encuentras un transehunte delirante que asegura haber visto piratas...\nSigues tu camino y llegas un nuevo cruce":
        return True
    elif vive == "llegas a un poblado!\nUn habitante te invita a pasar la noche en el granero de su casa,\nte da alimentos, cura tus heridas y te permite darte una ducha antes de dormir.\nAl día siguientes continuas tu viaje.":        
        return True 
    elif vive == "termina en un precipicio!\nPuedes ver que del otro lado hay un pueblo, pero el puente que cruza hasta el otro lado esta roto,\nlos zombies te alcanzan y mueres...\n":
        return False
    elif vive == "resulta ser un sendero tranquilo que te lleva a un nuevo cruce.":
        return True
    else:
        return "algo anda mal guacho"

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Funcion para que el jugador elija un camino 
def eleccion():

    camino = ""

    # Loop para que el jugador elija un camino, solo sale del loop si elige 1 o 2
    # El try-except es para evitar que el programa caiga si ingresa una letra
    while camino != 1 and camino != 2:
        try:
            camino = int(input("\n¿Camino 1 o camino 2?: "))
            time.sleep(2)
        except ValueError:
            print("Opción invalida")
    return camino

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Funcion que nos muestra las opciones de camino disponibles para elegir, con pistas
def opciones():
       
    print("\n 1. Este camino parece que",sospechaUno) # Muestra una pista de lo que parece que hay en el camino 1
    time.sleep(2)    
    print(" 2. Este camino parece que",sospechaDos) # Muestra una psita de lo que parece que hay en el camino 2
    time.sleep(2)
    print("\nElige con cuidado, tu vida depende de ello...")

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Funcion que nos muestra el mensaje de finalización del juego
def mensajeFin():

    time.sleep(2)
    print (romualdo.Nombre,"logró recorrer",distanciaRecorrida,"kms antes de morir.")
    time.sleep(1)
    print("\nGAME OVER MI CIELA\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Declaración de variables y estados iniciales
distanciaRecorrida = 0 # Empezamos en 0 por ahora je

# Este for es solo para generar 25 espacios vacíos antes de arrancar el programa... TOC
for i in range(50):
    print("\n")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CORRE ROMUALDO ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
 
romualdo = persona("Romualdo",100,True) # Defino de momento nombre, vida y estado de manera estatica al principio
romualdo.estado() # Funcion estado de la persona, solo para ver como anda...

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
        unCamino = eleccion() # llamo la funcion para que el usuario elija un camino

    # En base a lo que elige el jugador, muestra un camino o el otro
    if unCamino == 1:
        distanciaRecorrida = distanciaRecorrida + 1
        print("\nElegiste el camino que parece que", sospechaUno,"y", caminoUno)
        time.sleep(4)
        romualdo.Vida = romualdo.Vida + buffsCamino(caminoUno) # Asigno un buff o debuff para el camino 1
        romualdo.Viviendo = sigueVivo(caminoUno) # Definimos si Romualdo sigue vivo o no con el camino 1
        romualdo.check() # Imprimo el estado del personaje
    elif unCamino == 2:
        distanciaRecorrida = distanciaRecorrida + 1
        print("\nElegiste el camino que parece que", sospechaDos,"y", caminoDos)
        time.sleep(4)
        romualdo.Vida = romualdo.Vida + buffsCamino(caminoDos) # Asigno un buff o debuff para el camino 2
        romualdo.Viviendo = sigueVivo(caminoDos) # Definimos si Romualdo sigue vivo o no con el camino 2
        romualdo.check() # Imprimo el estado del personaje

mensajeFin() # Mostramos el mensaje de fin