from Juego import *

juego = Juego()

cantinero = juego.crearCantinero()
cerveza = juego.crearCerveza()
cliente = juego.crearCliente()

iterador_1 = juego.iteradorCerveza
iterador = juego.iteradorCliente

juego.hacerInicio()

checkpoint = juego.checkpoint
pygame.init()

pantalla = pygame.display.set_mode((424,300))
reloj = pygame.time.Clock()
myfont = pygame.font.SysFont('Times New Roman', 20)

while True:
    
    if juego.gameOver:
        pantalla.blit(juego.inicio, (0, 0))
        textsurface = myfont.render("3", True, (255, 255, 255))
        pantalla.blit(textsurface, (103,270))

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        if pygame.key.get_pressed()[K_F1]:
            juego.gameOver = False    
            juego.perderNivel = False

            cerveza.eliminar()
            cantinero.crear()
            niveles = Nivel(cliente)
            
            niveles.sumarNivel()    
            niveles.cambiarNivel()
            juego.numNivel = niveles.getNivel()
            cliente = niveles.getClientes()

            checkpoint.setMemento(niveles.createMemento())
    else:
        textsurface = myfont.render(str(cantinero.vidas), True, (255, 255, 255))
        textsurface1 = myfont.render(str(juego.puntos), True, (255, 255, 255))
        if juego.perderNivel:
            if cantinero.vidas == 1:
                juego.gameOver = True          
            else:
                cantinero.vidas -= 1
                juego.perderNivel = False
                
                cerveza.eliminar()
                niveles.setMemento(checkpoint.getMemento())
                niveles.cambiarNivel()
                juego.numNivel = niveles.getNivel()
                cliente = niveles.getClientes()
        else:
            juego.numNivel = niveles.getNivel()
            
            pantalla.blit(juego.taberna, (0, 0))
            pantalla.blit(textsurface, (103,270))
            pantalla.blit(textsurface1, (350,270))

            if juego.nivel:
                juego.nivel = False
                for i in range(len(cerveza.cervezas)):
                    cerveza.cervezas.pop()
                
                niveles.sumarNivel()
                niveles.cambiarNivel()
                cliente = niveles.getClientes()
                checkpoint.setMemento(niveles.createMemento())
                cantinero.dibujarGanador(pantalla)

                pygame.display.update()
                pygame.time.wait(1000)

            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type == KEYDOWN and juego.pressed == False:
                    if pygame.key.get_pressed()[K_DOWN]:
                        juego.pressed = True
                        cantinero.mover(0)

                    if pygame.key.get_pressed()[K_UP]:
                        juego.pressed = True
                        cantinero.mover(1)

                    if pygame.key.get_pressed()[K_SPACE]:
                        juego.pressed = True
                        cerveza.clone(cantinero.getBarra())
                else:
                    juego.pressed = False

            iterador.primero()
            while iterador.hayMas():
                if(iterador.actual().getGameOver()):
                    juego.perderNivel = True
                    cantinero.dibujarPerdido(pantalla)
                    pygame.display.update()
                    pygame.time.wait(1000)
                    break
                else:
                    if iterador.actual().getPosX() < iterador.actual().temp:
                        if(iterador.actual().satisfecho == False):
                            juego.sumarPuntos()
                        iterador.actual().satisfecho = True
                        
                    else:
                        iterador.actual().dibujar(pantalla)
                        if(not iterador.actual().getTomar()):
                            iterador.actual().mover(0.25)
                        else:
                            if(iterador.actual().cont < 200):
                                iterador.actual().mover(-0.4)
                                iterador.actual().cont += 1
                            else:
                                iterador.actual().cont = 0
                                iterador.actual().tomarCerveza(False)
                    pos = 0
                    iterador_1.primero()
                    while iterador_1.hayMas():
                        if(iterador_1.actual().getGameOver()):
                            juego.perderNivel = True
                            iterador_1.actual().dibujar(pantalla)
                            cerveza.cervezas.pop(pos)
                            cantinero.dibujarPerdido(pantalla)
                            pygame.display.update()
                            pygame.time.wait(1000)
                            break
                        else:
                            if iterador.actual().getBarra() == iterador_1.actual().getBarra():
                                if(abs(iterador.actual().getPosX() - iterador_1.actual().getPosX()) < 15 and iterador.actual().getTomar() == False):
                                    iterador.actual().tomarCerveza(True)
                                    cerveza.cervezas.pop(pos)
                                else:
                                    iterador_1.actual().dibujar(pantalla)
                                    iterador_1.actual().mover(1/(juego.numNivel))
                            else:
                                iterador_1.actual().dibujar(pantalla)
                                iterador_1.actual().mover(1/(juego.numNivel))
                        pos += 1
                        iterador_1.siguiente()

                iterador.siguiente()

            iterador.primero()
            
            while iterador.hayMas():
                if(iterador.actual().satisfecho == False):
                    juego.nivel = False
                    break
                else:
                    juego.nivel = True
                    iterador.siguiente()

            cantinero.dibujar(pantalla)
    reloj.tick(100)
    pygame.display.update()



