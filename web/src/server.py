from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.renderers import render_to_response

import mysql.connector as mysql
import os

db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']
db_host = os.environ['MYSQL_HOST']

def adduser(req):
  email=self.request.POST["email_text"]
  first_name=self.request.POST["firstname_text"]
  last_name=self.request.POST["lastname_text"]
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  query = "INSERT INTO Users (email, first_name, last_name) values (%s, %s, %s)"
  values = (email, first_name, last_name)
  cursor.execute(query, values)
  db.commit()


def get_home(req):
  # Connect to the database and retrieve the users
  return render_to_response('templates/home.html', request=req)

def get_about(req):
  # Connect to the database and retrieve the users
  return render_to_response('templates/about.html', request=req)

def get_signup(req):
  # Connect to the database and retrieve the users
  return render_to_response('templates/signup.html', request=req)

def get_pricing(req):
  # Connect to the database and retrieve the users
  return render_to_response('templates/pricing.html', request=req)

def get_features(req):
  # Connect to the database and retrieve the users
  return render_to_response('templates/features.html', request=req)

''' Route Configurations '''
if __name__ == '__main__':
  config = Configurator()

  config.include('pyramid_jinja2')
  config.add_jinja2_renderer('.html')

  config.add_route('get_home', '/')
  config.add_view(get_home, route_name='get_home')

  config.add_route('get_about', '/')
  config.add_view(get_home, route_name='get_about')

  config.add_route('get_pricing', '/')
  config.add_view(get_home, route_name='get_pricing')

  config.add_route('get_features', '/')
  config.add_view(get_home, route_name='get_features')

  config.add_route('get_signup', '/')
  config.add_view(get_home, route_name='get_signup')

  config.add_static_view(name='/', path='./public', cache_max_age=3600)

  app = config.make_wsgi_app()
  server = make_server('0.0.0.0', 6000, app)
  server.serve_forever()