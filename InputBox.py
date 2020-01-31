class InputBox:
    def __init__(self, name, web_element):
        self.name = name
        self.web_element = web_element

    def get_name(self):
        return self.name

    def get_web_element(self):
        return self.web_element
