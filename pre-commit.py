#! /usr/bin/env python3

import time
import sys
import os
import pprint
import subprocess

print("Hello from pre-commit python file")
time.sleep(2)
print(sys.argv[0])
time.sleep(2)
print(sys.argv[1:])
print(os.getcwd())
git_envs = {key: value for key, value in os.environ.items() if "GIT" in key}
pprint.pprint(git_envs)
subprocess.run(["flake8", "."])
subprocess.run(["black", "."])
