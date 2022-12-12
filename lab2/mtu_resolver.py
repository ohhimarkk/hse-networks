import subprocess
import sys
from socket import getaddrinfo


def ping_server(server, mtu=100) -> bool:
    print("Pinging with packet size of ", mtu, '...', sep='')
    return subprocess.call(
        ['ping', server, '-M', 'do', '-c', '1', '-s', str(mtu)],
        stderr=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
    ) == 0


if len(sys.argv) != 2:
    raise AttributeError('1 arg required, not ' + str(len(sys.argv)))

server = sys.argv[1]
try:
    getaddrinfo(server, None)
except Exception:
    raise AttributeError('Bad server')
try:
    assert subprocess.call(
        ['ping', server, '-c', '1'], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
    ) == 0
except Exception:
    raise ConnectionError('Bad connection')

try:
    min_, max_ = 68, 1600
    while max_ - min_ > 1:
        mtu = (min_ + max_) // 2
        if ping_server(server, mtu):
            min_ = mtu
        else:
            max_ = mtu
except Exception:
    raise ConnectionError('Bad connection')
print('Finally', min_ + 28)
