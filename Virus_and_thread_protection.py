import wmi
t=2
def check_virus_protection():
    try:
        wmi_obj = wmi.WMI(namespace=r'root\SecurityCenter2')
        antivirus = wmi_obj.ExecQuery("SELECT * FROM AntiVirusProduct")
        
        if len(antivirus) > 0:
            protection_enabled = antivirus[0].productState == 397568
            return protection_enabled
        else:
            return False
    except Exception as e:
        print("Error occurred:", str(e))
        return False

# Usage
def pt(t):
    protection_status = check_virus_protection()
    if protection_status:
        # print("Virus and threat protection is ON.")
        t=1
    else:
        # print("Virus and threat protection is OFF.")
        t=0
    return t

# print(pt(t))