
import os
import unittest
class pwdClass:
    takeArg = False
    name = "pwd"
    multiArg = False
    accept_zero = True

    def check_argument_allowness(self, arg):
        if self.takeArg and self.multiArg and len(arg) >= 1:
            return True
        elif self.takeArg and len(arg) == 1:
            return True
        elif self.accept_zero and len(arg) == 0:
            return True
        else:
            return False

    def exec(self, arguments=None):
        if arguments is None:
            arguments = list()
        if self.check_argument_allowness(arguments):
            return str(os.getcwd())
        else:
            print(arguments)
            return "This command not support arguments"

class Test_pwd(unittest.TestCase):
    def setUp(self):
        self.pwd_test = pwdClass()

    def test_not_arguments(self):
        result = self.pwd_test.exec()
        self.assertEqual(result, "C:\\Users\\artur\\PycharmProjects\\File Manager\\File Manager\\task")
    def test_arguments(self):
        result = self.pwd_test.exec("tasks")
        self.assertEqual(result, "This command not support arguments")
