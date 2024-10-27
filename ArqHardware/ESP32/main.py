from umqtt.robust import MQTTClient

import machine as m

ubidotsToken = "BBUS-bXgmuWeuji822RqGKmFwSHXva4h8hO"  

clientID = "RANDOM-ALPHA-NUMERIC-NAME_OR_IMEI DEVICE ID"

client = MQTTClient("clientID", "industrial.api.ubidots.com", 1883, user = ubidotsToken, password = ubidotsToken)

def checkwifi():

    while not sta_if.isconnected():

        time.sleep_ms(500)

        print(".")

        sta_if.connect()

pin13 = m.Pin(13, m.Pin.IN, m.Pin.PULL_UP)

def publish():

    while True:

        checkwifi()

        client.connect()

        lat = 6.2

        lng = -75.56

        var = repr(pin13.value())

        msg = b'{"location": {"value":%s, "context":{"lat":%s, "lng":%s}}}' % (var, lat, lng)

        print(msg)

        client.publish(b"/v1.6/devices/ESP32", msg)

        time.sleep(20)

publish()