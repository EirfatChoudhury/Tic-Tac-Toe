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
            n = 0
            while n == 0:
                user_input = self.model.ask_input()
                n = self.view.confirm_input(user_input)
            board_map = self.model.update_board(user_input, "X")
            self.view.print_updated_board(board_map)

            result = self.model.check_winner("X")
            keep_playing = self.view.print_winner(result, "X")
            if keep_playing == False:
                self.model.restart_program()

            board_map = self.model.enemy_turn()
            self.view.print_updated_board(board_map)

            result = self.model.check_winner("O")
            keep_playing = self.view.print_winner(result, "O")
            if keep_playing == False:
                self.model.restart_program()
    
if __name__ == "__main__":
    app = Controller()
    app.main()