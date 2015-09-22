from BaseHandler import Handler
from google.appengine.ext import db
from Db import Person
from datetime import datetime, timedelta
import re
import constants
class PayDues(Handler):
    def write_form(self, error = ""):
        self.render("payDues.html", error=error)
    #Renders the form with no error messages
    def get(self):
        self.write_form()
    #Deals with submitting the form
    def post(self):
        #Get information from the post request
        firstName = self.request.get('firstName')
        lastName = self.request.get('lastName')
        email = self.request.get('email')
        if email[-2:] == '@c':
            email += 'ollege.harvard.edu'
        if email[-7:] == '@college':
            email += '.harvard.edu'
        if email[-2:] == '@g':
            email += 'mail.com'
        EMAIL = re.compile(r"^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$")
        if not EMAIL.match(email):
            self.write_form(error = 'This is not a valid email')
            return
        password = self.request.get('password')
        if password != constants.PASSWORD:
            self.write_form(error = 'Wrong password!')
            return
        personQuery = db.GqlQuery("SELECT * FROM Person WHERE email = :1", email)
        if personQuery.count() > 0:
            person = personQuery.get()
            person.dues_paid = True
            person.put()
        else:
            person = Person(firstName = firstName,
                            lastName = lastName,
                            email = email,
                            dues_paid = True)
            person.put()
        self.redirect('payDues')
