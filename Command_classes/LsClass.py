
import os
import unittest

class lsClass:
    takeArg = True
    name = "ls"
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

    #Take in argument object(x) , if object is file, then try get file size and name of file
    def createString(self, x: str, makeHumanR:bool) -> str:

        if os.path.isfile(x):
            return self.getSize_ExtraOption(x, makeHumanR)
        else:
            return f"{x}"

    #Get size and return human readable format
    def hummanReadableSize(self, size: int) -> str:
        if size < 1024:
            return f"{size}B"
        elif (size >= 1024) and (size < (1024**2)):
            return f"{int(round(size / 1024, 0))}KB"
        elif (size >= 1024**2) and (size < (1024**3)):
            return f"{int(round(size/(1024**2),0))}MB"
        else:
            return f"{int(round(size / (1024**3),0))}GB"

    #Get file size , normal mode, or human readable
    def getSize_ExtraOption(self, file:str, make_human_readable:bool) -> str:

        if make_human_readable:
            return f"{file} {self.hummanReadableSize(os.path.getsize(file))}"
        else:
            return f"{file} {os.path.getsize(file)}"

    def sortedListLS(self):
        dirList = os.listdir(os.getcwd())
        dirList.sort(key = os.path.isfile)
        return dirList

    def exec(self, argument = None):
        if self.check_argument_allowness(argument):
            if len(argument) == 0:
                output = str()
                directoryList = self.sortedListLS()
                for i in directoryList:
                    output = output +  f"{i}\n"
                return output[0:-1]


            elif argument[0] == "-l":
                output = str()
                directoryList = [self.createString(x, makeHumanR=False) for x in self.sortedListLS()]
                for i in directoryList:
                    output = output +  f"{i}\n"
                return output[0:-1]


            elif argument[0] == "-lh":
                output = str()
                directoryList = [self.createString(x, makeHumanR=True) for x in self.sortedListLS()]
                for i in directoryList:
                    output = output + f"{i}\n"
                return output[0:-1]
            else:
                return "Invalid command"
        else:
            return "Invalid command"
