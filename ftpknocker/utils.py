from netaddr import IPSet


def targets_to_ip_list(targets):
    ipset = IPSet()
    for t in targets:
        ipset.add(t)
    return [str(ip) for ip in ipset]

def split_list(l, n):
    # Yield successive n-sized chunks from l
    for i in range(0, len(l), n):
        yield l[i:i + n]