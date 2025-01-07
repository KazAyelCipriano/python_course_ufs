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

## Loop principal do programa
T=0.1 # periodo de 100ms
t_or=time.time() # Tempo inicial usado para gerar timestamps
while (True):
    ti=time.time()
## Gets serial information
    if (comport.in_waiting>0):
        ## Read information in the serial port
        txt_serial=comport.readline()
        print txt_serial
        txt_serial=txt_serial.rstrip(' \t\r\n\0') ## remove o caracteres
        ## Converts information in numbers
        dados = map(float, txt_serial.split(' '))
        if len(dados)>=3:
            ## Saves information
            file = open('dados.txt','a')
            file.write('{:.3f}\t{:.2f}\t{:.2f}\t{:.2f}\n'.format(
                (time.time()-t_or),dados[0],dados[1],dados[2]))
            file.close()
    ## Waits the next sample
    time.sleep(T-(time.time()-ti))
