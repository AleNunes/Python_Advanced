#!/usr/bin/python

import jenkins
from lxml import etree
from ConfigParser import ConfigParser # Para ler o dexter.cfg


class Jenkins:
    def __init__(self):
        try:
            config = ConfigParser()
            config.read("dexter.cfg")
            self.server = jenkins.Jenkins("http://%s:8080"%config.get("jenkins", "server"))

            print self.server.get_version()
        except Exception as e:
            print "Nao foi possivel conectar ao Jenkins: ", e    
        
    def create_job(self, name, repo_url, cmd):
        try:

            with open("templates/job.xml","r") as f:
                #str(repo_url) forca a var de unicode para string
                xml = f.read().replace("REPO_URL",str(repo_url))  
            
            xml = self.generate_steps(xml, cmd)
            
            
            #print  jenkins.EMPTY_CONFIG_XML
            self.server.create_job(name, xml)
            print "Job criada com sucesso!"
        except Exception as e:
            print "Falhou ao criar job: ", e     
            


    def generate_steps(self, xml, cmd):
        root = etree.XML(xml)
        for b in root.findall("builders"):
            builder = b
        with open(cmd,"r") as f:
            for c in f.readlines():
        
                command = etree.Element("command")
                command.text = 'ssh forlinux@192.168.0.2 "%s"'%c

                shell = etree.Element("hudson.tasks.Shell")
                shell.append(command)
                builder.append(shell)

        return etree.tostring(root)

    def run_job(self, name, var, value):
        try:
            self.server.build_job(name, {var:value})
            print "Job Executado"
        except Exception as e:
            print "Falhou ao executar job", e


        
if __name__=="__main__":
    j = Jenkins()
    j.create_job("JobWordPress6")
    j.run_job("JobWordPress6", "CONTAINER","wordpress")



