import unittest
from app import app
import json
import flask
import os


class TestBase(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()
        self.app.post('/add_task_sheet', data={
            "task_sheet_name": (os.path.dirname(os.path.abspath(__file__)) + '/test_samples/test.json', 'mock_name')
        }, content_type='multipart/form-data')

    def extract_app_json(self):
        return json.loads(self.app.get('/get_task_sheet').data)

    def test_add_sheet(self):
        self.check_json('test.json')

    def check_json(self, exp_json_name):
        resp_json = self.extract_app_json()
        with open("test_samples/{}".format(exp_json_name)) as exp_file:
            exp_json = json.load(exp_file)
            self.assertEqual(resp_json, exp_json)

    def add_tasks(self):
        self.app.post('/add_task', data={
            "task_complexity": 0,
            "task_date": "2020-05-01",
            "task_info": "mock1_text",
            "task_name": "mock1"
        })
        self.app.post('/add_task', data={
            "task_complexity": 1,
            "task_date": "2020-05-02",
            "task_info": "mock2_text",
            "task_name": "mock2",
        })
        self.app.post('/add_task', data={
            "task_complexity": 9,
            "task_date": "2020-05-03",
            "task_info": "mock3_text",
            "task_name": "mock3",
        })
        self.app.post('/add_task', data={
            "task_complexity": 9,
            "task_date": "2020-05-04",
            "task_info": "mock4_text",
            "task_name": "mock4",
        })

    def test_add_tasks(self):
        self.add_tasks()
        self.check_json('test_after_adding.json')

    def move_tasks(self):
        for j in range(4, 7):
            for i in range(j, 7):  # look at tests
                self.app.post('/move_right/{}'.format(i))

    def test_move_tasks(self):
        self.add_tasks()
        self.move_tasks()
        self.check_json('test_after_moving.json')
