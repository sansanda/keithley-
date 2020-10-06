from communications.CommPort_I import CommPort_I
import socket



class EthernetPort(CommPort_I):
    """A concrete Comm Port"""

    def __int__(self,address:str, port:int):
        self.s = socket.socket()  # Establish a TCP/IP socket object
        self.config(address,port)
        self.s.connect((self.ip_address, self.scktNum))  # Connect to the instrument

    def config(self, address:str, port:int):
        """Config the port"""
        self.ip_address = address
        self.scktNum = port

    def send(self, s:str):
        """Send a string over the comm port"""
        self.s.send(s.encode())
        return

    def receive(self, bufferSize:int, flags=None):
        """gets response over comm port """
        return self.s.recv(bufferSize,flags).decode()
