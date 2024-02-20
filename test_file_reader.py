import unittest
from unittest.mock import patch, mock_open
from io import StringIO
import file_reader


class FileReaderTest(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_reckless_file_reader_happy_path_(self, mock_stdout):
        test_cases = [
            (
                "my_awesome_file.txt",
                "IF YOU ARE SEEING THIS ON YOUR CONSOLE,\n"
                "THAT MEANS YOUR PROGRAM WORKED AS EXPECTED.\n"
                "WHY AM I YELLING???"
            )
        ]
        for file_path, expected in test_cases:
            with self.subTest(f"{file_path}"):
                file_reader.reckless_file_reader(file_path)
                actual = mock_stdout.getvalue()
                self.assertEqual(expected, actual)

    def test_reckless_file_reader_exception(self):
        test_cases = [
            ("locked_out_file.txt", PermissionError),
            ("file_that_does_not_exist.txt", FileNotFoundError)
        ]
        for file_path, expected in test_cases:
            with self.subTest(f"{file_path}"):
                with self.assertRaises(expected):
                    file_reader.reckless_file_reader(file_path)

    @unittest.skip("Useless test. This exists simply to trigger and demo the function under test.")
    def test_quick_way_to_get_fired(self):
        with self.assertRaises(PermissionError):
            file_reader.quick_way_to_get_fired("locked_out_file.txt")

    def test_single_exception_handling_reader_handled(self):
        with self.assertLogs() as cm:
            file_reader.single_exception_handling_reader("file_that_does_not_exist.txt")
            self.assertIn("No such file or directory: 'file_that_does_not_exist.txt'", cm.output[0])

    def test_single_exception_handling_reader_unhandled(self):
        with self.assertRaises(PermissionError):
            file_reader.single_exception_handling_reader("locked_out_file.txt")

    def test_multiple_exception_handling_reader(self):
        test_cases = [
            (
                "file_that_does_not_exist.txt",
                "No such file or directory: 'file_that_does_not_exist.txt'"
            ),
            (
                "locked_out_file.txt",
                "Permission denied: 'locked_out_file.txt'"
            )
        ]
        for file_path, message in test_cases:
            with self.subTest(f"{file_path} -> {message}"):
                with self.assertLogs() as cm:
                    file_reader.multiple_exception_handling_reader(file_path)
                    self.assertIn(message, cm.output[0])

    @patch('sys.stdout', new_callable=StringIO)
    def test_base_class_exception_handling_reader(self, mock_stdout):
        test_cases = [
            "locked_out_file.txt",
            "file_that_does_not_exist.txt"
        ]
        for file_path in test_cases:
            with self.subTest(f"{file_path}"):
                file_reader.base_class_exception_handling_reader(file_path)
                self.assertIn(
                    "Error opening the file. Please ensure the file exists and has appropriate permissions.",
                    mock_stdout.getvalue()
                )

    @patch('sys.stdout', new_callable=StringIO)
    def test_tuple_exception_handling_reader(self, mock_stdout):
        test_cases = [
            "locked_out_file.txt",
            "file_that_does_not_exist.txt"
        ]
        for file_path in test_cases:
            with self.subTest(f"{file_path}"):
                file_reader.tuple_exception_handling_reader(file_path)
                self.assertIn(
                    "Error opening the file. Please ensure the file exists and has appropriate permissions.",
                    mock_stdout.getvalue()
                )

    @patch('sys.stdout', new_callable=StringIO)
    def test_better_file_reader_known_exceptions(self, mock_stdout):
        test_cases = [
            "locked_out_file.txt",
            "file_that_does_not_exist.txt"
        ]
        for file_path in test_cases:
            with self.subTest(f"{file_path}"):
                file_reader.better_file_reader(file_path)
                self.assertIn(
                    "Error opening the file. Please ensure the file exists and has appropriate permissions.",
                    mock_stdout.getvalue()
                )

    def test_better_file_reader_known_happy_path(self):
        with patch('file_reader.process_file') as cm:
            file_reader.better_file_reader("my_awesome_file.txt")
        cm.assert_called_once()
