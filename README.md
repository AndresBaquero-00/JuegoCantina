# Proyecto final
## Integrantes:
- Andrés Leonardo Baquero Hernandez
- Santiago Andrés Gordillo Piñeros

## Patrones implementados en el programa
- Factory Method:

Define una interfaz para crear un objeto, pero deja que sean las subclases quienes decidan qué clase instanciar. 
Permite que una clase delegue en sus subclases la creación de objetos.

Este patrón lo implementamos a la hora de crear los clientes, cervezas y el cantinero, en la clase llamada "Creador" la cual tiene métodos "crearProducto() y factoryMethod()". Estos se reparten en las subclases las cuales serían "CreadorCliente, CreadorCerveza y CreadorCantinero", cada una de estas crea un objeto del producto correspondiente.

![](https://github.com/SAGO2001/ModelosI/blob/master/FactoryMethod.png?raw=true)

- Memento:

Representa y externaliza el estado interno de un objeto sin violar la encapsulación, de forma que éste puede volver a dicho estado más tarde.

Este patrón lo implementamos con las clases "Nivel, Memento y Caretaker", en "Memento" se crean las variables a guardar, "clientes y nivel", en "Nivel" se crea la interacción de estas variables y por últio "Caretaker" tiene dos métodos, estos obtienen el memento o lo modifican.

![](https://github.com/AndresBaquero-00/JuegoCantina/blob/master/Memento.png?raw=true)

- Prototype:

Especifica los tipos de objetos a crear por medio de una instancia prototípica, y crear nuevos objetos copiando este prototipo.

Este patrón lo implementamos en las clases "Ceveza y Cliente" por medio de un metodo llamado "clone", con este clonamos el producto y lo guardamos en su arreglo correspondiente.

![](https://github.com/SAGO2001/ModelosI/blob/master/Prototype.png?raw=true)

- Iterator:

Proporciona un modo de acceder secuencialmente a los elementos de un objeto agregado sin exponer su representación interna.

Este patrón lo implementamos en la clase Iterador, aquí creamos los métodos "primero, siguiente, hayMas y actual", los cuales nos dan el primer elemento del arreglo de objeto, el siguiente objeto en el arreglo, si hay más objetos y el objeo actual respectivamente, por los productos correspondientes

![](https://github.com/SAGO2001/ModelosI/blob/master/Iterador.png?raw=true)

- Facade:

Proporciona una interfaz unificada para un conjunto de interfaces de un subsistema. Define una interfaz de alto nivel que hace que el subsistema se más fácil de usar.

Este patrón lo implementamos en la clase "Juego" ya que en esta clase importamos todas las clases que son necesarias para el funcionamiento del juego. Después en la clase "bar" importamos la clase "Juego" para ya crear la lógica del programa

![](https://github.com/SAGO2001/ModelosI/blob/master/Facade1.png?raw=true)

## ¿Por qué no usamos otros patrones?

- Los 5 patrones implementamos son suficientes para crear todas las funcionalidades del programa

- Creamos los clientes, las cervezas, al cantinero y todas las interacciones entre ellos 3

## Manual:

- Al abrir el juego presionamos la tecla F1 para iniciarlo, iniciamos en el nivel 1, vemos 4 barras

![](https://github.com/AndresBaquero-00/JuegoCantina/blob/master/Cantina.png?raw=true)

- Observaremos al cantinero y a un cliente en la primera barra, pulsamos la tecla UP y la tecla DOWN para subir y bajar entre las barras repectivamente

![](https://github.com/SAGO2001/ModelosI/blob/master/Cantina2.JPG?raw=true)

- Los clientes estarán posicionados en cada una de las barras de acuerdo al nivel y se irán acercando al borde derecho de la barra, si un cliente llega a este borde se perderá una vida, el juego termina cuando las vidas lleguen a 0

![](https://github.com/SAGO2001/ModelosI/blob/master/Cantina3.png?raw=true)

- Pulsamos la tecla SPACE para servir una cerveza en la barra la cual el cantinero esté posicionado

![](https://github.com/SAGO2001/ModelosI/blob/master/Cantina6.png?raw=true)

- Al servir la cerveza, esta se irá acercando a la pared izquierda, si la cerveza llega a un cliente este la beberá y en el proceso irá retrocediendo acercandose al muro de la izquierda, si llega a este muro el cliente se irá satisfecho

![](https://github.com/SAGO2001/ModelosI/blob/master/Cantina5.png?raw=true)

- Si una cerveza llega al muro izquierdo esta se romperá y se perderá una vida

![](https://github.com/SAGO2001/ModelosI/blob/master/Cantina4.png?raw=true)

- Se aumentará de nivel cuando todos los clientes de todas las barras se vayan satisfechos del bar
