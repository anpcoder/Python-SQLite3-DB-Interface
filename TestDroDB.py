#!/usr/bin/python
__author__ = 'anonymous'

import unittest
from DroDB import DroDB


class TestDroDBFunctions(unittest.TestCase):

    def setUp(self, **kwargs):
        self.fn = ':memory:'         # in-memory database
        self.t = 'foo'               # table name

        self.recs = [                # records to be inserted
            dict(string='one'),
            dict(string='two'),
            dict(string='three')
        ]

    def test_create_db(self):
        db = DroDB(filename=self.fn, table=self.t)
        db.sql_do('DROP TABLE IF EXISTS {}'.format(self.t))
        db.sql_do('CREATE TABLE {} (id INTEGER PRIMARY KEY, string TEXT)'.format(self.t))
        return db

    def test_insert(self):
        db = self.test_create_db()
        for r in self.recs:
            self.assertTrue(db.insert(r))

    def test_read(self):
        db = self.test_create_db()
        for r in db.getrecs():
            self.assertTrue(r)

    def test_update(self):
        db = self.test_create_db()
        self.assertTrue(db.update(2, dict(string='TWO')))

    def test_delete(self):
        db = self.test_create_db()
        newid = db.insert(dict(string='extra'))
        self.assertTrue(db.getrec(newid))
        self.assertTrue(db.delete(newid))


if __name__ == "__main__": unittest.main()