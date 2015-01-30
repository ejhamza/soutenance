#!/usr/bin/env python

import os
import webapp2
import jinja2
from datetime import time, date
import logging


#Preparation de l'environnement Jinja2
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)+'/html'))

class GetIndexView(webapp2.RequestHandler):
    def get(self):
        year = date.today().year
        template_values = {"year":year}
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))
        
        
class GetRapportView(webapp2.RequestHandler):
    def get(self):
        year = date.today().year
        template_values = {"year":year}
        template = JINJA_ENVIRONMENT.get_template('rapports.html')
        self.response.write(template.render(template_values))