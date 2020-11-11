# En este ejercicio vamos a trabajar los locks (from threading import Lock). Para declarar un lock: lock = Lock().
#
# Realizar un programa que genere 20 hilos a partir del programa principal.
# Cada hilo ejecutará una función en la que simularemos 20 personas bebiendo de un vaso.
# Cada hilo accede al lock, durante un segundo beberá del vaso y al liberarlo,
# imprimimos que el hilo con número está satisfecho y a continuación se ejecutará el siguiente hilo.
import threading
import time


def task():
    lock = threading.Lock()
    # print('hilo.-  {}'.format(threading.current_thread().name))
    # time.sleep(2)
    lock.acquire()
    print('bebiendo .-  {}'.format(threading.current_thread().name))
    time.sleep(1)
    lock.release()
    print(' {} estoy satisfecho'.format(threading.current_thread().name))


if __name__ == "__main__":
    num_hilos = 20
    hilos = list()

    for i in range(num_hilos):
        hilo = threading.Thread(target=task, name="hilo %s" % (i+1))
        hilos.append(hilo)

    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()

    print('finish')
