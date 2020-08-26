from Juego import *

juego = Juego()#Crea objeto juego

cantinero = juego.crearCantinero()#Crea  objeto cantinero
cerveza = juego.crearCerveza()#Crea  objeto cerveza
cliente = juego.crearCliente()#Crea  objeto cliente

iterador_1 = juego.iteradorCerveza#Crea iterador de cerveza
iterador = juego.iteradorCliente#Crea iterador de cliente

juego.hacerInicio()#Inicia juego

checkpoint = juego.checkpoint#Crea un checkpoint
pygame.init()

#Inicia la pantalla, el reloj y la fuente de la letra
pantalla = pygame.display.set_mode((424,300))
reloj = pygame.time.Clock()
myfont = pygame.font.SysFont('Times New Roman', 20)

#Iterador de cada momento del tiempo del juego
while True:
    
    if juego.gameOver:#Si gameOver es true, crea la pantalla (Inicio o fin del juego)
        pantalla.blit(juego.inicio, (0, 0))
        textsurface = myfont.render("3", True, (255, 255, 255))
        pantalla.blit(textsurface, (103,270))

        for event in pygame.event.get():#Revisar cada evento que pase en el juego
            if event.type == QUIT:#Si el evento es cerrar pestaña, cierra la pestaña
                exit()

        if pygame.key.get_pressed()[K_F1]:#Si se presiona F1 inicia el juego
            juego.gameOver = False#Se deja en False ya que se sigue jugando
            juego.perderNivel = False#No se ha perdido un nivel

            cerveza.eliminar()#Se eliminan todas las cervezas
            cantinero.crear()#Se crea a un cantinero
            niveles = Nivel(cliente)#Se crea un objeto cliente
            
            niveles.sumarNivel()#Se ajusta el nivel a 1
            niveles.cambiarNivel()#Se ajusta el número de clientes y sus respectivas posiciones
            juego.numNivel = niveles.getNivel()#Se le asigna a juego.numNivel el nivel actual (1)
            cliente = niveles.getClientes()#Se le asignan los clientes obtenidos después de cambiarNivel (1)

            checkpoint.setMemento(niveles.createMemento())#Se guarda un checkpoint con los clientes y el nivel
    else:
        textsurface = myfont.render(str(cantinero.vidas), True, (255, 255, 255))#Se asigna el texto de las vidas
        textsurface1 = myfont.render(str(juego.puntos), True, (255, 255, 255))#Se asigna el texto de los puntos
        if juego.perderNivel:#Si el usuario pierde un nivel
            if cantinero.vidas == 1:#Si el usuario pierde un nivel y su número de vidas era 1, pierde el juego
                juego.gameOver = True#Finalización del juego       
            else:#Si el númmero de vidas es mayor a 1
                cantinero.vidas -= 1#Se le resta 1 al número total de vidas
                juego.perderNivel = False#Se le reasigna perderNivel a False para que no entre en este ciclo eternamente
                
                cerveza.eliminar()#Se eliminan todas las cervezas
                niveles.setMemento(checkpoint.getMemento())#Se asignan los ultimos clientes y nivel guardados
                niveles.cambiarNivel()#Se crean los clientes y sus respectivas posiciones
                juego.numNivel = niveles.getNivel()#Se le asigna a juego.numNivel el nivel actual
                cliente = niveles.getClientes()#Se le asignan los clientes obtenidos después de cambiarNivel
        else:#Si no se pierde de nivel
            juego.numNivel = niveles.getNivel()#Se le asigna a juego.numNivel el nivel actual
            
            #Se cargan las imagenes y los textos
            pantalla.blit(juego.taberna, (0, 0))
            pantalla.blit(textsurface, (103,270))
            pantalla.blit(textsurface1, (350,270))

            if juego.nivel:#Pasa de nivel
                juego.nivel = False#Se reasigna juego.nivel a False para que no entre de nuevo hasta que pase nuevamente de nivel
                for i in range(len(cerveza.cervezas)):#Elimina todas las cervezas
                    cerveza.cervezas.pop()
                
                niveles.sumarNivel()#Aumenta en 1 el nivel
                niveles.cambiarNivel()#Proceso para modificar el numero de clientes y sus posiciones
                cliente = niveles.getClientes()#Obtiene los clientes existentes en ese nuevo nivel
                checkpoint.setMemento(niveles.createMemento())#Guarda el número de clientes y el nivel
                cantinero.dibujarGanador(pantalla)#Dibuja al cantinero festejando

                pygame.display.update()#Actualiza la pantalla
                pygame.time.wait(1000)#Deja un tiempo de espera para iniciar el nuevo nivel

            for event in pygame.event.get():
                if event.type == QUIT:#Salirse de la aplicación
                    exit()
                if event.type == KEYDOWN and juego.pressed == False:#Si se oprime una tecla y no se mantiene presionada pasa a hacer la acción
                    if pygame.key.get_pressed()[K_DOWN]:#Si la tecla es abajo
                        juego.pressed = True
                        cantinero.mover(0)#Mueve al cantinero una barra abajo

                    if pygame.key.get_pressed()[K_UP]:#Si la tecla es arriba
                        juego.pressed = True
                        cantinero.mover(1)#Mueve al cantinero una barra arriba

                    if pygame.key.get_pressed()[K_SPACE]:#Si la tecla es espacio
                        juego.pressed = True
                        cerveza.clone(cantinero.getBarra())#Crea una cerveza
                else:
                    juego.pressed = False#No permite que la tecla se mantenga oprimida

            iterador.primero()#Se selecciona al primer cliente
            while iterador.hayMas():#Mientras que hay mas clientes
                if(iterador.actual().getGameOver()):#Si se pierde el nivel ya que el cliente llegó al final de la barra
                    juego.perderNivel = True#Se deja en True ya que pierde el nivel
                    cantinero.dibujarPerdido(pantalla)#Se dibuja al cantinero triste
                    pygame.display.update()#Se actualiza la pantalla
                    pygame.time.wait(1000)#Tiempo de espera para iniciar nueva acción
                    break
                else:#Si no se ha perdido el nivel porque el cliente haya llegado al final de la barra
                    if iterador.actual().getPosX() < iterador.actual().temp:#Si el cliente ya supero el muro
                        if(iterador.actual().satisfecho == False):#Si el cliente no está saltisfecho
                            juego.sumarPuntos()                   #Se suman los puntos
                        iterador.actual().satisfecho = True       #Y el cliente pasa a estar satisfecho
                        
                    else:#Si no ha superado el muro
                        iterador.actual().dibujar(pantalla)#Se dibuja el cliente actual
                        if(not iterador.actual().getTomar()):#Si el cliente actual no esta tomando
                            iterador.actual().mover(0.25)#Se mueve 0.25 a la dercha continuamente
                        else:#Si el cliente está tomando
                            if(iterador.actual().cont < 200):#Se mueve a la izquierda por un "tiempo" de 200
                                iterador.actual().mover(-0.4)#Se mueve a la izquierda 0.4
                                iterador.actual().cont += 1#Contador aumenta hasta 200
                            else:#Si el cliente no está tomando
                                iterador.actual().cont = 0#El contador se asigna a 0
                                iterador.actual().tomarCerveza(False)#Se asigna que no está tomando cerveza
                    pos = 0
                    iterador_1.primero()#Se selecciona la primera cerveza
                    while iterador_1.hayMas():#Mientras que hay más cervezas
                        if(iterador_1.actual().getGameOver()):#Si se perdió ya que la cerveza se rompio
                            juego.perderNivel = True#Se deja en True ya que pierde el nivel
                            iterador_1.actual().dibujar(pantalla)#Se dibuja la cerveza actual (rota)
                            cerveza.cervezas.pop(pos)#Se eliminan todas las cervezas
                            cantinero.dibujarPerdido(pantalla)#Se dibuja al cantinero triste
                            pygame.display.update()#Se actualiza la pantalla
                            pygame.time.wait(1000)##Tiempo de espera para iniciar nueva acción
                            break
                        else:
                            if iterador.actual().getBarra() == iterador_1.actual().getBarra():#Si la barra de la cerveza y el cliente son la misma
                                if(abs(iterador.actual().getPosX() - iterador_1.actual().getPosX()) < 15 and iterador.actual().getTomar() == False):#Si la distancia de la cerveza
                                    iterador.actual().tomarCerveza(True)#El estado del cliente es tomando cerveza                                   #y el cliente es menor a 15,
                                    cerveza.cervezas.pop(pos)#Se elimina la cerveza actual ya que se está bebiendo                                  #y el cliente no esta tomando
                                else:#Si la distancia es mayor
                                    iterador_1.actual().dibujar(pantalla)#Se dibuja la cerveza actual
                                    iterador_1.actual().mover(1/(juego.numNivel))#Se mueve con una velocidad constante
                            else:#Si la barra de la cerveza y el cliente no son la misma
                                iterador_1.actual().dibujar(pantalla)#Se dibuja la cerveza actual
                                iterador_1.actual().mover(1/(juego.numNivel))#Se mueve con una velocidad constante
                        pos += 1#La posición aumenta en 1
                        iterador_1.siguiente()#Se pasa a la siguiente cerveza

                iterador.siguiente()#Se pasa al siguiente cliente

            iterador.primero()#Se vuelve a tomar al primer cliente
            
            while iterador.hayMas():#Mientras que haya más clientes
                if(iterador.actual().satisfecho == False):#Si el cliente actual no se encuentra satisfecho
                    juego.nivel = False#No se aumenta de nivel
                    break
                else:#Si el cliente actual se encuentra satisfecho
                    juego.nivel = True#Se aumenta de nivel
                    iterador.siguiente()#Se pasa al siguiente cliente

            cantinero.dibujar(pantalla)#Se dibuja al cantinero normal
    reloj.tick(100)
    pygame.display.update()



