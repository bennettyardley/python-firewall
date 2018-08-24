import pydivert

ports = []
a = True
filter = ""

while a:
    ports.append(input("Enter Port To Block (or 0 if no more ports are needed): "))
    if "0" in ports:
        a = False
ports.remove("0")
length = len(ports)
i = 0
while i < (length-1):
    filter += ("tcp.SrcPort == " + ports[i] + " or ")
    i = i + 1
filter += ("tcp.SrcPort == " + ports[length-1])
with pydivert.WinDivert(filter) as w:
    for packet in w:
        print("Firewall Started!")
