# @Author: allen
# @Date: Apr 14 19:55 2020
import re


def is_valid_ipv4(ip):
    m = re.match(r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$', ip)
    return bool(m) and all(map(lambda x: (not x.startswith('0') if len(x) >= 2 else True)
                                          and (0 <= int(x) <=255),
                               m.groups()))


def is_valid_netmask(ip):
    if is_valid_ipv4(ip):
        ns = ip.split('.')
        sbin = list(map(lambda n: bin(int(n))[2:].zfill(8), ns))
        s01 = ''.join(sbin)
        
        try:
            idx_0 = s01.index('0')
            idx_1 = s01[::-1].index('1')
            if idx_0 + idx_1 != len(s01):
                return False
        except ValueError:
            return False
        
        return True
    
    return False


A, B, C, D, E, ERR, P = 0, 0, 0, 0, 0, 0, 0

while 1:
    try:
        ip, netmask = input().split('~')

        if not (is_valid_ipv4(ip) and is_valid_netmask(netmask)):
            ERR += 1
            continue

        ns = ip.split('.')
        fst = int(ns[0])

        if 1 <= fst <= 126:
            A += 1
            if fst == 10:
                P += 1
        elif 128 <= fst <= 191:
            B += 1
            if fst == 172:
                if 16 <= int(ns[1]) <= 31:
                    P += 1
        elif 192 <= fst <= 223:
            C += 1
            if fst == 192:
                if int(ns[1]) == 168:
                    P += 1
        elif 224 <= fst <= 239:
            D += 1
        elif 240 <= fst <= 255:
            E += 1

    except:
        break

print(A, B, C, D, E, ERR, P)
