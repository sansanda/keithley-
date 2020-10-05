
pId = 0x6510
vId = 0x05e6

from time import sleep
from msvcrt import kbhit
import pywinusb.hid as hid


def sample_handler(data):
    print("Raw data: {0}".format(data))

def raw_test():

    print(hid.find_all_hid_devices())

    # device = (hid.HidDeviceFilter(vendor_id =vId , product_id = pId).get_devices())[0]
    # device.open()
    # #set custom raw data handler
    # device.set_raw_data_handler(sample_handler)
    # print("\nWaiting for data...\nPress any (system keyboard) key to stop...")
    # while not kbhit() and device.is_plugged():
    #     #just keep the device opened to receive events
    #     sleep(0.5)
    #
    # device.close()
    return

if __name__ == '__main__':
    raw_test()