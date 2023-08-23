import unittest
from unittest.mock import patch
from io import StringIO
import sys
from console import HBNBCommand

class TestConsoleCreateWithParams(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def run_console_command(self, command):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd(command)
            return mock_stdout.getvalue().strip()

    def test_create_state_with_params(self):
        command = 'create State name="California"'
        output = self.run_console_command(command)
        self.assertIn("d80e0344-63eb-434a-b1e0-07783522124e", output)

    def test_create_place_with_params(self):
        command = 'create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297'
        output = self.run_console_command(command)
        self.assertIn("76b65327-9e94-4632-b688-aaa22ab8a124", output)

if __name__ == '__main__':
    unittest.main()
