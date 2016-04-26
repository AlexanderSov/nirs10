#!/usr/bin/env python3

import paramiko
import time

class SSH_Conn:

    def __init__(self, host, username, password, commands):
        self.host = host
        self.username = username
        self.password = password
        self.commands = commands

    def single_host_conn(host, username, password):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy()    

        try:
            client.connect(hostname=host, username=useruse, password=sekret)
        except OSError as err:
            print(err)
            print (host, " is unreachable")
            hosts_w_problems +=host
            hosts_w_problems +=" "
            continue
        except paramiko.ssh_exception.AuthenticationException as err1:
            print (err1)
            print ("Authentication failed with", host)
            hosts_w_problems +=host
            hosts_w_problems +=" "
            continue
        interactive_shell=client.invoke_shell()
        print("SSH подключение устанвлено к ", host)
        return(interactive_shell)


    def send_commands_to_shell(self, ishell, host, commands)

        f=open(host+".txt", "a")

        for command in commands:
            command +="\n"
            ishell.send("\n")
            ishell.send(command)
            time.sleep(2)
            output=interactive_shell.recv(10000)
            print (output.decode('utf-8'), "\n")
            f.write(output.decode('utf-8')+"\n")

        f.close()
        client.close()

