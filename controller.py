from model import Model
from view import View

class Controller():
    def __init__(self):
        self.model = Model()
        self.view = View(self)
    
    def main(self):
        board_map = self.model.update_board()
        self.view.print_updated_board(board_map)
        while True:
            user_input = self.model.ask_input()
            self.view.confirm_input(user_input)
            board_map = self.model.update_board(user_input, "X")
            self.view.print_updated_board(board_map)
    
if __name__ == "__main__":
    app = Controller()
    app.main()