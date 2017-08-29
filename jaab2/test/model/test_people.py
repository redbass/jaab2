from jaab2.model import people

from unittest import TestCase


class TestPeople(TestCase):

    def setUp(self):
        pass

    def test_create_person(self):
        last_name = "Gallici"
        first_name = "Luca"

        person = people.create_person(first_name, last_name)

        self.assertEquals(person['first_name'], first_name)
        self.assertEquals(person['last_name'], last_name)
