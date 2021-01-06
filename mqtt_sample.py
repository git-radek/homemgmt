import paho.mqtt.publish as publish

publish.single("cmnd/taras1/power", "OFF", hostname="localhost")
