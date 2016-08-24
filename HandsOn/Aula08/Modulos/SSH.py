#!/usr/bin/python

import paramiko

class SSH:
    def __init__(self):
        self.client = paramiko.SSHClient()
        self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname="192.168.0.2",
                            username="forlinux",
                            password="4linux")
                            
    def exec_command(self, container, cmd):
        stdin,stdout,stderr = self.client.exec_command("docker exec {0} {1}".format(container, cmd))
        if stderr.channel.recv_exit_status() != 0:
            print stderr.read()
        else:
            print stdout.read()
            
            
