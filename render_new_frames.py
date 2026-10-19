import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1800, 1200
TITLE = "2026 外埔長青學苑結業典禮"

# Fonts
FONT_KAI = "C:/Windows/Fonts/kaiu.ttf"      # 標楷體 (書法感)
FONT_JH_BOLD = "C:/Windows/Fonts/msjhbd.ttc" # 微軟正黑體粗體 (POP可愛立體感)

def get_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()

def draw_text_with_outline(draw, pos, text, font, fill_color, outline_color, outline_width=6):
    x, y = pos
    for dx in range(-outline_width, outline_width + 1):
        for dy in range(-outline_width, outline_width + 1):
            if dx*dx + dy*dy <= outline_width*outline_width:
                draw.text((x + dx, y + dy), text, font=font, fill=outline_color)
    draw.text((x, y), text, font=font, fill=fill_color)

def draw_sunflower(draw, cx, cy, radius):
    # Draw cheerful sunflower
    petal_len = radius * 0.9
    num_petals = 12
    for i in range(num_petals):
        angle = i * (2 * math.pi / num_petals)
        px = cx + math.cos(angle) * petal_len
        py = cy + math.sin(angle) * petal_len
        draw.ellipse([px - radius*0.35, py - radius*0.35, px + radius*0.35, py + radius*0.35], fill=(255, 195, 0, 255))
        draw.ellipse([px - radius*0.25, py - radius*0.25, px + radius*0.25, py + radius*0.25], fill=(255, 160, 0, 255))
    draw.ellipse([cx - radius*0.55, cy - radius*0.55, cx + radius*0.55, cy + radius*0.55], fill=(110, 60, 15, 255))
    draw.ellipse([cx - radius*0.45, cy - radius*0.45, cx + radius*0.45, cy + radius*0.45], fill=(85, 45, 10, 255))

