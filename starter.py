# 모듈 인포트
from pico2d import *
import random

# 캔버스 오픈
TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

# 리소스 파일 불러오기
TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

# 키보드 입력 감지 함수
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# 손가락 위치 갱신 함수
def replace_hand():
    global hand_x, hand_y
    hand_x, hand_y = random.randint(0, 1280+1), random.randint(0, 1024+1)

# 캐릭터 위치 갱신 함수
def replace_character():
    global x, y, line_x, line_y, line_x_index, line_y_index
    line_x_index += 1
    line_y_index += 1
    x = line_x[line_x_index]
    y = line_y[line_y_index]

def replace_line():
    global x, y, hand_x, hand_y, line_x, line_y, line_x_index, line_y_index
    index_x = 0
    index_y = 0
    for i in range(0, 100+1, 5):
        t = i/100
        line_x[index_x] = (1-t)*x + t*hand_x
        line_y[index_y] = (1-t)*y + t*hand_y
        index_x += 1
        index_y += 1

    line_x_index = 0
    line_y_index = 0

# 전역변수 선언 및 초기화
running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
hand_x, hand_y = TUK_WIDTH // 2, TUK_HEIGHT // 2
character_dir = 1
line_x = [n for n in range(21)]
line_y = [n for n in range(21)]
line_x_index = 0
line_y_index = 0
frame = 0

# 커서 숨기기
hide_cursor()

# 메인함수
while running:
    clear_canvas()

    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if (x == hand_x) & (y == hand_y):
        replace_hand()
        replace_line()
        if (x <= hand_x):
            character_dir = 1 # 오른쪽
        else:
            character_dir = 0 # 왼쪽
    else:
        replace_character()
    hand_arrow.draw(hand_x, hand_y)
    character.clip_draw(frame * 100, 100 * character_dir, 100, 100, x, y)
    print(x, y, hand_x, hand_y)


    update_canvas()
    frame = (frame + 1) % 8
    handle_events()
    delay(0.05)

# 캔버스 닫기
close_canvas()




