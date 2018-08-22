import unittest
import os
import json
from app.app import db_connection
from app.app import create_app
from app.models.questions import Question


class TestQuestionFunctinality(unittest.TestCase):
    """This class represents the question test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        db_connection.create_tables()
        self.client = self.app.test_client()
        self.question = {"title": "No module found error",
                         "content": "What is the correct way to fix this ImportError error?"
                     }
    def tearDown(self):
        db.db_connection.drop_tables()

    def test_post_question_empty_content(self):
        """
        Tests user cannnot ask a question without body content
        """
        response = self.client.post("/api/v2/question",
                                 data=json.dumps(dict(title="how to delete git branch",
                                                      content="")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Content is required",
                      response_msg["Message"])

    def test_post_question_empty_title(self):
        """
        Tests user cannnot add a question without title
        """
        response = self.client.post("/api/v2/question",
                                 data=json.dumps(dict(title="",
                                                      content="I want to delete a branch both locally..")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Title is required",
                      response_msg["Message"])

    def test_user_can_fetch_all_questions(self):
        """
        Tests user can get all questions he/she has asked.
        """
        response = self.client.get("/api/v2/questions",
                                data=json.dumps(dict()),
                                content_type="application/json")
        self.assertEqual(response.status_code, 200)
        response_msg = json.loads(response.data.decode("UTF-8"))

    def test_user_can_get_one_question_by_id(self):
        """
        Tests a user can get a question by id.
        """
        response = self.client.post("/api/v2/signup",
                                    data=json.dumps(dict(first_name="joyce",
                                                         last_name="korir",
                                                         username="joykorry",
                                                         email="joy@gmail.com",
                                                         password="joy")),
                                    content_type="application/json")
        response = self.client.post("/api/v2/login",
                                    data=json.dumps(dict(
                                        username_or_email="joykorry",
                                        password="joy")),
                                    content_type="application/json")

        response = self.client.post("/api/v2/question",
                                 data=json.dumps(dict(
                                 title="test-title",
                                 content="test-content")),
                                 content_type="application/json")

        response = self.client.get("/api/v2/question/1",
                                 data=json.dumps(dict(question_id=1)),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 200)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Question found", response_msg["message"])
    
    def test_user_can_not_get_question_by_id_that_does_not_exist(self):
        response = self.client.get("/api/v2/question/5",
                                 data=json.dumps(dict(question_id=5)),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 404)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Question not found", response_msg["message"])

    def test_user_cant_ask_same_question_twice(self):
        response = self.client.post("/api/v2/signup",
                                    data=json.dumps(dict(first_name="joyce",
                                                         last_name="korir",
                                                         username="joykorry",
                                                         email="joy@gmail.com",
                                                         password="joy")),
                                    content_type="application/json")
        response = self.client.post("/api/v2/login",
                                    data=json.dumps(dict(
                                    username_or_email="joykorry",
                                    password="joy")),
                                    content_type="application/json")
        response = self.client.post("/api/v2/question",
                                    data=json.dumps(dict(
                                    title="import error bgfnhg",
                                    content="nbghtfrd jhgty")),
                                    content_type="application/json")
        response = self.client.post("/api/v2/question",
                                    data=json.dumps(dict(
                                    title="import error bgfnhg",
                                    content="nbghtfrd jhgty bgfvc")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 409)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Question already asked", response_msg["message"])


    def test_user_can_post_question(self):
        """
        Tests a user can post a question.
        """
        response = self.client.post("/api/v2/signup",
                                    data=json.dumps(dict(first_name="joyce",
                                                         last_name="korir",
                                                         username="joykorry",
                                                         email="joy@gmail.com",
                                                         password="joy")),
                                    content_type="application/json")

        response = self.client.post("/api/v2/login",
                                    data=json.dumps(dict(
                                        username_or_email="joykorry",
                                        password="joy")),
                                    content_type="application/json")

        response = self.client.post("/api/v2/question",
                                 data=json.dumps(dict(title="sdgetr git branch",
                                                      content="asdgfh ndgts")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Question posted", response_msg["Message"])

    def test_user_must_login_to_post_question(self):
        response = self.client.post("/api/v2/signup",
                                    data=json.dumps(dict(first_name="joyce",
                                                         last_name="korir",
                                                         username="joykorry",
                                                         email="joy@gmail.com",
                                                         password="joy")),
                                    content_type="application/json")
        
        response = self.client.post("/api/v2/question",
                                 data=json.dumps(dict(
                                 title="tesyhgt",
                                 content="nbghtfrd jhgty")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 400)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Login to post a question", response_msg["message"])