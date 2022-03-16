from time import sleep

#Sensores y bombas
Lin = False
Lout = False
Brec = False
Bfill = False

#variables simulación
inkLevel = 1000
inLevel = 0
inLevelSw = 40
outLevel = 0
outLevelSw = 20
levelSwMargin = 0
caudalBrec = 3
caudalBfill = 3
caudalHeads = 1



while True:

    #LOGICA RECIRCULACIÓN TINTA
    if Lin == False:
        Bfill = True
    else:
        Bfill = False

    if Lout == True:
        Brec = True
    else:
        Brec = False

    #LOGICA ACTIVACION BOMBAS
    if inLevel > inLevelSw - levelSwMargin and inLevel < inLevelSw + levelSwMargin:
        Bfill = False
    else:
        Bfill = True

    if outLevel > outLevelSw - levelSwMargin and outLevel < outLevelSw + levelSwMargin:
        Brec = True
    else:
        Brec = False

    #SIMULACION  TANQUES
    outLevel += caudalHeads
    if Brec == True:
        outLevel -= caudalBrec
        inLevel += caudalBrec

    inLevel -= caudalHeads
    if Bfill == True:
        inLevel += caudalBfill
        inkLevel -= caudalBfill


    print("Ink Level: {0}, Inlet Level: {1}, Outlet Level: {2}, Fill Bomb: {3}, Recirculation Bomb {4}".format(inkLevel, inLevel, outLevel, Bfill, Brec))
    sleep(0.5)




