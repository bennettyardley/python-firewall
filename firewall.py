import pydivert

w = pydivert.WinDivert("tcp.DstPort == 443 and tcp.PayloadLength > 0")
w.open()

while True:
    packet = w.recv()
    print(packet)
    #w.send(packet)

w.close()
