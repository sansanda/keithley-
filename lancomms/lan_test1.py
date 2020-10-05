## Communications Optimization Consideration Program Example...
import socket
import struct
import math
import time
import datetime

ip_address = "169.254.199.70" # Place your instrument's IP address here.
scktNum = 5025 # Define the instrument socket number

def send_reset(s):
    # This function issues the reset that clears all existing
    # instrument settings.
    s.send("*RST\n".encode())
    return

def cnfgFunc(s, fnc, chLst):
    # This function sets up the measurment function across
    # scan channels.
    if fnc == 0:
        s.send('FUNC \"TEMP\", (@{0})\n'.format(chLst).encode())
        s.send('SENS:TEMP:TRAN TC, (@{0})\n'.format(chLst).encode())
        s.send('SENS:TEMP:TC:TYPE K, (@{0})\n'.format(chLst).encode())
        s.send('SENS:TEMP:TC:RJUN:RSEL INT, (@{0})\n'.format(chLst).encode())
    elif fnc == 1:
        s.send('FUNC \"VOLT\", (@{0})\n'.format(chLst).encode())
    elif fnc == 2:
        s.send('SENS:FUNC \"RES\", (@{0})\n'.format(chLst).encode())
    elif fnc == 3:
        s.send('SENS:FUNC \"FRES\", (@{0})\n'.format(chLst).encode())
    elif fnc == 4:
        s.send('SENS:FUNC \"CURR\", (@{0})\n'.format(chLst).encode())

    return

def cnfgSetRng(s, fnc, rng, chLst):
    # This function sets the fixed range across scan channels.
    if fnc == 0:
        rng = 0
    elif fnc == 1:
        s.send('SENS:VOLT:RANG {0}, (@{1})\n'.format(rng, chLst).encode())
    elif fnc == 2:
        s.send('SENS:RES:RANG {0}, (@{1})\n'.format(rng, chLst).encode())
    elif fnc == 3:
        s.send('SENS:FRES:RANG {0}, (@{1})\n'.format(rng, chLst).encode())
    elif fnc == 4:
        s.send('SENS:CURR:RANG {0}, (@{1})\n'.format(rng, chLst).encode())
    return

def cnfgSetNplc(s, fnc, nplc, chLst):
    # This function sets the integration rate across scan channels.
    if fnc == 0:
        s.send('SENS:TEMP:NPLC {0}, (@{1})\n'.format(nplc, chLst).encode())
    elif fnc == 1:
        s.send('SENS:VOLT:NPLC {0}, (@{1})\n'.format(nplc, chLst).encode())
    elif fnc == 2:
        s.send('SENS:RES:NPLC {0}, (@{1})\n'.format(nplc, chLst).encode())
    elif fnc == 3:
        s.send('SENS:FRES:NPLC {0}, (@{1})\n'.format(nplc, chLst).encode())
    elif fnc == 4:
        s.send('SENS:CURR:NPLC {0}, (@{1})\n'.format(nplc, chLst).encode())

    return

def enblAZero(s, fnc, state, chLst):
    # This function sets the state of Auto Zero across scan channels
    if fnc == 0:
        s.send('SENS:TEMP:AZER {0}, (@{1})\n'.format(state, chLst).encode())
    elif fnc == 1:
        s.send('SENS:VOLT:AZER {0}, (@{1})\n'.format(state, chLst).encode())
    elif fnc == 2:
        s.send('SENS:RES:AZER {0}, (@{1})\n'.format(state, chLst).encode())
    elif fnc == 3:
        s.send('SENS:FRES:AZER {0}, (@{1})\n'.format(state, chLst).encode())
    elif fnc == 4:
        s.send('SENS:CURR:AZER {0}, (@{1})\n'.format(state, chLst).encode())
    #SENS:FRES:AZER ON
    return

def enblADelay(s, fnc, state, chLst):
    # This function sets the state of Auto Delay across scan channels.
    if fnc == 0:
        s.send('SENS:TEMP:DEL:AUTO {0}, (@{1})\n'.format(state, chLst).encode())
    elif fnc == 1:
        s.send('SENS:VOLT:DEL:AUTO {0}, (@{1})\n'.format(state, chLst).encode())
    elif fnc == 2:
        s.send('SENS:RES:DEL:AUTO {0}, (@{1})\n'.format(state, chLst).encode())
    elif fnc == 3:
        s.send('SENS:FRES:DEL:AUTO {0}, (@{1})\n'.format(state, chLst).encode())
    elif fnc == 4:
        s.send('SENS:CURR:DEL:AUTO {0}, (@{1})\n'.format(state, chLst).encode())

    return

