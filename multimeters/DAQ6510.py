from thermometers.Thermometer_I import ThermometerInstrument_I


class DAQ6510(ThermometerInstrument_I):
    """A concrete thermometer"""

    def __int__(self):
        pass

    def read_temperature(self):
        """Load in the data set"""
        pass

    def plug_transducer(self, transducer, channel):
        """plug transducer to the thermometer """
        pass
