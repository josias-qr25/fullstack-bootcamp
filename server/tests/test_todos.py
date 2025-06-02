import unittest
from app import create_app, db
from app.models.todo import Todo

class TodoTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
            # Add a sample todo
            todo = Todo(title="Buy milk", description="", completed=False)
            db.session.add(todo)
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_get_all_todos(self):
        response = self.client.get('/todos')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('todos', data)
        self.assertEqual(len(data['todos']), 1)
        self.assertEqual(data['todos'][0]['title'], "Buy milk")

if __name__ == '__main__':
    unittest.main()
