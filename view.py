class View():
    # Class Variables

    def __init__(self, controller):
        self.controller = controller
        
        self.board = ["#" for range in range(10)]
    
    def main(self):
        pass

    def print_updated_board(self, board_map):
        print(board_map)
    
    def confirm_input(self, user_input):
        if user_input == False:
            print("Please enter a number from 1-9, where a position has not been filled")
            return 0
        
        return 1
    
    def print_winner(self, result, letter):
        if result == True:
            print(f"Player {letter} wins!")
            return False
        
        return True