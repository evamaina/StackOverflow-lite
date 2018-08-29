import unittest
import os
import json
from app.manage import drop_tables, create_tables
from app.app import create_app
from app.common.validation import *
from app.manage import conn, cur
from app.models.answers import Answer


class TestAnswerFunctinality(unittest.TestCase):
    """This class represents the Answer test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        
        self.app = create_app('testing')
        create_tables()
        self.client = self.app.test_client()

        self.answer = {"answer_body":"wertghdfggdggdg"
                     }

    def tearDown(self):
        drop_tables()

    def test_user_can_post_answer(self):
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
        response3 = self.client.post("/api/v2/questions/1/answers",
                                    data=json.dumps(self.answer),
                                    content_type="application/json",
                                    headers={'Authorization': 'Bearer ' + token})
        self.assertEqual(response3.status_code, 200)
        

    def test_post_answer_empty_body(self):
        """
        Tests user cannnot answer a question without body 
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
        response3 = self.client.post("/api/v2/questions/1/answers",
                                 data=json.dumps(dict(answer_body=" ")),
                                 content_type="application/json",
                                 headers={'Authorization': 'Bearer ' + token})
        self.assertEqual(response3.status_code, 400)
        
  
   
   

    def test_post_answer_with_id_that_does_not_exist(self):
        """
        Tests user cannnot answer a question that does not exist
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
       

        response4 = self.client.post("/api/v2/questions/5/answers",
                                 data=json.dumps(dict(answer_body=" ")),
                                 content_type="application/json",
                                 headers={'Authorization': 'Bearer ' + token})
        self.assertEqual(response4.status_code, 400)
        response_msg = json.loads(response.data.decode("UTF-8"))
       





 
