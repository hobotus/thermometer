WIFI_NETWORKS = [(b'ncguest', 'uKpTLx7udjRgjs'), (b'dd-wrt', 'slonick home wifi')]

class NoKnownNetworkFound(Exception):
    pass

def connect_wifi():

    import network
    sta_if = network.WLAN(network.STA_IF)

    if not sta_if.isconnected():

        sta_if.active(True)
        nets = sta_if.scan()
        names = [n[0] for n in nets]

        for name, key in WIFI_NETWORKS:

            if name in names:
                sta_if.connect(name, key)
                break
        else:
            raise NoKnownNetworkFound("test")

        while not sta_if.isconnected():
            pass

    return sta_if


def create_ap():
    import network
    ap_if = network.WLAN(network.AP_IF)

    ap_if.active(True)

    return ap_if

if __name__ == '__main__':
    sta_if = connect_wifi()

    if sta_if.isconnected():
        print("Connected!")
        print(sta_if.ifconfig())
