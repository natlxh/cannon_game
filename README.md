# Cannon Game 🎯

Un juego simple de cañón creado con Python Turtle, parte de la colección **Free Python Games**.

## 📋 Descripción

Este es un juego arcade donde controlas un cañón que dispara una bola roja para destruir objetivos azules que se mueven de derecha a izquierda en la pantalla. El juego termina cuando un objetivo sale de la pantalla sin ser destruido.

## 🎮 Cómo Jugar

1. **Hacer clic en la pantalla** para disparar la bola desde la esquina inferior izquierda
2. El ángulo y velocidad del disparo se calculan según la posición del clic
3. Los **objetivos azules** aparecen aleatoriamente del lado derecho y se mueven hacia la izquierda
4. **Destruye los objetivos** haciendo que la bola los golpee
5. El juego termina si un objetivo sale de la pantalla por el lado izquierdo

## 🎯 Mecánicas del Juego

- **Bola roja**: Proyectil controlado por el jugador con física de gravedad
- **Objetivos azules**: Aparecen aleatoriamente y se mueven horizontalmente a velocidad constante
- **Gravedad**: La bola está sujeta a gravedad (desaceleración vertical de 0.35)
- **Colisión**: Los objetivos se destruyen cuando la bola pasa a menos de 13 unidades de distancia

## 🔧 Requisitos

```bash
pip install freegames
```

## 🚀 Ejecución

```bash
python cannon.py
```

O si tienes instalado `freegames`:

```bash
python -m freegames.cannon
```

## 📦 Dependencias

- **Python 3.x**
- **turtle** (incluido en Python estándar)
- **freegames**: Librería que proporciona utilidades como la clase `vector`

## 🎲 Características Técnicas

- Ventana de juego: 420x420 píxeles
- Área de juego: -200 a 200 en ambos ejes
- Velocidad de actualización: 50ms por frame
- Probabilidad de spawn de objetivos: 1/40 por frame
- Velocidad de objetivos: 0.5 unidades/frame

## 📝 Créditos

Este código pertenece a **Free Python Games**, una colección de juegos simples implementados en Python para fines educativos.

🔗 [Free Python Games - GitHub](https://github.com/grantjenks/free-python-games)

## 📄 Licencia

Este código es parte de Free Python Games. Consulta la licencia original del proyecto para más información.