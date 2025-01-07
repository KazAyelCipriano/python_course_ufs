import serial
import time

class CommSystem:
    def __init__(self,device, rate,T):
        self.comport = serial.Serial(device, rate,timeout=T)
#        self.comport.readline() ## Read and eliminates previous data
        self.my_sensors=['S1','S2','S3','S4','S5']
        
    def getAll(self,list_sensors):
        values = []

        m = "#All"
        self.comport.write(m)
        val_micro=self.read()

        for s in list_sensors:
            try:
                idx = self.my_sensors.index(s)
                values.append(val_micro[idx])
            except ValueError:
               print("O sensor " + s + " nao foi encontrado!!!")
            
        print(values)
        return values

    #def update_my_sensors(self):
    
    def read(self):
        time.sleep(0.2)
        txt_serial=self.comport.readline()
        values=map(int, txt_serial.split())
        print(values)
        return values
        

serial = CommSystem('/dev/ttyUSB0',9600,0.1)
sensors=['S1','S2','S5','S4','S3']
serial.getAll(sensors)
