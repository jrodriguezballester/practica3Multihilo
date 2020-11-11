import threading
import time


def task():
    print('Inicio tarea.-  {}'.format(threading.current_thread().name))
    time.sleep(3)
    print('fin tarea.-  {}'.format(threading.current_thread().name))


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
