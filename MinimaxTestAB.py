import copy


# Alpha-Beta Minimax Algorithm
def minimax(color, state, depth, alpha, beta):
    # print("DEPTH-------------------",depth)
    if depth == 0 or len(successors(state, color)) == 0:
        return utility(state, color)
    if color == 0:  # MAX player
        value = float('-inf')
        action_state_pairs = successors(state, 0)
        for action in action_state_pairs:
            value = max(value, minimax(1, action_state_pairs[action], depth-1, alpha, beta))
            if value > beta:  # Not worth looking thru rest of children
                break
            if value > alpha:  # Set children alpha to best available
                alpha = value

    else:  # MIN player
        value = float('inf')
        action_state_pairs = successors(state, 1)
        for action in action_state_pairs:
            value = min(value, minimax(0, action_state_pairs[action], depth-1, alpha, beta))
            if value < alpha:  # Not worth looking thru rest of children
                break
            if value < beta:  # Set children beta to best available
                beta = value
    return value

#
# def max_value(state, depth):
#     print("DEPTH-------------------",depth)
#     if len(successors(state, 0)) == 0 or depth == 0:
#         return utility(state, 0)
#     value = float('-inf')
#     for action_state_pair in successors(state, 0):
#         value = max(value, min_value(action_state_pair[1], depth-1))
#     return value
#
#
# def min_value(state, depth):
#     print("DEPTH-------------------",depth)
#     if len(successors(state, 1)) == 0 or depth == 0:
#         return utility(state, 1)
#     value = float('inf')
#     action_state_pairs = successors(state, 1)
#     for action in action_state_pairs:
#         value = min(value, max_value(action_state_pairs[action], depth-1))
#     return value


