import unittest
import os
import json
from app.manage import drop_tables, create_tables
from app.app import create_app

from app.models.users import User


class TestUserFunctinality(unittest.TestCase):
    """This class represents the user test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        create_tables()
        self.app = create_app('testing')
        self.client = self.app.test_client()

    def tearDown(self):
        drop_tables()

    def test_user_can_signup(self):
        response = self.client.post('/api/v2/signup',
                                    data=json.dumps(dict(first_name="evat",
                                                         last_name="maina",
                                                         username="johnson",
                                                         email="evajohnson@gmail.com",
                                                         password="sttt123",
                                                         confirm_password="sttt123")),
                                    content_type='application/json')

        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("User successfully created",
                         response_msg["Message"])

    def test_user_registration_empty_firstname(self):
        """
        Test user cannot enter blank firstname.
        """
        response = self.client.post("/api/v2/signup",
                                    data=json.dumps(dict(first_name="",
                                                         last_name="tnam",
                                                         username="name",
                                                         email="hjg@gmail.com",
                                                         password="evet",
                                                         confirm_password="evet")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 400)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("First name is required",
                         response_msg["Message"])

    def test_user_registration_empty_lastname(self):
        """
        Test user cannot enter blank last name.
        """
        response = self.client.post("/api/v2/signup",
                                    data=json.dumps(dict(first_name="james",
                                                         last_name="",
                                                         username="tom",
                                                         email="pwd@gmail.com",
                                                         password="pwd",
                                                         confirm_password="pwd")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 400)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Last name is required",
                         response_msg["Message"])

    def test_user_registration_empty_password(self):
        """
        Test user cannot enter blank password.
        """
        response = self.client.post("/api/v2/signup",
                                    data=json.dumps(dict(first_name="beat",
                                                         last_name="betty",
                                                         username="betz",
                                                         email="betz@gmail.com",
                                                         password="",
                                                         confirm_password="")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 400)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Password is required",
                         response_msg["Message"])

    def test__empty_username(self):
        """
        Test user cannot enter blank last name.
        """
        response = self.client.post("/api/v2/signup",
                                    data=json.dumps(dict(first_name="john",
                                                         last_name="doe",
                                                         username="",
                                                         email="doe@gmail.com",
                                                         password="jdoe",
                                                         confirm_password="jdoe")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 400)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Username is required",
                         response_msg["Message"])

    def test_user_email_exists(self):
        """
        Test new user already exist in the system to the system.
        """
        response = self.client.post("/api/v2/signup",
                                    data=json.dumps(dict(first_name="juliet",
                                                         last_name="smith",
                                                         username="jsmith",
                                                         email="smith@gmail.com",
                                                         password="smith23",
                                                         confirm_password="smith23")),
                                    content_type="application/json")
        response = self.client.post("/api/v2/signup",
                                    data=json.dumps(dict(first_name="juliet",
                                                         last_name="smith",
                                                         username="jsmith",
                                                         email="smith@gmail.com",
                                                         password="smith23",
                                                         confirm_password="smith23")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 409)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("user with this email address exist",
                         response_msg["Message"])

    def test_user_username_exists(self):
        """
        Test new user already exist in the system to the system.
        """
        response = self.client.post("/api/v2/signup",
                                    data=json.dumps(dict(first_name="peter",
                                                         last_name="will",
                                                         username="pwil",
                                                         email="ptw@mail.com",
                                                         password="ptt",
                                                         confirm_password="ptt")),
                                    content_type="application/json")
        response = self.client.post("/api/v2/signup",
                                    data=json.dumps(dict(first_name="peter",
                                                         last_name="will",
                                                         username="pwil",
                                                         email="pt@mail.com",
                                                         password="ptt",
                                                         confirm_password="ptt")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 409)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("user with this username already exist",
                         response_msg["Message"])

    def test_user_email_validity(self):
        """
        Test new user uses a valid email.
        """
        response = self.client.post("/api/v2/signup",
                                    data=json.dumps(dict(first_name="eve",
                                                         last_name="lastnam",
                                                         username="tusername",
                                                         email="testEmail",
                                                         password="mmmm",
                                                         confirm_password="mmmm")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 400)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Enter a valid email",
                         response_msg["Message"])

    def test_empty_password(self):
        """
        Test user cannot enter blank password.
        """
        response = self.client.post("/api/v2/signup",
                                    data=json.dumps(dict(first_name="Eva",
                                                         last_name="mfgh",
                                                         username="testuser",
                                                         email="testEvvt@gmail.com",
                                                         password="",
                                                         confirm_password="")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 400)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Password is required",
                         response_msg["Message"])

    def test_user_can_login(self):
        """
        Test new user can login to the system.
        """
        response = self.client.post("/api/v2/signup",
                                    data=json.dumps(dict(first_name="eva",
                                                         last_name="maina",
                                                         username="johnson",
                                                         email="evajohnson@gmail.com",
                                                         password="evaj",
                                                         confirm_password="evaj")),
                                    content_type="application/json")
        response_login = self.client.post("/api/v2/login",
                                          data=json.dumps(dict(
                                              username="johnson",
                                              password="evaj")),
                                          content_type="application/json",
                                          )

        self.assertEqual(response_login.status_code, 200)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("User logged in successfully",
                         response_msg["message"])

    def test_user_login_with_wrong_password(self):
        """
        Test new user cannot login with wrong credentials.
        """
        response = self.client.post("/api/v2/signup",
                                    data=json.dumps(dict(first_name="evawer",
                                                         last_name="maina",
                                                         username="eve",
                                                         email="ev@gmail.com",
                                                         password="evaj",
                                                         confirm_password="evaj")),
                                    content_type="application/json")
        response = self.client.post("/api/v2/login",
                                    data=json.dumps(dict(
                                        username="eve",
                                        password="evaj")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Enter correct username",
                         response_msg["message"])
