0:03
[Música] ok muy buenas tardes vamos a dar inicio
0:08
con lo que es el taller de pibil y como siempre sientas en la libertad de
0:13
generar los distintos comentarios o dudas que tengan en este en realidad el
0:20
taller es bastante voy a ir explicando ciertos conceptos para complementar
0:26
mucho de las cosas que hemos visto en el curso pero también poder ir entendiendo algunas de las funcionalidades
0:32
importantes que se tienen dividir es una biblioteca desarrollada tanto para parten como para
0:38
más la y está desarrollada principalmente por insania
0:45
laboratorio lo que es el laboratorio nacional de
0:50
modelado digamos para sistemas fotovoltaicos en el caso de los estados unidos hay muchos paquetes muchos
0:58
tutoriales y esto lo que quiero después darles una guía un poco tropicalizada lo que queremos hacer
1:05
por acá y les dejo la parte del enlace es súper importante que puedan estar
1:10
trabajando entonces para el trabajo del día de hoy vamos a estar trabajando con esta herramienta no sé si ustedes la
1:17
conocen se llama google cola que es una herramienta de trabajo colaborativo a nivel de los diferentes
1:24
desarrollos de software que se puede utilizar es bastante robusto y quizás
1:30
uno de los temas es que puede tener un tiempo de compilación mayor porque se trabaja un poco a nivel de nuevo ya de
1:36
lo que puede ser un editor o un entorno de desarrollo normal pero si permite
1:43
ciertas características interesantes especialmente en dos cosas que es lo que más nos interesa a
1:48
nosotros el primero de ellos va a ser el tema de el análisis de los datos y la
1:54
visualización eso es sumamente importante y lo podemos hacer al dedo en otros entornos de desarrollo pues hay
2:01
que sacarlo y uno segundo en la parte colaborativa es un documento como se hace con google
2:08
o cualquier parte de google se puede trabajar de forma colaborativa entonces nada más se puede nombrar dentro de él
2:22
dentro del entorno vamos a llamarlo taller introductorio de tribilín y vamos a ver que no tiene mayores entornos que
2:29
meto a una parte de índice uno de los temas importantes es que se pueden generar documentación y principalmente
2:36
casillas de texto entonces a nivel de las casillas de texto podemos colocar
2:45
bill es lo que podemos colocar casillas de texto por acá y simplemente tener
2:51
diferentes referencias y también dado la parte de visualización importante
2:57
entonces simplemente siempre a nivel de las casillas con trabajar check y enter
3:05
se puede pues trabajar en los diferentes aspectos por acá se maneja una parte de índices porque se puede ir colocando
3:12
texto normal con columnas o fragmentos de código ok se puede trabajar una parte
3:18
de herramienta de búsqueda lo cual va a ser bastante útil también todas las diferentes variables que se van generando así como toda la parte de los
3:25
diferentes archivos posiblemente aunque hoy la clase es de un solo script ok
3:32
cuando se trabaja en proyectos más complejos especialmente en temas de simulación en temas de optimización pues
3:39
va a ser necesario cargar todo lo que son las bases de datos disponibles etcétera etcétera entonces es una
3:46
herramienta bastante valiosa también en el taller y haya hablado algunas de las bibliotecas no tanto de esta herramienta
3:52
pero en términos generales es bastante simple de usar bueno cuenta con las
3:58
funciones normales de las muchas herramientas a nivel de archivo toda la parte de edición
4:04
principalmente para poder acomodar toda la parte de programación en la parte de visualización de que se puede ver que no
4:11
se puede ver hay un tema importante que puede ser interesante a nivel de desarrollo que permite ver también
4:17
historiales entre los diferentes participantes del código y bueno todo lo que es la incorporación de celdas
4:23
ejecutar todo además sin más preámbulo vamos a lo que vinimos ok entonces lo
4:29
primero que nos toca es la instalación de civiles como tal hay un tema
4:37
importante y es el gestor de paquetes pp que es un
4:43
gestor de paquetes nativo de payton simplemente para la parte de instalación de diferentes bibliotecas con esto se
4:49
puede instalar y este voy a instalar una vez otra biblioteca que va a ser de
4:54
utilidad a nivel de el taller del día de hoy que
5:00
va a ser paper y vamos a hablar de ella más adelante install a de tus porque
5:07
entonces simplemente pueden ejecutar o simplemente con control entes también
5:12
pueden pasar de casilla entonces va a ser la parte de ejecución va a instalar los no necesariamente deben de estar
5:19
instalados el hecho de que sea un signo de exclamación y simplemente para hacerlo en un entorno virtual y con esto
5:26
puedes generar las diferentes características importantes entonces bueno aquí ya se
5:31
están generando la parte de requerimientos a nivel de payton pues
5:37
siempre es importante poder tener ciertos elementos generales está terminando la parte de
5:42
instalación de ustedes pueden ver los comandos de ejecución y el tiempo que se utiliza para hacerlo como les digo puede
5:49
ser un poco más lento ahora bien a lo que hemos con lo que puede ser de utilidad y es
5:57
la importación es normal en impacto que la importación
6:05
de bibliotecas una pregunta pueden ver bien la pantalla o walt un poco más grande la letra
6:13
si la pueda ser mejor si la puede ser grande mejor
6:19
porque está mejor no tal vez ahí
6:25
ahí se ve mejor mucho mejor ok perfecto entonces bueno a nivel de
6:30
importación de las bibliotecas bueno está haciendo no la ejecuté ni nada pero entonces vamos a importar ciertas
6:36
bibliotecas importantes y una vez que ya tenemos instalado el paquete importamos pib y le ven ustedes que ya también el
6:42
gestor de paquetes me lo asigna también vamos a importar bandas que es una
6:49
biblioteca de manejo de datos que va a ser sumamente importante me voy a
6:55
referir de ir más adelante y vamos a importar más blog live
7:01
by plot así que nada más un comentario al margen estos as que se utilizan a
7:08
nivel de las bibliotecas lo que se conocen es para generar un alias entonces vamos a ver cómo funcionan
7:14
estas bibliotecas son básicamente un llamado a un objeto y entonces para no
7:19
estar colocando todo simplemente se llama a nivel del alias ok entonces
7:26
sabrán que hemos con una parte de ejemplo voy a crear un diccionario o más bien una tabla de objetos para poder
7:33
hacer una primera comparación general el software va a arrancar básicamente como también hemos arrancado en el curso
7:40
con lo que es el manejo de bases de datos a nivel general
7:46
entonces en este caso voy a arrancar con diferentes aspectos importantes dentro
7:54
del ejemplo nada más este primer ejemplo que voy a mostrarles es un seguimiento del tutorial que ya
8:02
viene por acá y simplemente para el que a nivel registrado entonces tengo que las latitudes lo que el
8:10
latitud y la longitud y cómo se acomodan entonces punto cero
8:18
juntos pero como entonces aquí colocamos el nombre de la ciudad nada más para generar una referencia se coloca al
8:26
nivel de altura y esto ya lo vamos a ver porque 700 y colocamos entonces en la zona
8:34
horaria que vamos a utilizar en la zona horaria nada normal gtm más 7 ok
8:41
entonces como les dije vamos a generar la tecla que es una serie de elementos
8:47
importantes entonces la mayoría de los archivos en tbilisi funciona de la
8:52
siguiente forma va a utilizar como como un parámetro de entrada la actitud
8:58
y la longitud el nombre ok pero el nombre simplemente
9:05
puede ser cualquiera no es un atributo que lo voy a utilizar para computar y la zona horaria en la zona horaria pues se
9:13
puede utilizar diferentes nomenclaturas en este caso podemos utilizar simplemente por zona horaria donde
9:20
pertenece cada uno de estos lugares en este caso vamos a meter otro lugar para
9:26
que vean una parte comparativa y cómo se pueden generar con computar cálculos en paralelo del mismo tiempo esto punto 6
9:34
esto lo vamos a llamar al you're que aunque esto también es en eeuu la
9:42
sede donde se encuentra sand ya va a ser importante porque ya les voy a contar la parte de la historia y entonces esto va
9:51
a ser también 77
9:59
y entonces simplemente lo voy a copiar
10:11
y luego pues entonces vamos a copiar nada más un par de ocasiones para el listo entonces me voy a devolver
10:20
por acá aquí vamos a poner 37.8 que en la localización que tenemos igual esto
10:26
luego al final del taller lo voy a estar tropicalizando con un ejemplo pues de
10:31
nuestro querido text para que lo tengamos a nivel de la localización que decía y qué puedo hacer de diferencia
10:38
también para los diferentes proyectos de ustedes en este caso vamos a hacerlo como san francisco
10:45
donde la altura con respecto al nivel del mar es de 10 metros ok y vamos a
10:53
utilizarlo al otro lado del planeta a kim cercano de donde estoy evelyn entonces berlín se encuentra a
11:01
una latitud de 37.6 a nivel de coordenadas y por acá y ya
11:07
tenemos berlin 34 ok
11:13
7 m menos 1 nada más para tenerlo aquí como la parte de referencia ok nada más
11:21
antes de entrar a hacer algún cálculo lo otro que me interesa es obtener lo que
11:27
son los módulos e inversores ok entonces vamos a
11:34
utilizar los siguientes comandos simplemente donde no mire una variable que es una variable que va a ser un
11:41
objeto de datos completo y en este caso vamos a llamar porque y aquí es donde
11:48
empieza la primera parte de las convocatorias o los llamados a la biblioteca de pib y si
11:55
me quedo con efecto según aparentemente almaguer correcto y es lo que me estaba
12:02
arrastrando problemas en todos muchas gracias
12:07
entonces vamos a arrancar con lo que es el llamado de la biblioteca la
12:13
biblioteca siempre se va a llamar y les voy a enseñar un método abreviado más adelante vamos a llamarlo y lo siguiente
12:20
que vamos a llamar es las diferentes funciones si ustedes nos ven el conforme
12:26
se va avanzando jetsun
12:32
ok y esto vamos a llamar la parte de sand ya modo en este caso cuando
12:39
trabajamos a nivel de los sistemas y este se trabaja a nivel de los
12:44
diferentes componentes trabajamos
12:50
aunque hay una forma fácil de buscar yo dentro de la biblioteca simplemente buscamos todo esto lo pegamos por acá a
12:57
nivel de la documentación que me queda fácil para poderles explicar en este caso simplemente nos devuelve los
13:04
diferentes modelos por defecto que ya cuenta la herramienta en este caso hay varios modelos entonces
13:12
el de la comisión de energía de california en el laboratorio también y
13:18
el de anthony dice que es un investigador que trabaja bastante en la parte de modelado bastante fuerte
13:24
entonces existen diferentes modelos básicamente lo que hacemos es solicitarle los distintos modelos que
13:30
tenemos ok y en este caso también vamos a solicitar inviertes en verter entonces
13:38
estos son de el sistema para eso model en que básicamente es un ente del departamento
13:46
de los eeuu entonces igual generamos un paquete de datos en el cual le vamos a solicitar y bilic punto crisis
13:55
si este punto dos brit trip en este caso le vamos a pedir también
14:02
los inversos entonces esto lo vamos a llamar css inglés ok vamos a correr la
14:09
línea esta primer bloque de código pues todo se hace sin ningún problema y vamos a corroborar qué fue lo que pedimos el
14:15
primero de los bloques que llamamos llamamos los módulos disponibles aunque estos son módulos comerciales que
14:21
disponen la herramienta todos ustedes ven que se genera una base de datos con distintos paneles
14:28
que son bastantes y se generan todos absolutamente todas las características
14:33
importantes del módulo tanto lo que es el área verdad y lo que es la fecha en
14:40
la que se generó la cantidad de seres en serie en paralelo cuánto es la corriente
14:46
de cortocircuito la corriente el voltaje del circuito abierto la corriente y potencia máxima y los diferentes
14:52
parámetros o las pérdidas que se pueden tener bajo diferentes modelos que más adelante los vamos a ir viendo más
14:59
utilizados vean ustedes que tenemos 42 filas y una
15:04
523 columnas desde si tenemos 523 paneles disponibles en esta base de
15:10
datos lo mismo pues pasaría si nos venimos con la parte de los inversores aunque entonces simplemente llamamos
15:16
nuestra variable
15:22
y entonces vamos a tener lo mismo esto es perdón es un clásico de
15:29
programación simplemente hacerlo y tenemos 3.274 modelos de inversores nada más una
15:36
nota al margen a nivel de cómo funciona la biblioteca la biblioteca casi tiene
15:42
una dependencia directa de pandas entonces esto que vemos acá son de
15:48
objetos de datos porque yo lo que se conoce como data frame y por ahí pues
15:53
pueden revisar también cómo funciona pandas y entonces él a lo interno lo que hace es un llamado a pandas y por eso es
16:00
que lo va a terminar pidiendo porque entonces es bueno tenerlo por ahí aunque no lo estemos llamando directamente
16:06
entonces lo que ven es que es un data frenó bases de datos que simplemente da de diferentes características a nivel de
16:12
inversores la el voltaje que eso todavía no hemos hablado un poco a nivel del curso el voltaje de red las potencias
16:19
que se tienen en general en la potencia hace la potencia en desee los voltajes y
16:25
los diferentes componentes a nivel de los modelados que se pueden tener ok entonces ahora ya una vez que que nada
16:33
más convocamos a todos los modelos vamos a seleccionar uno específico ok siguiendo la falta del ejemplo para
16:40
poderles explicar vamos a utilizar de los modelos de sand ya que entonces vamos a convocar esto es relativamente
16:46
fácil es hacer un llamado como ustedes hicieron llamado analista oa un repositorio el programa condicional no
16:53
una hora lista en realidad entonces vamos a llamar al canadiense las
17:00
que es el modelo del panel entonces vamos a utilizar el
17:07
cs 5 p
17:13
a los 20m ok y aquí va a ser
17:21
y 2009 porque ese es el modelo del nombre nada más en la convocatoria del nombre
17:28
que ustedes pueden tener por acá esto que estoy colocando acá es exactamente el nombre de él
17:36
del panel solar tal cual como viene a nivel general entonces
17:42
lo mismo vamos a hacer para el inversor entonces en este caso el buscaron
17:48
inverter simplemente voy a utilizar un micro inversor eso también los vamos a ver un poco a nivel del curso podemos
17:55
tener la parte de los inversores en este caso y vamos a generar
18:02
este inversor el que creo que es el primero es el micro
18:07
este es el primero que vamos a tomar podríamos simplemente copiarlo desde acá pegarlo por acá
18:14
y luego tenemos también que vamos a generar un tema de la temperatura tubo
18:21
del modelo térmico del pan que como se ven ya se pueden ir generando las diferentes
18:29
modelos de corrección por temperatura entonces en este caso vamos a decirle
18:34
deme los parámetros del modelo
18:41
y donde entonces volvemos a llamar a la biblioteca civil y en este caso vamos a
18:46
llamar al módulo temper ayer la temperatura y en este caso vamos a
18:52
llamar el sub módulo en mayúsculas y témperas your mother
19:02
mires entonces ahí ya lo tenemos el
19:09
simplemente lo que hace es la parte de los nuevos diccionarios en la creación y vamos a darle varias cosas lo primero
19:14
que le damos en este caso es el modelo que es el del sistema al país o el
19:20
modelo que es este que tenemos por acá donde calcula la temperatura de celda utilizando el modelo de sant ya hay
19:27
varios modelos también están los modelos de como lo pueden ver tenemos el modelo de sand ya el modelo de facebook de
19:34
fuentes del bosque simplemente los diferentes autores que lo tienen nosotros ahora vamos por la luna con el
19:39
de santiago el de piscis y vamos a trabajar también con el de facebook que el que se les enseña a ustedes es el de
19:47
facebook que es muy similar al msp que es el que actualmente hemos trabajado para fines del objeto y lo otro que
19:54
quede sigue para el cálculo del módulo porque ahora si lo hace un poco más preciso es el modelo que debe seguir en
20:00
este caso es copper drive
20:08
glass glass o que un panel glass simplemente en un rack abierto corremos
20:14
la línea y aunque parece que hay un error dentro del módulo entonces más de
20:22
verlo por acá y este error de un módulo a le hacía falta aún si hacía falta
20:28
ondas no nada más lo copiamos en los de fruta y parece que
20:36
[Música] parece que no les está gustando vamos a
20:41
ver i
20:47
y aquí es simplemente sandía performance módulo es al revés 9 cmpc y
20:54
9 pm y entonces ahora si ya está ocurriendo sin ningún problema agregamos una casilla de código y ahora tenemos
21:00
las variables definidas de módulo e inversor que son unos objetos ya lo
21:06
vamos a ver entonces nada más para ver la convocatoria que tenemos a nivel del model lo llamamos al nivel de módulo y
21:13
aquí vemos todas las características del panel canal y el solar el csp 5p y de
21:21
220 vatios demanda el área 2 el tipo de porcentajes que se quiera y todas las
21:27
características eléctricas que son básicamente las mismas características eléctricas que vienen a nivel del módulo
21:32
llamamos el inversor nada más para corroborar cuál es la información que se genera y todos los datos pues necesarios
21:39
a nivel del inversor si quisiéramos ver los modos los de temperaturas también
21:44
que acabamos de calcular simplemente son los factores de
21:50
corrección
21:58
entonces vamos a ver que nos da como resultado esta modelo de ecuación y esto
22:05
es importante nos da un modelo de temperatura de celda pero todavía no nos
22:11
da la temperatura de celda porque recordemos que esta temperatura de celda depende de la temperatura ambiente lo
22:18
que nos da es simplemente las variables o las constantes para irlo calculando a
22:23
nivel general y vean ustedes que en este caso para este módulo en específico que
22:29
va en función de las características que ya presenta al módulo nos dan la constante a b y delta de este modelo y
22:38
este modelo está proporcional a la irradiancia tal cual como el que es muy similar el que mostramos en clase que es
22:44
el más práctico a nivel de trabajo manual ya nivel de modelado se utilizan
22:50
estos modelos de corrección por la velocidad del viento que lo vamos a ver más adelante y la temperatura
22:57
ambiente que es lo que se puede generar luego la temperatura del módulo en la parte trasera y esto calcula la
23:03
temperatura de trabajadores simplemente generamos las constantes para la
23:08
siguiente parte de geolocalización que se puede tener entonces ahora vamos a
23:14
entrar en detalles y lo que quisiéramos ver con este ejercicio es cuánto es la
23:19
energía que un panel de estos porque con un inversor de estos que es un micro inversor
23:26
nos puede generar vean que es un inversor pequeño vea la potencia que tiene es una potencia en hace de 250
23:35
vatios entonces esta potencia son apenas para colocarlo en la parte trasera del
23:41
módulo de alimenta cada uno de ellos y todo lo que quisiéramos con el experimento es simplemente hacer un
23:46
modelo de los paneles y estimar cuánto de la energía necesaria para cada uno de
23:52
ellos y durante todo el año entonces vamos poco a poco para eso para eso vamos a
23:59
dado que vamos a trabajar con la integración de una lista nos vamos a integrar sobre la lista vamos a generar
24:06
una lista vacía qué es básicamente una lista posibilidad
24:11
que va a guardar los datos atmosféricos que se tienen a nivel de la planta ok y
24:16
en este caso vamos a generar un fork por lo que jason que fue los que ya estuvimos viendo a la vez anterior en
24:23
con emails que simplemente es ir viendo sobre la lista y para esto vamos a obtener la latitud
24:34
el nombre la altitud que son todos los variables que se tienen y la zona horaria que va a
24:42
ser igual a la locación en este caso vamos a convocar a otra
24:49
variable que sea la variable climatológica para conocer las condiciones del tiempo y en este caso
24:55
vamos a llamar a philip ok que es la biblioteca ya la hemos conocido y vamos
25:00
a utilizar pidió tools que está por acá y vamos a decirle que
25:07
quisiéramos conocer [Música] en el tiempo
25:14
en las condiciones meteorológicas que podemos tener y ya lo vamos a ir viendo como tal porque lo que me va a entregar
25:21
es la base de datos que esto es importante basado en la meteorología
25:27
te sale entonces en este caso esta es la función vamos a buscar la nada más para
25:33
para poder explicar tener un poco más de forma más atractiva de que la documentación es bastante robusta
25:41
y entonces en este caso lo que va a obtener es en función de un time de la
25:48
longitud y la latitud básicamente que le doy va a obtener la data de la base de
25:53
datos del data his en esto obtener básicamente toda la data que ya la vamos a ir viendo entonces obtenemos las
26:01
diferentes funciones y le vamos a decir el latitud
26:07
la longitud vamos a hacer un mapeo de las variables
26:12
que simplemente es para que mate o extraiga todas las variables que yo puedo tener si a esto le doy false lo
26:20
que me toca de forma adicional es decirle qué variables quisiera obtener
26:26
en el general hacemos el mapeo le decimos entonces que quiero todas las
26:31
variables siles y esto es fútbol tengo que indicarle manualmente cuáles son las variables que tienen y lo que voy a
26:38
hacer dentro de la cómoda es simplemente hacer un indexado que esto lo hacen
26:45
pandas ok de los diferentes nombres que se tienen y esto se va a llamar a good
26:55
time por qué porque esta función lo que
27:00
me va a extraer es cada uno de las condiciones metereológicas para un
27:06
período de tiempo general entonces va a crear una base de datos completa donde yo voy a poder obtener los diferentes
27:13
aspectos generales que y simplemente éste index o cada uno de sus bloques porque
27:20
lo va a empezar a indexar por diferentes años ya vamos a ver el resultado y esto simplemente luego lo traslado
27:27
a mi variable oa mi diccionario que ya creía anteriormente entonces a esto vamos a usar papel que
27:34
básicamente nada más agregar al final que es otra variable de pandas y esto
27:40
simplemente nos da la variable de webber que es simplemente la que creamos acá y
27:46
la que estuvimos llamando por acá porque al ser una base de datos vean que demora su tiempo a nivel de la ejecución y lo
27:55
que intenta extraer es una base de datos de todo lo que esté disponible para esas épocas entonces va a ser una consulta al
28:02
servidor y empieza a extraer absolutamente todos los datos habidos y por haber ya se ejecutó entonces para
28:11
poder corroborar vean que es algo interesante que tiene también la herramienta
28:16
el google con la que yo no tengo que hacer temas de impresión sino que lo veo entonces lo que hicimos acá es para cada
28:23
una de estas longitudes y latitudes obtener la base de datos meteorológica
28:28
que podemos tener a nivel general y en este caso la base de datos meteorológica me lo da completamente todo lo que eso
28:35
le podrías de ser de utilidad para ustedes a nivel de los proyectos la temperatura del aire la humedad relativa
28:41
todo lo que es la radiación global
28:47
en el plano horizontal perdón la radiación directa la radiación difusa todo lo que es el índice de claridad que
28:55
se puede tener la velocidad del viento la dirección del viento la presión la temperatura del aire la humedad relativa
29:01
y ya vuelve otra vez simplemente por la parte de cómoda porque estábamos
29:06
haciéndolo para cuatro lugares distintos ok entonces nada más parte de las
29:12
condiciones que se pueden tener y con eso ya tenemos la base de datos incluso ustedes podrían descargar y jugar un
29:18
poco con dicha base de datos a nivel general más adelante vamos a ver
29:23
algunas cosillas de la base de datos a nivel general ahora sí vamos a hacer lo
29:29
que puede ser el tema más complejo que es ahora si toda la
29:35
continuación y la basada en esa base de datos comentamos esta base de datos para
29:41
cada una de las locaciones con el sistema con el sistema que el sistema es el módulo y el inversor es en este caso
29:48
vamos a tener el sistema y este sistema va a ser igual a
29:53
el módulo este mono es un diccionario lo que
30:01
estamos generando por aquel entonces el módulo o hacer la variable módulo el inversor
30:09
hacer el inversor como tal
30:16
y luego vamos a tener la y hacia dónde nos estamos localizando a
30:24
nivel del panel ok entonces de nuevo por acá recordamos las clases de energía solar de recursos perdón donde tenemos
30:32
una cima y este así lo vamos a definir en 180 en este caso la cima lo definimos
30:41
en 180 simplemente por el hecho de estar trabajando bajo una herramienta
30:47
estadounidense en la notación americana este surface máximos de 180 lo que
30:53
significa es que estamos viendo de cara al sol ok nuestro panel va a estar de
30:58
cara al sol en un ángulo de inclinación óptimo porque con lo que vamos a trabajar es el cálculo del ángulo de
31:04
optimización óptima que podemos tener entonces a nivel de las energías
31:12
o sea general simplemente la energía total de cada uno de los sistemas
31:18
entonces generamos una lista vacía para poderlo general y ahora si comenzamos con la parte de integración entonces
31:24
para cada una de las ocasiones que ya tenemos vamos a solicitar el güero y en
31:32
esto vamos a utilizar la función ser que es una función alternativa de
31:39
de payton donde esta función interactiva logra dos cosas en función de las
31:45
coordenadas obtiene el tiempo basado en la zona horaria simplemente para poder
31:52
complementar de poder hacer las consultas en bases de datos entonces en este caso vamos a llamarlo en función de
31:57
las coordenadas y de la variable en base de datos que ya tenemos para cada uno de ellos ok entonces ahora vamos a empezar
32:08
con la parte del lote vamos básicamente a llamar todas las variables que tenemos
32:13
de correlación la latitud y la longitud ok el nombre la altitud del lugar la
32:24
zona horaria ya esto entonces
32:31
lo vamos a llamar la educación de nuevo simplemente como el ejemplo anterior
32:36
ok a esto vamos a decirle que el sistema lo vamos a orientar
32:43
por la educación que tiene lo vamos a orientar como surface
32:54
es la variable que ya definimos y esto simplemente lo está calculando para cada
33:00
una de las latitudes del sistema recordemos que en los ángulos óptimos
33:06
los vamos a ir generando para los ángulos del sistema entonces básicamente acá no me estoy
33:11
complicando respecto a la inclinación ya vamos a hablar un poco de la inclinación del panel pero en este caso lo que
33:18
estamos diciendo es que el sistema va a estar viendo hacia el sur pero en
33:24
inclinación d de la latitud exactamente el mismo grado
33:30
que se tiene a ese grado va a estar el nivel general del sistema y ahora lo que
33:35
vamos a calcular lo primero que se tiene que calcular o computar es la posición del sol entonces peeling solar
33:42
position qué es la variable que nos da y utilizamos la variable get
33:49
solar position
33:56
en este caso entonces abrimos la posición del solar de la posición solar
34:03
y para esto necesitamos darle algunos aspectos importantes lo primero es la variable de tiempo dentro de la boca de
34:11
la función ya les voy a mostrar la función nada más para que lo vean y como
34:16
lo estuvimos anexando la vice anterior de la de la columna anterior ok vean que
34:23
el index name es simplemente el tiempo que estamos colocando por acá entonces esto
34:30
está bien vamos a utilizar entonces la latitud
34:37
igual como un latitud que vean ustedes que la misma los
34:43
parámetros me los está dando en función de la utilidad del lado de la función que necesita es una función un poco
34:49
compleja luego tenemos la longitud la longitud y esta longitud es igual a
34:58
la longitud altitud
35:04
s igual a la altitud
35:11
y la temperatura en este caso la vamos a obtener de nuestra base de datos que es
35:19
where ok y simplemente hacemos la convocatoria dentro del el sistema
35:28
ok vamos a llamarla como está nombrada en
35:35
la base de datos como la temperatura del aire
35:42
ok y a esto vamos a generar entonces la presión y la presión se obtiene mediante
35:50
otra biblioteca más pequeña que se llama pib y le damos field
35:57
ok altitud a presión hace una conversión directa y esto simplemente toma la
36:04
altitud que ya tenemos por acá entonces vamos por partes primero para entender
36:09
la descomposición de la función vamos a buscar la función para ver la parte de documentación vean
36:16
que lo que estoy haciendo es asignándole las variables de mi sistema a cada una
36:21
de las diferentes componentes bien que simplemente estoy asignando por casualidad les puse igual pero la
36:26
actitud podría ser la longitud podría serlo entonces simplemente es para irlo
36:31
descomponiendo y nos va a dar como resultado la posición del sol ok entonces
36:38
si no corto no deberíamos tener problemas y simplemente en este caso si yo llamo
36:46
son post ok lo que obtengo es la posición del sol basado en la base de
36:53
datos que se tiene que en este caso vean que esta base de datos me da cinco mediciones por minuto
37:02
entonces se vuelve bastante robusta a nivel general y entonces ya lo pueden ir
37:07
viendo paso a paso entonces bueno aquí ya se vuelve un poco por la cual se
37:14
puede volver un poco pesada de visualización y simplemente me lo devolvió sigamos con los diferentes
37:20
aspectos que nos hace falta tenemos la exposición del sol con la posición del sol podemos computar cuánto es la
37:27
radiación en el plano que se tiene y para esto vamos a utilizar entonces la
37:32
radiación directa normal extra que se puede recibir producto d
37:37
los diferentes elementos que se tienen poder vamos a llamar a extra igual y bilic
37:46
punto y gracias punto get
37:56
extra direction que simplemente es la
38:03
radiación extra que se podría generar producto de la posición del sol
38:09
d ok
38:14
no computará y sin problema sigamos con otras líneas vamos a obtener la masa de
38:19
aire recordemos que la masa de aire es importante para poder determinar cuánto de esta radiación normal se convierte en
38:27
difusa entonces en este caso vamos a llamar a la biblioteca pib y le punto atmósfera
38:37
punto 10 de latir
38:50
además y la masa de aire recordemos de las partes del recurso la
38:57
que es dependencia de la posición que se tiene del sol porque en esta la forma que incide sobre
39:05
la parte de la nubosidad y entonces la cantidad de rayos que nos pueden estar afectados y en este caso de la posición
39:12
solar vamos a utilizar el el cenit vamos a ver si puedo visualizar lo que no el
39:19
completo vean ustedes que de la posición solar me calcula varias cosas la elevación es el cenit senieta aparente
39:27
que simplemente es una parte de conexión la ecuación de tiempo solar que se tiene
39:32
las inútiles elevación que es tal cual el diagrama si bien dijo que tenemos de hecho que más adelante vamos a hacer un
39:38
pequeño ejercicio al respecto entonces yo tengo la masa de aire
39:44
a nivel del sistema vamos a calcular la presión también para que vean que este
39:50
es la simulación ahora si me da bajo las características
39:55
completas que se puede tener al tour 3
40:05
altitud
40:11
y luego tenemos la masa absoluta del aire
40:17
la anterior es relativa y esto es a nivel de los modelos que podemos ir
40:23
generando ya ya entre detalles un poco el modelo entonces nada más
40:31
inquieta
40:50
lo otro que nos corresponde es obtener el el ángulo de incidencia a nivel del
40:56
sistema entonces en este caso vamos a llamar en la biblioteca pibil y irradiados
41:03
punto ángulo de incidencia ok en este caso es una función un poco más compleja pero esta función lo que
41:11
nos permite es computar en función de la posición del sol la posición que se
41:16
puede tener entonces en este caso vamos a llamar a la del sistema simplemente que entienda
41:23
la superficie subsistir
41:30
aunque que esto lo definimos que fuera en la posición esto lo definimos por la
41:35
carrera que fuera nada más la latitud cuál podría ser cualquier otro valor system
41:43
surface
41:49
ok luego de esto vamos a utilizar como computación de esta variable
42:08
ok y este mismo vamos a utilizar del sol post
42:16
vamos a utilizar el así mod
42:27
a todos estos nos falta comer dentro de lo que es la función como tal
42:40
no te voy a compilar lo que puede ser un error dice que no están definidos y es
42:47
porque lo definí aquí nada más para que nosotros a base elevar y stella por en semis
42:54
[Música] y está dentro de la base de datos de acá es estar un doblete
43:05
aparece mit
43:13
ok y ahora lo que nos toca para de
43:19
generarlo de forma parecida y me voy lo voy a copiar nada más para ir adelantando y no tener que esperar la
43:24
parte de la explicaciones tenemos el ángulo de incidencia ok que simplemente es calcular bajo cada uno de los
43:31
diferentes temas la computación del sistema para eso ocupamos el ángulo en
43:36
el que estoy colocando el panel el azimut en el que estoy colocando el panel y sobre esto que compute sobre lo
43:42
que es el cemento o la elevación y el azimut donde se ubica el sol recordando el diagrama
43:48
cilíndrico lo mismo sucede para la radiación total que recibe el panel y de
43:54
nuevo el panel sobre la superficie el panel en el azimut cuál es la orientación de dicho panel la posición
44:01
del panel y la posición de la cima y ahora bien de la base de datos obtengo
44:06
la radiación directa la radiación global y la radiación difusa más el porcentaje
44:13
de radiación extra que se obtiene a nivel general y aquí los modelos van a
44:18
variar el que está por defecto es el de hyde davis que en esto voy a buscar acá
44:23
nada más para que vean los distintos modelos que se pueden tener entonces
44:31
en este caso son los diferentes modelos de radiación difusa que se pueden
44:37
generar que está el de hey davis que es el más utilizado o el de pérez también que es uno de los más viejos de hecho
44:44
que el de gente dice es una corrección del de pérez y hay que definirlos en función de los
44:49
modelos entonces va a determinar la radiación total en el plan una vez y
44:55
basándonos en lo mismo vamos a calcular la temperatura de celda en este caso la temperatura de celda va a tomar como
45:02
como variables de entrada el porcentaje de radiación total que se tiene la
45:09
temperatura del aire la la velocidad del viento y va a calcular basado en los
45:17
parámetros que habíamos calculado anteriormente a nivel de los módulos simplemente para obtener la ecuación de
45:23
aproximación del módulo fotovoltaico luego de esto vamos a calcular la
45:28
radiación efectiva esta anterior es toda la radiación general y esta radiación efectiva
45:34
refleja dentro de la radiación que ya tenemos la radiación difusa pero lo que
45:39
son las masas de aire que la masa de aire recordemos que está relacionado con la nubosidad de que tiene a nivel de
45:45
sistema y este son pues funciones repetitivas y el ángulo de inclinación
45:51
que se tiene el nivel del módulo ahora bien con todo esto yo tengo la
45:57
la parte digamos de la 'top model' para poderlo
46:04
general y ahora sí como genera el panel fotovoltaico es fácil simplemente yo utilizo pibil y punto el pib y system
46:13
ahora si estamos haciendo
46:18
en lo que es la parte de generación del momento y en este caso vamos a utilizar
46:24
efectivo la alliance ok como parámetro y la
46:29
temperatura de la del padre del bono
46:37
temperatura y luego vamos a utilizar el módulo que ya hemos seleccionado y en
46:43
este caso vamos a ver aquí yo tengo no tenía por acá pero simplemente este
46:49
parámetro de los modelos ya lo que nos da son los diferentes
46:55
modelos o los sistemas que se pueden generar y estos son simplemente para la
47:01
generación de la energía producida como resultado luego tengo el lazy y este y
47:08
si me va a dar como resultado básicamente es civil y punto inverter
47:16
sandhya ok y esto vamos a tenerlo como desee
47:25
vamos a del modelo de sandiás que es simplemente la parte de los
47:31
inversores vamos a utilizar el 9 el a nivel de deseo también
47:39
el pp que esto es los resultados del módulo
47:45
qué bien que está dc ya lo vamos a ir desglosando cuando tengamos todo el resultado y todo esto simplemente con el
47:52
inversor configurado a nivel del inversor y entonces simplemente voy a hacer una
47:57
sumatoria en él
48:04
e igual a la sumatoria de hace para cada uno de los lugares y luego tengo que en
48:11
x ven
48:18
igual a anual
48:23
y esto ahora si fuera del loop simplemente le voy a decir que todo esto
48:29
se va a guardar en una serie de datos y esta llamada mobility es nada más para
48:36
guardarlo entonces voy a correr y él está haciendo la computación vea que la computación dura muy poco y nada
48:43
más para ir viendo algunas características importantes por ejemplo si yo llamo dentro de lo que convocamos
48:49
a cada la radiación total del sistema ok
48:55
entonces en este caso tenemos todas las características como si tuviéramos una
49:00
base de datos el cual funciona exactamente igual y por ejemplo si yo calculo la parte de bs que simplemente
49:07
desde el sistema la parte de lo que me genera el módulo pues obtengo la corriente cortocircuito la corriente de
49:15
máxima potencia el voltaje del circuito abierto voltaje demasiada potencia la máxima potencia y factores de corrección que
49:22
puedo tener a nivel general y entonces con esto y ya yo puedo tener los
49:28
diferentes parámetros a nivel del sistema que se pueden ir generando y tengo entonces la parte de energía
49:36
entonces si yo llamo la parte de energías me ha resultado en vatios ahora
49:41
lo que es de una vez dentro del cómputo para cada uno de los sitios como un
49:48
módulo fotovoltaico canadá del solar porque es el que teníamos acá el
49:53
canadiense solar con un módulo a bb o un micro en persona bebé me genera para cada uno de esos sitios ok
50:00
esta parte de lo que ya corresponde a nivel de bloquear los diferentes
50:06
sistemas entonces en este caso simplemente voy a hacer una comparativa al nivel de cada uno de los sistemas le
50:13
voy a decir que la adaptación sea igual a cero ok y nada más voy a agregar el
50:19
pellet punto huelen una etiqueta en la parte de el eje y
50:27
donde me indique cada uno de los diferentes aspectos que estoy con
50:33
relación al y esto está dado en vatios ahora
50:41
entonces simplemente explote a lo que estoy planteando son los resultados anteriores vean ustedes entonces que es
50:47
más fácil verlo por acá lo que es en algo que que está en una zona desértica en los eeuu pues tiene mejor rendimiento
50:54
de lo que puede ser en tucson eeuu y lo que puede ser en berlín que tiene un porcentaje de nubosidad bastante alto
51:01
entonces con esto estoy completando el primero de los ejemplos que es el que se
51:06
va a encontrar dos cuevas importantes no hay como que caer en pánico porque hay
51:11
muchas referencias pero también la en que quiero mostrarles con este webinar es simplemente cuál es la lógica detrás
51:19
de cada uno de ellos y vean que pues ya se va siguiendo un poco la lógica general hay alguna pregunta hasta acá
51:36
vamos bien no vamos también
51:53
gracias ok entonces bueno continuemos con otra
52:00
parte de los ejemplos vean que de las primeras cosas que les puedo enseñar es que si queremos hacer mucho código y
52:06
estar llamando a pili en cada momento puede ser algo extravagante alguna tiene
52:12
python no solamente para esta biblioteca vamos a llamar varias de éstos voy a utilizar la biblioteca por defecto o es
52:19
simplemente para poder tener mejores desempeños y tertulia es
52:24
una biblioteca de
52:30
de propietaria también de payton digamos que está incluida que simplemente lo que
52:36
me sirve es para poder generar mejores herramientas de integración vean que lo que estamos haciendo acá es yendo
52:42
columna por columna básicamente en periodos de 10 años ok entonces
52:47
simplemente es para mejorar un poco rendimiento vamos a llamar a la biblioteca que es la que tiene el día de
52:52
hoy y existen diferentes modelos que yo podría ir generando entonces en lugar de
52:59
estar llamando primero yo puedo simplificar el llamado como lo puedo simplificar extrayendo los componentes
53:05
de cada uno de ellos que tengo otros en este caso todo tener vivir el import
53:11
solar posición entonces en este caso para llamarlo sería philip puntos o la posición con
53:19
esto cada vez que yo llamo a solar posición ya no tengo que estar llamando pibil y ok para este ejemplo voy a
53:26
llamar a varios de ellos que estoy llamando al pin y sistema que
53:32
ya lo usamos a location que ya también lo usamos y estamos utilizando skype
53:37
atmospheres o la posición y location y a nivel de irradiación también para una
53:43
herramienta útil que les voy a mostrar y esto podemos hablarlo más adelante también puede empezar a importar otra
53:50
herramienta que es bastante similar a piscis que básicamente es una
53:57
herramienta de análisis de históricos o de series que es más fácil no va a usar muchas funciones de esto para análisis
54:05
en sistemas de energía que no solamente a nivel fotovoltaico sino a nivel de energía lo importante es el análisis de
54:12
serie de tiempo series de tiempo es una de las ramas de la estadística quizás es
54:18
de las más importantes que pueden ver por las diferentes aplicaciones que pueden tener desde por ejemplo a nivel
54:23
de economía como toda la parte a nivel de control como todo lo que es estos flujos que estamos manejando por acá
54:30
todo simplemente voy a utilizar esto y de este ente de tulse voy a llamar nada
54:36
más a uno que me da mejores resultados que es estimar la cantidad de cielo abierto en función de la temperatura que
54:43
tengo entonces lo que sigue es llamar a las bibliotecas normales por defecto con que ya las
54:50
llamamos arriba y simplemente para tenerlas por acá in fort
54:55
pandas espere ok y como ustedes son bastante
55:02
responsables pues por ahí se pudieron ver el vídeo de martín y simplemente estoy llamando las bibliotecas usando la
55:09
misma metodología general porque esto simplemente es
55:14
quiero variar todas las figuras para una mejor presentación porque esta no me gusta esta por defecto entonces vuelvo a
55:22
hacer una variación de las diferentes figuras estos de mattel y ahora si entremos en materia vamos a hacer un
55:28
ejemplo pequeño de ubicación a nivel de costa rica entonces lo primero que vamos
55:33
a utilizar es definir nuestra zona horaria en este caso dentro de las formas que se pueden definir la zona
55:39
horaria que puede ser de interés en las primeras formas para ustedes es utilizar américa
55:45
costa rica ok con esto es exactamente en la zona horaria que estábamos utilizando
55:52
anteriormente entonces la latitud simplemente la voy a amar ya no le voy a
55:58
llamar largas estoy utilizando la parte habilidad que estamos generando
56:03
simplemente voy a copiar por acá lo que son las coordenadas del texto que
56:10
nada más para que vean que no hay el truco simplemente me estoy yendo al google
56:16
maps ok
56:21
un segundo
56:32
entonces clique o para que alguna parte de googlemaps dentro del url como
56:39
respuesta obtengo lo que es la latitud y la longitud y esto simplemente es lo que
56:44
estoy copiando también poquito pero simplemente el
56:49
nivel de la posición que se tiene y listo con esto ya tenemos la ubicación para cartago que sigue bajo esta misma
56:56
lógica de diseño tenemos la locación vea que ya no utilizo pib y le punto la ocasión porque lo importe como
57:03
componente acá entonces utilizó la ocasión de la ocasión llamó a la función
57:09
location que simplemente es para determinar la longitud la longitud y en
57:14
el dictamen son porque ésta hay que declarar porque estoy aplicando algunos elementos entonces tenemos que
57:23
llamarlo como time son también entonces ahora si tenemos esto por acá les voy a
57:30
enseñar una herramienta bastante útil y que ha puesto como ejemplo que es
57:35
generar una función que nos dé final y lo que es la irradiación total en el
57:41
sitio entonces vamos a utilizarlo a nivel de radiación esta es una función que estoy creando hoy aquí en los anuncios de
57:47
predeterminada edades ok y en esto van a utilizar el
57:53
site lo que vamos a utilizar
57:58
un inicio al final estos son fechas de inicio que
58:03
podemos utilizar vamos a hablar de un ángulo de inclinación y vamos a utilizar
58:12
hacia donde estaba orientada la superficie del panel eso es una función
58:19
que estoy creando no es una función general y entonces en esto vamos a crear
58:24
primer nuestro nuestra zona de tiempo entonces a nivel de tiempos vamos a decirle que lo primero que necesito
58:32
es que se genere un dato una base de datos
58:38
de pandas que una serie de datos de pandas donde yo tengo data
58:44
esto lo tengo como range o que simplemente donde voy a tener un estar
58:50
que es el mismo que tengo anteriormente que es el período de cuando inicia cuando terminan utilizó la parte de
58:57
frecuencia que esta parte de frecuencia sea de un minuto
59:02
ok simplemente lo que estoy creando es que los índices de base horaria que puedo
59:09
tener y que esto sea la locación que voy a estar utilizando
59:15
por acá hay location punto tercera porque esa el ok sión es el objeto que
59:22
estoy creando por acá entonces tendríamos esto como función vamos a
59:28
determinar el porcentaje de irradiancia que podemos tener en cielo
59:34
abierto entonces vamos a llamar site location
59:42
punto get clear sky
59:49
simplemente como lo estuvo explicando anteriormente a nivel de clase si yo tengo la radiación total y tengo el
59:55
porcentaje de radiación con cielo abierto puedo también es otra de las formas de obtener la debida difusa que
1:00:01
puedo tener tengo solar position ok intentamos obtener la posición del
1:00:08
sol y ya lo sabemos cómo calcular entonces soltar posición y
1:00:17
o la posición porque y en este caso simplemente como ya times tiene todo
1:00:23
simplemente que lo haga para times porque times toma las coordenadas del sitio y ya no tengo que convocarlo como
1:00:30
lo hice anteriormente luego vamos a calcular entonces
1:00:37
la radiación en el plano d
1:00:43
de la red ok eso es con lo que se puede encontrar a nivel de simulación normalmente y simplemente es la
1:00:49
corrección del plan de la del ángulo que podemos tener de una vez dentro de la
1:00:56
altura o la inclinación que podemos tener en el líbano el entonces tenemos
1:01:01
en varios puntos get punto total
1:01:07
y esto vamos a llamar los radios porque esto sí es vean que es de las que estuve
1:01:13
convocando de pibil y todo ese lugar es el spirit punto simplemente convocó a gracias y en este caso vamos a tener
1:01:22
como parámetros de entrada de esta función que ya las vimos anteriormente vamos a tener
1:01:30
estas funciones porque qué son
1:01:36
y lo que está mal es todo lo demás vamos a
1:01:43
tener como parámetro de entrada el ángulo del panel el azimut al que
1:01:51
está orientado el panel los 1000 sistema general de las coordenadas de clean sky pues el de ese modelo crezca en la
1:01:59
irradiancia normal la irradiancia global y la radiante difusa y luego de esto
1:02:07
vamos a tener entonces la posición del sol
1:02:14
y del cenit y la parte de hacemos que son
1:02:20
importantes a nivel del cálculo de esto vamos a decirle que de esta función yo quiero que se me retorne
1:02:27
i que el pd data frame
1:02:33
donde yo quiero dentro de ese dato frame tiene un diccionario donde tengo
1:02:40
la radiación normal e indirecta
1:02:46
trigger sky
1:02:53
y esto lo vamos a llamar el dni aunque entonces esta es una de
1:03:01
las partes del diccionario la siguiente parte del diccionario que vamos a traernos es la radiación difusa en plano
1:03:21
la radiación global que voy a traer de una vez del modelo de ejemplo
1:03:28
que yo tenía
1:03:34
el paréntesis entonces esto es lo que me retorna de esta función de obtener la radiación el
1:03:41
retorno es un data frame esta data pen que ya lo genera y simplemente me genera
1:03:49
la parte de radiación entonces con esta función es una función que ya les puede quedar a ustedes para la futura
1:03:55
referencia ya nosotros simplemente podemos estar generando lo siguiente
1:04:03
[Música] ok podemos entonces es decir
1:04:10
e
1:04:16
dentro de la convocatoria o que simplemente llamados a la función
1:04:23
ya que es esta función que ya tenemos vamos de crear ok entonces estamos
1:04:30
diciendo que sea el sitio que ya lo tenemos definido en la parte de arriba y que sea el periodo de tiempo vamos a
1:04:37
arrancar con un ejemplo pequeño de 0.6 perdón del 20 de junio del año anterior
1:04:48
bajo un modelo americano de las fechas
1:04:53
tenemos entonces del 06 al 22 de julio
1:04:58
del 2021 ok lo otro que le vamos a decir que ocupamos en esta función
1:05:05
tenemos la locación el inicio de la consulta de la ocasión el final
1:05:10
necesitamos el ángulo de radiación
1:05:16
y el azimut ok que son 180 porque es sur en este caso y entonces ya lo que se
1:05:22
viene por acá es simplemente lo que hay que estudiar es de makled entonces simplemente lo voy a pegar por acá
1:05:28
corremos la asunción la corre y me dice que hay un problema
1:05:36
con cuál es el problema
1:05:49
el problema de vettel simplemente por aquí y esto es
1:05:59
y ryan simplemente el nombre de la variable y ahora si él está calculando y ok
1:06:07
entonces tenemos una herramienta ven qué interesante esta herramienta de lo que teníamos en el examen 1 vean
1:06:15
de amar es toda importante desde la introducción anterior ya estamos creando funciones ok funciones con funciones básicamente
1:06:22
de la herramienta entonces la función lo que nos da nos da dos cosas nos da el
1:06:28
ángulo total horizontal y el ángulo de irradiación en el plan naranja porque
1:06:36
entonces vean qué interesante nótese ustedes que para el caso de junio y el
1:06:42
ángulo en el de incidencia en el panel es menor que el ángulo horizontal alguna
1:06:48
razón al respecto se acuerdan un poco ya este materia de
1:06:54
vista materia olvidada porque tenemos esta característica en junio
1:07:12
alguna idea para el caso del diagrama cilíndrico de
1:07:19
costa rica hola el movimiento del sol en costa rica
1:07:43
ese código se lo contesta no me ayuda a contestar la
1:07:51
pregunta que les hice porque en junio en la radiación en el plan no es menor que
1:07:56
la radiación global alguna idea
1:08:09
porque en esa época la
1:08:14
posición está posicionado más encima de nosotros
1:08:22
en esa época para las otras a como más inclinado como hacia el norte y es más
1:08:27
martín en esta gente de pronto sí sí en el resto de la amistad del sur pero desde los meses de abril a agosto
1:08:33
estancia en el norte entonces qué pasa si le damos vuelta al panel a 0 grados
1:08:40
hacia el norte veamos el resultado vamos siguiendo el sol lo ven justamente
1:08:46
es la respuesta que quería escuchar y es porque el sol se va más hacia el norte en esa posición
1:08:54
entonces si el tenemos el panel de nuestra posición ideal que ya supimos
1:08:59
con la clase de recurso solar porque se maneja mejor mantenerlo en una
1:09:05
orientación fija se pierden algunos meses ok pero en el total se genera más en el energía simplemente el ángulo de
1:09:13
nada en la radiación en el ángulo de inclinación va a ser menor al ángulo horizontal ok
1:09:20
tratan que esta herramienta pues ya le genera ustedes bastante provecho por ejemplo si quisiéramos evaluar entonces
1:09:28
en el primero de enero esto que les estoy diciendo al diciembre
1:09:33
que esto va a durar un poco computando pues vamos a poder ver esa variación porque lo que está comparando acá es
1:09:40
simplemente la radiación global horizontal y la radiación en el plano
1:09:49
entonces lo que va a computar volverá como unos 28 segundos
1:09:58
porque y entonces vean que la función pues ya les da simplemente como parámetros de resultados
1:10:05
está terminando de ejecutar está apropiando entonces vean qué interesante esto es en la radiación en el plano ves
1:10:16
una radiación que yo puedo tener horizontal lo alto de ante interesante
1:10:21
de enero febrero marzo lo tengo pues por encima de lo que puedo esperar a nivel
1:10:28
de horizontal pero durante los meses de abril mayo junio y agosto y todavía casi
1:10:35
llegando a septiembre pues el sol se encuentra en posición del norte y por
1:10:42
esta razón la radiación global horizontal es menor ok pero la inclinada
1:10:49
es menor a la horizontal y luego vuelve recordemos que lo ideal sería que yo pudiera tener algún este
1:10:58
algún seguidor pero eso podría volverse inviable y entonces simplemente tengo
1:11:04
mejor caso que todos no sabemos que andar para el caso de costa rica ante de los 10 grados a 180 que de salta bueno
1:11:11
nada nos lo buscamos lo hacen 0.6 para hacerlo un poco más rápido
1:11:17
en la parte de los cálculos qué es algo interesante que les da esta
1:11:24
herramienta esta es que yo ustedes pueden calcular qué pasa si el panel no está rotando al sur que porque es un
1:11:31
modelo que se da lo pueden ver por acá simplemente recordemos un poco a agosto
1:11:36
para que nos van a computar tantos días y por ejemplo qué pasa si el sol o el techo está inclinado hacia el este
1:11:52
ok entonces volvamos al caso original 0.8 para ver en términos de radiación lo
1:12:00
que se puede tener
1:12:07
el punto es el punto 6 nada más para un par de ellas entonces es una de las
1:12:14
funciones que pueden ser de interés vean ustedes que voy a tener una expresión primero producto de cómo se encuentra el
1:12:21
panel ubicado aunque tal vez no hay muchas pérdidas de momento a nivel general que lo que pasa que en el este
1:12:29
cuando el sol se está acostando en el oeste si voy a tener una diferencia importante respecto a los puntos
1:12:36
producto de la propia sombra que se puede generar entonces nos decíamos bien hasta acá
1:12:49
ok ahora hacemos un poco tenemos la parte de localización y lo que vamos a ver la
1:12:55
otra de las variables que pueden ser utilidad entender para ustedes es cómo calcular la diferencia entre la
1:13:03
temperatura del panel y la temperatura de celda entonces en este caso vamos a
1:13:11
llamarlo como no habíamos llamado américa a
1:13:16
[Música] rica aunque entonces en este caso vamos a decirle la altitud de cartago que es
1:13:23
de 425 y en este caso vamos a definir la ciudad como cartaya
1:13:30
ok en este caso vamos a generar una parte de pandas
1:13:40
mis fans cuando tiene el punto d
1:13:47
range ok y simplemente es el inicio y el empiezo que puedo tener entonces en este
1:13:55
caso vamos a decirle que empiece en las mismas fechas porque aquí ya teníamos
1:14:00
anteriormente dentro de la parte del cálculo y vamos a obtener la temperatura ambiente producto de la radiación ok
1:14:08
skype igual a
1:14:15
jets
1:14:21
skype
1:14:27
con el temperatura ambiente y en este caso el tiempo que tengo una plataforma
1:14:32
va a ser igual a la base de todo el tiempo que tenga la latitud y ya la ha
1:14:38
definido a ser igual a la variable lat y la longitud del igual
1:14:47
y por aquí un problema [Música] más como es igual
1:14:56
y esto es así es acá vamos a calcular la temperatura del módulo entonces en este
1:15:02
caso como uno la convoqué anteriormente ya que no están todas las opciones esta biblioteca
1:15:10
vamos a llamarla como la temperatura del de sanya lapso el modelo de sandia lapse
1:15:17
a nivel de la celda esto a nivel de el verano
1:15:22
respecto a la irradiancia que tiene en el sistema y
1:15:28
con la que el porcentaje de radiación esto no es sobre esto es
1:15:37
el site gracias ok y tenemos entonces el cliente
1:15:46
skype con la temperatura ambiente que fue lo
1:15:54
que definimos anteriormente que es este site e irradian ok y en este caso vamos
1:16:00
a utilizar modelos de corrección por defecto entonces vamos a decir los 5 ya
1:16:06
vamos a buscar la documentación para que puedan entender esto 56
1:16:12
- 0 puntos de 275 3 y a mil vatios por metro cuadrado lo
1:16:22
que entonces y aquí tengo la parte de temperatura y lo que sigue simplemente
1:16:28
explote al no generar dos blogs el primero de ellos va a ser la temperatura
1:16:34
ambiente en el segundo de ellos la temperatura de celda vamos a plantearlo por eje
1:16:40
vamos a ver algún paso a tecleo un doble punto
1:16:47
y entonces tengo la temperatura ambiente del 20 al 21 tengo que volver a computar
1:16:55
acá porque él está estimando la radiación en función de la radiación que está a nivel de la temperatura pero
1:17:01
simplemente para que pueda calcular ambos de la base de datos obtenida yo tengo la temperatura ambiente y la
1:17:07
temperatura del módulo para que puedan entender esta función es esta que justamente tengo abierta por acá es la
1:17:15
diferentes factores que yo podría tener de el funcionamiento a nivel del sistema
1:17:21
que ya lo vemos donde tengo que definir en la el parámetro de corrección que es simplemente el que estoy
1:17:26
definiendo acá como 5 el para por defecto de menos 3.5 y el delta de
1:17:34
temperatura menos 0.75 lo siguiente es
1:17:40
para la 3era la velocidad del viento vamos de vuelta velocidad del viento el
1:17:45
factor de corrección el factor de corrección ve el delta de temperatura y 1000 que también si lo recuerdan pues lo
1:17:52
obtuvimos anteriormente a nivel de los parámetros del sistema y lo que estoy planteando es la diferencia de
1:17:59
temperatura ya que lo que se pretende de la temperatura ambiente que normalmente se tiene que andar por los 15 un poco
1:18:06
más de 15-20 una temperatura fresca en cartago pero en función de la radiación
1:18:12
y la temperatura de la celda en todo momento en función de la radiación asumiendo que yo tengo mil vatios por
1:18:18
metro cuadrado cosa que no es cierta ok simplemente voy a tener diferentes
1:18:24
temperaturas del módulo a mediodía pues es esperable que va a alcanzar casi los 45 48 grados celsius que es la
1:18:33
temperatura nominal que tiene a nivel de operación y esto sería pues en el caso de cartago a nivel de lo que se tiene
1:18:40
vean que conforme pasa la radiación suceden dos cosas generales que están un poco desfasada esto es una capa inercia
1:18:48
a nivel meteorológico es decir el domo caliente se está calentando producto del sol y al calentarse este domo pues
1:18:56
simplemente lo que pasa es que se vuelve la calor se mantiene mientras que en el panel la calidad es inmediata apenas se
1:19:03
va la radiación empieza a caer porque baja la presión o la producción que se
1:19:09
tiene hagamos un último ejemplo ya para ir cerrando porque la clase se ha vuelto
1:19:15
tal vez un poco larga tenemos una parte de temperatura del módulo en este caso
1:19:21
vamos a hacer otro cálculo de simulación y bilic beavis systems que con esta
1:19:28
variable que ya estamos hablando vamos a traernos la base de datos del sun
1:19:38
ok en este caso nada más estoy cambiando la variable y ya no voy a traerlos del
1:19:43
samco anteriormente voy a traer los modelos que vienen a base de datos del set ok y vamos a buscar en los modelos
1:19:53
un modelo que nadie sólo mermó de ese ok voy a llamar nuevo a6
1:19:59
mods igual que convoquen la parte anterior y voy a hacer una búsqueda en
1:20:05
el objeto mediante los índices lo voy a extraer como un string ok y que debería
1:20:12
arrancar con stars with esto es una parte de búsqueda que se genera en
1:20:17
cualquier biblioteca de de payton pues voy a extraer todos los que ya van canadienne solas
1:20:26
ok entonces simplemente es una parte d
1:20:32
para poder extraer que es un método que les puede ser de interés a ustedes que simplemente lo genera
1:20:41
como siempre nada más un dedazo
1:20:53
y aquí es mi fortuna es stars with simplemente de la base de datos que ya
1:20:58
les mostré es simplemente buscar los modelos que empiezan con ese modelo dentro de la búsqueda es una forma
1:21:05
interesante de hacerlo en este caso todos los paneles que a nadien solos y pues me dice en este caso que no
1:21:11
arrancan a nivel de los modelos vamos a hacer la convocatoria del modelo y vamos
1:21:19
a crear la confusión de la base de datos porque no me lo arrojó entonces creado
1:21:25
un modelo y simplemente no vuelve a ser la consulta en función de los diferentes
1:21:31
modelos que pueda obtener y en este caso creo el módulo canadians o la csp 550
1:21:39
que fue en la misma forma que uno veces anteriormente lo como lo traigo por acá y vuelvo a generar los diferentes
1:21:46
elementos que tengo al nivel del panel ok en este caso vamos a generar un
1:21:52
modelo de soto
1:21:57
que es un modelo de cálculo del sistema basado en aproximación que puedo tener
1:22:03
vean ustedes que estos modelos de simulación y es importante con móvil o viendo lo vamos a ver luego con la otra
1:22:11
herramienta de crisis existen diferentes metodologías para hacerlo de soto se
1:22:16
llama así por el autor de ese tipo de modelado que es de apellido de soto que
1:22:22
simplemente proponen mejorías a nivel del modelo entonces para modelar lo que
1:22:27
es la conversión de energía del sistema vamos a calcular la temperatura del módulo iii o diferente y extraer los
1:22:34
diferentes parámetros a nivel de modelado del panel y esos parámetros nos extraemos en función de las ecuaciones
1:22:41
del vídeo simple
1:22:59
es otro paramos igual a bilic
1:23:05
punto system ok puntocom
1:23:19
soto y en este caso vamos a llamar a
1:23:26
a no no
1:23:31
la radiación efectiva sobre el módulo ok de acuerdo a lo que ya tenemos por acá
1:23:37
que ya lo calculamos también por acá ok esta radiación que ya tenemos acá en él
1:23:42
en el plano vamos a tener la temperatura de celda
1:23:47
2
1:23:55
en la temperatura de celda y vamos a traer varios parámetros por acá que son
1:24:02
los siguientes parámetros y les voy a mostrar la parte de convocatoria que se tiene por acá en este caso de los mismos
1:24:10
factores debido que se pueden tener obtengo los siguientes parámetros que no
1:24:15
son tan desconocidos como ustedes podrían pensar tengo el alfa del módulo
1:24:20
que la alfa es el porcentaje de pérdidas por [Música]
1:24:25
en el voltaje ok por temperatura en el voltaje tengo la parte de referencias
1:24:31
que tengo por acá alves tengo la corriente de referencia a nivel
1:24:38
del módulo que es la corriente de potencia que puedo tener la corriente de radiación y vean que simplemente los
1:24:45
módulos cuando yo los extraigo de la base de datos como un objeto atrás simplemente busco por el atributo alfons
1:24:53
necesidad el porcentaje de pérdidas y las corrientes y luego simplemente en el
1:24:58
modelo como es un modelo de dios este que tengo por acá es una parte del
1:25:03
modelo de dios que es los cinco parámetros de efectivos simplemente para
1:25:09
ver la parte de terminación pues utilizó la parte de y la resistencia de sión
1:25:16
recordemos que las celdas se modela con una resistencia de sión la resistencia
1:25:21
en 6 y luego los factores de corrección a nivel de la temperatura que puedo
1:25:26
tener por acá luego de esto extraigo los principales modelos que es la corriente
1:25:33
de carga corriente foto generada la resistencia
1:25:40
de todas forma la resistencia ya está la resistencia adhesión y luego voy a
1:25:47
obtener el valor de colección del dio en el voltaje térmico que se recuerda que
1:25:53
era ese a la cape ok simplemente es toda esta
1:26:00
expresión esto es en el vph y aquí simplemente le estoy diciendo ok esos
1:26:06
son los parámetros que usted necesita para el cálculo del modelo
1:26:16
por aquí ustedes van a continuar con una parte de esta parte del modelo de
1:26:22
una parte hace falta una col
1:26:29
problemas de problema tenía un paréntesis de más
1:26:37
[Música] sin tener
1:26:43
[Música] a más y este mes es baby system
1:26:51
ok y entonces los parámetros que me da es el cálculo de la ecuación la que hemos
1:26:59
visto a nivel del modelo ok simplemente para cada uno de estos para cada uno de
1:27:04
los tiempos que podemos tener y ya para ir sembrando un poco entonces lo que
1:27:11
vamos a ir viendo es cómo conectarlo con el modelo del panel entonces vamos a ver
1:27:18
a nivel de generación entonces generamos con una info del
1:27:25
modelo para obtener todos los diferentes parámetros tribilín
1:27:31
punto piscis
1:27:36
voltaire ok y en este caso yo obtuve los modelos
1:27:45
de de soto para obtener los parámetros y ahora voy a calcular la corriente de fútbol generación del sistema entonces
1:27:51
de la ecuación del módulo voy a obtener todos los parámetros distintos el método
1:27:58
de la dirección es un método de lambert que de hecho que posiblemente algunos lo han visto a nivel de aproximación los
1:28:06
sistemas de control simplemente es la forma en la que yo digitalizó la ecuación y luego puedo extraer la
1:28:13
información del sistema entonces en este caso de la información del sistema yo extraigo la corriente
1:28:27
la corriente del lodo info o que simplemente lo hago como
1:28:35
i en vez
1:28:41
ok le voy a decir que si hay corrientes por debajo de cero que las hagas el que
1:28:49
puede pasar eso son porque el el cálculo de esta ecuación del yodo simple lo hace
1:28:56
al nivel general y entonces queda la parte de el arco revelar el voltaje de
1:29:03
mayor potencia el voltaje del circuito abierto y simplemente algunas aproximaciones importantes ya para a
1:29:10
nivel del cálculo entonces en este caso vamos a decir que la temperatura de
1:29:16
referencia del sistema es igual a 25 puntos 0 grados ok el voltaje máximo del
1:29:23
sistema que debería alcanzar el módulo es d
1:29:32
250 voltios de 50.0 luego la corriente
1:29:37
máxima en dc que podría alcanzar es de 30.0
1:29:44
y luego vamos a tener varias cosas importantes vamos a decir que la máxima
1:29:50
el máximo voltaje el circuito abierto es el voltaje de referencia del panel más
1:29:57
el voltaje de referencia del panel por la diferencia de temperatura bien ustedes que básicamente es el cálculo
1:30:03
que tuvieron que hacer para el examen anterior donde tenemos la temperatura de referencia multiplicamos por esa por ese
1:30:10
incremento de temperatura que se tiene en función de la hoja de datos y está la temperatura máxima que tiene el padre
1:30:17
cuando la temperatura ambiente es mínima y la temperatura que hubo más bien el
1:30:22
voltaje webó se pues va a ser simplemente la parte corregida para cualquier momento a nivel general
1:30:28
entonces vamos a hacer un string que simplemente va a obtener lo que es el voltaje máximo y la corriente máxima
1:30:36
y en este caso el largo del stream va a ser el voltaje máximo en función de la
1:30:42
cantidad de paneles que vamos a tener que en este caso va a ser una extensión máxima de cinco
1:30:50
paneles el voltaje de la cadena que va a
1:30:56
ser en la red la longitud del arreglo entre el voltaje de el voltaje de máxima
1:31:05
potencia y luego la salida del panel que es la salida de diesel tc la mora que
1:31:11
dentro del modelo es etc 250 vatios por
1:31:17
la cantidad de paneles que vamos a tener vea que aquí lo que está obteniendo que es un string completo y luego la cuenta
1:31:25
a nivel de cuántos paneles un en serie corresponde a la parte de corriente que
1:31:31
yo voy a tener a nivel del sistema o la diferencia que tengo entre esos paneles la corriente total es la cantidad de la
1:31:38
corriente que tengo por la cantidad de nodos que puedo tener ahí la corriente
1:31:45
den arreglo va a ser igual a la corriente por la corriente mpt y la
1:31:51
capacidad en dc va a ser igual al arreglo que tengo por la salida del
1:31:56
arreglo y finalmente la corriente del
1:32:02
sistema va a estar igual da el arreglo que yo tengo a nivel de sistema por el
1:32:09
voltaje por la corriente de mi abrigo o del ministerio fotovoltaico y entonces en este caso
1:32:15
vamos a tener por ejemplo de aquí podemos obtener toda la información que queramos entonces los records
1:32:22
el máximo voltaje y corriente directa no de esas características es de
1:32:27
154 y lo que estoy haciendo acá es simplemente decir cuántos paneles yo
1:32:33
puedo colocar a nivel del sistema ok entonces por ejemplo si yo quisiera ver bajo esta dimensión a miento que nos va
1:32:40
a ser de utilidad para la siguiente clase entonces veo que tengo nada más un
1:32:46
para mí ok que es dentro de las características que puedo tener y luego tengo la
1:32:55
corriente del sistema de las características a nivel del reino que
1:33:00
puedo estar generando ok entonces estos son los diferentes parámetros para
1:33:06
generar un arreglo y luego de esto ya lo que queda es simplemente un arco que una
1:33:13
concatenación de los diferentes arreglos que puedo tener entonces voy a hacer los
1:33:19
apremios que ya tengo sobre la el cálculo anterior los parámetros que
1:33:26
tengo que calcular en donde tengo
1:33:33
con cat ok y en este tengo el sar de
1:33:39
ciudades es amigo variable que habíamos calculado desde siempre tengo el clicker
1:33:45
skype de la temperatura ambiente
1:33:53
ok tengo la temperatura de celda guardad tengo la corriente de línea el
1:34:01
voltaje del circuito abierto tengo el arreglo de la corriente que puedo tener
1:34:08
tengo el arreglo del voltaje
1:34:15
tengo el arreglo de la potencia
1:34:22
y esto tiene que ir todo en paréntesis cuadrados
1:34:33
voy a decirle que lo vaya equiparando columna por color fila por fila y luego
1:34:39
vamos a darle nada más nombres a los parámetros entonces
1:34:44
lo que está creando nada más es una tabla ok donde tengo las diferentes columnas
1:34:52
al nivel de sistema no
1:34:58
el bebé entonces este otro se va a llamar
1:35:04
de h otro que tengo es
1:35:11
que allí qué son los resultados de las funciones
1:35:16
que estoy llamando la radiación en el plano luego tengo la temperatura
1:35:22
ambiente tengo la temperatura de celda
1:35:34
tengo la corriente de línea
1:35:43
y voy a tener entonces acá lo que es el voltaje
1:35:49
el circuito abierto la corriente de la red
1:36:03
y tengo también lo que es la potencia de mi arreglo de mini cadena
1:36:12
3
1:36:17
en ok entonces este es el data feliz que
1:36:25
tengo por acá vamos a ver qué tal dice que hay un tema con a gray powell a
1:36:33
tener una doble nada w w y aquí dice que nos hace falta
1:36:43
a posee un además tengo 16 de allí y hp va
1:36:53
y
1:36:58
y lo sé me hace falta la corriente
1:37:15
mp entonces es por acá debería tener y entonces por ejemplo si yo llamo al
1:37:22
objeto
1:37:29
pues aquí lo voy a poder ver todas sus características
1:37:35
y lo está computando voy a poder ver todas sus características se fue
1:37:43
dentro del periodo que son los dos días que tengo en este comenta parte del sistema a nivel de la generación que se
1:37:51
tiene en general entonces lo puedan ver por acá todo lo que es
1:37:57
el índice que está fue el objeto que creamos en la radiación directa la radiación difusa la radiación de uruguay
1:38:04
en el plano lo que es la radiación personación global la radiación en el plano la
1:38:10
temperatura ambiente la temperatura de la celda la corriente de línea el
1:38:15
voltaje de circuito abierto ya las diferentes corrientes a nivel de la red ok esto pues a nivel de datos ya no
1:38:23
genera una base de datos completa lo que sigue es simplemente poderlo graficar que esta parte de la gratificación de
1:38:30
todas formas en código les queda ya simplemente es carpintería de la herramienta de mattel entonces voy a
1:38:38
pegarlo por acá y simplemente ustedes pueden ver lo que es el ploteo de la
1:38:43
función donde yo tengo los voltajes a nivel del sistema las corrientes y la
1:38:49
potencia que tengo con esto bien que los voltajes llegan a ser máximos del
1:38:54
sistema pero producto del mediodía consiguen un mínimo general que esto es
1:39:01
el mínimo a nivel de módulos por qué se bajan en función del incremento de la
1:39:09
temperatura que fue una de las gráficas que vimos en la parte de arriba lo que entonces
1:39:18
me gusta es que tenemos la temperatura máxima del módulo y esta temperatura máxima del módulo haya que o
1:39:25
supone que exista una pérdida bastante completa por la parte de temperatura a
1:39:31
nivel del mar que se puede tener entonces con esto yo creo que estoy cerrando la sesión del día de hoy la
1:39:38
idea es que ustedes puedan tener una noción importante vamos a dejar el trabajo de simulación y lo más
1:39:44
importante es que ustedes puedan aprender a utilizar un poco la herramienta no va a ser tan compleja va
1:39:51
a ser en términos más de generar una parte de ejemplos para sus sitios ok
1:39:56
pero el objetivo es que puedan entender cuál es la dinámica vean que hay cosas
1:40:02
que son ocultas pero no son tan ocultas y realmente se saben qué es lo que se está realizando entonces no sé si tienen
1:40:09
alguna consulta en términos generales