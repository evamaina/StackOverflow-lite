import unittest
import os
import json
from app.manage import conn, cur
from app.manage import drop_tables, create_tables
from app.app import create_app
from app.common.validation import *
from app.models.questions import Question


class TestQuestionFunctinality(unittest.TestCase):
    """This class represents the question test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app("testing")
        create_tables()
        self.client = self.app.test_client()

    def tearDown(self):
        drop_tables()

    def test_user_can_post_question(self):
        """
        Tests a user can post a question.
        """
        response = self.client.post("/api/v2/signup",
                                    data=json.dumps(dict(first_name="Evet",
                                                         last_name="maina",
                                                         username="eve",
                                                         email="ev@gkjklmail.com",
                                                         password="evaj",
                                                         confirm_password="evaj")),
                                    content_type="application/json")
        response1 = self.client.post("/api/v2/login",
                                     data=json.dumps(dict(
                                         username="eve",
                                         password="evaj")),
                                     content_type="application/json",)

        decoded_response = json.loads(response1.data.decode("UTF-8"))

        token = decoded_response['token']

        response2 = self.client.post("/api/v2/question",
                                     data=json.dumps(dict(title="sdgetr git branch bvfg",
                                                          content="asdgfh ndgts nbv")),
                                     content_type="application/json",
                                     headers={'Authorization': 'Bearer ' + token})
        
        self.assertEqual(response2.status_code, 201)

    def test_post_question_empty_content(self):
        """
        Tests user cannnot ask a question without body content
        """
        response = self.client.post("/api/v2/signup",
                                    data=json.dumps(dict(first_name="Evet",
                                                         last_name="maina",
                                                         username="eve",
                                                         email="ev@gkjklmail.com",
                                                         password="evaj",
                                                         confirm_password="evaj")),
                                    content_type="application/json")
        response1 = self.client.post("/api/v2/login",
                                     data=json.dumps(dict(
                                         username="eve",
                                         password="evaj")),
                                     content_type="application/json",)

        decoded_response = json.loads(response1.data.decode('UTF-8'))

        token = decoded_response['token']

        response3 = self.client.post("/api/v2/question",
                                     data=json.dumps(dict(title="how to delete git branch",
                                                          content="")),
                                     content_type="application/json",
                                     headers={'Authorization': 'Bearer ' + token})
        self.assertEqual(response3.status_code, 400)
        response_msg = json.loads(response3.data.decode("UTF-8"))
        self.assertEqual("Content is required",
                         response_msg["Message"])

    def test_post_question_empty_title(self):
        """
        Tests user cannnot ask a question without body content
        """

        response = self.client.post("/api/v2/signup",
                                    data=json.dumps(dict(first_name="Evet",
                                                         last_name="maina",
                                                         username="eve",
                                                         email="ev@gkjklmail.com",
                                                         password="evaj",
                                                         confirm_password="evaj")),
                                    content_type="application/json")
        response1 = self.client.post("/api/v2/login",
                                     data=json.dumps(dict(
                                         username="eve",
                                         password="evaj")),
                                     content_type="application/json",)

        decoded_response = json.loads(response1.data.decode('UTF-8'))

        token = decoded_response['token']

        response3 = self.client.post("/api/v2/question",
                                     data=json.dumps(dict(title="",
                                                          content="wthe uyt")),
                                     content_type="application/json",
                                     headers={'Authorization': 'Bearer ' + token})
        self.assertEqual(response3.status_code, 400)
        response_msg = json.loads(response3.data.decode("UTF-8"))
        self.assertEqual("Title is required",
                         response_msg["Message"])

    def test_user_can_fetch_all_questions(self):
        """
        Tests user can get all questions he/she has asked.
        """
        response = self.client.post("/api/v2/signup",
                                    data=json.dumps(dict(first_name="Evet",
                                                         last_name="maina",
                                                         username="eve",
                                                         email="ev@gkjklmail.com",
                                                         password="evaj",
                                                         confirm_password="evaj")),
                                    content_type="application/json")
        response1 = self.client.post("/api/v2/login",
                                     data=json.dumps(dict(
                                         username="eve",
                                         password="evaj")),
                                     content_type="application/json",)

        decoded_response = json.loads(response1.data.decode("UTF-8"))

        token = decoded_response['token']

        response2 = self.client.post("/api/v2/question",
                                     data=json.dumps(dict(title="sdgetr git branch bvfg",
                                                          content="asdgfh ndgts nbv")),
                                     content_type="application/json",
                                     headers={'Authorization': 'Bearer ' + token})
        response3 = self.client.get("/api/v2/questions",
                                    data=json.dumps(dict()),
                                    content_type="application/json")
        self.assertEqual(response3.status_code, 200)
        response_msg = json.loads(response.data.decode("UTF-8"))

    def test_user_can_get_one_question_by_id(self):
        """
        Tests a user can get a question by id.
        """
        response = self.client.post("/api/v2/signup",
                                    data=json.dumps(dict(first_name="Evet",
                                                         last_name="maina",
                                                         username="eve",
                                                         email="ev@gkjklmail.com",
                                                         password="evaj",
                                                         confirm_password="evaj")),
                                    content_type="application/json")
        response1 = self.client.post("/api/v2/login",
                                     data=json.dumps(dict(
                                         username="eve",
                                         password="evaj")),
                                     content_type="application/json",)

        decoded_response = json.loads(response1.data.decode("UTF-8"))

        token = decoded_response['token']

        response2 = self.client.post("/api/v2/question",
                                     data=json.dumps(dict(title="sdgetr git branch bvfg",
                                                          content="asdgfh ndgts nbv")),
                                     content_type="application/json",
                                     headers={'Authorization': 'Bearer ' + token})

        response = self.client.get("/api/v2/question/1",
                                   data=json.dumps(dict(question_id=1)),
                                   content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_user_can_not_get_question_by_id_that_does_not_exist(self):

        response = self.client.get("/api/v2/question/5",
                                   data=json.dumps(dict(question_id=5)),
                                   content_type="application/json")
        self.assertEqual(response.status_code, 404)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("No question found", response_msg["Message"])

    def test_user_cant_ask_same_question_twice(self):
        response = self.client.post("/api/v2/signup",
                                    data=json.dumps(dict(first_name="Evet",
                                                         last_name="maina",
                                                         username="eve",
                                                         email="ev@gkjklmail.com",
                                                         password="evaj",
                                                         confirm_password="evaj")),
                                    content_type="application/json")
        response1 = self.client.post("/api/v2/login",
                                     data=json.dumps(dict(
                                         username="eve",
                                         password="evaj")),
                                     content_type="application/json",)

        decoded_response = json.loads(response1.data.decode())

        token = decoded_response['token']

        response2 = self.client.post("/api/v2/question",
                                     data=json.dumps(dict(
                                         title="import error bgfnhg",
                                         content="nbghtfrd jhgty")),
                                     content_type="application/json",
                                     headers={'Authorization': 'Bearer ' + token})
        response3 = self.client.post("/api/v2/question",
                                     data=json.dumps(dict(
                                         title="import error bgfnhg",
                                         content="nbghtfrd jhgty bgfvc")),
                                     content_type="application/json",
                                     headers={'Authorization': 'Bearer ' + token})
        self.assertEqual(response3.status_code, 409)

    def test_question_can_be_deleted(self):
        """
        Test a user can delete a question from the system.
        """
        response = self.client.post("/api/v2/signup",
                                    data=json.dumps(dict(first_name="Evet",
                                                         last_name="maina",
                                                         username="eve",
                                                         email="ev@gkjklmail.com",
                                                         password="evaj",
                                                         confirm_password="evaj")),
                                    content_type="application/json")
        response1 = self.client.post("/api/v2/login",
                                     data=json.dumps(dict(
                                         username="eve",
                                         password="evaj")),
                                     content_type="application/json",)

        decoded_response = json.loads(response1.data.decode("UTF-8"))

        token = decoded_response['token']

        self.client.post("/api/v2/question",
                         data=json.dumps(dict(title="hdfgstt bdgrts",
                                              content="bcgdtrt ndgtsrt")),
                         content_type="application/json",
                         headers={'Authorization': 'Bearer ' + token})
        response3 = self.client.delete("/api/v2/question/1",
                                       data=json.dumps(dict(question_id=1)),
                                       content_type="application/json",
                                       headers={'Authorization': 'Bearer ' + token})
        self.assertEqual(response3.status_code, 200)
