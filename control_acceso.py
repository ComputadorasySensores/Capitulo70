from machine import Pin
from mfrc522 import MFRC522
import time
       
lector = MFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=1,rst=0)

rojo = Pin(13, Pin.OUT)
verde = Pin(12, Pin.OUT)

TARJETA = 2766409360
LLAVERO = 3643110918

print("Lector activo...\n")

while True:
    lector.init()
    (stat, tag_type) = lector.request(lector.REQIDL)
    if stat == lector.OK:
        (stat, uid) = lector.SelectTagSN()
        if stat == lector.OK:
            identificador = int.from_bytes(bytes(uid),"little",False)
            
            if identificador == TARJETA:
                print("UID: "+ str(identificador)+" Acceso concedido")
                rojo.value(0)
                verde.value(1)
                time.sleep(2)
                verde.value(0)
                
            #elif identificador == LLAVERO:
            #    print("UID: "+ str(identificador)+" Acceso concedido")
            #    rojo.value(0)
            #    verde.value(1)
            #    time.sleep(2)
            #    verde.value(0)
                
            else:
                print("UID: "+ str(identificador)+" desconocido: Acceso denegado")
                rojo.value(1)
                verde.value(0)
                time.sleep(2)
                rojo.value(0)
