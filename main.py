import streamlit as st
# import pygame

# pygame.init()


# if "board" not in st.session_state:
#     st.session_state.board = [
#         #1 2 3 4 5 6 7 8
#         [0,0,0,0,0,0,0,0,],#1
#         [0,0,0,0,0,0,0,0,],#2
#         [0,0,0,0,0,0,0,0,],#3
#         [0,0,0,-1,1,0,0,0,],#4
#         [0,0,0,1,-1,0,0,0,],#5
#         [0,0,0,0,0,0,0,0,],#6
#         [0,0,0,0,0,0,0,0,],#7
#         [0,0,0,0,0,0,0,0],#8
#     ]#8

# #プレイヤー
# st.session_state.player =1
# st.session_state.game_over=False

# vec_table=[
#     (-1,-1), #左上
#     (0,-1),  #上
#     (1,-1),  #右上
#     (-1,0),  #左
#     (1,0),   #右
#     (-1,1),  #左下
#     (0,1),   #下 
#     (1,1),   #右下
# ]


# #関数------------------------------------------------------

#     #グリッド線描画
# # def draw_grid():
#     # for i in range (square_num):
#     #     #横線
#     #     pygame.draw.line(screen,BLACK, (0,i*square_size),(screen_width, i * square_size),3)
#     #     #縦線
#     #     pygame.draw.line(screen,BLACK,(i*square_size,0),( i *square_size , screen_height),3)

# #盤面描写
# def draw_board():    
#     # for row_index,row in enumerate(st.session_state.board):
#     #      for col_index,col in enumerate(row):
#     #         if col ==1:
#     #             pygame.draw.circle(screen,BLACK,(col_index*square_size+40,row_index*square_size+40),35)
#     #         elif col==-1:
#     #             pygame.draw.circle(screen,WHITE,(col_index*square_size+40,row_index*square_size+40),35)

#     for row_index,row in enumerate(st.session_state.board):
#         cols=st.columns(8)
#         for col_index,col in enumerate(row):
#             with cols[col_index]:

#                 if col ==1:
#                     ladel="⚫"
#                 elif col==-1:
#                     ladel="⚪"
#                 elif (col_index,row_index) in st.session_state.valid_position_list:
#                     ladel="🟡"
#                 else:
#                     ladel=""
#                 if st.button(label, key=f"{col_index}_{row_index}"):
#                     st.write(f"{col_index}, {row_index} を押した")

# #石を置く場所取得
# def get_validation_positions(): 
#     valid_position_list=[]
#     for row in range(8):
#         for col in range(8):
#             #石を置いてない場所のチェック
#             if st.session_state.board[row][col]==0:
#                 for vx,vy in vec_table:
#                     x=vx+col
#                     y=vy+row
#                     #マス範囲内、かつプレイヤーと異なる石がある場合、その方向は引き続きチェック
#                     if 0<=x<8 and 0<=y<8 and st.session_state.board[y][x]==-st.session_state.player:
#                         while True:
#                             x+=vx
#                             y+=vy
#                             #プレイヤーの石とことなる石がある場合、その方向は引き続きチェック
#                             if 0<=x<8 and 0<=y<8 and st.session_state.board[y][x]==-st.session_state.player:
#                                 continue
#                             #プレイヤーの石と同色の石がある場合、石を置けるためインデックスを保存
#                             elif 0<=x<8 and 0<=y<8 and st.session_state.board[y][x]==st.session_state.player:
#                                 valid_position_list.append((col,row))
#                                 break
#                             else:
#                                 break
#     return valid_position_list


# #石をひっくり返す
# def flip_pieces(col,row):
#     for vx, vy in vec_table:
#         flip_list=[]
#         x=vx+col
#         y=vy+row
#         while 0<=x<8 and 0<=y<8 and st.session_state.board[y][x]==-st.session_state.player:
#             flip_list.append((x,y))
#             x+=vx
#             y+=vy
#             if 0<=x<8 and 0<=y<8 and st.session_state.board[y][x]==st.session_state.player:
#                 for flip_x,flip_y in flip_list:
#                     st.session_state.board[flip_y][flip_x]=st.session_state.player

# def reset_game():
#     st.session_state.board=[
#         #1 2 3 4 5 6 7 8
#         [0,0,0,0,0,0,0,0,],#1
#         [0,0,0,0,0,0,0,0,],#2
#         [0,0,0,0,0,0,0,0,],#3
#         [0,0,0,-1,1,0,0,0,],#4
#         [0,0,0,1,-1,0,0,0,],#5
#         [0,0,0,0,0,0,0,0,],#6
#         [0,0,0,0,0,0,0,0],#7
#         [0,0,0,0,0,0,0]#8
#     ]
#     st.session_state.player =1
#     st.session_state.game_over=False
#     st.session_state.pass_num=0


