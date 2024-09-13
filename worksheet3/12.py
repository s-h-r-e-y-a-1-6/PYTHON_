class StringManipulation:
    def __init__(self):
        self.input_string = ""

    def get_String(self):
        self.input_string = input("Enter a string: ")

    def print_String(self):
        print(self.input_string.upper())

s = StringManipulation()
s.get_String()
s.print_String()
