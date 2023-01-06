from random import choice
import sys
import os

class Model():
    def __init__(self):
        self.board = [" " for range in range(10)]
        self.taken_spots = []
    
    def ask_input(self):
        try:
            user_input = int(input("Enter a number from 1-9: "))
            if user_input < 1 or user_input > 9:
                return False
        except (ValueError):
            return False

        if user_input in self.taken_spots:
            return False
        
        self.taken_spots.append(user_input)
        return user_input
    
    def update_board(self, changed_index=0, letter=" "): 
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

    def enemy_turn(self):
        num = choice(list(set([x for x in range(1, 10)]) - set(self.taken_spots)))
        self.taken_spots.append(num)
        return self.update_board(num, "O")
    
    def check_winner(self, letter):
        if (self.board[1] == letter and self.board[2] == letter and self.board[3] == letter):
            result = True 
        elif (self.board[1] == letter and self.board[4] == letter and self.board[7] == letter):
            result = True 
        elif (self.board[1] == letter and self.board[5] == letter and self.board[9] == letter):
            result = True
        elif (self.board[7] == letter and self.board[8] == letter and self.board[9] == letter):
            result = True
        elif (self.board[3] == letter and self.board[6] == letter and self.board[9] == letter):
            result = True
        elif (self.board[4] == letter and self.board[5] == letter and self.board[6] == letter):
            result = True
        elif (self.board[3] == letter and self.board[5] == letter and self.board[7] == letter):
            result = True
        else:
            result = False
        
        return result
    
    def restart_program(self):
        python = sys.executable
        input("Press enter to restart!")
        os.execl(python, python, * sys.argv)