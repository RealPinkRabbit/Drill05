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
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

def create_hand():
    hand_arrow.draw(random.randint(0,1280+1), random.randint(0, 1024+1))

# 전역변수 선언
running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hide_cursor()

# 메인함수
while running:
    clear_canvas()

    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    create_hand()
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)

    update_canvas()
    frame = (frame + 1) % 8
    handle_events()
    delay(0.05)

# 캔버스 닫기
close_canvas()




