#!/usr/bin/python

#sudo pip install pyyaml
import yaml
import argparse
from Modulos.Docker import Docker
from Modulos.SSH import SSH


class DeployTool:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-i", help="Define arquivo de deploy")
        
    def yaml_parser(self, arquivo):
        with open(arquivo, "r") as  f:
            self.arquivo = yaml.load(f.read())
        
    def deploy(self):
        #Criar container
        docker = Docker()
        #docker.remove_container(self.arquivo.get("application"))
        try:
            docker.create_container(self.arquivo.get("application"),"ubuntu")
        except Exception as e:
            print "Container ja existee", 

        ssh = SSH()
        for c in self.arquivo.get("deploy-sequence"):
            print "Executando comando: ", c
            ssh.exec_command(self.arquivo.get("application"),c)
        #fazer deploy
        #testar aplicacao
        
        
if __name__=="__main__":
    
    d =  DeployTool()
    #le argumentoss passados pelo usuaio
    args = d.parser.parse_args()
    #converte arquivo yaml para dicionario
    d.yaml_parser(args.i)
    #faz deploy da aplicacao
    d.deploy()
    #print args.i
    #print "Arquivo de deploy selecionado: ", args.i #Correspondee  ao -i definido acima

        
        
        
