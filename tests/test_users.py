import unittest
import os
import json
from app.app import create_app
from app.models.users import User
from app.app import answer,question,user


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
                     "password": "evet123"
                     }
    def tearDown(self):
      del user.users[:]
      del question.questions[:]
      del answer.answers[:]

    def test_user_can_register(self):
        """
        Test new user can be registered to the system.
        """
        response = self.client.post("/api/v1/register",
                                    data=json.dumps(self.user),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("User successfully created", response_msg["Message"])

    def test_user_registration_empty_firstname(self):
        """
        Test user cannot enter blank firstname.
        """
        response = self.client.post("/api/v1/register",
                                    data=json.dumps(dict(first_name="",
                                                         last_name="testlastnam",
                                                         username="testusername",
                                                         email="testEvet@gmail.com",
                                                         password="testpassword")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("First name is required",
                         response_msg["Message"])

    def test_user_registration_empty_lastname(self):
        """
        Test user cannot enter blank last name.
        """
        response = self.client.post("/api/v1/register",
                                    data=json.dumps(dict(first_name="Eva",
                                                         last_name="",
                                                         username="testusername",
                                                         email="testEvet@gmail.com",
                                                         password="testpassword")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Last name is required",
                         response_msg["Message"])

    def test_user_registration_empty_password(self):
        """
        Test user cannot enter blank password.
        """
        response = self.client.post("/api/v1/register",
                                    data=json.dumps(dict(first_name="Eva",
                                                         last_name="testlastnam",
                                                         username="testusername",
                                                         email="testEvet@gmail.com",
                                                         password="")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Password is required",
                         response_msg["Message"])

    def test__empty_username(self):
        """
        Test user cannot enter blank last name.
        """
        response = self.client.post("/api/v1/register",
                                    data=json.dumps(dict(first_name="Eva",
                                                         last_name="test",
                                                         username="",
                                                         email="asgf@gmail.com",
                                                         password="evvv")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Username is required",
                         response_msg["Message"])

    def test_user_email_exists(self):
        """
        Test new user already exist in the system to the system.
        """
        response = self.client.post("/api/v1/register",
                                    data=json.dumps(dict(first_name="eve",
                                                         last_name="maina",
                                                         username="eva",
                                                         email="ev@gmail.com",
                                                         password="evt")),
                                    content_type="application/json")
        response = self.client.post("/api/v1/register",
                                    data=json.dumps(dict(first_name="eve",
                                                         last_name="maina",
                                                         username="ev",
                                                         email="ev@gmail.com",
                                                         password="evt")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 409)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("user with this email address exist",
                         response_msg["Message"])

    def test_user_username_exists(self):
        """
        Test new user already exist in the system to the system.
        """
        response = self.client.post("/api/v1/register",
                                    data=json.dumps(dict(first_name="evej",
                                                         last_name="mainaj",
                                                         username="evajjj",
                                                         email="evjj@mail.com",
                                                         password="evjt")),
                                    content_type="application/json")
        response = self.client.post("/api/v1/register",
                                    data=json.dumps(dict(first_name="evej",
                                                         last_name="mainaj",
                                                         username="evajjj",
                                                         email="evjjj@mail.com",
                                                         password="evjt")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 409)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("user with this username already exist",
                         response_msg["Message"])

    def test_user_email_validity(self):
        """
        Test new user uses a valid email.
        """
        response = self.client.post("/api/v1/register",
                                    data=json.dumps(dict(first_name="eve",
                                                         last_name="testlastnam",
                                                         username="testusername",
                                                         email="testEmail",
                                                         password="testpassword")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Enter a valid email",
                         response_msg["Message"])

    def test_empty_password(self):
        """
        Test user cannot enter blank password.
        """
        response = self.client.post("/api/v1/register",
                                    data=json.dumps(dict(first_name="Eva",
                                                         last_name="mfgh",
                                                         username="testuser",
                                                         email="testEvvt@gmail.com",
                                                         password="")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Password is required",
                         response_msg["Message"])

    def test_user_can_get_all_users(self):
        """
        Tests user can get all users in the system.
        """
        response = self.client.get("/api/v1/users",
                                data=json.dumps(dict()),
                                content_type="application/json")
        self.assertEqual(response.status_code, 200)
        response_msg = json.loads(response.data.decode("UTF-8"))

    def test_user_can_login(self):
        """
        Test new user can login to the system.
        """
        response = self.client.post("/api/v1/register",
                                    data=json.dumps(dict(first_name="eva",
                                                         last_name="maina",
                                                         username="johnson",
                                                         email="evajohnson@gmail.com",
                                                         password="evaj")),
                                    content_type="application/json")
        response = self.client.post("/api/v1/login",
                                    data=json.dumps(dict(
                                        username_or_email="johnson",
                                        password="evaj")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 200)
        # response_msg = json.loads(response.data.decode("UTF-8"))
        # self.assertEqual("User logged in successfully", response_msg["message"])


    def test_user_login_with_wrong_password(self):
        """
        Test new user cannot login with wrong credentials.
        """
        response = self.client.post("/api/v1/register",
                                    data=json.dumps(dict(first_name="evawer",
                                                         last_name="maina",
                                                         username="johnsonjj",
                                                         email="evajjohnson@gmail.com",
                                                         password="evaj")),
                                    content_type="application/json")
        response = self.client.post("/api/v1/login",
                                    data=json.dumps(dict(
                                        username_or_email="johnsonjj",
                                        password="eve")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 404)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Enter correct username or password",
                         response_msg["message"])

    

    def test_user_not_logged_in(self):
        """
        Test new user can login to the system.
        """
        response = self.client.post("/api/v1/logout",
                                    data=json.dumps(dict(
                                        username_or_email="maisha",
                                        password="me")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("User is not logged in, please login.",
                         response_msg["Message"])

    
    def test_user_already_logged_in(self):
        """
        Test user already logged in to the system.
        """
        response = self.client.post("/api/v1/register",
                                    data=json.dumps(dict(first_name="eveM",
                                                         last_name="maina",
                                                         username="evetM",
                                                         email="evetj@gmail.com",
                                                         password="evvt")),
                                    content_type="application/json")
        response = self.client.post("/api/v1/login",
                                    data=json.dumps(dict(
                                        username_or_email="evetM",
                                        password="evvt")),
                                    content_type="application/json")
        response = self.client.post("/api/v1/login",
                                    data=json.dumps(dict(
                                        username_or_email="evetM",
                                        password="evvt")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 409)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("User Already Logged in", response_msg["message"])
    
    def test_user_can_logout(self):
        """
        Test new user can logout.
        """
        response = self.client.post("/api/v1/register",
                                    data=json.dumps(dict(first_name="eva",
                                                         last_name="maina",
                                                         username="jeyson",
                                                         email="en@gmail.com",
                                                         password="evajj")),
                                    content_type="application/json")
        response = self.client.post("/api/v1/login",
                                    data=json.dumps(dict(
                                        username_or_email="jeyson",
                                        password="evajj")),
                                    content_type="application/json")

        response = self.client.post("/api/v1/logout",
                                    data=json.dumps(dict(
                                        username_or_email="jeyson",
                                        password="evajj")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 200)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("User logged out successfully",
                         response_msg["Message"])