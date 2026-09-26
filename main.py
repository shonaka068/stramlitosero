import streamlit as st

# ------------------------------------------------------
# CSS
# ------------------------------------------------------
st.markdown("""
<style>
div.stButton > button {
    width: 60px;
    height: 40px;
    padding: 0px;
    margin: 0px;
    border-radius: 0px;
    border: 1px solid black;
    background-color: #228B22;
    color: black;
    font-size: 24px;
    font-weight: bold;
}

div[data-testid="column"] {
    padding-left: 0px;
    padding-right: 0px;
}

.block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
    padding-left: 1rem;
    padding-right: 1rem;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------
# 初期化
# ------------------------------------------------------
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

if "player" not in st.session_state:
    st.session_state.player = 1

if "game_over" not in st.session_state:
    st.session_state.game_over = False

if "pass_num" not in st.session_state:
    st.session_state.pass_num = 0

# ------------------------------------------------------
# 方向
# ------------------------------------------------------
vec_table = [
    (-1, -1), (0, -1), (1, -1),
    (-1,  0),           (1,  0),
    (-1,  1), (0,  1), (1,  1),
]

# ------------------------------------------------------
# 関数
# ------------------------------------------------------
def get_validation_positions():
    valid_position_list = []
    for row in range(8):
        for col in range(8):
            if st.session_state.board[row][col] == 0:
                for vx, vy in vec_table:
                    x = col + vx
                    y = row + vy

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

def flip_pieces(col, row):
    for vx, vy in vec_table:
        flip_list = []
        x = col + vx
        y = row + vy

        while 0 <= x < 8 and 0 <= y < 8 and st.session_state.board[y][x] == -st.session_state.player:
            flip_list.append((x, y))
            x += vx
            y += vy

        if 0 <= x < 8 and 0 <= y < 8 and st.session_state.board[y][x] == st.session_state.player:
            for flip_x, flip_y in flip_list:
                st.session_state.board[flip_y][flip_x] = st.session_state.player

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

black_num = sum(row.count(1) for row in st.session_state.board)
white_num = sum(row.count(-1) for row in st.session_state.board)

if black_num + white_num == 64:
    st.session_state.game_over = True

if len(valid_position_list) < 1 and not st.session_state.game_over:
    st.session_state.pass_num += 1
    if st.session_state.pass_num >= 2:
        st.session_state.game_over = True
    else:
        st.session_state.player *= -1
        st.rerun()

# ------------------------------------------------------
# 表示
# ------------------------------------------------------
st.title("オセロゲーム")
st.write(f"今の手番: {'黒' if st.session_state.player == 1 else '白'}")
st.write(f"黒: {black_num} / 白: {white_num}")

if st.session_state.game_over:
    if black_num > white_num:
        st.success("Black win!!")
    elif white_num > black_num:
        st.success("White win!!")
    else:
        st.info("Draw...")

    if st.button("リセット"):
        reset_game()
        st.rerun()

# ------------------------------------------------------
# 盤面表示＋操作
# ------------------------------------------------------
if not st.session_state.game_over:
    st.write("置きたいマスを押してね")

for row in range(8):
    cols = st.columns(8)
    for col in range(8):
        with cols[col]:
            if st.session_state.board[row][col] == 1:
                label = "⚫"
            elif st.session_state.board[row][col] == -1:
                label = "⚪"
            elif (col, row) in valid_position_list:
                label = "🟡"
            else:
                label = " "

            if st.button(label, key=f"{row}_{col}"):
                if not st.session_state.game_over and (col, row) in valid_position_list:
                    flip_pieces(col, row)
                    st.session_state.board[row][col] = st.session_state.player
                    st.session_state.player *= -1
                    st.session_state.pass_num = 0
                    st.rerun()