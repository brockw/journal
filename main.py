import webapp2
import logging
from google.appengine.api import app_identity
from google.appengine.api import mail
import datetime
import pytz

import os


class Send(webapp2.RequestHandler):
    def get(self):
        sentFromAddress = 'journal@{}.appspotemail.com'.format(app_identity.get_application_id())
        name = os.environ.get("NAME")
        email = os.environ.get("EMAIL")
        logging.info("Send email from " + sentFromAddress + " to " + email)
        today = datetime.datetime.now(pytz.timezone('America/Edmonton'))
        todaysDate = today.strftime("%A %d/%m/%Y")
        logging.info(todaysDate)

        
        mail.send_mail(sender=email,
                        to="{} <{}>".format(name, email),
                        subject="Journal",
                        body="""{}
                             """.format(todaysDate))

app = webapp2.WSGIApplication([
    ('/send', Send),
], debug=True)
