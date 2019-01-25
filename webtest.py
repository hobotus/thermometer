from network_setup import connect_wifi


sta_if = connect_wifi()

import picoweb

app = picoweb.WebApp(__name__)

from ui import page

@app.route("/")
def index(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite(page)

host = sta_if.ifconfig()[0]

app.run(debug=True, host = host)
