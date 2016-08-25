#!/usr/bin/python

import requests
import json
from ConfigParser import ConfigParser # Para ler o dexter.cfg



class Gitlab:
    def __init__(self):
        try:
            config = ConfigParser()
            config.read("dexter.cfg")
            self.token = config.get("gitlab", "token")
            self.server = config.get("gitlab", "server")
        except Exception as e:
            print "Falha ao buscar configuracoes"

    # _metodos privados
    def _make_get(self, resource, params=""):
        url = "http://{2}/api/v3/{0}?private_token={1}" \
                .format(resource, self.token, self.server)  # .format substitui os {0} e {1}
        response = requests.get(url)
        return response


    def _make_post(self, resource, data):
        url = "http://{2}/api/v3/{0}?private_token={1}" \
                .format(resource, self.token, self.server)  # .format substitui os {0} e {1}
        headers = {"Content-Type":"application/json"}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        return response


    def get_users(self):
        users = self._make_get("users")
        users = json.loads(users._content)
        return users

    def get_projects(self):
        projects = self._make_get("projects")
        projects = json.loads(projects._content)
        return projects

    def create_user(self, name, email):
        user_data = {"name":name,
                     "username":name,
                     "email":email,
                     "password":"!23Mudar"}
        user = self._make_post("users", user_data)
        if user.status_code == 201:  #201 = comando executado com sucesso
            return True
        else:
            print user.status_code
            print  user._content
            return False


    def create_project(self, name):
        project_data = {"name":name}
        project = self._make_post("projects", project_data)
        if project.status_code == 201:  #201 = comando executado com sucesso
            return True
        else:
            print project.status_code
            print project._content
            return False

    def add_user_project(self, user_email, project_name):
        projects = self.get_projects() #_make_get("projects")
        users =  self.get_users()
        
        p = [ p for p in projects if p.get("name") == project_name]
        u = [ u for u in users if u.get("email") == user_email]
        
        if not p:        
            print "Projeto nao encontrado"
            return False
        if not u:
            print "Usuario nao encontrado"
            return False

        data={"id":p[0].get("id"), "user_id":u[0].get("id"), "access_level":30}  #30 = Developer
        response = self._make_post("projects/%s/members"%p[0].get("id"), data)
        
        if response.status_code == 201:
            return True
        else:
            return False
        

    def add_webhook(self, project_name, url):
        
        data={"url":url, "push_events":True}

        projects = self.get_projects() 
        p = [ p for p in projects if p.get("name") == project_name]

        if not p:
            print "webhook - Projeto nao encontrado"
            return False
        response = self._make_post("projects/%s/hooks"%p[0].get("id"), data)
        if response.status_code == 201:
            return True
        else:
            return False


    def get_repo_url(self, project_name):
        print "=== Projeto: ", project_name

        projects = self.get_projects() 
        
#        print "==", projects
        
        p = [ p for p in projects if p.get("name") == project_name]

        if not p:
            print "get_repo_url - Projeto nao encontrado"
            return False
        repo_url = p[0].get("ssh_url_to_repo")
        print repo_url
        return repo_url
        

if __name__=="__main__":

    g = Gitlab()
#    g.get_users()
#    print g.get_projects()

# Criando usuario:
    if g.create_user("TesteDexter","teste.dexter@dexter.com.br"):
        print "Usuario criado com sucesso"
    else:
        print "Falha ao criar usuario"

# Criando projeto
#    if g.create_project("Teste2"):
#        print "Projeto criado com sucesso"
#    else:
#        print "Falha ao criar projeto"

# Associando usuario ao projeto
#    g.add_user_project("teste@dexter.com.br", "Teste2")

# Criando Web Hook - trigger para quando houver um commit, uma outra aplicacao fazer um build por exemplo
#    if g.add_webhook("Teste2", "http://jenkins.dexter.com.br:8080/gitlab/build_now"):
#        print "Web Hook adicionado com sucesso"
#    else:
#        print "Falhou ao adicionar web hook"

