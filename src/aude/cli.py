from .version import get_version
from . import cmd_registry
from .run_cmd import run_command
import sys

default_cmd_map = {}
default_cmd_map.update(cmd_registry.cmd_map)

argslist = sys.argv[1:]

def main():
   if len(sys.argv) < 2:
      print("""
      aude setup      - to make a new custom command
      aude <cmd> <arg>- to run a custom command
      aude del <cmd>  - to delete an existing command
      aude info <cmd> - to check about an existing command""")
      
   run_command(argslist)
      
   
      