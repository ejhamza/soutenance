#!/usr/bin/env python

from datetime import time, date
import logging
import os
import webapp2

from google.appengine.api import users
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
import jinja2

import models
from google.storage.speckle.proto.jdbc_type import NULL


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
        # Current year for the footer
        year = date.today().year
        # Extract the list of reports
        list_report = models.GetAllReports()        
        
        template_values = {"year":year,"list_report":list_report}
        template = JINJA_ENVIRONMENT.get_template('rapports.html')
        self.response.write(template.render(template_values))
        
        
class GetAddRapportView(webapp2.RequestHandler):
    def get(self):
        upload_url = blobstore.create_upload_url('/upload')
        year = date.today().year
        template_values = {"year":year,'upload_url':upload_url}
        template = JINJA_ENVIRONMENT.get_template('addreport.html')
        self.response.write(template.render(template_values))
        
        
class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
  def post(self):
    societe = self.request.get('societe')
    filiere = self.request.get('filiere')
    sujet = self.request.get('sujet')
    
    upload_files = self.get_uploads('file')  # 'file' is file upload field in the form
    blob_info = upload_files[0]
    nom = "haha"
    #get the connected user 
    user = users.get_current_user()
    if user:
        nom = user.email()
    else:
        self.redirect(users.create_login_url(self.request.uri))
    
    models.AddReport(nom,sujet,societe,filiere,blob_info.key())
    self.redirect('/rapport')