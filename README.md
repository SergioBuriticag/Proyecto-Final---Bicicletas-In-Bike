# README Proyecto final - Tema 04:
### Empresa: IN - BIKE :bicyclist:

En este proyecto se da solucion a la problematica planteada en el archivo
-> **Tema_04_bicicletas**

Esto consiste en el desarrollo de un sistema de gestión de bicicletas, diseñado para facilitar el registro, consulta y administración de la información relacionada con los anclajes _(si la bicicleta esta o no en una estación)_ y sus respectivos mantenimientos.

El sistema permite almacenar información, consultar registros existentes y llevar un control de las actividades de mantenimiento, utilizando archivos CSV como medio de almacenamiento de datos.

Su propósito es organizar y facilitar la gestión de la información, ofreciendo una herramienta sencilla que permita realizar estas operaciones de manera estructurada.
<p>
**Nombre de los desarrolladores: **
- Mateo Espinosa Atehortua
- Sergio Alejandro Buritica Gonzalez
</p>

### Explicación

El proyecto surge de crear la gestión y el seguimiento de una empresa de bicicletas llamada **In-bike**, evitando problemas como la pérdida de información, la desorganización de los registros y el tiempo excesivo dedicado al control manual de su estado físico y operativo.

Este proyecto se hace desde la perspecetiva de un controlador/administrador el cual controla remotamente desde una central el sistema operativo; **No** se hace desde la perspectiva de un usuario

Para ello, se desarrollo una solución que permite centralizar la información de las bicicetas, facilitar el control de su disponibilidad tanto como unidad como en las estaciones y organizar el historial de sus reparaciones y mantenimientos ademas de los historiales de prestamo, clientes, etc.. _(La mayoria de estos archivos son creados internamente gracias al proceso del codigo)_. De esta manera, se busca simplificar las posibles tareas administrativas y mejorar el acceso a la información.

#### Objetivos especificos
1. Mostrar de manera dinamica la forma en que estan disponibles las bicicletas en las diferentes estaciones, actualizando de manera automatica su estado utilizando caracteres de referencia como:
-"000" Si esta vacio el espacio.
-"XXX" Si el anclaje esta en mantenimiento.
-"B01" Si el anclaje posee una bicicleta, siendo la "B" la forma de denominar la palabra. **Bicicleta** y los dos numeros consecuentes el numero de registro de la bicicleta.

1. iniciar el prestamo de bicicletas, creando el archivo de registro de usuarios ademas de tener un control de lo usuarios que tienen un prestamo activo para que no se realicen mas prestamos para la misma persona.
Tambien se debe implementar un uso de tiempo para tener control de salida de la bicicleta y el inicio del prestamo.

1. Teniendo en cuenta lo que se explico en el intem anterior, se muestra de manera especifica la cantidad de prestamos acrivos que posee el sistema en el momento gracias a los debidos procesos que se deben de realizar en el item 2.

1. Se verificara que existan bicicletas prestadas y anclajes disponibles en las estaciones para poder hacer la devolucion de la bicicleta. Se solicitara la hora de finalizacion de prestamo para hacer un cobro por el tiempo que se utilizo la bicicleta, tambien para hacer una actualizacion de los archivos de datos.

1. Como anteriormente lo definimos, en el principio de este docuemento, al ser un administrador/controlador debemos tener la capacidad de poner un anclaje en MANTENIMIENTO o respectivamente porder REACTIVARLO dependiendo de la circusntancia, ademas de tener un control de estos movimientos en otro historial independiente.

1. Hacer la distribucion respectiva de bicicletas en el caso de que alguna estacion se este quedando sin equipos, logicamnte, de manera automatica haciendo que el controlador solo tenga que aceptar el cambio, esto viendose reeflejado en el item 1 por su actualizacion inmediata.

1. La salida de manera correcta del programa.

Tenga encuenta que cada uno de estos **items** define cada punto que puede encontrar en el menu principal del codigo.


#### Herramientas
Se utiliza python como lenguaje de programacion y las librerias necesarias para hacer este proceso fueron:
- time: Se utiliza la variable para hacer animaciones a lo largo del codigo.
- csv: Indispensable, así se interpretan de manera adecuada los diferentes archivos CSV que se manejan a lo largo del codigo


#### Correcta instalación del codigo
Se recomienda tener el archivo guardado/alojado en el **ESCRITORIO**, para la correcta ejecucion se le compartira todo el conjunto de archivos dentro de la carpera **logica de programacion U** junto con todos los archivos necesarios para su correcto funcionamiento, cree la carpeta ayudandose con el siguiente fragmento:
```
with open("logica de programacion U/- PROYECTO FINAL/estacion.csv", "r", encoding="utf-8") as Archivo_Estacion:
```
Verifique que este requisito sea realizado con exito puesto que la funcionalidad del codigo se puede ver comprometida.
Si no funciona de manera adecuada el codigo, realize el cambio manual de cada una de las **rulas relativas** en cada uno de los **With**, cercioreze reiteradamente que esta condicion se cumple.

#### Archivos
Se compartiran la siguiente lista de archivos:
1. **anclajes.csv:** Archivo donde se encontrara los anclajes junto a su bicicleta correspondiente en una posicion predeterminada con el siguente orden:
| estacionID | fila | columna | estadoAnclaje | bicicletaID |
Se entregara de manera base para que se pueda operar si el usuario desea hacer operaciones.
1. **bicicletas.csv:**Archivo donde se encontrara los ID de las bicicletas, su estado y la estacion donde esta ubicada, tendra el siguiente orden:
| biciID | estadoBici | estacionActual |
1. **estacion.csv:**Archivo donde se espicifa cuantas filas y cuantas columnas va a tener la matriz y sucesivamente las matrices posteriores que dependen de la general
(Basicamente si este archivo sufre alguna modificacion, todo el codigo colapsa o como diria un profesor _Explota ;) _)

Se le entraga una carpeta de archivos originales en el **.ZIP** entregable, SAQUE ESTA CARPETA DE LA  CARPETA LOGICA DE PROGRAMACION U , esta carpeta solo cumple con la funcionalidad de que tenga un respaldo de los archivos con los cuales va a trabajar, no aporta nada a la ejecucion del codigo, no modifique estos archivos bajo ninguna circunstancia.

Se le proporcionaran los diferentes casos de prueba ejecutando cada uno de los apartados del menu principal con sus archivos en la forma necesaria para la ejecucion.

Revise atentamente las carpetas adjuntas, dentro de cada Case # hay un archivo .txt que contiene lo que va a pasar en el codigo.
