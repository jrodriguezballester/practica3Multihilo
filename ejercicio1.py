import threading
import time


def task():
    print('Inicio tarea.-  {}'.format(threading.current_thread().name))
    time.sleep(3)
    print('fin tarea.-  {}'.format(threading.current_thread().name))


if __name__ == "__main__":
    h1 = threading.Thread(target=task, name='hilo 1')
    h2 = threading.Thread(target=task, name='hilo 2')
    h3 = threading.Thread(target=task, name='hilo 3')
    h4 = threading.Thread(target=task, name='hilo 4')
    h5 = threading.Thread(target=task, name='hilo 5')

    h1.start()
    h2.start()
    h3.start()
    h4.start()
    h5.start()

    h1.join()
    h2.join()
    h3.join()
    h4.join()
    h5.join()

    print('finish')
