### AUTORES:
### CARLOS ALBERTO SOTO
### SEBASTIAN SALAMANDO
### ANDRES FELIPE OROZCO

import pygame,sys
from random import choice

def movimiento_gato(gato,jugadorr,paredes):
    """es una funcion que se encarga del movimiento que realiza el gato
    Entrada:la imagen del gato, jugador y paredes
    Salida: Persigue al jugador cuando esta cerca"""
    if abs(jugadorr.top-gato.rect.top) < 20:
        if jugadorr.top < gato.rect.top:
            gato.vely = -gato.vel
        else:
            gato.vely = gato.vel
    elif abs(jugadorr.left-gato.rect.left) < 20:
            if jugadorr.left < gato.rect.left:
                gato.velx = gato.vel
            else:
                gato.velx = -gato.vel
    else:
        gato.velx,gato.vely=0,0
    
    antx = gato.rect.left
    anty = gato.rect.top
    
    gato.rect.move_ip(gato.vely,gato.velx)
    
    if gato.rect.collidelist(paredes)>(-1):
        gato.rect.top = anty
        gato.rect.left = antx

def movimiento_raton(sprite):
    """es una funcion que se encarga del movimiento que realiza el raton
    entrada es un objeto sprite
    realiza cambios en la posicion del objeto sprite"""
    value = choice((sprite.vel*-1,sprite.vel))
    if choice((1,0))==1:
        sprite.velx = value
        sprite.vely = 0
    else:
        sprite.vely = value
        sprite.velx = 0

def movimientos_rvel(l_sprites):
    """es una funcion que toma una lista de objetos sprite
    y realiza cambios en la posicion de los objetos sprite"""
    for e in l_sprites:
        movimiento_raton(e)
        
def movimiento_ratones(l_sprites,paredes):

    """es una funcion que recibe como parametros una lista de objetos sprite y las pardes
    y realiza colisiones con las paredes"""
    for e in l_sprites:
        ratonx = e.rect.left
        ratony = e.rect.top
        
        e.rect.move_ip(e.velx,e.vely)
        if e.rect.collidelist(paredes)>(-1):
            e.rect.top = ratony
            e.rect.left = ratonx
        

def crear_raton(x,y,limite,imagen_s):
    """es una funcion que recibe como parametros posicion en x y en y y la imagen a crear"""
    sprite = pygame.sprite.Sprite()

    sprite.image = imagen_s
    sprite.rect = imagen_s.get_rect()
    sprite.rect.left = x
    sprite.rect.top = y
    sprite.vel = 8
    sprite.velx = 0
    sprite.vely = 0
    sprite.delay = 30
    return sprite
    

