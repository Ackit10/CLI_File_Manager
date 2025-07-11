import unittest
import os

class mkDir:
    takeArg = True
    name = "mv"
    multiArg = False
    accept_zero = False




    def check_argument_allowness(self, arg):
        if self.takeArg and self.multiArg and len(arg) >= 1:
            print(arg)
            return True
        elif self.takeArg and len(arg) == 1:
            return True
        elif self.accept_zero and len(arg) == 0:
            return True
        else:
            return False

    def exec(self, argument):
        if self.check_argument_allowness(argument):
            try:
                os.mkdir(argument[0])
                return ""
            except FileExistsError:
                return "The directory already exists"
            except FileNotFoundError:
                return "Path not exist"

        else:
            return "Specify the name of the directory to be made"

class test_mkdir(unittest.TestCase):
    def setUp(self):
        self.mkdir_test = mkDir()

    def test_no_arguments(self):
        result = self.mkdir_test.exec([])
        self.assertEqual(result, "Specify the name of the directory to be made")

    def test_normal_arguments(self):
        self.mkdir_test.exec(["New_dir"])
        self.assertIn("New_dir", os.listdir(os.getcwd()))
        try:
            os.remove("New_dir")
        except:
            None

    def test_errors(self):
            os.mkdir("New_dir")
            result = self.mkdir_test.exec(["New_dir"])
            self.assertEqual(result, "The directory already exists")