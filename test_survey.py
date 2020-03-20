# import unittest
#
# from survey import AnonymousSurvey
#
# class TestAnonymosSurvey(unittest.TestCase):
#     def test_store_single_response(self):
#         question = "What's your favorite language ?"
#         my_survey = AnonymousSurvey(question)
#         my_survey.store_response("English")
#         self.assertIn('English', my_survey.responses)
#
#
#     def test_store_three_responses(self):
#         question = "What's your favorite language ?"
#         my_survey = AnonymousSurvey(question)
#         responses = ['English', 'Spanish', 'Mandarin']
#         for response in responses:
#             my_survey.store_response(response)
#             self.assertIn(response, my_survey.responses)
#
# unittest.main()

##---------------------------------------------setUp()-------------------------------------------------------

import unittest

from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):

    def setUp(self):
        question = "What's your favorite language? "
        self.my_survey = AnonymousSurvey(question)        ## my_car = Car('Tesla', 'model s', 2020)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_response(self):
        for response in self.responses:
            self.my_survey.store_response(response)
            self.assertIn(response, self.my_survey.responses)


unittest.main()
















