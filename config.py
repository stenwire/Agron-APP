import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database - done


# TODO IMPLEMENT DATABASE URL - done
SQLALCHEMY_DATABASE_URI = 'postgres://vyzbwuexwsgoyb:d02c39d997a30e5d8cc5884ebf6fbdb240cf1549e59352f3f0642add46bc0173@ec2-44-205-41-76.compute-1.amazonaws.com:5432/d3c1ph7oj62k6e'
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:despicable01@localhost:5432/genzapp'
SQLALCHEMY_TRACK_MODIFICATIONS = False
