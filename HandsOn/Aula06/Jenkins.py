#!/usr/bin/python

import jenkins

class Jenkins:
    def __init__(self):
        try:
            self.server = jenkins.Jenkins("http://192.168.0.4:8080")
            print self.server.get_version()
        except Exception as e:
            print "Nao foi possivel conectar ao Jenkins: ", e    
        
    def create_job(self, name):
        try:
            print  jenkins.EMPTY_CONFIG_XML
            self.server.create_job(name, jenkins.EMPTY_CONFIG_XML)
            print "Job criada com sucesso!"
        except Exception as e:
            print "Falhou ao criar job: ", e     
            
        
if __name__=="__main__":
    j = Jenkins()
    j.create_job("Job Python")




