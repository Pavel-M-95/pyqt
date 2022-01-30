import subprocess


def host_ping(ip_addresses):
    reachable = []
    unreachable = []

    for ip in ip_addresses:
        result = subprocess.run(
            ["ping", "-c", "3", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        if result.returncode == 0:
            reachable.append(ip)
        else:
            unreachable.append(ip)

    return reachable, unreachable


if __name__ == "__main__":
    print(host_ping(["10.1.1.1", "8.8.8.8"]))