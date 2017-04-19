class User:

    def __init__(self, name):
        self.name = name


class MyContext:
    def __init__(self, file, mode):
        self.file = file
        self.mode = mode

    def __enter__(self):
        try:
            self.f = open(self.file, self.mode)
        except Exception as e:
            print(e)
            return None
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        user = User("Dkuleshov")
        self.f.write("\nEdited by {}".format(user.name))
        self.f.close()

with MyContext('/tmp/context', 'a') as f:
    f.write("string")



