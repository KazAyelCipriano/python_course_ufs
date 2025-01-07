import serial
import serial.tools.list_ports
import time


ports = list(serial.tools.list_ports.comports())
print 'Foram detectadas as seguintes portas:'
i=0
for p in ports:
    print p.device, ' -> ',i

idx = int(raw_input('Digite o numero da porta desejada:'))

comport = serial.Serial(ports[idx].device, 9600,timeout=0.10)
comport.readline() ## Read and eliminates previous data

## Dados Coletados
d1=[];d2=[];d3=[]
## Loop principal do programa
T=0.1 # periodo de 100ms
t_or=time.time()
while (True):
    ti=time.time()
## Gets serial information
    if (comport.in_waiting>0):
        ## Read information in the serial port
        VALUE_SERIAL=comport.readline()
        print VALUE_SERIAL
        VALUE_SERIAL=VALUE_SERIAL.rstrip(' \t\r\n\0')
        ## Converts information in numbers
        values = map(float, VALUE_SERIAL.split(' '))
        if len(values)>=3:
            ## Adds information into lists
            d1.append(values[0])
            d2.append(values[1])
            d3.append(values[2])
            ## Saves information
            file = open('dados.txt','a')
            file.write('{:.3f}\t{:.2f}\t{:.2f}\t{:.2f}\n'.format(
                (time.time()-t_or),values[0],values[1],values[2]))
            file.close()
    ## Waits the next sample
    time.sleep(T-(time.time()-ti))
