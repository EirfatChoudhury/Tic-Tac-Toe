from model import Model
from view import View

class Controller():
    def __init__(self):
        self.model = Model()
        self.view = View(self)
    
    def main(self):
        self.view.main()
    
    def take_input(self, user_input):
        pass
    
if __name__ == "__main__":
    app = Controller()
    app.main()