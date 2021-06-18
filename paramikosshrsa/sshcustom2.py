#!/usr/bin/env python3

## std library imports on top
import os

## 3rd party imports below
import paramiko

## work assigned to a junior programming asset on our team
from jrprogrammer import cmdissue

def ourCommands():
    """presents a list of user commands to send"""    
    our_commands = ["touch sshworked.txt", "touch create.txt", "touch file3.txt", "ls"]
    print("Commands Available: \n")
    for x in our_commands:
        print(x)
    cmd = input("Issue command: \n>")

    if cmd in our_commands:    
        return cmd   
    else:
        print("Command not avilable")
        return 'clear'

def getUserData():
    data = {}
    print("Please type in username and hostname IP for servers or type done")

    while True:
        i=0
        host = input("IP: ")
        if host == "done" and len(data) != 0:
            break  
        user = input("username: ")
        if user == "done" and len(data) !=0:
            break
        data[i] = [host,user]
        i += 1
    return data

def main():
  ## create session object
  sshsession = paramiko.SSHClient()
  sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

  mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")
  
  ## create SSH connection
  data = getUserData()

  for entry in data.values():
      sshsession.connect(hostname=entry[0], username=entry[1], pkey=mykey)
  
  x =  ourCommands()
  
  resp = cmdissue(x, sshsession)
  
  if resp != "":
      print(resp)

  ## end the SSH connection
  sshsession.close()

if __name__ == '__main__':
  main()

