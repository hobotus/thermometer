#
# This is a picoweb example showing a centralized web page route
# specification (classical Django style).
#
#import ure as re
import picoweb

app = picoweb.WebApp(__name__)

@app.route("/")
def index(req, resp):
    yield from picoweb.start_response(resp)
    #yield from resp.awrite("Hello world from picoweb running on the ESP32")
    yield "test"

def connect_ncguest():
    import network
    sta_if = network.WLAN(network.STA_IF)

    if not sta_if.isconnected():

        sta_if.active(True)
        sta_if.connect('ncguest', 'uKpTLx7udjRgjs')

        while not sta_if.isconnected():
            pass

    return sta_if




#import ulogging as logging
#logging.basicConfig(level=logging.INFO)
#logging.basicConfig(level=logging.DEBUG)

sta_if = connect_ncguest()

print(sta_if.ifconfig())

if sta_if.isconnected():
    print('Connected!')

app.run(debug=True, host = "10.100.15.192", port = 1000)
