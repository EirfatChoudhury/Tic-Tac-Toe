class Model():
    def __init__(self):
        self.board = ["#" for range in range(10)]
    
    def ask_input(self):
        try:
            user_input = int(input("Enter a number from 1-9: "))
            if user_input < 1 or user_input > 9:
                return False
        except (ValueError):
            return False
        return user_input
    
    def update_board(self, changed_index=0, letter=" "):
        if self.board[changed_index] in ["O", "X"]:
            return False
        
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

        return "".join(board_map)