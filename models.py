#!/usr/bin/env python
from google.appengine.api import mail, users
from google.appengine.ext import db, blobstore


class Rapport(db.Model):
    user = db.StringProperty()
    sujet = db.StringProperty(multiline=True)
    filiere = db.StringProperty(multiline=True)
    societe = db.StringProperty(multiline=True)
    cle = blobstore.BlobReferenceProperty()
    ajout = db.DateTimeProperty(auto_now=True)
    
# def GetUser(key,passe):
#     user = db.Query(Personne).filter('username =', key).get()
#     if user:
#         return user
#     else:
#         return None
#    

def AddReport(user,sujet,societe,filiere,keys):
    user = users.get_current_user()
    rapport = Rapport(user=user,sujet=sujet,societe=societe,filiere=filiere,cle=keys)
    db.put(rapport)
    
    
def GetAllReports():
    list_of_reports = Rapport.all()
    
    return list_of_reports
    

def senEmail(to):
    # Send the message via API Mail.
    mail.send_mail(sender= "ej.hamza@gmail.com", to= "ej.hamza@gmail.com", subject= "test Email Send", body= "Hello")