import streamlit as st
import random  # AIが置く場所をランダムに選ぶために使う

# ------------------------------------------------------
# CSS
# ------------------------------------------------------
st.markdown("""
<style>
div.stButton > button {
    width: 45px;
    height: 45px;
    padding: 0px;
    margin: 0px;
    border-radius: 0px;
    border: 1px solid black;
    background-color: #228B22;
    color: black;
    font-size: 40px;
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

if "mode" not in st.session_state:
    st.session_state.mode = "2人プレイ"  # 最初は2人プレイにする

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

def count_flips(col, row):
    # そのマスに置いたとき、何個ひっくり返せるか数える
    total = 0
    for vx, vy in vec_table:
        x = col + vx
        y = row + vy
        count = 0

        # 相手の石が続く間は数える
        while 0 <= x < 8 and 0 <= y < 8 and st.session_state.board[y][x] == -st.session_state.player:
            count += 1
            x += vx
            y += vy

        # 先に自分の石があれば、その方向は有効
        if 0 <= x < 8 and 0 <= y < 8 and st.session_state.board[y][x] == st.session_state.player:
            total += count

    return total


def is_corner_2x2(col, row):
    # 盤面の4つの角にある2×2エリアなら True
    return (col < 2 and row < 2) or (col >= 6 and row < 2) or (col < 2 and row >= 6) or (col >= 6 and row >= 6)

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

    import random  # AIが置く場所をランダムに選ぶために使う

# ------------------------------------------------------
# AIの処理
# ------------------------------------------------------
def ai_move():
    st.session_state.player = -1
    valid_position_list = get_validation_positions()

    if len(valid_position_list) == 0:
        return

    total_stones = sum(row.count(1) + row.count(-1) for row in st.session_state.board)

    scored_moves = []
    for col, row in valid_position_list:
        flips = count_flips(col, row)

        # 序盤は少なく返す手を優先
        if total_stones < 40:
            score = -flips
        else:
            score = flips

        # 角の2×2は基本的に避ける
        if is_corner_2x2(col, row):
            score -= 100

        scored_moves.append((score, col, row))

    scored_moves.sort(reverse=True)
    _, col, row = scored_moves[0]

    flip_pieces(col, row)
    st.session_state.board[row][col] = st.session_state.player
    st.session_state.player = 1
    st.session_state.pass_num = 0

# ------------------------------------------------------
# ゲーム処理
# ------------------------------------------------------
valid_position_list = get_validation_positions()

if not st.session_state.game_over and st.session_state.mode == "1人プレイ" and st.session_state.player == -1:
    ai_move()
    st.rerun()

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
st.session_state.mode = st.radio(
    "プレイモードを選んでね",
    ["1人プレイ", "2人プレイ"],
    horizontal=True
)

st.header(f"今の手番: {'黒' if st.session_state.player == 1 else '白'}")
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