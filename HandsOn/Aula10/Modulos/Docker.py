#!/usr/bin/python

#VER ANOTACOES.TXT PARA CONFIGURAR LIB DO DOCKER

from docker import Client
from ConfigParser import ConfigParser # Para ler o dexter.cfg

class Docker:
    def __init__(self):

        try:
            config = ConfigParser()
            config.read("dexter.cfg")
            self.client = Client(base_url="tcp://192.168.0.2:2376")
        except Exception as e:
            print "Falhou ao conectar com docker: ",e

    def list_container(self):
        containers = self.client.containers(all=True) #docker ps -a
        return containers


    def create_container(self, name, image):
        try:
            container = self.client.create_container(name=name,
                                                     image=image,
                                                     command="/bin/bash",
                                                     stdin_open=True,
                                                     tty=True,
                                                     detach=True)
            self.client.start(container)
            return {"message":"Container criado com sucesso"}
        except Exception as e:
            return {"message":"Falha ao criar container: %s"%e}            


    def remove_container(self, name):
        container = self.client.stop(name)
        container = self.client.remove_container(name)
        print "Container removido com sucesso"


    def exec_command(self, name, cmd):
        # Apenas cria o comando, mas nao executa. Retorna o ID para executar abaixo
        exec_id = self.client.exec_create(name, cmd)
        response = self.client.exec_start(exec_id)
        print response 

    
    def inspect_container(self, name):
        container = self.client.inspect_container(name)
        print container

    def  stop_container(self, cid):
        try:
            container = self.client.stop(cid)
            #print "===", cid, " | ", container
            return {"message":"Container parado com sucesso"}
        except Exception as e:
            return {"message":"Falha ao parar container: %s"%e}


    def  start_container(self, cid):
        try:
            container = self.client.start(cid)
            return {"message":"Container startado com sucesso"}
        except Exception as e:
            return {"message":"Falha ao startar container: %s"%e}



if __name__=="__main__":

    d = Docker()
    d.remove_container("proxy")
    d.create_container("proxy","ubuntu")
#    print d.list_container()

#    d.exec_command("proxy", "ls -la")
    
#    d.inspect_container("proxy")
    
#    d.remove_container("proxy")





