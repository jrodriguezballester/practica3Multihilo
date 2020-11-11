import threading
import time


def task():
    finalizar = True
    hilo_actual = threading.current_thread().getName()
    num_intentos = 0
    while finalizar:
        me_atienden = lock.acquire(blocking=False)

        if me_atienden:
            print('\033[;31mBEBIENDO CERVEZA -LOS DEMAS NO PUEDEN PEDIR SOY: ', hilo_actual, '\033[;37m')
            time.sleep(0.01)
            print('ESTOY SATISFECHO- LOS DEMAS AHORA PUEDEN PEDIR', hilo_actual)
            lock.release()
            finalizar = False
        else:
            num_intentos += 1
            print('     estoy llamando al camarero \033[;34m', num_intentos, '\033[;37m veces y El camarero no me esta haciendo ni puto caso ', hilo_actual)

            #time.sleep(0.08)


if __name__ == "__main__":
    num_hilos = 20
    hilos = list()
    lock = threading.Lock()
    for i in range(num_hilos):
        hilo = threading.Thread(target=task, name="hilo %s" % (i + 1))
        hilos.append(hilo)

    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()

    print('finish')
