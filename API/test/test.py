import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

import app
from app import db, Farmer, Investor, Trader, Product


class GenzTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app()
        self.client = self.app.test_client
        self.database_name = "genzapp_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format(
            "postgres", "despicable01", "localhost:5432", self.database_name)
        db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass
