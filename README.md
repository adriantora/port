port
Un generador de código QR para simplificar la exportación 
de texto sin conexión.

uso:
Es tan facil como ejecutar desde una terminal o un cmd el port.py seguido de 
el texto que se transformar en QR.

Ejemplo:
$ python port.py google.com

archivos
En caso de que se desee transformar un archivo a codigo QR se debe agregar 
un "-f" antes del nombre del archivo.

Ejemplo:
$ python port.py -f bloc1.txt

Para emitir datos hacia el ordenador se puede usar un servidor web en lan instantaneo 
con "--import" para alzar escribir datos al terminal 

$ python port.py --import

Esta funcion puede llegar a ser bastante util para convertir un supuesto 
archivo.py para ser ejecutado desde un smartphone con la app de QPython que 
se encuentra en la Play Store.

