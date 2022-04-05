import os
from sys import argv
from time import sleep

childs = []

def main(message:str, processes:int, iterations:int):
    """
    :param message: сообщение
    :param processes: количество процессов(fork)
    :param iterations: количество итерация
    :return:
    """

    parrent_id = os.getpid()
    for proc in range(processes):
        pid = os.fork()
        # дочерний процесс
        if pid == 0:
            for iter in range(iterations*(proc+1)):
                with open('file.log', 'a+') as file:
                    file.write(f'{proc}: {message} {iter+1}\n')
                sleep(1)
            os.abort()
        childs.append(pid)

    for child in childs:
        os.waitpid(child, 0)


if __name__ == "__main__":
    if len(argv) < 4:
        print("main.py <message> <process> <iterations>")
        exit(-1)
    try:
        main(argv[1], int(argv[2]), int(argv[3]))
    except:
        for child in childs:
            os.kill(child, 0)
