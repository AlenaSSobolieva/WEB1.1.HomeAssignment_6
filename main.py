import sqlite3
import unittest
from faker import Faker
import random

fake = Faker()


def create_tables(conn, cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Student (
            student_id INTEGER PRIMARY KEY,
            name TEXT,
            group_id INTEGER,
            CONSTRAINT fk_group FOREIGN KEY (group_id) REFERENCES "Group"(group_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "Group" (
            group_id INTEGER PRIMARY KEY,
            name TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Teacher (
            teacher_id INTEGER PRIMARY KEY,
            name TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Subject (
            subject_id INTEGER PRIMARY KEY,
            name TEXT,
            teacher_id INTEGER,
            CONSTRAINT fk_teacher FOREIGN KEY (teacher_id) REFERENCES Teacher(teacher_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Grade (
            grade_id INTEGER PRIMARY KEY,
            student_id INTEGER,
            subject_id INTEGER,
            score INTEGER,
            date_received DATE,
            CONSTRAINT fk_student FOREIGN KEY (student_id) REFERENCES Student(student_id),
            CONSTRAINT fk_subject FOREIGN KEY (subject_id) REFERENCES Subject(subject_id)
        )
    ''')


def populate_database(conn, cursor):
    num_students = 50
    num_groups = 3
    num_subjects = 8
    num_teachers = 5
    num_grades_per_student = 20

    for i in range(1, num_groups + 1):
        while True:
            group_id = random.randint(1, num_groups)
            cursor.execute('SELECT group_id FROM "Group" WHERE group_id = ?', (group_id,))
            if not cursor.fetchone():
                break

        cursor.execute('INSERT INTO "Group" (group_id, name) VALUES (?, ?)', (group_id, fake.word()))

    for i in range(1, num_teachers + 1):
        cursor.execute('INSERT INTO Teacher (teacher_id, name) VALUES (?, ?)', (i, fake.name()))

    for i in range(1, num_subjects + 1):
        teacher_id = random.randint(1, num_teachers)
        cursor.execute('INSERT INTO Subject (subject_id, name, teacher_id) VALUES (?, ?, ?)', (i, fake.word(), teacher_id))

    for i in range(1, num_students + 1):
        group_id = random.randint(1, num_groups)
        cursor.execute('INSERT INTO Student (student_id, name, group_id) VALUES (?, ?, ?)', (i, fake.name(), group_id))

    for i in range(1, num_grades_per_student + 1):
        student_id = random.randint(1, num_students)
        subject_id = random.randint(1, num_subjects)
        score = random.randint(50, 100)
        date_received = fake.date_this_decade()
        cursor.execute('INSERT INTO Grade (student_id, subject_id, score, date_received) VALUES (?, ?, ?, ?)',
                       (student_id, subject_id, score, date_received))

    conn.commit()


class TestDatabasePopulation(unittest.TestCase):

    def setUp(self):
        self.fake = Faker()
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        create_tables(self.conn, self.cursor)

    def tearDown(self):
        self.conn.close()

    def test_populate_database(self):
        populate_database(self.conn, self.cursor)

        self.assertGreater(self.count_records('Student'), 0)
        self.assertGreater(self.count_records('Group'), 0)
        self.assertGreater(self.count_records('Teacher'), 0)
        self.assertGreater(self.count_records('Subject'), 0)
        self.assertGreater(self.count_records('Grade'), 0)

    def count_records(self, table):
        self.cursor.execute(f'SELECT COUNT(*) FROM "{table}"')
        return self.cursor.fetchone()[0]


if __name__ == '__main__':
    unittest.main()

