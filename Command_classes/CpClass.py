import os.path
import shutil

class cpClass:
    takeArg = True
    name = "cp"
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
        elif self.accept_zero and len(arg) == 0:
            return True
        else:
            return False

    def exec(self, arguments):
        if self.check_argument_allowness(arguments):
            if len(arguments) == 2:
                try:
                    if self.detect_extension_option(arguments):
                        if arguments[1] == "..":
                            back_path = os.path.split(os.getcwd())[0]
                        else:
                            back_path = arguments[1]
                        if self.detect_extension_option(arguments):
                            file_list = os.listdir(os.getcwd())
                            files_for_move = []
                            for file in file_list:
                                if arguments[0] in os.path.splitext(file):
                                    files_for_move.append(file)
                            if len(files_for_move) > 0:
                                dir_to_move = os.listdir(arguments[1])
                                for file in files_for_move:
                                    try:
                                        if file in dir_to_move:
                                            print(f"{file} already exists in this directory. Replace? (y/n)")
                                            answer = input()
                                            if answer == "y":
                                                os.remove(os.path.join(back_path, file))
                                                shutil.copy(file, back_path)
                                            else:
                                                continue
                                        else:
                                            shutil.copy(file, back_path)
                                    except:
                                        return "Unknown error"

                                return ''
                            else:
                                return f"File extension  {arguments[0]} not found in this directory"
                    elif arguments[1] == "..":
                        back = os.path.split(os.getcwd())[0]
                        shutil.copy(arguments[0], back)
                        return ''
                    else:
                        shutil.copy(arguments[0], arguments[1])
                except FileNotFoundError:
                    return "No such file or directory"
                except FileExistsError:
                    return f"{os.path.basename(arguments[0])} already exists in this directory"
                except shutil.SameFileError:
                    return f"{os.path.basename(arguments[0])} already exists in this directory"
            elif len(arguments) == 1:
                return "Specify the current name of the file or directory and the new location and/or name"
            else:
                return "Specify the current name of the file or directory and the new location and/or name"
        else:
            return "Specify the file"