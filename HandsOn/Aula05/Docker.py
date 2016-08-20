#!/usr/bin/python


from docker import Client

class Docker:
    def __init__(self):
        self.client = Client(base_url="tcp://192.168.0.2:2376")

    def list_container(self):
        containers = self.client.containers(all=True) #docker ps -a
        return containers


    def create_container(self, name, image):
        container = self.client.create_container(name=name,
                                                 image=image,
                                                 command="/bin/bash",
                                                 stdin_open=True,
                                                 tty=True,
                                                 detach=True)
        self.client.start(container)
        print "Container criado com sucesso"


if __name__=="__main__":

    d = Docker()
#    print d.list_container()
    d.create_container("proxy","ubuntu")






