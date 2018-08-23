# import unittest
# import os
# import json
# from app.app import db_connection
# from app.app import create_app
# from app.models.answers import Answer


# class TestAnswerFunctinality(unittest.TestCase):
#     """This class represents the Answer test case"""

#     def setUp(self):
#         """Define test variables and initialize app."""
#         self.app = create_app(config_name="testing")
#         db_connection.create_tables()
#         self.client = self.app.test_client()
#         self.question = {"title": "No module found error",
#                          "content": "What is the correct way to fix this ImportError error?"
#                      }
#         self.answer = {"answer_body":"wertghdfggdggdg"
#                      }
#     def tearDown(self):
#       db.db_connection.drop_tables()


#     def test_user_can_post_answer(self):
#         """
#         Tests a user can post a question.
#         """
#         response = self.client.post("/api/v2/signup",
#                                     data=json.dumps(dict(first_name="jyce",
#                                                          last_name="krir",
#                                                          username="jkorry",
#                                                          email="jy@gmal.com",
#                                                          password="jy")),
#                                     content_type="application/json")

#         response = self.client.post("/api/v2/login",
#                                     data=json.dumps(dict(
#                                         username_or_email="jkorry",
#                                         password="jy")),
#                                     content_type="application/json")

#         response = self.client.post("/api/v2/question",
#                                     data=json.dumps(self.question),
#                                     content_type="application/json")
#         response = self.client.post("/api/v2/questions/1/answers",
#                                     data=json.dumps(self.answer),
#                                     content_type="application/json")
#         self.assertEqual(response.status_code, 200)
#         response_msg = json.loads(response.data.decode("UTF-8"))
#         self.assertEqual("Answer added successfully", response_msg["Message"])

#     def test_post_answer_empty_body(self):
#         """
#         Tests user cannnot answer a question without body 
#         """
#         response = self.client.post("/api/v2/questions/1/answers",
#                                  data=json.dumps(dict(answer_body=" ")),
#                                  content_type="application/json")
#         self.assertEqual(response.status_code, 401)
#         response_msg = json.loads(response.data.decode("UTF-8"))
#         self.assertEqual("Answer body is required",
#                       response_msg["Message"])

  
#     def test_user_can_fetch_all_answers(self):
#         """
#         Tests user can get all answers for a partiular question.
#         """
#         response = self.client.get("/api/v2/questions/1/answers",
#                                 data=json.dumps(dict()),
#                                 content_type="application/json")
#         self.assertEqual(response.status_code, 200)
#         response_msg = json.loads(response.data.decode("UTF-8"))

    

#     def test_user_must_login_to_answer_question(self):
#         response = self.client.post("/api/v2/signup",
#                                     data=json.dumps(dict(first_name="jyce",
#                                                          last_name="krir",
#                                                          username="jkorry",
#                                                          email="jy@gmal.com",
#                                                          password="jy")),
#                                     content_type="application/json")

#         response = self.client.post("/api/v2/question",
#                                     data=json.dumps(dict(title="abdg gahs",
#                                     content = "wsertd vdfer")),
#                                     content_type="application/json")
#         response = self.client.post("/api/v2/questions/1/answers",
#                                     data=json.dumps(self.answer),
#                                     content_type="application/json")
#         self.assertEqual(response.status_code, 400)
#         response_msg = json.loads(response.data.decode("UTF-8"))
#         self.assertEqual("Login to post answer", response_msg["message"])

#     def test_user_must_be_registered_to_answer_question(self):
        
#         response = self.client.post("/api/v2/questions/1/answers",
#                                     data=json.dumps(self.answer),
#                                     content_type="application/json")
#         self.assertEqual(response.status_code, 400)
#         response_msg = json.loads(response.data.decode("UTF-8"))
#         self.assertIn("User does not exist", response_msg["message"])
   
   

#     def test_post_answer_with_id_that_does_not_exist(self):
#         """
#         Tests user cannnot answer a question that does not exist
#         """
#         response = self.client.post("/api/v2/signup",
#                                     data=json.dumps(dict(first_name="jyce",
#                                                          last_name="krir",
#                                                          username="jkorry",
#                                                          email="jy@gmal.com",
#                                                          password="jy")),
#                                     content_type="application/json")

#         response = self.client.post("/api/v2/login",
#                                     data=json.dumps(dict(
#                                         username_or_email="jkorry",
#                                         password="jy")),
#                                     content_type="application/json")

#         response = self.client.post("/api/v2/question",
#                                     data=json.dumps(self.question),
#                                     content_type="application/json")

#         response = self.client.post("/api/2/questions/5/answers",
#                                  data=json.dumps(dict(question_id="5",
#                                                       username="evet",
#                                                       answer_body="wertghdfggdggdg")),
#                                  content_type="application/json")
#         self.assertEqual(response.status_code, 404)
#         response_msg = json.loads(response.data.decode("UTF-8"))
#         self.assertEqual("Question with that id not found",
#                       response_msg["Message"])
