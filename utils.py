import time
import math
import socket


def _calculate_time_between_pkts(bw):
    packets_to_send_per_second = math.ceil(bw / 117760)
    #print(f'paquetes a enviar en 1 segundo: {packets_to_send_per_second}')
    time_lapse_per_packet = (1 / packets_to_send_per_second) - 0.0001 #0.0001 tiempo promedio máquina
    #print(f'tiempo de espera entre paquetes: {time_lapse_per_packet} segundos')
    return time_lapse_per_packet

def _calculate_uptime(bw, wait):
    packets_to_send_per_second = math.ceil(bw / 117760)
    return int(packets_to_send_per_second * wait)

def generate(ip, bandwidth, probe_time, ttl=30, version=4):
    calculated_sleep = _calculate_time_between_pkts(bandwidth)
    calculated_time = _calculate_uptime(bandwidth, probe_time)
    message = b'A'*1472*10
    if (version == 4):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    else:
        sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, ttl)
    for _ in range(1,calculated_time):
        sock.sendto(message, (ip, 5000))
        time.sleep(calculated_sleep)