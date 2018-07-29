import pydivert

#choose ports
#choose incoming or outgoing traffic

w = pydivert.WinDivert("tcp.DstPort == 443 and tcp.PayloadLength > 0")
w.open()

 True:
    packet = w.recv()
    print(packet)
    #w.send(packet)

w.close()
