from random import randrange
from turtle import *
from freegames import vector


ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


def tap(x, y):
    "Dispara una nueva bala desde la esquina inferior izquierda."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        #  Aumentar velocidad del proyectil (antes /25, ahora /15)
        speed.x = (x + 200) / 15
        speed.y = (y + 200) / 15


def inside(xy):
    "Regresa True si el punto xy está dentro de la ventana."
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    "Dibuja la bala y los blancos (targets)."
    clear()


    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')


    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')


    update()


def move():
    "Mueve la bala y los blancos."
    # Aparecen nuevos targets ocasionalmente
    if randrange(30) == 0:  # Más frecuentes
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)


    # Los targets se mueven más rápido
    for target in targets:
        target.x -= 2


        # Si un target sale por la izquierda, reaparece a la derecha
        if target.x < -210:
            target.x = 210
            target.y = randrange(-150, 150)


    # Simula gravedad en la bala
    if inside(ball):
        speed.y -= 0.5  # Un poco más fuerte
        ball.move(speed)


    dupe = targets.copy()
    targets.clear()


    # Eliminar targets si la bala los toca
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)


    draw()


    ontimer(move, 30)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()