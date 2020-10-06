import abc

class CommPort_I(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'config')   and
                callable(subclass.config)     and
                hasattr(subclass, 'send')   and
                callable(subclass.send)     and
                hasattr(subclass, 'receive')   and
                callable(subclass.receive)     or
                NotImplemented)

    @abc.abstractmethod
    def config(self, address:str, port:int):
        """Config the port"""
        raise NotImplementedError

    @abc.abstractmethod
    def send(self, s:str):
        """Send a string over the comm port"""
        raise NotImplementedError

    @abc.abstractmethod
    def receive(self, bufferSize:int, flags=None):
        """gets data over comm port """
        raise NotImplementedError
