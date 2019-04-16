#!/usr/bin/env python3

import argparse

def args_gestion():
  parser = argparse.ArgumentParser(description="Test script")
  parser.add_argument("-nb", metavar=int, required=True)
  return parser.parse_args()
 
if __name__ == 'main':
  PARAM = args_gestion()
  a = PARAM.nb * 10
  print(a)
