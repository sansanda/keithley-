import random
from thermometers.Thermometer_I import Thermometer_I

class KThermometer(Thermometer_I):

    def __int__(self):
        pass

    def read_temperature(self):
        """Load in the data set"""
        return random.random()*100

    def plug_transducer(self, transducer, channel):
        """plug transducer to the thermometer """
        pass