# Returns a list of possible states and actions
# which result in these states.
# @params state: 8x8 grid, color: curr player's color.
def successors(state, color):
    ret_dict = dict()
    # print("successors CALLED with color = ", color)
    static_state = copy.deepcopy(state)
    for y in range(8):
        for x in range(8):
            # A unique curr_board_grid to work with for every cell
            curr_board_grid = copy.deepcopy(static_state)
            # Iter through all board positions to check for possible moves
            # print("y=",y,"x=",x)
            # print("value at this location =",curr_board_grid[y][x])
            if curr_board_grid[y][x] == -1:
                # print("Possible move for", color, "player @", x, y)
                # Vars for horizontal movement
                a = copy.deepcopy(x)
                b = copy.deepcopy(x)
                c = copy.deepcopy(y)
                d = copy.deepcopy(y)

                # Vars for diagonal movement
                x1 = copy.deepcopy(x)
                x2 = copy.deepcopy(x)
                x3 = copy.deepcopy(x)
                x4 = copy.deepcopy(x)
                y1 = copy.deepcopy(y)
                y2 = copy.deepcopy(y)
                y3 = copy.deepcopy(y)
                y4 = copy.deepcopy(y)

                # Left movement, decreasing col index = left movement
                left_flag = False
                first_move = True
                while a-1 >= 0 and curr_board_grid[y][a-1] != -1:
                    # print("Can move left")
                    if curr_board_grid[y][a-1] == color and first_move:
                        break
                    elif curr_board_grid[y][a-1] == color and not first_move:
                        left_flag = True
                        break
                    else:
                        first_move = False
                        a -= 1
                a = copy.deepcopy(x)
                if left_flag:  # Initiate left movement
                    while a-1 >= 0 and curr_board_grid[y][a-1] != -1:
                        if curr_board_grid[y][a-1] == color:
                            break
                        else:
                            curr_board_grid[y][a-1] = color
                            a -= 1

                # Right movement, increasing col index = right movement
                right_flag = False
                first_move = True
                while b+1 <= 7 and curr_board_grid[y][b+1] != -1:
                    # print("Can move right")
                    if curr_board_grid[y][b+1] == color and first_move:
                        break
                    elif curr_board_grid[y][b+1] == color and not first_move:
                        right_flag = True
                        break
                    else:
                        first_move = False
                        b += 1
                b = copy.deepcopy(x)
                if right_flag:  # Initiate right movement
                    while b+1 <= 7 and curr_board_grid[y][b+1] != -1:
                        if curr_board_grid[y][b+1] == color:
                            break
                        else:
                            curr_board_grid[y][b+1] = color
                            b += 1

                # Up movement, decreasing row index = upward movement
                up_flag = False
                first_move = True
                while c-1 >= 0 and curr_board_grid[c-1][x] != -1:
                    # print("Can move up")
                    if curr_board_grid[c-1][x] == color and first_move:
                        break
                    elif curr_board_grid[c-1][x] == color and not first_move:
                        up_flag = True
                        break
                    else:
                        first_move = False
                        c -= 1
                c = copy.deepcopy(y)
                if up_flag:  # Initiate upward movement
                    while c-1 >=0 and curr_board_grid[c-1][x] != -1:
                        if curr_board_grid[c-1][x] == color:
                            break
                        else:
                            curr_board_grid[c-1][x] = color
                            c -= 1

                # Down movement, increasing row index = downward movement
                down_flag = False
                first_move = True
                while d+1 <= 7 and curr_board_grid[d+1][x] != -1:
                    # print("Can move down")
                    if curr_board_grid[d+1][x] == color and first_move:
                        break
                    elif curr_board_grid[d+1][x] == color and not first_move:
                        down_flag = True
                        break
                    else:
                        first_move = False
                        d += 1
                d = copy.deepcopy(y)
                if down_flag:  # Initiate downward movement
                    while d+1 <= 7 and curr_board_grid[d+1][x] != -1:
                        if curr_board_grid[d+1][x] == color:
                            break
                        else:
                            curr_board_grid[d+1][x] = color
                            d += 1

                # Upper-left movement, decreasing col index = left movement, decreasing row index = upward movement
                upper_left_flag = False
                first_move = True
                while x1-1 >= 0 and y1-1 >= 0 and curr_board_grid[y1-1][x1-1] != -1:
                    # print("Can move upper-left")
                    if curr_board_grid[y1-1][x1-1] == color and first_move:
                        break
                    elif curr_board_grid[y1-1][x1-1] == color and not first_move:
                        upper_left_flag = True
                        break
                    else:
                        first_move = False
                        x1 -= 1
                        y1 -= 1
                x1 = copy.deepcopy(x)
                y1 = copy.deepcopy(y)
                if upper_left_flag:  # Initiate upper-left movement
                    while x1-1 >= 0 and y1-1 >= 0 and curr_board_grid[y1-1][x1-1] != -1:
                        if curr_board_grid[y1-1][x1-1] == color:
                            break
                        else:
                            curr_board_grid[y1-1][x1-1] = color
                            x1 -= 1
                            y1 -= 1

                # Upper-right movement, increasing col index = right movement, decreasing row index = upward movement
                upper_right_flag = False
                first_move = True
                while x2+1 <= 7 and y2-1 >= 0 and curr_board_grid[y2-1][x2+1] != -1:
                    # print("Can move upper-right")
                    if curr_board_grid[y2-1][x2+1] == color and first_move:
                        break
                    elif curr_board_grid[y2-1][x2+1] == color and not first_move:
                        upper_right_flag = True
                        break
                    else:
                        first_move = False
                        x2 += 1
                        y2 -= 1
                x2 = copy.deepcopy(x)
                y2 = copy.deepcopy(y)
                if upper_right_flag:  # Initiate upper-right movement
                    while x2+1 <= 7 and y2-1 >= 0 and curr_board_grid[y2-1][x2+1] != -1:
                        if curr_board_grid[y2-1][x2+1] == color:
                            break
                        else:
                            curr_board_grid[y2-1][x2+1] = color
                            x2 += 1
                            y2 -= 1

                # Lower-left movement, decreasing col index = left movement, increasing row index = downward movement
                lower_left_flag = False
                first_move = True
                while x3-1 >= 0 and y3+1 <= 7 and curr_board_grid[y3+1][x3-1] != -1:
                    # print("Can move lower-left")
                    if curr_board_grid[y3+1][x3-1] == color and first_move:
                        break
                    elif curr_board_grid[y3+1][x3-1] == color and not first_move:
                        lower_left_flag = True
                        break
                    else:
                        first_move = False
                        x3 -= 1
                        y3 += 1
                x3 = copy.deepcopy(x)
                y3 = copy.deepcopy(y)
                if lower_left_flag:  # Initiate lower-left movement
                    while x3-1 >= 0 and y3+1 <= 7 and curr_board_grid[y3+1][x3-1] != -1:
                        if curr_board_grid[y3+1][x3-1] == color:
                            break
                        else:
                            curr_board_grid[y3+1][x3-1] = color
                            x3 -= 1
                            y3 += 1

                # Lower-right movement, increasing col index = right movement, increasing row index = downward movement
                lower_right_flag = False
                first_move = True
                while x4+1 <= 7 and y4+1 <= 7 and curr_board_grid[y4+1][x4+1] != -1:
                    # print("Can move lower-right")
                    if curr_board_grid[y4+1][x4+1] == color and first_move:
                        break
                    elif curr_board_grid[y4+1][x4+1] == color and not first_move:
                        lower_right_flag = True
                        break
                    else:
                        first_move = False
                        x4 += 1
                        y4 += 1
                x4 = copy.deepcopy(x)
                y4 = copy.deepcopy(y)
                if lower_right_flag:  # Initiate lower-right movement
                    while x4+1 <= 7 and y4+1 <= 7 and curr_board_grid[y4+1][x4+1] != -1:
                        if curr_board_grid[y4+1][x4+1] == color:
                            break
                        else:
                            curr_board_grid[y4+1][x4+1] = color
                            x4 += 1
                            y4 += 1

                # If placing a piece here is legal -> Add to return list
                if left_flag or right_flag or up_flag or down_flag or upper_left_flag or upper_right_flag or lower_left_flag or lower_right_flag:
                    curr_board_grid[y][x] = color
                    possible_board_state = copy.deepcopy(curr_board_grid)
                    action = ""
                    action += str(copy.deepcopy(x))
                    action += str(copy.deepcopy(y))
                    ret_dict[action] = possible_board_state
            # else:
                # print("Skipped: Attempting to place a piece on an occupied cell.")
    return ret_dict


