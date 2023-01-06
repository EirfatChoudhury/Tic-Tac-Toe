class View():
    # Class Variables

    def __init__(self, controller):
        self.controller = controller
        
        self.board = ["#" for range in range(10)]
    
    def main(self):
        pass

    def print_updated_board(self, board_map):
        if board_map == False:
            return print("Position already filled")
        
        return print(board_map, end="")
    
    def confirm_input(self, user_input):
        if user_input == False:
            print("Please enter a number from 1-9")