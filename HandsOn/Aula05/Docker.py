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


    def remove_container(self, name):
        container = self.client.stop(name)
        container = self.client.remove_container(name)
        print "Container removido com sucesso"


    def exec_command(self, name, cmd):
        # Apenas cria o comando, mas nao executa. Retorna o ID para executar abaixo
        exec_id = self.client.exec_create(name, cmd)
        response = self.client.exec_start(exec_id)
        print response 



if __name__=="__main__":

    d = Docker()
#    d.create_container("proxy","ubuntu")
#    print d.list_container()

    d.exec_command("proxy", "apt-get update")
    
#    d.remove_container("proxy")





