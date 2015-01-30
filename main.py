import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app
from views import GetIndexView, GetRapportView


application = webapp2.WSGIApplication([(r'/', GetIndexView),
                                       (r'/rapport', GetRapportView),
                                       ], debug=True)