#!/usr/bin/python

#sudo pip install pyyaml

#python DeployTool.py -i deploy.yml

import yaml
import argparse
from Modulos.Docker import Docker
from Modulos.gitlab import Gitlab
from Modulos.Jenkins import Jenkins




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
        jenkins = Jenkins()
        gitlab = Gitlab()
        application = self.arquivo.get("application")
        devs = self.arquivo.get("developers")
        

        
        try:
            if gitlab.create_project(application):
                print "Projeto criado com sucesso"
            else:
                print "Falha ao criar projeto"
            for d in devs:
                if gitlab.create_user(d.split("@")[0], d):
                    print "Usuario criado com sucesso"
                if gitlab.add_user_project(d, application):
                    print "Usuario adicionado ao projeto"
            
            #print "Tentar adicionar webhook:"
            webhook = gitlab.add_webhook(application, "http://192.168.0.4:8080/gitlab/build_now")
            if webhook:
                print "WebHook adicionada com sucesso"
            
            #print "buscando url:"
            repo_url = gitlab.get_repo_url(application)

            jobname = self.arquivo.get("job").get("name")
            cmd = self.arquivo.get("job").get("deploy")
            jenkins.create_job(jobname, repo_url, cmd)
            docker.create_container(application, "ubuntu")
        except Exception as e:
            print "Container ja existee", e

        
        
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

        
        
        
