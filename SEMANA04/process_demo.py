import concurrent.futures
import time
import  multiprocessing

start = time.perf_counter()

# funcao para esperar alguns segundos, representando uma tarefa pesada
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

# Cria um executor de processos, o parametro 5 é o numero de processos que serao inciados para realizar o map
with concurrent.futures.ProcessPoolExecutor(5) as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)
    r = list(results)
    print(r)
finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')


# sao mais lentos para mudar o valor da variavel
# se livra do problema GIL, o qual nao permite executar mais de um codico python, GIL.lock

process = []
for _ in range(10):
    p = multiprocessing.Process(target=do_something,args=(1.5,))
    process.append(p)
    p.start()

for p in process:
    p.join()


print(f'Finished in {round(finish-start, 2)} second(s)')
