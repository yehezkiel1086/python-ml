#!/bin/python3

import os

if os.path.exists("test.txt"):
  os.remove("test.txt")
  print("[+] File is removed")
else:
  print("[-] File doesn't exist")