from .config import DATA_FILE
from .registration_sys import data
import subprocess

def run_cmd(cmd):
   for item in data['custom_cmd']:
      if item['Name'] == cmd:
         i = 1
         for line in item['tasks']:
            line = line.replace(f"arg{i}", arglist[i])
            subprocess.run(line,shell=True)
            i += 1
            subprocess.run(f"{line}")
            
            
   
   
   