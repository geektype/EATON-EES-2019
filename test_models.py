import unittest
from models import create_connection, storeReadings
import datetime

class TestDatabase(unittest.TestCase):
    def setUp(self):
        try:
            self.db_conn, self.cursor = create_connection("remotemysql.com", "VUqnoHhiHe", "DyOeYyDKHw", "VUqnoHhiHe")
        
        except Exception as e:
            print(e)
            self.fail("Failed to connect to test database")
    # def test_test_database_empty(self):
    #     self.cursor.execute("SELECT * FROM test;")
        
    #     self.result = []
    #     for row in self.cursor:
    #         self.result.append(row)
    #     self.assertEquals(self.result, [], "test database should be empty")

    def test_insert_reading(self):
        self.time = '2019-01-01 00:00:00'
        self.reading = [['ldr1', '434'], ['ldr2', '361']]
        storeReadings(self.reading, self.cursor, time=self.time)
        self.db_conn.commit()


        self.cursor.execute("SELECT name, value, time FROM test")
        self.result = []
        for row in self.cursor:
            self.result.append(row)

        self.expected = [('ldr1', 434.0, datetime.datetime(2019, 1, 1, 0, 0)), ('ldr2', 361.0, datetime.datetime(2019, 1, 1, 0, 0))]
        self.cursor.execute("DELETE FROM test WHERE UID > 1")
        self.db_conn.commit()
        self.assertEquals(self.result, self.expected, "wrong or no entry")

        

