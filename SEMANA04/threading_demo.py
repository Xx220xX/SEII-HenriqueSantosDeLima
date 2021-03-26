import concurrent.futures as cf
from threading import Thread
import time
# tempo inicial
start = time.perf_counter()


def fazAlgo(seconds):
    print(f'Esperar {seconds} secondo(s)...')
    time.sleep(seconds)
    return seconds+1


# a funcao map da classe ThreadPoolExecutor aplica uma funcao a cada elemento do parametro
# executa em ordem
# a sincronização é feita quando 'metodo _next() é chamado



with cf.ThreadPoolExecutor() as executor:
    print(executor._max_workers)# numero maximo de threads
    secs = [5, 4, 3, 2, 1]
    results = executor.map(fazAlgo, secs)
    r = list(results)
    print(r)



finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')


# Thread incia uma funcao com parametors
# nao é possivel pegar o valor de retorno
# para sincronizar utiliza-se o metodo join

threads = []
for _ in range(10):
    t = Thread(target=fazAlgo, args=(1.5,))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')