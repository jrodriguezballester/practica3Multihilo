# En este ejercicio vamos a trabajar los Conditions (from threading import Condition).
# Este tipo de bloqueo son los más sofisticados ya que tenemos las funciones de .notify(), .wait(), .release(), .acquire().
# Para declarar un lock: cond = Condition().
#
# Realizar un programa que genere 20 hilos a partir del programa principal.
# Cada hilo ejecutará una función en la que simularemos 20 personas bebiendo de un vaso.
# En este caso cada hilo tomará el semáforo, mientras pueda, sino esperará 0,5s hasta poder adquirirlo
# (trabajamos los tiempos de espera de los procesos),
# una vez conseguimos acceder al semáforo, ejecutamos la función que nos da la posibilidad de beber.
# Bebemos durante un tiempo aleatorio (from random import randint, s = randint(1,10)),
# al finalizar avisamos al siguiente proceso en espera y liberamos la condición.

# La salida que tenemos que observar es una lista de inicio de procesos ordenada y sin embargo una lista de procesos finalizados desordenada.
import threading
import time
from random import randint


def task():
    hilo_actual = threading.current_thread().getName()
    print('llegando al bar', hilo_actual)
    with condicion:
        condicion.wait(0.5)
        s = randint(1, 10)
        time.sleep(s)
        print('\033[;31mBEBIENDO CERVEZA durrante ', s, 'segundos,-LOS DEMAS NO PUEDEN PEDIR SOY: ', hilo_actual,
              '\033[;37m')
        condicion.notifyAll()
        print('ESTOY SATISFECHO ahora LOS DEMAS AHORA PUEDEN PEDIR', hilo_actual)


if __name__ == "__main__":
    num_hilos = 20
    hilos = list()
    condicion = threading.Condition()
    for i in range(num_hilos):
        hilo = threading.Thread(target=task, name="hilo %s" % (i + 1))
        hilos.append(hilo)

    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()

    print('finish')
