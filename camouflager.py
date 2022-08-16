#I want to create a script that would allow me to camouflage a file 

#Useful libraries that I would be using
import os
import sys
from platform import system


#Declaring the various variables
class Meisaigakure:
    def __init__(self):
        self.os = system()

    #This function performs the hide function
    def hide(self, filePath):
        try:
            if self.os == "Windows":
                os.system(f"attrib +h {filePath}")
            elif self.os == "Darwin":
                os.system(f"chflags hidden {filePath}")
            else:
                #This should check for linux operations
                pass
            stat = "File camouflaged successfully"
        except Exception as e:
            stat = f"File not camouflaged successfully due to [{e}]"
        return stat

    #This function performs the unhide function
    def unhide(self, filePath):
        try:
            if self.os == "Windows":
                os.system(f"attrib -h {filePath}")
            elif self.os == "Darwin":
                os.system(f"chflags nohidden {filePath}")
            else:
                #This should check for linux operations
                pass
            stat = "File un-camouflaged successfully"
        except Exception as e:
            stat = f"File not un-camouflaged successfully due to [{e}]"
        return stat

    #This function handles the mode checking and implementation
    def mode(self, filePath, mode_):
        try:
            if os.path.exists(filePath):
                if mode_ == "hide":
                    stat = self.hide(filePath)
                elif mode_ == "unhide":
                    stat = self.unhide(filePath)
                else:
                    raise ValueError(f"{mode_} argument is invalid")
            else:
                raise FileNotFoundError(f"{filePath} is invalid")
        except Exception as e:
            stat = f"An error occurred in mode function due to [{e}]"
        return stat


if __name__ == "__main__":
    print("CAMOUFLAGER \n")

    filepath = r"_banner_.exe"
    mode_ = "unhide"
    stat = Meisaigakure().mode(filepath, mode_)
    print(f"Stat: {stat}")

    print("\nExecuted successfully!!")