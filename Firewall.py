import subprocess
import time
FWPUD = 0
FWD = 0
FWPRI = 0

def get_firewall_status():

  result = subprocess.check_output(["netsh", "advfirewall", "show", "allprofiles", "state"])
  status = result.decode("utf-8").split()[5::6]
  firewall_types = ["Domain", "Private", "Public"]
  return list(zip(firewall_types, status))


def Fire(FWPUD,FWD,FWPRI):
    
    status = get_firewall_status()

    for s in status:
      if(s[1] == "ON" and s[0] == "Domain"):
        FWD = 1
      if(s[1] == "ON" and s[0] == "Private"):
        FWPRI = 1
      if(s[1] == "ON" and s[0] == "Public"):
        FWPUD = 1
    return FWD,FWPRI,FWPUD


  

  



