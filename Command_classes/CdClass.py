
import os
import unittest
class cdClass:
    takeArg = True
    name = "cd"
    multiArg = False
    accept_zero = False

    def check_argument_allowness(self, arg):
        if self.takeArg and self.multiArg and len(arg) >= 1:
            return True
        elif self.takeArg and len(arg) == 1:
            return True
        elif self.accept_zero and len(arg) == 0:
            return True
        else:
            return False

    def exec(self, arg):
        if self.check_argument_allowness(arg):
            if arg[0] == "..":
                back = os.path.split(os.getcwd())[0]
                os.chdir(back)
                return os.path.basename(back)
            else:
                try:
                    os.chdir(arg[0])
                    new_directory = os.getcwd()
                    return os.path.basename(new_directory)
                except:
                    return "Path not exist"
        else:
            return "No arguments support"


class Test_cd(unittest.TestCase):
    def setUp(self):
        self.cd_test = cdClass()

    def test_no_arguments(self):
        result = self.cd_test.exec([])
        self.assertEqual(result, "No arguments support")
    def test_argument(self):
        test_cases = {".." : "File Manager",
                       "C:\\Users\\artur\\PycharmProjects":"PycharmProjects",
                       "C:\\Users\\artur\\PycharmProjects\\None":"Path not exist",}
        for test, argument in zip(test_cases.keys(), test_cases.values()):
            self.assertEqual(self.cd_test.exec([test]), argument)

    def test_multiArgument(self):
        result = self.cd_test.exec(["Hello", "World"])
        self.assertEqual(result, "No arguments support")



