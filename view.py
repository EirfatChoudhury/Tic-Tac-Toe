class View():
    # Class Variables

    def __init__(self, controller):
        self.controller = controller
        
        self.board = ["#" for range in range(10)]
    
    def main(self):
        self._update_board()
        self._ask_input()
    
    def _update_board(self, changed_index=0, letter=" "):
        if self.board[changed_index] in ["O", "X"]:
            print("Position already filled")
            return self._ask_input()
        
        row = 1
        board_map = []
        index = 1
        break_count_horizontal = 1
        while row < 4:
            column = 1
            break_count_vertical = 1
            while column < 4:
                if index == changed_index:
                    self.board[index] = letter
                
                board_map.append(self.board[index])
                index += 1
                column += 1
                if break_count_vertical < 3:
                    board_map.append("|")
                    break_count_vertical += 1
            board_map.append("\n")
            row += 1
            if break_count_horizontal < 3:
                board_map.append("-----\n")
                break_count_horizontal += 1
        return print("".join(board_map), end="")
    
    def _ask_input(self):
        n = 1
        while n == 1:
            try:
                user_input = int(input("Enter a number from 1-9: "))
                if user_input < 1 or user_input > 9:
                    print("Please enter a number from 1-9")
                    continue
                n = 2
            except (ValueError):
                print("Please enter a number from 1-9")
        return self.controller.take_input(user_input)