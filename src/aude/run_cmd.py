from .config import DATA_FILE
from .registration_sys import data
import subprocess

def run_cmd(cmd):
   for item in data['custom_cmd']:
      if item['Name'] == cmd:
         parsed_task = []
         for line in item['tasks']:
            if line.find("%") != -1:
               for word in line.split():
                  if word.startswith("%"):
                     prsd_line = line.replace(word, arglist[word[1:]])
                     parsed_task.append(prsd_line)
                  else:
                     parsed_task.append(line)
      
            
            subprocess.run(line,shell=True)
      
            
            
   
   
   