import os
import random
import unittest
import json

from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category

load_dotenv()


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = os.environ['TEST_DATABASE_PATH']
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_question = {
            'question': 'What is the capital of Kenya?',
            'answer': 'Nairobi',
            'category': 1,
            'difficulty': 1,

        }

        # self.categories = {}
        # self.categories_query = Category.query.all()
        # for category in self.categories_query:
        #     self.categories['quiz_category'] = {
        #         'type': category.type,
        #         'id': str(category.id)
        #     }

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    # success - get paginated questions
    def test_get_paginated_questions(self):
        res = self.client().get('/questions')
        print(res)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data))

    # failure - get paginated questions
    def test_404_sent_requesting_beyond_valid_page(self):
        res = self.client().get('/questions?page=1000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'resource not found')

    # success - create new question
    def test_create_new_question(self):
        res = self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['success'], True)

    # failure - create question
    def test_for_question_not_created(self):
        res = self.client().post('/questions')
        print(res)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    # success - delete question
    def test_delete_question(self):
        # create a question
        res = self.client().post('/questions', json=self.new_question)
        # get id of created question
        new_id = res.get_json()['question']['id']

        del_res = self.client().delete(f'/questions/{new_id}')
        data = del_res.get_json()

        self.assertEqual(del_res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['id'], new_id)

    # failure - delete question
    def test_404_if_question_does_not_exist(self):
        res = self.client().delete('/questions/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    # success - get search-term
    def test_get_question_search_with_results(self):
        res = self.client().post('/questions/search', json={'searchTerm': 'capital'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])

    # failure - get search-term
    def test_get_question_search_without_results(self):
        res = self.client().post('/questions/search', json={'searchTerm': 'amala'})
        data = json.loads(res.data)
        print(data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['total_questions'], 0)
        self.assertEqual(len(data['questions']), 0)

    # success - post quizzes
    def test_get_quizzes(self):
        self.new_quiz = {
            'previous_questions': [],
            'quiz_category': {'type': 'Science', 'id': '1'}
        }
        res = self.client().post('/quizzes', json=self.new_quiz)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # success - get questions by category
    def test_get_questions_by_category(self):
        result = self.client().get('categories/1/questions')
        print(result.data)
        # checks
        # checks status and questions in returned obj
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.get_json()['success'], True)
        self.assertIn("questions", result.get_json())

    # failure - get questions by category
    def test_get_questions_by_category_error(self):
        result = self.client().get('/categories/8100/questions')
        # checks
        # checks searching by category that doesn't exist
        self.assertEqual(result.status_code, 404)
        self.assertEqual(result.get_json()['success'], False)
        self.assertIn("message", result.get_json())
        self.assertEqual(result.get_json()['message'], "resource not found")


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
