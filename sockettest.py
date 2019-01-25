import machine


def connect_ncguest():
    import network
    sta_if = network.WLAN(network.STA_IF)

    if not sta_if.isconnected():

        sta_if.active(True)
        sta_if.connect('ncguest', 'uKpTLx7udjRgjs')

        while not sta_if.isconnected():
            pass

    return sta_if


html = """<!DOCTYPE html>
<html>
    <head> <title>ESP8266 Pins</title> </head>
    <body> <h1>ESP8266 Pins</h1>
        <table border="1"> <tr><th>Pin</th><th>Value</th></tr> %s </table>
    </body>
</html>
"""

sta_if = connect_ncguest()

if sta_if.isconnected():
    print('Connected!')

import socket
addr = socket.getaddrinfo('10.100.15.192', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    cl_file = cl.makefile('rwb', 0)
    while True:
        line = cl_file.readline()
        if not line or line == b'\r\n':
            break

    response = html
    cl.send(response)
    cl.close()
