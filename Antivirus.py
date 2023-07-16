import subprocess
import re
N_AV=1 
N_WD=1
def execute_cmd(cmd, show_output=False):
  """Executes a shell command and returns the output.

  Args:
    cmd: The shell command to execute.
    show_output: Whether to show the output of the command.

  Returns:
    The output of the command, or an empty string if the command failed.
  """

  with subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc:
    output, err = proc.communicate()
    if show_output:
      print(output.decode())
    return output.decode() if output else err.decode()

def get_av_products(N_AV,N_WD):
  
  """Gets the list of antivirus products installed on the system.

  Returns:
    A tuple of two lists, the first list containing the names of third-party
    antivirus products and the second list containing the names of Windows
    Defender.
  """
  text = execute_cmd(r'WMIC /Node:localhost /Namespace:\\root\SecurityCenter2 Path AntiVirusProduct Get displayName /Format:List')
  third_party = []
  windows = []
  for line in text.split('\n'):
    if line.strip():
      match = re.match(r'displayName=(.*)', line)
      if match:
        name = match.group(1)
        if 'windows' in name.lower():
          windows.append(name)
        else:
          third_party.append(name)
        if(len(third_party) == 0):
          N_AV=0
        if(len(windows) == 0):
          N_WD=0

  return N_AV,N_WD

# if __name__ == '__main__':
#   get_av_products()
  # AV_N, WD_N = get_av_products()  
  # print(WD_N,AV_N)
  # if third_party:
  #   print('Third Party Anti Viruses:')
  #   # print('\n'.join(third_party))
  #   print(AV)
  # else:
  #   print('Third Party Anti Viruses:')
  #   print(AV)

  # if windows:
  #   print('Windows Anti Virus Tool:')
  #   print(WD)
  #   # print('\n'.join(windows))
  # else:
  #   print('Windows Anti Virus Tool:')
  #   print(WD)
