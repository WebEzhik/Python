

# Задача 1
# line = "asdf asfdg asdfg ergfres asfdgergre"
# words = line.split(" ")
# print(line)

# simv = "asd"
# new_words = []

# for i in words:
#     if i.find(simv) == -1:
#         new_words.append(i)

# new_line =''
# for j in new_words:
#     new_line = new_line + j + " "
# print(new_line)




# Задача 2






# Задача 3

# print("Крестики-нолики")

# board = list(range(1,10))

# def draw_board(board):
#    print("-" * 13)
#    for i in range(3):
#       print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#       print("-" * 13)

# def take_input(player_token):
#    valid = False
#    while not valid:
#       player_answer = input("Куда поставим " + player_token+"? ")
#       try:
#          player_answer = int(player_answer)
#       except:
#          print("Некорректный ввод. Вы уверены, что ввели число?")
#          continue
#       if player_answer >= 1 and player_answer <= 9:
#          if(str(board[player_answer-1]) not in "XO"):
#             board[player_answer-1] = player_token
#             valid = True
#          else:
#             print("Эта клетка уже занята!")
#       else:
#         print("Некорректный ввод. Введите число от 1 до 9.")

# def check_win(board):
#    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
#    for each in win_coord:
#        if board[each[0]] == board[each[1]] == board[each[2]]:
#           return board[each[0]]
#    return False

# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#            take_input("X")
#         else:
#            take_input("O")
#         counter += 1
#         if counter > 4:
#            tmp = check_win(board)
#            if tmp:
#               print(tmp, "выиграл!")
#               win = True
#               break
#         if counter == 9:
#             print("Ничья!")
#             break
#     draw_board(board)

# main(board)





# Задача 4

def rle_encod(src):
    result = []
    if src:
        current = src.pop(0)
        count = 1
        for e in src:
            if e == current:
                count += 1
            else:
                result.append((count, current))
                current = e
                count = 1
        result.append((count, current))
    return result


def rle_decod(src):
    new_string = ""
    for i in src:
        new_string = new_string + i[1] * int(i[0])
    # print(new_string)
    return new_string


string = "3333333333333333322222222222222222111145tttttt4444"
str_list = list(string)
print(string)


rle_data_encod = rle_encod(str_list)
print(rle_data_encod)

rle_data_decod = rle_decod(rle_data_encod)

print(rle_data_decod)
