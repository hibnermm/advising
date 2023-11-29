from django.test import TestCase
from checklist.views import index
from .models import Program, ProgramCourses
from django.urls import reverse

# Create your tests here.


class TestProgramModel(TestCase):
    def setUp(self):
        self.program = Program(
            level_abbrev="bs",
            major="biology",
            major_abbrev="biol",
            specialization="",
            spec_abbrev="",
        )

    def test_create_program(self):
        self.assertIsNotNone(self.program, Program)

    def test_str_representation(self):
        self.assertEquals(str(self.program), "bs: biology")


class TestViews(TestCase):
    def test_index(self):
        url = reverse("index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


# py manage.py test
