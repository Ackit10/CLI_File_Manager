import unittest
import os
import shutil

class mvClass:
    takeArg = True
    name = "mv"
    multiArg = True
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

    def exec(self,argument):
        if self.check_argument_allowness(argument):
            if len(argument) > 2:
                return "Invalid command"
            elif len(argument) == 2:
                try:
                    if self.detect_extension_option(argument):
                        if argument[1] == "..":
                            back_path = os.path.split(os.getcwd())[0]
                        else:
                            back_path = argument[1]
                        file_list = os.listdir(os.getcwd())
                        files_for_move = []
                        for file in file_list:
                            if argument[0] in os.path.splitext(file):
                                files_for_move.append(file)
                        if len(files_for_move) > 0:
                            dir_to_move = os.listdir(argument[1])
                            for file in files_for_move:
                                try:
                                    if file in dir_to_move:
                                        print(f"{file} already exists in this directory. Replace? (y/n)")
                                        answer = input()
                                        if answer == "y":
                                            os.remove(os.path.join(back_path, file))
                                            shutil.move(file, back_path)
                                        else:
                                            continue
                                    else:
                                        shutil.move(file, back_path)
                                except:
                                    return "Unknown error"


                            return ''
                        else:
                            return f"File extension  {argument[0]} not found in this directory"
                    elif os.path.exists(argument[1]):
                        if os.path.isfile(argument[1]):
                            return "The file or directory already exists"
                        elif os.path.isdir(argument[1]):
                            if argument[0] in os.listdir(argument[1]):
                                return "The file or directory already exists"
                            else:
                                shutil.move(argument[0], argument[1])
                                return '3'
                    elif len(os.path.dirname(argument[1])) > 0:
                        os.rename(argument[0], os.path.basename(argument[1]))
                        new_file_name = os.path.basename(argument[1])
                        shutil.move(new_file_name, os.path.dirname(argument[1]))
                        return '2'
                    else:
                        os.rename(argument[0], argument[1])
                        return '1'
                except FileNotFoundError:
                    return "No such file or directory"
                except FileExistsError:
                    return "The file or directory already exists"
            else:
                return "Specify the current name of the file or directory and the new location and/or name"

        else:
            return "Specify the current name of the file or directory and the new location and/or name"


class MV_TestCases(unittest.TestCase):
    def setUp(self):
        self.mv_test = mvClass()
        self.test_fileName = ["testFile.txt", "test_directory"]
        self.renamed_objects = ["changed.txt", "changed_directory"]
        self.not_exist = ["not_exist_file.txt", "not_exist_dir"]


    def test_no_arguments(self):
        result = self.mv_test.exec([])
        self.assertEqual(result, "Specify the current name of the file or directory and the new name")

    def test_normal_work(self):
        with open(self.test_fileName[0], "w") as file:
            file.write("Just testing, suppose to be name 'changed.txt'")
        os.mkdir("test_directory")
        for name,renamed in zip(self.test_fileName, self.renamed_objects):
            self.mv_test.exec([name,renamed])
            self.assertIn(renamed, os.listdir(os.getcwd()))
            self.assertNotIn(name, os.listdir(os.getcwd()))
        os.remove(self.renamed_objects[0])
        os.rmdir(self.renamed_objects[1])


    def test_not_exist_errors(self):
        for name,renamed in zip(self.not_exist, ["not_file.txt", "not_ex_dir2"]):
            result = self.mv_test.exec([name,renamed])
            self.assertEqual(result, "No such file or directory")

    def test_already_exist_error(self):
        os.mkdir("dir_to_rename")
        os.mkdir("already_exist_dir")
        file = open("already_exist.txt", "w")
        file.close()
        file = open("file_rename.txt", "w")
        file.close()

        for name, renamed in zip(["dir_to_rename","already_exist_dir"], ["file_rename.txt", "already_exist.txt"]):
            result = self.mv_test.exec([name, renamed])
            self.assertEqual(result,"The file or directory already exists" )

        os.rmdir("dir_to_rename")
        os.rmdir("already_exist_dir")
        os.remove("already_exist.txt")
        os.remove("file_rename.txt")