def seleccionar_nivel(level):
    """es una funcion que recibe como parametro el nivel del juego"""
    ratamala=pygame.image.load("ratamala.png")
    cat=pygame.image.load("gatonuevo.png")
    imagenjugador = pygame.image.load("jugador.png")



    if level == 4:
        nivel4=pygame.image.load("nivel4.png")
        imagenjugador = pygame.image.load("raton2.png")
        #ESTRELLAS
        p_s = pygame.Rect(0,0,600,30)
        p_i = pygame.Rect(0,570,600,30)
        p_iz = pygame.Rect(0,30,30,570)
        p_de = pygame.Rect(570,30,30,570)
        r1=pygame.Rect(30,150,30,120)
        r2=pygame.Rect(60,60,30,120)
        r3=pygame.Rect(60,240,30,180)
        r4=pygame.Rect(60,480,60,30)
        r5=pygame.Rect(90,510,90,30)
        r6=pygame.Rect(120,60,120,30)
        r7=pygame.Rect(150,90,30,30)
        r8=pygame.Rect(150,540,30,30)
        r9=pygame.Rect(150,150,30,240)
        r10=pygame.Rect(150,420,30,60)
        r11=pygame.Rect(180,150,300,30)
        r12=pygame.Rect(180,450,120,30)
        r13=pygame.Rect(210,210,120,30)
        r14=pygame.Rect(210,240,30,90)
        r15=pygame.Rect(270,30,90,30)
        r16=pygame.Rect(300,90,30,60)
        r17=pygame.Rect(330,90,60,30)
        r18=pygame.Rect(210,360,30,60)
        r19=pygame.Rect(240,390,180,30)
        r20=pygame.Rect(210,480,60,30)
        r21=pygame.Rect(210,510,30,30)
        r22=pygame.Rect(420,30,30,60)
        r23=pygame.Rect(480,60,30,60)
        r24=pygame.Rect(540,30,30,30)
        r25=pygame.Rect(510,90,60,30)
        r26=pygame.Rect(540,120,30,180)
        r27=pygame.Rect(510,270,30,30)
        r28=pygame.Rect(270,540,30,30)
        r29=pygame.Rect(300,510,30,60)
        r30=pygame.Rect(270,270,30,90)
        r31=pygame.Rect(330,270,30,90)
        r32=pygame.Rect(300,270,30,30)
        r33=pygame.Rect(360,210,60,30)
        r34=pygame.Rect(390,210,30,120)
        r35=pygame.Rect(420,330,30,30)
        r36=pygame.Rect(450,180,30,300)
        r37=pygame.Rect(510,360,30,180)
        r38=pygame.Rect(330,420,30,60)
        r39=pygame.Rect(360,450,90,30)
        r40=pygame.Rect(360,480,60,30)
        r41=pygame.Rect(390,510,120,30)
        r42=pygame.Rect(390,540,30,30)
        r43=pygame.Rect(390,330,30,30)
        paredes=[p_s,p_i,p_iz,p_de,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18,r19,r20,r21,r22,r23,r24,r25,r26,r27,r28,r29,r30,r31,r32,r33,r34,r35,r36,r37,r38,r39,r40,r41,r42,r43]

        #QUESOS PEQUENOS

        q1= pygame.Rect(120,540,30,30)
        q2= pygame.Rect(390,30,30,30)
        q3= pygame.Rect(240,240,30,30)
        q4= pygame.Rect(300,420,30,30)
        q5= pygame.Rect(360,360,30,30)
        q6= pygame.Rect(360,420,30,30)
        q7= pygame.Rect(420,480,30,30)
        q8= pygame.Rect(510,240,30,30)
        quesosc=[q1,q2,q3,q4,q5,q6,q7,q8]

        #QUESOS GRANDES
        q9= pygame.Rect(30,120,30,30)
        q10= pygame.Rect(60,210,30,30)
        q11= pygame.Rect(30,270,30,30)
        q12= pygame.Rect(330,120,30,30)
        q13= pygame.Rect(360,540,30,30)
        q14= pygame.Rect(420,540,30,30)
        q15= pygame.Rect(420,300,30,30)
        q16= pygame.Rect(540,60,30,30)
        quesosg=[q9,q10,q11,q12,q13,q14,q15,q16]

        #RELOJES
        reloj1 = pygame.Rect(210,540,30,30)
        relojes=[reloj1]

        #RATONES
        raton1 = crear_raton(60,450,30,ratamala)
        raton2 = crear_raton(150,120,30,ratamala)
        raton3 = crear_raton(330,210,30,ratamala)
        raton4 = crear_raton(270,480,30,ratamala)
        raton5 = crear_raton(510,330,30,ratamala)
        
        ratonesm = [raton1,raton2,raton3,raton4,raton5]

        #GATOS
        gato= crear_raton(120,270,500,cat)
        gato2= crear_raton(180,270,500,cat)
        gato3= crear_raton(450,120,500,cat)
        
        gato.vel = 9
        gato2.vel = 9
        gato3.vel = 9
        
        
        gatos = [gato,gato2,gato3]
        
        return paredes,quesosc,quesosg,relojes,ratonesm,gatos,imagenjugador
    


    if level ==  3:
        nivel3=pygame.image.load("nivel3.png")
        
        #VOLCANES
        p_s = pygame.Rect(0,0,600,30)
        p_i = pygame.Rect(0,570,600,30)
        p_iz = pygame.Rect(0,30,30,570)
        p_de = pygame.Rect(570,30,30,570)
        r1=pygame.Rect(30,60,60,30)
        r2=pygame.Rect(60,90,30,90)
        r3=pygame.Rect(90,120,30,60)
        r4=pygame.Rect(120,120,120,30)
        r5=pygame.Rect(150,150,30,30)
        r6=pygame.Rect(210,150,60,60)
        r7=pygame.Rect(240,180,60,30)
        r8=pygame.Rect(270,210,30,90)
        r9=pygame.Rect(210,240,60,30)
        r10=pygame.Rect(60,210,30,270)
        r11=pygame.Rect(30,240,30,30)
        r12=pygame.Rect(90,450,60,30)
        r13=pygame.Rect(60,510,90,30)
        r14=pygame.Rect(180,450,30,120)
        r15=pygame.Rect(90,210,90,30)
        r16=pygame.Rect(150,240,30,180)
        r17=pygame.Rect(180,300,30,60)
        r18=pygame.Rect(150,30,30,60)
        r19=pygame.Rect(180,60,120,30)
        r20=pygame.Rect(270,90,150,30)
        r21=pygame.Rect(390,60,150,30)
        r22=pygame.Rect(330,150,30,30)
        r23=pygame.Rect(510,90,30,30)
        r24=pygame.Rect(180,390,90,30)
        r25=pygame.Rect(240,360,60,30)
        r26=pygame.Rect(270,330,60,30)
        r27=pygame.Rect(300,360,30,150)
        r28=pygame.Rect(270,540,90,30)
        r29=pygame.Rect(450,90,30,90)
        r30=pygame.Rect(480,150,30,150)
        r31=pygame.Rect(390,180,30,120)
        r32=pygame.Rect(420,270,60,30)
        r33=pygame.Rect(390,360,120,30)
        r34=pygame.Rect(390,390,30,90)
        r35=pygame.Rect(480,390,30,90)
        r36=pygame.Rect(420,510,30,60)
        r37=pygame.Rect(510,510,30,30)
        r38=pygame.Rect(540,360,30,180)
        
        paredes=[p_s,p_i,p_iz,p_de,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18,r19,r20,r21,r22,r23,r24,r25,r26,r27,r28,r29,r30,r31,r32,r33,r34,r35,r36,r37,r38]

        #QUESOS PEQUENOS

        q1= pygame.Rect(90,480,30,30)
        q2= pygame.Rect(210,300,30,30)
        q3= pygame.Rect(510,270,30,30)
        quesosc=[q1,q2,q3]

        #QUESOS GRANDES
        q4= pygame.Rect(30,90,30,30)
        q5= pygame.Rect(30,270,30,30)
        q6= pygame.Rect(90,240,30,30)
        q7= pygame.Rect(270,390,30,30)
        q8= pygame.Rect(330,60,30,30)
        q9= pygame.Rect(330,120,30,30)
        q10= pygame.Rect(420,390,30,30)
        q11= pygame.Rect(540,540,30,30)
        quesosg=[q4,q5,q6,q7,q8,q9,q10,q11]

        #RELOJES
        reloj1 = pygame.Rect(210,480,30,30)
        reloj2 = pygame.Rect(480,90,30,30)
        relojes=[reloj1,reloj2]

        #RATONES
        raton1 = crear_raton(30,480,30,ratamala)
        raton2 = crear_raton(180,180,30,ratamala)
        raton3 = crear_raton(450,330,30,ratamala)
        raton4 = crear_raton(480,30,30,ratamala)
        ratonesm = [raton1,raton2,raton3,raton4]

        #GATOS
        gato= crear_raton(90,330,500,cat)
        gato2= crear_raton(330,210,500,cat)
        gato3= crear_raton(360,510,500,cat)
        
        gato.vel = 9
        gato2.vel = 9
        gato3.vel = 9
        
        
        gatos = [gato,gato2,gato3]
        
        return paredes,quesosc,quesosg,relojes,ratonesm,gatos,imagenjugador
        
        
        
    if level == 2:
        nivel2=pygame.image.load("nivel2.png")
        #CACTUS
        p_s = pygame.Rect(0,0,600,30)
        p_i = pygame.Rect(0,570,600,30)
        p_iz = pygame.Rect(0,30,30,570)
        p_de = pygame.Rect(570,30,30,570)
        r1=pygame.Rect(60,30,30,30)
        r2=pygame.Rect(120,30,30,210)
        r3=pygame.Rect(60,90,30,150)
        r4=pygame.Rect(90,90,30,30)
        r5=pygame.Rect(60,270,120,30)
        r6=pygame.Rect(90,330,30,120)
        r7=pygame.Rect(120,330,30,30)
        r8=pygame.Rect(120,420,120,30)
        r9=pygame.Rect(60,480,30,90)
        r10=pygame.Rect(180,90,30,300)
        r11=pygame.Rect(210,90,90,30)
        r12=pygame.Rect(210,360,90,30)
        r13=pygame.Rect(240,150,30,120)
        r14=pygame.Rect(270,150,90,30)
        r15=pygame.Rect(330,60,30,60)
        r16=pygame.Rect(270,240,30,90)
        r17=pygame.Rect(330,180,30,90)
        r18=pygame.Rect(300,300,60,30)
        r19=pygame.Rect(330,330,30,210)
        r20=pygame.Rect(270,390,30,120)
        r21=pygame.Rect(90,480,180,30)
        r22=pygame.Rect(90,540,180,30)
        r23=pygame.Rect(360,240,60,30)
        r24=pygame.Rect(390,60,30,180)
        r25=pygame.Rect(420,60,90,30)
        r26=pygame.Rect(480,90,30,240)
        r27=pygame.Rect(420,300,60,30)
        r28=pygame.Rect(420,330,30,120)
        r29=pygame.Rect(450,420,60,30)
        r30=pygame.Rect(480,450,30,120)
        r31=pygame.Rect(390,540,90,30)
        paredes=[p_s,p_i,p_iz,p_de,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18,r19,r20,r21,r22,r23,r24,r25,r26,r27,r28,r29,r30,r31]

        #QUESOS PEQUENOS
        q1= pygame.Rect(90,510,30,30)
        q2= pygame.Rect(210,330,30,30)
        q3= pygame.Rect(360,120,30,30)
        q4= pygame.Rect(450,510,30,30)
        q5= pygame.Rect(510,90,30,30)
        quesosc=[q1,q2,q3,q4,q5]

        #QUESOS GRANDES

        q6= pygame.Rect(30,510,30,30)
        q7= pygame.Rect(90,120,30,30)
        q8= pygame.Rect(210,30,30,30)
        q9= pygame.Rect(270,180,30,30)
        q10= pygame.Rect(270,540,30,30)
        q11= pygame.Rect(450,90,30,30)
        q12= pygame.Rect(450,330,30,30)
        q13= pygame.Rect(180,390,30,30)
        quesosg=[q6,q7,q8,q9,q10,q11,q12,q13]

        #RELOJES
        reloj1 = pygame.Rect(90,30,30,30)
        reloj2 = pygame.Rect(360,210,30,30)
        reloj3 = pygame.Rect(510,540,30,30)
        relojes=[reloj1,reloj2,reloj3]

        #RATONES
        raton1 = crear_raton(150,180,30,ratamala)
        raton2 = crear_raton(300,480,30,ratamala)
        raton3 = crear_raton(480,360,30,ratamala)
        ratonesm = [raton1,raton2,raton3]

        #GATOS
        gato= crear_raton(240,450,500,cat)
        gato2= crear_raton(420,210,500,cat)
        
        gato.vel = 5
        gato2.vel = 5
        
        gatos = [gato,gato2]
        
        return paredes,quesosc,quesosg,relojes,ratonesm,gatos,imagenjugador

     

        
    if level ==1:
        nivel1=pygame.image.load("nivel1.png")
        #ARBOLES
        p_s = pygame.Rect(0,0,600,30)
        p_i = pygame.Rect(0,570,600,30)
        p_iz = pygame.Rect(0,30,30,570)
        p_de = pygame.Rect(570,30,30,570)
        r1=pygame.Rect(120,30,210,30)
        r2=pygame.Rect(60,510,240,30)
        r3=pygame.Rect(150,90,360,30)
        r4=pygame.Rect(60,30,30,30)
        r5=pygame.Rect(60,120,60,210)
        r6=pygame.Rect(120,210,180,30)
        r7=pygame.Rect(450,60,30,240)
        r8=pygame.Rect(540,120,30,330)
        r9=pygame.Rect(210,120,30,90)
        r10=pygame.Rect(480,120,30,300)
        r11=pygame.Rect(60,360,30,120)
        r12=pygame.Rect(120,360,30,90)
        r13=pygame.Rect(330,510,210,30)
        r14=pygame.Rect(330,150,30,150)
        r15=pygame.Rect(330,360,30,150)
        r16=pygame.Rect(180,300,30,210)
        r17=pygame.Rect(240,240,30,240)
        r18=pygame.Rect(60,60,30,30)
        paredes = [p_s,p_i,p_iz,p_de,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17]

        #QUESOS PEQUENOS
        q1= pygame.Rect(270,150,30,30)
        q2= pygame.Rect(90,30,30,30)
        q3= pygame.Rect(60,330,30,30)
        q4= pygame.Rect(480,60,30,30)
        q5= pygame.Rect(420,540,30,30)
        quesosc= [q1,q2,q3,q4,q5]

        #QUESOS GRANDES
        q6= pygame.Rect(180,180,30,30)
        q7= pygame.Rect(510,240,30,30)
        q8= pygame.Rect(240,480,30,30)
        quesosg= [q6,q7,q8]

        #RELOJES
        reloj1 = pygame.Rect(360,480,30,30)
        reloj2 = pygame.Rect(180,150,30,30)
        reloj3 = pygame.Rect(330,300,30,30)
        reloj4 = pygame.Rect(30,540,30,30)
        relojes = [reloj1,reloj2,reloj3,reloj4]
        
        #RATONES
        raton1 = crear_raton(330,30,500,ratamala)
        raton2 = crear_raton(360,450,500,ratamala)
        ratones=[raton1,raton2]
        
        #GATOS
        gato= crear_raton(150,240,500,cat)
        gato.vel = 5
        
        gatos = [gato]
        
        return paredes,quesosc,quesosg,relojes,ratones,gatos,imagenjugador
        


