from flask import Flask
from flask_restful import Resource, Api
import uuid
import random
import threading
import datetime

#Initialize the app
app = Flask(__name__)
api = Api(app)

#Setup core data
init_time = datetime.datetime.now()
uid = uuid.uuid4()

#Setup temperature data
last_update = datetime.datetime.now()
temperature = 325.0

#Base reactor information
class Core(Resource):
    def get(self):
        return {
            'id': str(uid),
            'created': str(init_time)
        }

#Reactor temperature information
class Temperature(Resource):
    def get(self):
        return {
            'temperature': str(temperature),
            'last_update': str(last_update)
        }

#Continuous updates temperature in the core based on a sophisticated sensor.
def update_temperature():
    global temperature
    global last_update 
    temperature = temperature + (random.random() - 0.3)
    last_update = datetime.datetime.now()
    threading.Timer(5.0, update_temperature).start()

#Ensure that reactor temperature is up to date
threading.Timer(5.0, update_temperature).start()

#Set up the endpoints
api.add_resource(Core, '/')
api.add_resource(Temperature, '/temperature')

#Initialize the app
if(__name__ == '__main__'):
    app.run(debug=True, host='0.0.0.0')
