#this function will read data from a file/source

class readdata:
    def __init__(self,data):
        self.data = data

    def readfile(self):
        count = 0
        nl = []
        try:
            with open(self.data, "r") as f:
                for lines in f:
                    if lines.strip():
                        regex = ("")
                        nl.append(regex)
        except FileNotFoundError:
            print("no file found")

        for i in regex:
            count+=1
            print(i)
        return count

ob = readdata("path")
op = ob.readfile()
print(op)