def draw_grad_cap(draw, cx, cy, size):
    # Diamond mortarboard
    half = size // 2
    pts = [(cx, cy - half//2), (cx + half, cy), (cx, cy + half//2), (cx - half, cy)]
    draw.polygon(pts, fill=(35, 40, 55, 255), outline=(245, 180, 0, 255))
    # Cap skull
    draw.rectangle([cx - half//3, cy, cx + half//3, cy + half//3], fill=(25, 30, 45, 255))
    # Tassel
    draw.line([(cx, cy), (cx + half*0.8, cy + half*0.6)], fill=(245, 180, 0, 255), width=4)
    draw.ellipse([cx + half*0.8 - 4, cy + half*0.6 - 4, cx + half*0.8 + 4, cy + half*0.6 + 4], fill=(245, 180, 0, 255))

# -------------------------------------------------------------
# FRAME 1: 冬日暖陽・金色銀杏 (Winter Warmth & Golden Ginkgo)
# -------------------------------------------------------------
def make_frame_warmth():
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Cutout photo window: 1300 x 780 centered
    hole_w, hole_h = 1320, 780
    hole_x = (W - hole_w) // 2   # 240
    hole_y = 280                # y from 280 to 1060

    # Draw solid border around cutout
    # Top banner background: Warm creamy amber gradient
    draw.rounded_rectangle([40, 30, W - 40, H - 30], radius=45, fill=(254, 250, 240, 255), outline=(245, 166, 35, 255), width=10)
    # Inner border frame around hole
    draw.rounded_rectangle([hole_x - 14, hole_y - 14, hole_x + hole_w + 14, hole_y + hole_h + 14], radius=28, fill=(250, 238, 215, 255), outline=(230, 140, 20, 255), width=8)

    # Cut out transparent hole
    for y in range(hole_y, hole_y + hole_h):
        for x in range(hole_x, hole_x + hole_w):
            img.putpixel((x, y), (0, 0, 0, 0))

    # Re-draw on top of cutout
    draw = ImageDraw.Draw(img)

    # Top Ribbon Banner for Title
    draw.rounded_rectangle([180, 50, W - 180, 210], radius=40, fill=(245, 120, 30, 255), outline=(255, 220, 120, 255), width=6)
    draw.rounded_rectangle([190, 60, W - 190, 200], radius=32, fill=(255, 140, 45, 255))

    # Title Text (Cute & Bold)
    font_title = get_font(FONT_JH_BOLD, 74)
    draw_text_with_outline(draw, (250, 90), TITLE, font_title, (255, 255, 255, 255), (160, 50, 5, 255), outline_width=6)

    # Cute icons top left & top right
    draw_grad_cap(draw, 220, 130, 90)
    draw_sunflower(draw, W - 225, 130, 48)

    # Subtitle / Inspiring winter motto
    font_sub = get_font(FONT_JH_BOLD, 36)
    draw_text_with_outline(draw, (W//2 - 270, 225), "✨ 冬陽暖心・活到老學到老・友誼常青 ✨", font_sub, (180, 75, 10, 255), (255, 255, 255, 255), outline_width=4)

    # Bottom decorations: Golden warmth & flowers
    draw_sunflower(draw, 140, H - 140, 65)
    draw_sunflower(draw, 230, H - 110, 45)
    draw_sunflower(draw, W - 140, H - 140, 65)
    draw_sunflower(draw, W - 230, H - 110, 45)

    # Bottom cheer banner
    font_bottom = get_font(FONT_KAI, 46)
    draw.rounded_rectangle([W//2 - 320, H - 120, W//2 + 320, H - 45], radius=25, fill=(245, 166, 35, 255), outline=(255, 255, 255, 255), width=4)
    draw_text_with_outline(draw, (W//2 - 275, H - 112), "🎓 恭喜結業・迎向活力新篇章 🌟", font_bottom, (255, 255, 255, 255), (140, 50, 0, 255), outline_width=3)

    return img

# -------------------------------------------------------------
# FRAME 2: 喜慶溫馨・新春紅韻 (Joyful Festive Red & Warm Blessings)
# -------------------------------------------------------------
def make_frame_festive():
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    hole_w, hole_h = 1320, 780
    hole_x = (W - hole_w) // 2
    hole_y = 280

    # Festive Red border with gold trim (Warm 12-month winter celebration)
    draw.rounded_rectangle([40, 30, W - 40, H - 30], radius=45, fill=(255, 245, 245, 255), outline=(215, 45, 45, 255), width=12)
    draw.rounded_rectangle([hole_x - 14, hole_y - 14, hole_x + hole_w + 14, hole_y + hole_h + 14], radius=28, fill=(255, 235, 235, 255), outline=(220, 60, 60, 255), width=8)

    # Cut out center hole
    for y in range(hole_y, hole_y + hole_h):
        for x in range(hole_x, hole_x + hole_w):
            img.putpixel((x, y), (0, 0, 0, 0))

    draw = ImageDraw.Draw(img)

    # Top Royal Red & Gold Crest
    draw.rounded_rectangle([180, 50, W - 180, 210], radius=40, fill=(200, 30, 40, 255), outline=(255, 215, 0, 255), width=6)
    draw.rounded_rectangle([190, 60, W - 190, 200], radius=32, fill=(225, 40, 50, 255))

    # Title Text (Calligraphy Kaiu with Gold & White glow)
    font_title = get_font(FONT_KAI, 82)
    draw_text_with_outline(draw, (240, 85), TITLE, font_title, (255, 245, 180, 255), (110, 10, 15, 255), outline_width=6)

    draw_grad_cap(draw, 220, 130, 95)
    # Lantern / Lucky icon top right
    draw.ellipse([W - 245, 95, W - 185, 165], fill=(245, 180, 0, 255), outline=(255, 255, 255, 255), width=3)
    draw_text_with_outline(draw, (W - 232, 105), "福", get_font(FONT_KAI, 46), (180, 20, 20, 255), (255, 255, 255, 255), outline_width=2)

    # Subtitle
    font_sub = get_font(FONT_JH_BOLD, 36)
    draw_text_with_outline(draw, (W//2 - 270, 225), "🌸 圓滿結業・歲月添福・平安喜樂 🌸", font_sub, (180, 30, 30, 255), (255, 255, 255, 255), outline_width=4)

    # Bottom cheer banner
    font_bottom = get_font(FONT_JH_BOLD, 44)
    draw.rounded_rectangle([W//2 - 340, H - 120, W//2 + 340, H - 45], radius=25, fill=(200, 30, 40, 255), outline=(255, 215, 0, 255), width=5)
    draw_text_with_outline(draw, (W//2 - 300, H - 110), "❤️ 快樂學習每一天・我們結業啦！ 🎉", font_bottom, (255, 255, 255, 255), (100, 10, 15, 255), outline_width=3)

    return img

# -------------------------------------------------------------
# FRAME 3: 晴空希望・生機繁花 (Fresh Hope Sky & Blooming Garden)
# -------------------------------------------------------------
def make_frame_fresh():
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    hole_w, hole_h = 1320, 780
    hole_x = (W - hole_w) // 2
    hole_y = 280

    # Fresh Cyan & Emerald Green Border (Symbolizing Spring renewal & vibrant energy)
    draw.rounded_rectangle([40, 30, W - 40, H - 30], radius=45, fill=(240, 252, 255, 255), outline=(20, 160, 180, 255), width=12)
    draw.rounded_rectangle([hole_x - 14, hole_y - 14, hole_x + hole_w + 14, hole_y + hole_h + 14], radius=28, fill=(230, 248, 255, 255), outline=(30, 175, 140, 255), width=8)

    # Cut out center hole
    for y in range(hole_y, hole_y + hole_h):
        for x in range(hole_x, hole_x + hole_w):
            img.putpixel((x, y), (0, 0, 0, 0))

    draw = ImageDraw.Draw(img)

    # Top Cyan-Green Ribbon
    draw.rounded_rectangle([180, 50, W - 180, 210], radius=40, fill=(15, 155, 175, 255), outline=(255, 255, 255, 255), width=6)
    draw.rounded_rectangle([190, 60, W - 190, 200], radius=32, fill=(25, 175, 195, 255))

    # Title Text
    font_title = get_font(FONT_JH_BOLD, 74)
    draw_text_with_outline(draw, (250, 90), TITLE, font_title, (255, 255, 255, 255), (10, 85, 100, 255), outline_width=6)

    draw_grad_cap(draw, 220, 130, 90)
    # Bright sun top right
    draw.ellipse([W - 245, 95, W - 185, 155], fill=(255, 215, 0, 255), outline=(255, 255, 255, 255), width=4)

    # Subtitle
    font_sub = get_font(FONT_JH_BOLD, 36)
    draw_text_with_outline(draw, (W//2 - 270, 225), "🌱 擁抱新知・常保青春・迎向燦爛陽光 🌱", font_sub, (15, 120, 135, 255), (255, 255, 255, 255), outline_width=4)

    # Bottom cheerful banner
    font_bottom = get_font(FONT_JH_BOLD, 44)
    draw.rounded_rectangle([W//2 - 320, H - 120, W//2 + 320, H - 45], radius=25, fill=(20, 165, 135, 255), outline=(255, 255, 255, 255), width=5)
    draw_text_with_outline(draw, (W//2 - 280, H - 110), "🌻 結業不是終點，而是精彩新起點 🎈", font_bottom, (255, 255, 255, 255), (5, 90, 70, 255), outline_width=3)

    return img

print("Rendering frames...")
f1 = make_frame_warmth()
f1.save("d:/Work/拍貼機/frames/frame_warm_sunshine.png")
print("Saved frame_warm_sunshine.png")

f2 = make_frame_festive()
f2.save("d:/Work/拍貼機/frames/frame_festive_celebration.png")
print("Saved frame_festive_celebration.png")

f3 = make_frame_fresh()
f3.save("d:/Work/拍貼機/frames/frame_fresh_hope.png")
print("Saved frame_fresh_hope.png")
