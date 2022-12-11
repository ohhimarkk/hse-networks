import subprocess
import sys


def ping_server(server, mtu) -> bool:
    print("Pinging with packet size of ", mtu, '...', sep='')
    return subprocess.call(
        ['ping', server, '-M', 'do', '-c', '1', '-s', str(mtu)],
        stderr=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
    ) == 0


server = sys.argv[1]
min_, max_ = 1, 1600
while max_ - min_ > 1:
    mtu = (min_ + max_) // 2
    if ping_server(server, mtu):
        min_ = mtu
    else:
        max_ = mtu
print('Finally', min_ + 28)
