import usb.core
import usb.util

dev = usb.core.find(idVendor=0x05E6, idProduct=0x6510)

if dev is None:
    raise ValueError('Device not found')
else:
    print(dev)
    dev.set_configuration()

def send(cmd):
    # address taken from results of print(dev):   ENDPOINT 0x3: Bulk OUT
    dev.write(0x2,cmd)
    # address taken from results of print(dev):   ENDPOINT 0x81: Bulk IN
    result = (dev.read(0x81,100000,1000))
    return result

def get_id():
    return send('*IDN?').tobytes().decode('utf-8')

get_id()


