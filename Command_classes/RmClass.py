
import os
import unittest
import shutil

class rmClass:
    takeArg = True
    name = "rm"
    multiArg = False
    accept_zero = False

    def detect_extension_option(self, argument):
        if argument[0][0] == ".":
            return True
        else:
            return False

    def check_argument_allowness(self, arg):
        if self.takeArg and self.multiArg and len(arg) >= 1:
            return True
        elif self.takeArg and len(arg) == 1:
            return True
        elif self.accept_zero and len(arg) == 0:
            return True
        else:
            return False

    def exec(self, argument = None):
        if self.check_argument_allowness(argument):
            if self.detect_extension_option(argument):
                file_list = os.listdir(os.getcwd())
                files_for_move = []
                for file in file_list:
                    if argument[0] in os.path.splitext(file):
                        files_for_move.append(file)
                if len(files_for_move) > 0:
                    for file in files_for_move:
                        os.remove(file)
                    return ''
                else:
                    return f"File extension  {argument[0]} not found in this directory"
            elif os.path.isfile(argument[0]):
                os.remove(argument[0])
                return ""
            elif os.path.isdir(argument[0]):
                try:
                    os.rmdir(argument[0])
                    return ""
                except OSError:
                    shutil.rmtree(argument[0])
                    return ""
            else:
                return "No such file or directory"
        else:
            return "Specify the file or directory"

class rm_Test(unittest.TestCase):
    def setUp(self):
        self.rm_test = rmClass()


    def test_no_arguments(self):
        self.assertEqual(self.rm_test.exec([]), "Specify the file or directory")

    def test_argument(self):
        with open("TestFile.txt", "w") as file:
            file.write("If I'm exist, then it's not working")
        os.mkdir("C:\\Users\\artur\\PycharmProjects\\File Manager\\File Manager\\task\\Command_classes\\not_exist_dir")
        test_one = ["TestFile.txt", "not_exist_dir"]
        f_d_list = os.listdir("C:\\Users\\artur\\PycharmProjects\\File Manager\\File Manager\\task")
        for test in test_one:
            self.rm_test.exec([test])
            self.assertNotIn(test, f_d_list)

    def test_not_exist(self):
        test_f_d = ["dir1", "file.txt"]
        for test in test_f_d:
            self.assertEqual(self.rm_test.exec([test]), "No such file or directory")

    def test_multiArg(self):
        self.assertEqual(self.rm_test.exec(["one", "two"]), "Specify the file or directory")