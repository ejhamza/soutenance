import webapp2

from google.appengine.ext.webapp.util import run_wsgi_app
from views import *

application = webapp2.WSGIApplication([(r'/', GetIndexView),
                                       (r'/rapport', GetRapportView),
                                       (r'/addreport', GetAddRapportView),
                                       ('/upload', UploadHandler),
                                       ], debug=True)