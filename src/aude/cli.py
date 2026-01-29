from .version import get_version
from . import cmd_registry
from .run_cmd import run_cmd
import sys

default_cmd_map = {"v": get_version()}
default_cmd_map.update(cmd_registry.cmd_map)

argslist = sys.argv[1:]

def main():
   
   if len(sys.argv) < 2:
      print("""
      aude setup      - to make a new custom command
      aude <cmd> <arg>- to run a custom command
      aude del <cmd>  - to delete an existing command
      aude info <cmd> - to check about an existing command
      aude l          - to see all custom  commands
      aude v          - to check version""")
      
   if argslist[0] in default_cmd_map.keys():
      return default_cmd_map[argslist[0]]
   else:
      return run_cmd(argslist)
      
   
      