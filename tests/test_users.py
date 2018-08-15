import unittest
import os
import json

from app.app import create_app
from app.models.user import User



class TestUserFunctinality(unittest.TestCase):
    """This class represents the user test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.user = {"first_name": "Eva",
                     "last_name": "Maina",
                     "username": "Evet",
                     "email": "testEvet@gmail.com",
                     "password": "evet123",
                     "confirm_password": "evet123"
                    }


    def test_user_can_register(self):
        """
        Test new user can be registered to the system.
        """
        response = self.app.post("/api/v1/register",
                                 data=json.dumps(self.users),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("User successfully created", response_msg["Message"])

    def test_user_registration_empty_firstname(self):
        """
        Test user cannot enter blank firstname.
        """
        response = self.app.post("/api/v1/register",
                                 data=json.dumps(dict(first_name="",
        											  last_name="testlastnam",
                                 	                  username="testusername",
                                 	                  email="testEvet@gmail.com",
                                 	                  password="testpassword",
                                                      confirm_password="testconfirmpassword")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("First name is required",
                         response_msg["Message"])

    def test_user_registration_empty_lastname(self):
        """
        Test user cannot enter blank last name.
        """
        response = self.app.post("/api/v1/register",
                                 data=json.dumps(dict(first_name="Eva",
                                                      last_name="",
                                                      username="testusername",
                                                      email="testEvet@gmail.com",
                                                      password="testpassword",
                                                      confirm_password="testconfirmpassword")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Last name is required",
                         response_msg["Message"])

    def test_user_registration_empty_password(self):
        """
        Test user cannot enter blank password.
        """
        response = self.app.post("/api/v1/register",
                                 data=json.dumps(dict(first_name="Eva",
                                                      last_name="testlastnam",
                                                      username="testusername",
                                                      email="testEvet@gmail.com",
                                                      password="",
                                                      confirm_password="testconfirmpassword")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("First name is required",
                         response_msg["Message"])

    def test_user_registration_empty_email(self):
        """
        Test user cannot enter blank last name.
        """
        response = self.app.post("/api/v1/register",
                                 data=json.dumps(dict(first_name="Eva",
                                                      last_name="testlastnam",
                                                      username="testusername",
                                                      email="",
                                                      password="testpassword",
                                                      confirm_password="testconfirmpassword")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Email is required",
                         response_msg["Message"])

    def test_user_exists(self):
        """
        Test new user can be registered to the system.
        """
        response = self.app.post("/api/v1/register",
                                 data=json.dumps(dict(first_name="eve",
                                                      last_name="testlastnam",
                                                      username="evet",
                                                      email="evet@gmail.com",
                                                      password="evat",
                                                      confirm_password="testconfirmpassword")),
                                 content_type="application/json")
        response = self.app.post("/api/v1/register",
                                 data=json.dumps(dict(first_name="eve",
                                                      last_name="testlastnam",
                                                      username="evet",
                                                      email="evet@gmail.com",
                                                      password="evat",
                                                      confirm_password="testconfirmpassword")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 409)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("User already exist", response_msg["Message"])

    def test_user_email_validity(self):
        """
        Test new user uses a valid email.
        """
        response = self.app.post("/api/v1/register",
                                 data=json.dumps(dict(first_name="eve",
                                                      last_name="testlastnam",
                                                      username="testusername",
                                                      email="testEmail",
                                                      password="testpassword",
                                                      confirm_password="testconfirmpassword")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Enter valid email address",
                      response_msg["Message"])

    