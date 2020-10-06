import abc


class Thermometer_I(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'read_temperature') and
                callable(subclass.read_temperature) and
                hasattr(subclass, 'plug_transducer') and
                callable(subclass.plug_transducer) or
                NotImplemented)

    @abc.abstractmethod
    def read_temperature(self):
        """Load in the data set"""
        raise NotImplementedError

    @abc.abstractmethod
    def plug_transducer(self, transducer, channel):
        """plug transducer to the thermometer """
        raise NotImplementedError