def pintar(pantalla,nivel):
    """esta funcion recibe como parametro la pantalla y el nievel e imprime la imagen en el nivel deseado"""

    if nivel == 4:

        estrellass=pygame.image.load("fondoultimo.png")
        pantalla.blit(estrellass,(0,0))

    if nivel == 3:
        volcaness=pygame.image.load("mapavolcanes.png")
        pantalla.blit(volcaness,(0,0))
    
    
    if nivel == 2:
        cactuss=pygame.image.load("cactusmapa.png")
        pantalla.blit(cactuss,(0,0))
    
    
    if nivel == 1:
        
        arbol=pygame.image.load("arbolnuevo.png")
        pantalla.fill((255,255,255))
        pos=30
        while (pos<=540):  
            pantalla.blit(arbol,(pos,0))
            pos+=30
        pos=0
        while (pos<=540):
            pantalla.blit(arbol,(0,pos))
            pos+=30
        pos=0
        while (pos<=570):
            pantalla.blit(arbol,(pos,570))
            pos+=30
        pos=0
        while (pos<=540):
            pantalla.blit(arbol,(570,pos))
            pos+=30
        pos=60    
        while (pos<=270):     
            pantalla.blit(arbol,(pos,510))
            pos+=30
        pos= 360
        while (pos<=510):
            pantalla.blit(arbol,(pos,510))
            pos+=30
        pos=120   
        while (pos<=300):      
            pantalla.blit(arbol,(60,pos))
            pos+=30
        pos=120  
        while (pos<=300):      
            pantalla.blit(arbol,(90,pos))
            pos+=30
        pos=120 
        while (pos<=300):
            pantalla.blit(arbol,(pos,30))
            pos+=30
        pos=360
        while (pos<=450):
            pantalla.blit(arbol,(60,pos))
            pos+=30
        pos=360
        while (pos<=510):
            pantalla.blit(arbol,(330,pos))
            pos+=30
        pos=150
        while (pos<=270):
            pantalla.blit(arbol,(330,pos))
            pos+=30
        pos=90
        while (pos<=390):
            pantalla.blit(arbol,(480,pos))
            pos+=30
        pos=60
        while (pos<=280):
            pantalla.blit(arbol,(450,pos))
            pos+=30
        pos=210
        while (pos<=450):
            pantalla.blit(arbol,(240,pos))
            pos+=30
        pos=360
        while (pos<=450):
            pantalla.blit(arbol,(240,pos))
            pos+=30
        pos=120
        while (pos<=270):
            pantalla.blit(arbol,(pos,210))
            pos+=30
        pos=90
        while (pos<=210):
            pantalla.blit(arbol,(210,pos))
            pos+=30
        pos=150
        while (pos<=480):
            pantalla.blit(arbol,(pos,90))
            pos+=30
        pos=300
        while (pos<=480):
            pantalla.blit(arbol,(180,pos))
            pos+=30
        pos=360
        while (pos<=420):
            pantalla.blit(arbol,(120,pos))
            pos+=30
        pos=120
        while (pos<=420):
            pantalla.blit(arbol,(540,pos))
            pos+=30
        pantalla.blit(arbol,(60,30))
    