# Passes state through ValueNet and returns win/lose likelihood.
def utility(state, color):
    black_counter = 0
    white_counter = 0
    for j in range(8):
        for i in range(8):
            if state[i][j] == 0:
                black_counter += 1
            elif state[i][j] == 1:
                white_counter += 1
    # for y in range(8):
    #     for x in range(8):
    #         print(state[y][x],"\t",end="")
    #     print()
    return black_counter - white_counter


# FOLLOWING IS DEBUGGING CODE---------------------------------------------
# init grid state, where -1 is empty cell, 0 is black, 1 is white
init_grid0 = [[-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, 1, 0, -1, -1, -1],
        [-1, -1, -1, 0, 1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1]]

init_grid = [[-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, 0, 1, -1, 1, 0, -1],
        [-1, -1, 0, 1, 1, 0, 0, -1],
        [-1, -1, 0, 1, 0, 1, 0, -1],
        [-1, -1, -1, 1, 1, 1, -1, -1],
        [-1, -1, -1, 0, 0, -1, -1, -1],
        [-1, -1, -1, -1, 0, -1, -1, -1]]

full_grid = [[1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]]

# Test chart in blk-bk, verifiable with depth values up to 3
ab_test = [[-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, 0, 0, -1, -1, -1, -1],
        [-1, -1, -1, 1, -1, -1, -1, -1],
        [-1, -1, -1, 1, -1, -1, -1, -1],
        [-1, -1, -1, 1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1]]


# ret = successors(init_grid, 0)

# print(len(ret))
# print(ret.keys())

# print(minimax(0, init_grid, 6, float('-inf'), float('inf')))
