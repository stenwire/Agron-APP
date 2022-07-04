import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database - done


# TODO IMPLEMENT DATABASE URL - done
SQLALCHEMY_DATABASE_URI = 'postgres://zqlpsfkclvlbrx:3222e0ffd847d08da74e5bc23be4370ad5892174dc8aa4573c00938271d0345c@ec2-23-23-151-191.compute-1.amazonaws.com:5432/d8hgqv66uofo5a'
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:despicable01@localhost:5432/genzapp'
SQLALCHEMY_TRACK_MODIFICATIONS = False
