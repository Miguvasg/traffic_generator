import ipaddress
from ipaddress import IPv4Address


SCI_BW = {
    'k': 1_000,
    'm': 1_000_000,
    'g': 1_000_000_000,
    'K': 1_000,
    'M': 1_000_000,
    'G': 1_000_000_000
}


class Data:
    
    def __init__(self) -> None:
        error = ''
        while True:
            ip = input(f'{error}Escribe la IP hacía donde quieres generar tráfico\n')
            try:
                prov_ip = ipaddress.ip_address(ip)
                self.ip = ip
                error = ''
                break
            except Exception:
                error = '(Error) El formato de la dirección IP no es válido. '
        while True:
            bandwidth = input(f'{error}Escribe el ancho de banda, ejemplo: 10m, 1g, 1G, 100M, 900K...\n')
            try:
                self.bandwidth =  float(bandwidth[0:-1]) * SCI_BW[bandwidth[-1]]
                error = ''
                break
            except Exception:
                error = '(Error) El valor de BW no es válido. '
        while True:
            probe_time = input(f'{error}Escribe el tiempo de la prueba en segundos (1-600 segundos)\n')
            try:
                if int(probe_time) < 1 or int(probe_time) > 600:
                    raise ValueError
                self.probe_time = int(probe_time)
                error = ''
                break
            except Exception:
                error = '(Error) El valor de tiempo de la prueba no es válido. '
        while True:
            ttl = input(f'{error}Escribe el ttl para el tráfico generado (3-30)\n')
            try:
                if int(ttl) < 3 or int(ttl) > 30:
                    raise ValueError
                self.ttl = int(ttl)
                error = ''
                break
            except Exception:
                error = '(Error) El TTL debe ser un valor entre 3 y 30. '
        if isinstance(prov_ip, IPv4Address):
            self.ip_version = 4
        else:
            self.ip_version = 6