def enblLimit(s, fnc, use1, use2, chLst):
    # This function sets the state of limits checking across scan channels.
    if fnc == 0:
        s.send('CALC2:TEMP:LIM1:STAT {0}, (@{1})\n'.format(use1, chLst).encode())
        s.send('CALC2:TEMP:LIM2:STAT {0}, (@{1})\n'.format(use2, chLst).encode())
    elif fnc == 1:
        s.send('CALC2:VOLT:LIM1:STAT {0}, (@{1})\n'.format(use1, chLst).encode())
        s.send('CALC2:VOLT:LIM2:STAT {0}, (@{1})\n'.format(use2, chLst).encode())
    elif fnc == 2:
        s.send('CALC2:RES:LIM1:STAT {0}, (@{1})\n'.format(use1, chLst).encode())
        s.send('CALC2:RES:LIM2:STAT {0}, (@{1})\n'.format(use2, chLst).encode())
    elif fnc == 3:
        s.send('CALC2:FRES:LIM1:STAT {0}, (@{1})\n'.format(use1, chLst).encode())
        s.send('CALC2:FRES:LIM2:STAT {0}, (@{1})\n'.format(use2, chLst).encode())
    elif fnc == 4:
        s.send('CALC2:CURR:LIM1:STAT {0}, (@{1})\n'.format(use1, chLst).encode())
        s.send('CALC2:CURR:LIM2:STAT {0}, (@{1})\n'.format(use2, chLst).encode())
    return

def enblLineSync(s, fnc, state, chLst):
    # This function sets the state of Line Sync across scan channels.
    if fnc == 0:
        s.send('TEMP:LINE:SYNC {0}, (@{1})\n'.format(state, chLst).encode())
    elif fnc == 1:
        s.send('VOLT:LINE:SYNC {0}, (@{1})\n'.format(state, chLst).encode())
    elif fnc == 2:
        s.send('RES:LINE:SYNC {0}, (@{1})\n'.format(state, chLst).encode())
    elif fnc == 3:
        s.send('FRES:LINE:SYNC {0}, (@{1})\n'.format(state, chLst).encode())
    elif fnc == 4:
        s.send('CURR:LINE:SYNC {0}, (@{1})\n'.format(state, chLst).encode())

    return

def setScanList(s, chLst):
    # This function sets the active list of scan channels.
    s.send('ROUT:SCAN:CRE (@{0})\n'.format(chLst).encode())

    return

def setScanCount(s, cnt):
    # This function sets the number of times the scan will
    # iterate.
    s.send('ROUT:SCAN:COUN:SCAN {0}\n'.format(cnt).encode())
    return

def setScn2Scn(s, stosIntvl):
    # This function sets the delay time between the start
    # of one scan to the start of the next.
    s.send('ROUT:SCAN:INT {0}\n'.format(stosIntvl).encode())
    return

def sendOpc():
    # This function is issued to allow all blocking commands
    # to complete their operation before moving on to other
    # control commands.
    s.send('*OPC\n'.format(cnt).encode())
    return

def cnfgSpeedScan(s, fnc, chLst, rng, nplc, cnt, s2sInt):
    # This function configures the speed scan setup as
    # defined by the passed parameters.
    cnfgFunc(s, fnc, chLst)
    cnfgSetRng(s, fnc, rng, chLst)
    cnfgSetNplc(s, fnc, nplc, chLst)
    enblAZero(s, fnc, 0, chLst)
    enblADelay(s, fnc, 0, chLst)
    enblLimit(s, fnc, 0, 0, chLst)
    enblLineSync(s, fnc, 0, chLst)
    setScanList(s, chLst)
    setScanCount(s, cnt)
    setScn2Scn(s, s2sInt)
    sendOpc()
    return

def send_init(s):
    # This function starts a scan.
    s.send("INIT\n".encode())
    return

def send_waitForScan(s):
    # This function is used to poll the DAQ6510 to determine the
    # active trigger state. If RUNNING or WAITING, this means the
    # trigger model is still running and the scan is not done.
    s.send("TRIG:STAT?\n".encode())
    response = s.recv(1024).decode()
    #print(response)
    while (response.find('RUNNING') != -1 or response.find('WAITING') != -1):
        s.send("TRIG:STAT?\n".encode())
        response = s.recv(1024).decode()
    return

def get_ScanData(s, val):
    # This function extracts the scanned readings
    # from the DAQ6510
    s.send("TRAC:DATA? 1, {0}, \"defbuffer1\", READ\n".format(val).encode())
    response = s.recv(1024).decode()
    return response

#=================================================================================
# Main body of our program...
#configure, trigger, transfer
s = socket.socket() # Establish a TCP/IP socket object
s.connect((ip_address, scktNum)) # Connect to the instrument
nplc = 0.001 # Set the integration rate
cnt = 1 # Set the scan count
s2sInt = 0 # Set the scan to scan interval
t1 = datetime.datetime.now() # Capture the start time of our operation
send_reset(s)
# Configure DC Voltage scan
dcvScanList = '101:110'
rng = 10
cnfgSpeedScan(s, 1, dcvScanList, rng, nplc, cnt, s2sInt)
for j in range(0, 10):
    send_init(s)
    sendOpc()
    send_waitForScan(s)
    print(get_ScanData(s, 10))
    time.sleep(1)
s.close() # Close the socket.
t2 = datetime.datetime.now() # Capture the stop time of the operation
delta = t2-t1
print("Run time: {0:.0f} ms".format(delta.total_seconds() * 1000))
input("Press Enter to continue...")
exit()