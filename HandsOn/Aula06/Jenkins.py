#!/usr/bin/python

import jenkins
from lxml import etree

class Jenkins:
    def __init__(self):
        try:
            self.server = jenkins.Jenkins("http://192.168.0.4:8080")
            print self.server.get_version()
        except Exception as e:
            print "Nao foi possivel conectar ao Jenkins: ", e    
        
    def create_job(self, name):
        try:
            with open("templates/job.xml","r") as f:
                xml = f.read().replace("REPO_TESTE","git@git.com.br")
            
            xml = self.generate_steps(xml)
                
            #print  jenkins.EMPTY_CONFIG_XML
            self.server.create_job(name, jenkins.EMPTY_CONFIG_XML)
            print "Job criada com sucesso!"
        except Exception as e:
            print "Falhou ao criar job: ", e     
            


    def generate_steps(self, xml):
        root = etree.XML(xml)
        for b in root.findall("builders"):
            builder = b
        for c in builder.iterchildren():
            print c.tag, c.text
            for j in c.iterchildren():
                print j.tag
            
if __name__=="__main__":
    j = Jenkins()
    j.create_job("Job Python 2")




