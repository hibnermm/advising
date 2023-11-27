from django.test import TestCase, unittest
from checklist.views import index
from .models import Program, ProgramCourses

# Create your tests here.

class TestProgramModel(TestCase):
  def setUp(self):
    self.program = Program(level_abbrev="bs", major="biology", major_abbrev="biol", specialization="", spec_abbrev="")
  def test_create_program(self):
    self.assertIsNotNone(self.program, Program)
  def test_str_representation(self):
    self.assertEquals(str(self.program), "bs: biology")
  




