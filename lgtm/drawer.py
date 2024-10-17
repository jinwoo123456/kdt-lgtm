from PIL import Image, ImageDraw, ImageFont

# 이미지 전체에 대한 메시지 그리기 가능한 영역의 비율
MAX_RATIO = 0.8

# 폰트 관련 상수
FONT_MAX_SIZE = 256
FONT_MIN_SIZE = 24

# Windows나 Linux에서는 경로가 다름
import sys

if sys.platform=='win32':
    FONT_NAME = r'C:\Windows\Fonts\HMFMPYUN.TTF'
    FONT_COLOR_WHITE = (255, 255, 255, 0)
else:    
    FONT_NAME = '/Library/Fonts/Arial Bold.ttf'
    FONT_COLOR_WHITE = (255, 255, 255, 0)

# 출력 관련 상수
OUTPUT_NAME = 'output.png'
OUTPUT_FORMAT = 'PNG'


def save_with_message(fp, message):
    image = Image.open(fp)
    draw = ImageDraw.Draw(image)
    # 메시지를 그릴 수 있는 영역의 크기
    # 튜플의 요소별로 계산
    image_width, image_height = image.size
    message_area_width = image_width * MAX_RATIO
    message_area_height = image_height * MAX_RATIO

    # 폰트 크기를 결정
    for font_size in range(FONT_MAX_SIZE, FONT_MIN_SIZE, -1):

        font = ImageFont.truetype(FONT_NAME, font_size)
        
        # 그리기에 필요한 크기
        # text_width, text_height = draw.textsize(message, font=font)
        aa= (0,0)
        text_width, text_height, x, y = draw.textbbox(aa, message, font=font)

        print(text_width)
        print(text_height)
        print(x)
        print(y)
        w = message_area_width - text_width
        h = message_area_height - text_height

        # 너비와 높이가 모두 영역 내에 들어가는 값을 채택
        if w > 0 and h > 0:
            position = ((image_width - text_width) / 2, (image_height - text_height) / 2)
            # 메시지 그리기
            draw.text(position, message, fill=FONT_COLOR_WHITE, font=font)
            break

    # 이미지 저장
    image.save(OUTPUT_NAME, OUTPUT_FORMAT)
