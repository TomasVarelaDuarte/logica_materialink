#Simulación del sistema de recirculación de tinta para el proyecto Materialink

import time

class Tank:
    def __init__(self, size: int, lowsw: int, highsw: int):
        self.size = size #Tamaño de la base del tanque, en mm^2
        self.lowsw = lowsw #Posición del switch de nivel bajo en cm
        self.highsw = highsw #Posición del switch de nivel alto en cm
        self.level = 0.0 #Nivel de tinta en cm

    def fill(self, qinlet):
        self.level += qinlet / self.size

    def empty(self, qoutlet):
        self.level -= qoutlet / self.size

outTank = Tank(30, 2, 3)
inTank = Tank(30, 2, 3)
qRecPump = 90 #Caudal de la bomba de recirculación ¿en ml/min
qFillPump = 100
qHeads = 80 #caudal de tinta en los cabezales ##¿Sale del tanque inlet la misma tinta que entra en el tanque outlet?
recPumpOn = False
fillPumpOn = False

while True:
        #Logica bombas y sensores
    if inTank.level < inTank.lowsw:
        fillPumpOn = True
    elif inTank.level > inTank.highsw:
        fillPumpOn = False
    if outTank.level > outTank.highsw:
        recPumpOn = True
    elif outTank.level < outTank.lowsw:
        recPumpOn = False

        #circuito de tinta
    #Circulación constante entre los tanques
    inTank.empty(qHeads)
    outTank.fill(qHeads)
    #Accion bombas
    if fillPumpOn:
        inTank.fill(qFillPump)
    if recPumpOn:
        outTank.empty(qRecPump)
        inTank.fill(qRecPump)

    print(' Inlet tank level: {} \n Outlet tank level: {} \n --- \n fillPump {} \n recPump {} \n ================='.format(inTank.level, outTank.level, fillPumpOn, recPumpOn))
    time.sleep(1)
