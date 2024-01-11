#!/usr/bin/python
import time
from structures import Data
from utils import generate


def main():
    data = Data()
    print(f'Inicia el generador de tráfico para {data.bandwidth} bps')
    start = time.time()
    generate(data.ip, 
            data.bandwidth, 
            data.probe_time,
            data.ttl,
            data.ip_version)
    end = time.time()
    exec_time = end - start
    print(f'Finaliza el generador de tráfico después de {exec_time} segundos')

if __name__ == "__main__":
    main()
