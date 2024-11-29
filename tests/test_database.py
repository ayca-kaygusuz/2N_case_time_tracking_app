import unittest
from database import Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database(dbname='attendance_db', user='your_username', password='your_password')

    def test_execute(self):
        self.db.execute("CREATE TEMP TABLE test (id SERIAL PRIMARY KEY, name VARCHAR(50));")
        self.db.execute("INSERT INTO test (name) VALUES (%s);", ('Test',))
        result = self.db.fetchone("SELECT * FROM test;")
        self.assertEqual(result[1], 'Test')

    def tearDown(self):
        self.db.close()

if __name__ == '__main__':
    unittest.main()