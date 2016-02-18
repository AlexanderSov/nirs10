#!/usr/bin/env python3

import paramiko
import time

#тест git'a
#тест git'a 2

hosts1=input("Введите адреса устройств через пробел: ")
hosts=hosts1.split()
print(hosts)
user=input("Введите логин: ")
sekret=input("Введите пароль: ")
commands1=input("""Введите комманды, отделяя их\
 точкой с запятой и пробелом (; ): """)
t="; "
commands=commands1.split(t)
print(commands)
hosts_w_problems=""

for host in hosts:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=host, username=user, password=sekret)
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
    for command in commands:
        command +="\n"
        interactive_shell.send("\n")
        interactive_shell.send(command)
        time.sleep(2)
        output=interactive_shell.recv(10000)
        print (output.decode('utf-8'), "\n")
        f=open(host+".txt", "a")
        f.write(output.decode('utf-8'))
        f.write("\n")
        f.close()
    client.close()
print("Хосты с проблемами: ", hosts_w_problems)

