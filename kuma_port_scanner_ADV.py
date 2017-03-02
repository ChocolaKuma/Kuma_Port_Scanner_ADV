import socket



np=0
ip="0"
STARTPORT = 1
ENDPORT = 300
ip1 = "8"
ip2 = "8"
ip3 = "8"
ip4 = 8
ALLIPSINRANGE= False    #Changes wither scan one ip or range
GUI = True              # turns gui on and off if off uses defult values
iplock = ip1 + "." + ip2 + "."+ ip3 + "." + str(ip4)


def setUp():
    global s,ip,STARTPORT,ENDPORT,ip1,ip2,ip3,ip4,ALLIPSINRANGE,GUI
    
    print("")
    
    GUIq = 999
    while GUIq != 1 and GUIq !=0:
        
        GUIq = int(input("Do you want GUI enabled? (0)False(1)True\n"))
        if (GUIq != 1 and GUIq !=0):
            print("Not Accaptable Mode")
    if (GUIq == 1):
        print("GUI ON")
        GUI = True
    if (GUIq == 0):
        print("GUI off defaults will be used")
        GUI = False    


    ALLIPSINRANGEq = 999
    while ALLIPSINRANGEq != 1 and ALLIPSINRANGEq !=0:
        ALLIPSINRANGEq = int(input("Do you want ALL_IPS_IN_RANGE enabled? (0)False(1)True\n"))
        if (ALLIPSINRANGEq != 1 and ALLIPSINRANGEq !=0):
            print("Not Accaptable Mode")
    if (ALLIPSINRANGEq == 1):
        print("GUI ON")
        ALLIPSINRANGE = True
    if (ALLIPSINRANGEq == 0):
        print("GUI off defaults will be used")
        ALLIPSINRANGE = False              


    

    if(GUI == True):
        STARTPORT = int(input("Please enter the start port :"))
        ENDPORT = int(input("Please enter the end port :"))
        ip1 = str(input("Please enter the First Octet :"))
        ip2 = str(input("Please enter the Secound Octet :"))
        ip3 = str(input("Please enter the Third Octet :"))
        if(ALLIPSINRANGE == False):
            ip4 =  int(input("Please enter the Fourth Octet :"))


def portScanner():
    global s,ip,STARTPORT,ENDPORT,ip1,ip2,ip3,ip4,ALLIPSINRANGE,GUI 

    print("\nRunning\n")
    print("Scanning IP:",iplock,"\nPorts",STARTPORT,"-",ENDPORT)
    while(ip4 < 256 + 1):

        ip = ip1 + "." + ip2 + "."+ ip3 + "." + str(ip4)
        for np in range(STARTPORT, ENDPORT + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #if in while loop could DDOS
            try:
                s.connect((ip,np))
                print(ip,np,"OPEN")
                np = np +1
                if (ALLIPSINRANGE == False):
                    ip4 = 9999
            except:
                #print("Connection Error 'TIME_OUT'")
                print(ip,np,"CLOSED")
                np = np +1
                if (ALLIPSINRANGE == False):
                    ip4 = 9999
            s.close
        if(ALLIPSINRANGE == True):
            ip4 = ip4 + 1

def main():
    setUp()
    portScanner()



main()