# #-------------------------------------------------------------------

# #ウィンドウ作成
# # screen_width=640
# # screen_height=640
# # screen=pygame.display.set_mode((screen_width,screen_height))
# # pygame.display.set_caption("オセロゲーム")

# #マス目設定
# # square_num=8
# # square_size=screen_width//square_num

# #FPSS設定
# # FPS=60
# # clock=pygame.time.Clock()

# #色設定
# # BLACK=(0,0,0)
# # WHITE=(255,255,255)
# # RED=(255,0,0)
# # GREEN=(0,128,0)
# # BLUE=(0,0,255)
# # YELLOW=(255,255,0)

# #盤面(黒：1,白：-1)
# # if "board" not in st.session_state:
# #     st.session_state.board = [
# #         #1 2 3 4 5 6 7 8
# #         [0,0,0,0,0,0,0,0,],#1
# #         [0,0,0,0,0,0,0,0,],#2
# #         [0,0,0,0,0,0,0,0,],#3
# #         [0,0,0,-1,1,0,0,0,],#4
# #         [0,0,0,1,-1,0,0,0,],#5
# #         [0,0,0,0,0,0,0,0,],#6
# #         [0,0,0,0,0,0,0,0,],#7
# #         [0,0,0,0,0,0,0,0],#8
# #     ]#8

# # #プレイヤー
# # st.session_state.player =1
# # st.session_state.game_over=False

# # vec_table=[
# #     (-1,-1), #左上
# #     (0,-1),  #上
# #     (1,-1),  #右上
# #     (-1,0),  #左
# #     (1,0),   #右
# #     (-1,1),  #左下
# #     (0,1),   #下 
# #     (1,1),   #右下
# # ]

# game_over=False
# st.session_state.pass_num=0

# #フォント設定
# font=pygame.font.SysFont(None,100,bold=False,italic=False)

# black_win_surface=font.render("Black win!!",False,BLACK,RED)
# white_win_surface=font.render("White win!!",False,WHITE,RED)
# draw_surface=font.render("Draw...",False,BLUE,RED)
# reset_surface=font.render("click to reset!",False,BLACK,RED)
# skip_surface=font.render("skip",False,WHITE,RED)
# #メインループ========================================================
# black_num=0
# white_num=0
# run=True
# while run:

#     #背景
#     screen.fill(GREEN)

#     #グリット線描画
#     draw_grid()

#     #盤面描画
#     draw_board()

#    #石を置く場所取得
#     valid_position_list=get_validation_positions()

#     #石を置ける場所の表示
#     # for x,y in valid_position_list:
#     #      pygame.draw.circle(screen,YELLOW,(x*square_size+40,y*square_size+40),35,3)
    
    
#     black_num=0
#     white_num=0                    
#     black_num=sum(row.count(1) for row in board)
#     white_num=sum(row.count(-1) for row in board)
#     black_num_white_num = black_num + white_num
    
#     if black_num_white_num == 64:
#         game_over=True
#         print(black_num_white_num)
#     else:
#         #石を置ける場所がない場合、パス
#         if len (valid_position_list)<1:
#             if pass_num == 2:
#                     game_over=True
#             else:
#                 if game_over==False:
#                     player*=-1
#                     screen.blit(skip_surface,(230,200))
#                     print("s")
#                     pygame.display.update()
#                     #二回パスしたらゲーム終了
#                     pass_num+=1
#                     pygame.time.delay(1000)
#                     print(pass_num)
    
#     #勝敗判定
#     black_num=0
#     white_num=0
#     if game_over:
    
#         black_num=sum(row.count(1) for row in board)

#         white_num=sum(row.count(-1) for row in board)
#         if black_num>white_num:
#             screen.blit(black_win_surface,(230,200))
#             screen.blit(reset_surface,(180,400))
#             print(game_over)
#         elif white_num>black_num:
#             screen.blit(white_win_surface,(230,200))
#             screen.blit(reset_surface,(180,400))
#             print(game_over)
#         else:
#             screen.blit(draw_surface,(230,200))
#             screen.blit(reset_surface,(180,400))
#             print(game_over)
#     #イベント取得
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             run=False
#         if event.type==pygame.KEYDOWN:
#             if event.key==pygame.K_ESCAPE:
#                 run=False
#         #マウスクリック
#         if event.type==pygame.MOUSEBUTTONDOWN:
#             if game_over==False:
#                 mx,my=pygame.mouse.get_pos()
#                 x=mx//square_size
#                 y=my//square_size
#                 if board[y][x]==0 and (x,y)in valid_position_list:

#                     #石をひっくり返す
#                     flip_pieces(x,y)

#                     board[y][x]=player
#                     player*=-1
#                     pass_num=0

