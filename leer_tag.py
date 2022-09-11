from mfrc522 import MFRC522
import time

lector = MFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=1,rst=0)

print("Lector activo...\n")


while True:
    lector.init()
    (stat, tag_type) = lector.request(lector.REQIDL)
    if stat == lector.OK:
        (stat, uid) = lector.SelectTagSN()
        if stat == lector.OK:
            identificador = int.from_bytes(bytes(uid),"little",False)
            print("UID: "+str(identificador))
time.sleep(1) 
