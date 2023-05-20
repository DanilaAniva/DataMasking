import secrets
from random import randint
from secrets import choice
import random
import ipaddr
def ipv4_generator():
    '''Генератор случайных публичных IPv4'''
    reserved4 = ['0.0.0.0', '10.0.0.0', '100.64.0.0', '127.0.0.0',
                '169.254.0.0', '172.16.0.0', '192.0.0.0',
                '192.0.0.0', '192.0.2.0', '192.88.99.0',
                '192.168.0.0', '192.18.0.0', '198.51.100.0',
                '203.0.113.0', '240.0.0.0', '255.255.255.255']
    private = [10,127,169,172,192]
    a = randint(1,255)
    if (a not in private):
        rndIP = [a,randint(0,255), randint(0,255), randint(0,255)]
        ip = '.'.join(str(x) for x in rndIP)
        if ip not in reserved4:
            return ip
        else:
            ipv4_generator()
    else:
        ipv4_generator()
def ipv6_generator():
    '''Случайный IP в формате IPv6'''
    return ':'.join('{:04x}'.format(randint(0,255)) for i in range(8))

def ip_private_generator():
    '''Генератор частных IP'''
    startswith = [10,127,169,172,192]
    rndIP = [secrets.choice(startswith), randint(0,255),randint(0,255), randint(0,255)]
    ip = '.'.join(str(x) for x in rndIP)
    return ip

def mac_adress_generator(prefix = None):
    '''Генератор MAC адресов'''
    mac = prefix.split(':') if prefix else list()
    while len(mac) < 6:
        mac.append('{:02x}'.format(randint(0,255)))
    return ':'.join(mac)

def mask_ip_v4(ip):
    '''Замена IPv4 по словарю'''
    ip_replacements = {}
    ip_replacements[ip] = ipv4_generator()
    return ip_replacements[ip]

# print(ipv6_generator())

def mask_ip_v6(ip):
    '''Замена IPv6 по словарю'''
    ip_replacement = {}
    ip_replacement[ip] = ipv6_generator()
    return ip_replacement[ip]
def mask_mac(mac):
    '''Замена mac по словарю'''
    mac_replacement = {}
    mac_replacement[mac] = mac_adress_generator()
    return mac_replacement[mac]
def mask_df_ip_v4(df,column):
    df[column] = df[column].apply(lambda x: mask_ip_v4(x))
def mask_df_ip_v6(df,column):
    df[column] = df[column].apply(lambda x: mask_ip_v6(x))
def mask_df_mac(df, column):
    df[column] = df[column].apply(lambda x: mask_mac(x))
# print (mac_adress_generator())