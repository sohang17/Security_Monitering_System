import Antivirus
import Firewall
import Virus_and_thread_protection
import time

O_AV=Antivirus.N_AV
O_Wd=Antivirus.N_WD
O_FWPUD=Firewall.FWPUD
O_FWD=Firewall.FWD
O_FWPRI=Firewall.FWPRI
O_VNT=Virus_and_thread_protection.t

FWD,FWPRI,FWPUD = Firewall.Fire(O_FWD,O_FWPUD,O_FWPRI)

AV,Wd = Antivirus.get_av_products(O_AV,O_Wd)

vnt=Virus_and_thread_protection.pt(O_VNT)

VPN=1


fw=FWPUD+FWD+FWPRI
# print("fwPub : ", FWPUD)
# print("fwD : ", FWD)
# print("fwPri : ", FWPRI)
# print("fw : ", fw)

# print("AV : ", AV)
# print("VNT : ", vnt)
# print("Wd : ", Wd)

def func():
    if fw == 3 :
        if ((vnt and AV )== 1):
            if((VPN and Wd) == 1):
                return("Excellent")
            elif(VPN ==0  and Wd == 1):
                return("Excellent")
            elif(VPN ==1  and Wd == 0):
                return("Good")
            else:
                return("Average")
        elif (vnt ==1  and AV == 0):
            if((VPN and Wd) == 1):
                return("Excellent")
            elif(VPN ==0  and Wd == 1):
                return("Good")
            elif(VPN ==1  and Wd == 0):
                return("Good")
            else:
                return("Average")
        elif(vnt ==0  and AV == 1):
            if((VPN and Wd) == 1):
                return("Good")
            elif(VPN ==0  and Wd == 1):
                return("Average")
            elif(VPN ==1  and Wd == 0):
                return("Average")
            else:
                return("Bad")
        else:
            if((VPN and Wd) == 1):
                return("Good")
            elif(VPN ==0  and Wd == 1):
                return("Average")
            elif(VPN ==1  and Wd == 0):
                return("Average")
            else:
                return("Bad")
    
    elif fw == 2:
        if ((vnt and AV )== 1):
            if((VPN and Wd) == 1):
                return("Good")
            elif(VPN ==0  and Wd == 1):
                return("Average")
            elif(VPN ==1  and Wd == 0):
                return("Average")
            else:
                return("Bad")
        elif (vnt == 1  and AV == 0):
            if((VPN and Wd) == 1):
                return("Good")
            elif(VPN ==0  and Wd == 1):
                return("Average")
            elif(VPN ==1  and Wd == 0):
                return("Average")
            else:
                return("Bad")
        elif(vnt == 0  and AV == 1):
            if((VPN and Wd) == 1):
                return("Average")
            elif(VPN ==0  and Wd == 1):
                return("Bad")
            elif(VPN ==1  and Wd == 0):
                return("Bad")
            else:
                return("Bad")
        else:
            if((VPN and Wd) == 1):
                return("Average")
            elif(VPN ==0  and Wd == 1):
                return("Bad")
            elif(VPN ==1  and Wd == 0):
                return("Bad")
            else:
                return("Bad")

    elif fw == 1:
        if ((vnt and AV )== 1):
            if((VPN and Wd) == 1):
                return("Average")
            elif(VPN ==0  and Wd == 1):
                return("Bad")
            elif(VPN ==1  and Wd == 0):
                return("Bad")
            else:
                return("Bad")
        elif (vnt ==1  and AV == 0):
            if((VPN and Wd) == 1):
                return("Average")
            elif(VPN ==0  and Wd == 1):
                return("Bad")
            elif(VPN ==1  and Wd == 0):
                return("Bad")
            else:
                return("Bad")
        elif(vnt ==0  and AV == 1):
            if((VPN and Wd) == 1):
                return("Average")
            elif(VPN ==0  and Wd == 1):
                return("Bad")
            elif(VPN ==1  and Wd == 0):
                return("Bad")
            else:
                return("Bad")
        else:
            if((VPN and Wd) == 1):
                return("Bad")
            elif(VPN ==0  and Wd == 1):
                return("Very Bad")
            elif(VPN ==1  and Wd == 0):
                return("Bad")
            else:
                return("Very Bad")

    else:
        return("Very Bad")

def suggestion ():
    if FWPUD == 0 :
        return ("your windows public firewall is off ,\nPublic Windows Firewall is a security feature in Windows that safeguards \n your computer from threats and unauthorized network connections when using public networks.")
    if FWD == 0:
        return ("your windows defender is off,\nWindows Defender is the default antivirus and anti-malware \nsoftware in Windows, offering real-time protection against viruses, \n spyware, and other online threats.")
    if FWPRI == 0 :
        return ("your windows private firewall is off ,\n A private window firewall is a security measure that \n combines two important elements: private browsing and \n firewall protection.")
    if AV == 0 :
        return ("your windows antivirus is not available ,\n An antivirus is a software program designed to detect,\n prevent, and remove malicious software, or malware,\n from computer systems, protecting them from potential threats and unauthorized access.")
    if vnt == 0:
        return ("your windows virus and threat detection is off \n ,Virus and threat protection involves using software and security measures \nto defend against viruses, malware, and other malicious threats to computer \n systems and networks.")
    if Wd == 0:
        return ("yuor windows defender is off \n, Windows Defender is the default antivirus and anti-malware \n software in Windows, offering real-time protection \n against viruses, spyware, and other online threats.")
# print(func())
x = func()
# print(x)
b=suggestion()
# print(b)