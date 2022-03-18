import time
class Tank:
    def __init__(self, size, lowsw, highsw):
        self.size = size
        self.lowsw = lowsw
        self.highsw = highsw
        self.level = 0.0

    def fill(self, qinlet):
        self.level += qinlet / self.size

    def empty(self, qoutlet):
        self.level -= qoutlet / self.size

outTank = Tank(50, 5, 7)
qin = 90
qout = 120
pumpout = False
while True:
    outTank.fill(qin)

    if outTank.level > outTank.highsw:
        pumpout = True
    if outTank.level < outTank.lowsw:
        pumpout = False

    if pumpout == True:
        outTank.empty(qout)
    print(" Tank level: {}/n Pump: {}".format(outTank.level, pumpout))
    time.sleep(1)
