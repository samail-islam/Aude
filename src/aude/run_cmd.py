from .registration_sys import data
import subprocess

def run_cmd(arglist):
   cmd = arglist[0]
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
      
            for line in parsed_task: 
               print(line)
            print("commands printed above will be run")
            cns = input("you want to continue?(just hit enter to continue or type 'n' to stop)")
            if cns =! "n":
               subprocess.run(line,shell=True)
            else: 
               raise SystemExit(1)
            return
      
   print(f"Unknown command {cmd}")  
            
   
   
   