#             else:
#                 board=[
#                     #1 2 3 4 5 6 7 8
#                     [0,0,0,0,0,0,0,0,],#1
#                     [0,0,0,0,0,0,0,0,],#2
#                     [0,0,0,0,0,0,0,0,],#3
#                     [0,0,0,-1,1,0,0,0,],#4
#                     [0,0,0,1,-1,0,0,0,],#5
#                     [0,0,0,0,0,0,0,0,],#6
#                     [0,0,0,0,0,0,0,0,],#7
#                     [0,0,0,0,0,0,0,0,]]#8
                
#                 player =1
#                 game_over=False
#                 pass_num=0

#     #更新
#     pygame.display.update()
#     clock.tick(FPS)

# #===================================================================
# pygame.quit()



if "board" not in st.session_state:
    st.session_state.board = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,-1,1,0,0,0],
        [0,0,0,1,-1,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
    ]
    st.session_state.player = 1
    st.session_state.game_over = False
    st.session_state.pass_num = 0

vec_table = [
    (-1,-1), #左上
    (0,-1),  #上
    (1,-1),  #右上
    (-1,0),  #左
    (1,0),   #右
    (-1,1),  #左下
    (0,1),   #下
    (1,1),   #右下
]

# ------------------------------------------------------
# 関数
# ------------------------------------------------------

# 石を置ける場所取得
def get_validation_positions():
    valid_position_list = []
    for row in range(8):
        for col in range(8):
            if st.session_state.board[row][col] == 0:
                for vx, vy in vec_table:
                    x = vx + col
                    y = vy + row

                    if 0 <= x < 8 and 0 <= y < 8 and st.session_state.board[y][x] == -st.session_state.player:
                        while True:
                            x += vx
                            y += vy

                            if 0 <= x < 8 and 0 <= y < 8 and st.session_state.board[y][x] == -st.session_state.player:
                                continue

                            elif 0 <= x < 8 and 0 <= y < 8 and st.session_state.board[y][x] == st.session_state.player:
                                valid_position_list.append((col, row))
                                break
                            else:
                                break
    return valid_position_list

# 石をひっくり返す
def flip_pieces(col, row):
    for vx, vy in vec_table:
        flip_list = []
        x = vx + col
        y = vy + row

        while 0 <= x < 8 and 0 <= y < 8 and st.session_state.board[y][x] == -st.session_state.player:
            flip_list.append((x, y))
            x += vx
            y += vy

            if 0 <= x < 8 and 0 <= y < 8 and st.session_state.board[y][x] == st.session_state.player:
                for flip_x, flip_y in flip_list:
                    st.session_state.board[flip_y][flip_x] = st.session_state.player

# 盤面を元に戻す
def reset_game():
    st.session_state.board = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,-1,1,0,0,0],
        [0,0,0,1,-1,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
    ]
    st.session_state.player = 1
    st.session_state.game_over = False
    st.session_state.pass_num = 0

# ------------------------------------------------------
# ゲーム処理
# ------------------------------------------------------

valid_position_list = get_validation_positions()
st.session_state.valid_position_list = valid_position_list

# 石を置ける場所がない場合
if len(valid_position_list) < 1 and not st.session_state.game_over:
    st.session_state.pass_num += 1
    if st.session_state.pass_num >= 2:
        st.session_state.game_over = True
    else:
        st.session_state.player *= -1
        st.write("パスです")
        st.rerun()

# 盤面の石の数を数える
black_num = sum(row.count(1) for row in st.session_state.board)
white_num = sum(row.count(-1) for row in st.session_state.board)
black_num_white_num = black_num + white_num

# すべて埋まったら終了
if black_num_white_num == 64:
    st.session_state.game_over = True

# ------------------------------------------------------
# 表示
# ------------------------------------------------------

st.write(f"今の手番: {'黒' if st.session_state.player == 1 else '白'}")
st.write(f"黒: {black_num}  白: {white_num}")

# 盤面表示
for row_index, row in enumerate(st.session_state.board):
    cols = st.columns(8)
    for col_index, col in enumerate(row):
        with cols[col_index]:
            if col == 1:
                label = "●"
            elif col == -1:
                label = "○"
            elif (col_index, row_index) in valid_position_list:
                label = "◎"
            else:
                label = " "

            if st.button(label, key=f"{col_index}_{row_index}"):
                if not st.session_state.game_over:
                    if (col_index, row_index) in valid_position_list:
                        flip_pieces(col_index, row_index)
                        st.session_state.board[row_index][col_index] = st.session_state.player
                        st.session_state.player *= -1
                        st.session_state.pass_num = 0
                        st.rerun()

# 勝敗表示
if st.session_state.game_over:
    if black_num > white_num:
        st.write("Black win!!")
    elif white_num > black_num:
        st.write("White win!!")
    else:
        st.write("Draw...")

    if st.button("リセット"):
        reset_game()
        st.rerun()