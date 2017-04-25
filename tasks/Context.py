class User:

    def __init__(self, name):
        self.name = name


class MyContext:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode

    def __enter__(self):
        try:
            self.f = open(self.file_path, self.mode)
        except IOError as e:
            self.__exit__(e)
        return self.f

    def __exit__(self, *args):
        if args[0]:
            raise args[0]
        user = User("Dkuleshov")
        self.f.write("\nEdited by {}".format(user.name))
        self.f.close()

with MyContext('/tmp/context', 'a') as f:
    f.write("string")
