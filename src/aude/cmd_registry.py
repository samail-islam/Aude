from .config import DATA_FILE
import json
import time

if not DATA_FILE.exists():
      DATA_FILE.write_text(json.dumps({"custom_cmds": []}, indent=4))

data = json.loads(DATA_FILE.read_text())

def cmd_check():
   cmd = input("Name: ")
   exists = [item for item in data if item["Name"] == cmd]
   if exists:
      overwrite = input(f"{cmd} already exists, want to overwrite it?(Y/n): " )
      if overwrite:
         registration_sys(cmd, remove=True)
         registration_sys(cmd)
      else:
         raise SystemExit(0)
   else:
      registration_sys(cmd=cmd, remove=False)
         
      

# registration system function
def registration_sys(cmd, remove=False):

   if not remove:
      print("Commands to run:\n")
      tasks = []
      lnum = 1
      while True :
         line = input(f'{lnum} ')
         if line == ".save":
            print(f'saving {cmd} ...')
            break
         else:
            tasks.append(line.strip())
            lnum += 1
      
      data['custom_cmds'].append({
         "Name": cmd,
         "Creation Date": time.strftime("%A, %d %b,%Y at %l:%M:%S %P %Z%z"),
         "tasks": tasks
        })
        
   else:
      print(f"Deleting {cmd} ...")
      data["custom_cmds"] = [
         item for item in data['custom_cmds'] if item["Name"] != cmd
        ]
        

   DATA_FILE.write_text(json.dumps(data, indent=4))
   print("Done")
    
    
def cmd_list():
   for item in data['custom_cmds']: 
      print(f"Name: {item['Name']} Creation date: {item['Creation Date']}")

def cmd_info(cmd):
   for item in data['custom_cmds']:
      if item['Name'] == cmd: 
         return item
   print(f"no custom command found called {cmd}")
cmd_map = {
   "setup": cmd_check()
   "del": registration_sys(cmd=arglist[1],remove=True)
   "l": cmd_list()
   "info": cmd_info(arglist[1]) 
   
}