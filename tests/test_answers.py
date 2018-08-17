import unittest
import os
import json
from app.app import create_app
from app.models.questions import Question


class TestAnswerFunctinality(unittest.TestCase):
    """This class represents the Answer test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.question = {"title": "No module found error",
                         "content": "What is the correct way to fix this ImportError error?"
                     }
        self.answer = {"question_id": "1",
                       "username": "evet",
                       "answer_body":"wertghdfggdggdg",
                     }
    def test_user_can_post_answer(self):
        """
        Tests a user can post a question.
        """
        response = self.client.post("/api/v1/register",
                                    data=json.dumps(dict(first_name="jyce",
                                                         last_name="krir",
                                                         username="jkorry",
                                                         email="jy@gmal.com",
                                                         password="jy")),
                                    content_type="application/json")

        response = self.client.post("/api/v1/login",
                                    data=json.dumps(dict(
                                        username_or_email="jkorry",
                                        password="jy")),
                                    content_type="application/json")

        response = self.client.post("/api/v1/question",
                                    data=json.dumps(self.question),
                                    content_type="application/json")
        response = self.client.post("/api/v1/answer/1",
                                    data=json.dumps(self.answer),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 200)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Answer added successfully", response_msg["Message"])

    def test_post_answer_empty_body(self):
        """
        Tests user cannnot answer a question without body 
        """
        response = self.client.post("/api/v1/answer/1",
                                 data=json.dumps(dict(question_id="1",
                                                      username="evet",
                                                      answer_body=" ")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Answer body is required",
                      response_msg["Message"])

    def test_post_answer_blank_username(self):
        """
        Tests user cannnot answer a question without body 
        """
        response = self.client.post("/api/v1/answer/1",
                                 data=json.dumps(dict(question_id="1",
                                                      username="",
                                                      answer_body="wertghdfggdggdg")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Username is required",
                      response_msg["Message"]) 

    def test_post_answer_empty_questionId(self):
        """
        Tests user cannnot answer a question with wrong question id 
        """

        response = self.client.post("/api/v1/answer/1",
                                 data=json.dumps(dict(question_id="",
                                                      username="evet",
                                                      answer_body="wertghdfggdggdg")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Question id is required",
                      response_msg["Message"])                   

    def test_post_answer_incorrect_questionId(self):
        """
        Tests user cannnot answer a question without body 
        """
        response = self.client.post("/api/v1/answer/1",
                                 data=json.dumps(dict(question_id="2",
                                                      username="evet",
                                                      answer_body="wertghdfggdggdg")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 409)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Enter correct id",
                      response_msg["Message"])

    def test_post_answer_with_id_that_does_not_exist(self):
        """
        Tests user cannnot answer a question that does not exist
        """
        response = self.client.post("/api/v1/register",
                                    data=json.dumps(dict(first_name="jyce",
                                                         last_name="krir",
                                                         username="jkorry",
                                                         email="jy@gmal.com",
                                                         password="jy")),
                                    content_type="application/json")

        response = self.client.post("/api/v1/login",
                                    data=json.dumps(dict(
                                        username_or_email="jkorry",
                                        password="jy")),
                                    content_type="application/json")

        response = self.client.post("/api/v1/question",
                                    data=json.dumps(self.question),
                                    content_type="application/json")

        response = self.client.post("/api/v1/answer/5",
                                 data=json.dumps(dict(question_id="5",
                                                      username="evet",
                                                      answer_body="wertghdfggdggdg")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 404)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Question with that id not found",
                      response_msg["Message"])

    def test_user_must_login_to_answer_question(self):
    	response = self.client.post("/api/v1/answer",
                                 data=json.dumps(dict(
                                 title="tesyhgt bgcv",
                                 content="nbghtfrd jhgty bgfv")),
                                 content_type="application/json")
    	self.assertEqual(response.status_code, 400)
    	response_msg = json.loads(response.data.decode("UTF-8"))
    	self.assertIn("Login to post a answer", response_msg["message"])
   