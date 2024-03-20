import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
import os


class TestConsoleCreate(unittest.TestCase):
    def setUp(self):
        """Sets up test environment"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Tears down test environment"""
        del self.console

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_base(self, mock_stdout):
        """Tests object creation with basic parameters"""
        self.console.onecmd("create BaseModel")
        self.assertTrue(mock_stdout.getvalue().strip())
        self.assertIn("BaseModel", mock_stdout.getvalue())

        self.console.onecmd("create BaseModel id=\"345\" name=\"test\"")
        self.assertTrue(mock_stdout.getValue().strip())
        self.assertIn("BaseModel", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_quoted_params(self, mock_stdout):
        """Tests object creation with quoted parameters"""
        self.console.onecmd("create BaseModel")
        self.assertTrue(mock_stdout.getvalue().strip())
        self.assertIn("BaseModel", mock_stdout.getvalue())

        self.console.onecmd("create BaseModel "
                            "name=\"Another test\" "
                            "description=\"Test description\"")
        self.assertTrue(mock_stdout.getValue().strip())
        self.assertIn("BaseModel", mock_stdout.getvalue(i))

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_invalid_params(self, mock_stdout):
        """Tests object creation with invalid parameters"""
        self.console.oncmd("create BaseModel id=234")
        self.assertFalse(mock_stdout.getvalue().strip())

        self.console.onecmd("create BaseModel name\"Test\" invalid_param")
        self.assertFalse(mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_missing_class_name(self, mock_stdout):
        """Tests object creation with missng class name"""
        self.console.onecmd("create")
        self.assertIn(
                "** class name missing **", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_nonexistence_class(self, mock_stdout):
        """Tests object creation with nonexistent class"""
        self.console.onecmd("createInvalidClass name=\"Object\"")
        self.assertIn(
                "** class doesn't exist **", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_invalid_data_types(self, mock_stdout):
        """Tests object creation with invalid data types"""
        self.console.onecmd("create BaseModel name=\"Test\" id=\"invalid+is\"")
        self.assertFalse(mock_stdout.getvalue().strip())

        self.console.onecmd("create BaseModel name=\"Invalid Model\" "
                            "number_rooms==\"Two\"")
        self.assertFalse(mock_stdout.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
