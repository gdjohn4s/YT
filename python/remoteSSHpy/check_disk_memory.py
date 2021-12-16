#!/usr/bin/python3
"""
Scope: Checking remote file system disks
"""

import paramiko
import sys


def print_usage():
    print(f'Usage: python {sys.argv[0]} [IP] [USER] [PASS]')


# if sys.argv[1] is None or sys.argv[2] is None or sys.argv[3] is None: print_usage()

v_server: str = sys.argv[1]
v_user: str = sys.argv[2]
v_pass: str = sys.argv[3]
v_cmd: str = sys.argv[4]

v_client = paramiko.SSHClient()
v_client.save_host_keys("host_key.txt")
v_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    v_client.connect(v_server, username=v_user, password=v_pass)
except paramiko.AuthenticationException:
    print("AUTH FAILED")

v_stdin, v_stdout, v_stderr = v_client.exec_command(v_cmd)

for line in v_stdout:
    print(line.strip('\n'))

v_client.close()