def main():
    """funcion principal para iniciar el juego"""
    pygame.init()
    
    pantalla=pygame.display.set_mode([900,600])
    pygame.display.set_caption("PAC-RAT")
    
    fuente1=pygame.font.SysFont("Arial",40,True,False)
    fuente2=pygame.font.SysFont("Chiller",40,False,True)
    puntaje=fuente2.render("SCORE",0,(0,0,0))
    fuente3=pygame.font.SysFont("Chiller",40,False,True)
    info=fuente3.render("VIDAS",0,(0,0,0))
    fuente4=pygame.font.SysFont("Chiller",40,False,True)
    tiem=fuente4.render("TIME",0,(0,0,0))
    nombre=fuente4.render("NOMBRE",0,(0,0,0))
    nombre=fuente4.render("NIVEL",0,(0,0,0))
    
    
    FPS=pygame.time.Clock()
    segundosint=50
    termino=False
    comidos=0
    blanco=(255,255,255)

    #IMAGENES
    pasto=pygame.image.load("pasto1.png")
    quesop=pygame.image.load("quesop.png")
    quesog=pygame.image.load("quesog.png")
    reloj=pygame.image.load("reloj.png")
    vidas=pygame.image.load("vidasrat2.png")

    #JUGADOR
    jugador=pygame.image.load("jugador.png")
    jugadorr=jugador.get_rect()
    jugadorr.top=35
    jugadorr.left=35
    inmune = False

    #SUPERFICIES
    fondo_s = pygame.Surface((600,600),0,32)
    
    #TIEMPO DE CAMBIO DE DIRECCION
    ratones_delay = 40

    #Variable de tiempo restante
    tiempo = 60

    #Variable para puntos
    score = 0

    #Variable de vidas
    lifes = 3
    
    #Nivel
    vnivel = 1
    
    #SUPERFICIE PINTADA
    pintar(fondo_s,vnivel)
    paredes,quesosc,quesosg,relojes,ratones,gatos,jugador = seleccionar_nivel(vnivel)
    
    (x,y)=(0,0)
    vx=0
    vy=0
    
    segundo_ant = 1
    while True:
        mapa = pygame.Surface([600,600])
        
        if 0 >= segundosint or not(lifes):
            pygame.quit()
            sys.exit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_w:
                    quesosc = []
                    quesosg = []

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_LEFT:
                    vx=-10
                    vy = 0
                if event.key == pygame.K_RIGHT:
                    vx=10
                    vy = 0
                if event.key == pygame.K_UP:
                    vy=-10
                    vx = 0
                if event.key == pygame.K_DOWN:
                    vy=10
                    vx = 0

                if event.key == pygame.K_m:
                    inmune = not(inmune)
                    
        x=vx
        y=vy           
        FPS.tick(20)
        
        pantalla.fill(blanco)
        pantalla.blit(fondo_s,(0,0))

        
        
        for e in gatos:
            movimiento_gato(e,jugadorr,paredes)
            pantalla.blit(e.image,e.rect)

        if ratones_delay == 0:
            movimientos_rvel(ratones)
            ratones_delay = 40
        else:
            ratones_delay -= 1
        
        movimiento_ratones(ratones,paredes)
        
        for e in ratones:
            pantalla.blit(e.image,e.rect)

        
        anty = jugadorr.top
        antx = jugadorr.left
        jugadorr.move_ip(x,y)

       
        for e in gatos:
            if jugadorr.colliderect(e.rect) and not(inmune):
                lifes-=1
                jugadorr.top,jugadorr.left = 30,30
        for e in ratones:
            if jugadorr.colliderect(e.rect) and not(inmune):
                lifes-=1
                jugadorr.top,jugadorr.left = 30,30
        if jugadorr.collidelist(paredes)>(-1):
            jugadorr.top = anty
            jugadorr.left = antx

        #for e in paredes:
         #   pygame.draw.rect(pantalla,(255,255,0),e)

        #Detecta si colisiono con los quesos
        #Lo que detecta es si la posicion de los quesos colisiono con el rectangulo del raton
        #Si es asi elimina el queso de la lista

            
        l_quesosc = jugadorr.collidelistall(quesosc)
        for e in sorted(l_quesosc,reverse=True):
            quesosc.pop(e)
            score += 200
            
        pantalla.blit(jugador,jugadorr)
        for e in quesosc:
            pantalla.blit(quesop,e)
            mapa.blit(quesop,e)
            
        l_quesosg = jugadorr.collidelistall(quesosg)
        for e in sorted(l_quesosg,reverse=True):
            quesosg.pop(e)
            score += 500
            
    
        for e in quesosg:
            pantalla.blit(quesog,e)
            mapa.blit(quesog,e)
        
        l_reloj = jugadorr.collidelistall(relojes)
        for e in sorted(l_reloj,reverse=True):
            relojes.pop(e)
            score += 50
            tiempo += 20            
            
        for e in relojes:
            pantalla.blit(reloj,e)
            mapa.blit(reloj,e)

        if segundosint==0:
            termino=True
        if termino==False:
            segundos=pygame.time.get_ticks()/1000.0
            
            segundosint = tiempo-segundos
            segundos=str(int(segundosint))
            contador=fuente1.render(segundos,0,(0,0,0))
            s_lifes = fuente1.render(str(lifes),0,(0,0,0))
           
            
        else:
            contador=fuente1.render(segundos+"quesos que se comio"+str(comidos),0,(0,0,0))
        score1 = fuente1.render(str(score),0,(0,0,0))
        pantalla.blit(info,(715,230))
        pantalla.blit(puntaje,(710,120))
        pantalla.blit(score1,(720,170))
        pantalla.blit(contador,(720,60))
        pantalla.blit(tiem,(710,20))
        pantalla.blit(nombre,(700,380))
        mapa = pygame.transform.scale(mapa,(150,150))
        pantalla.blit(mapa,(700,425))
        
        for i in range(lifes):
            pantalla.blit(vidas,(680+(40*i),280))
        if quesosg == [] and quesosc == []:
            vnivel+=1
            jugadorr.top,jugadorr.left = 30,30
        
            fondo_s.fill((0,0,0))
            pintar(fondo_s,vnivel)
            paredes,quesosc,quesosg,relojes,ratones,gatos,jugador = seleccionar_nivel(vnivel)
    
      
        pygame.display.update()
        
      
main()
