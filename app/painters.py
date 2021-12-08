import textwrap
from PIL import Image, ImageDraw, ImageFont
from textwrap import wrap

BASE_COLOR = (255, 255, 255, 255)

def draw_lvlup(uid: int, level: int):
    w, h = 130, 140
    # Fonts
    font_xp = ImageFont.truetype("app/fonts/Comfortaa-Light.ttf", 22)
    font_name = ImageFont.truetype("app/fonts/Roboto-Bold.ttf", 25)
    # ---------------------------
    # User avatar
    pfp_img = Image.open(f"app/images/avatars/{uid}.png").resize((w//2, h//2))
    # ---------------------------
    # Background and lvlup element images
    bg_img = Image.open("app/images/backgrounds/lvlup/default_lvlup.png").convert("RGBA")
    # ---------------------------

    background = Image.new("RGBA", (w, h))
    background_draw = ImageDraw.Draw(background)
    background.paste(bg_img, (0, 0), bg_img)
    background_draw.rectangle((0, 65, w, h), fill="white", width=1)

    pfp_bg = Image.new("RGBA", (w//2, h//2), BASE_COLOR)
    pfp_mask = Image.new("L", (w//2, h//2), 0)
    pfp_mask_draw = ImageDraw.Draw(pfp_mask)
    pfp_mask_draw.rounded_rectangle((0, 0, w//2, h//2), fill=255, radius=7)
    pfp = Image.composite(pfp_img, pfp_bg, pfp_mask)
    background.paste(pfp, (34, 20), pfp)

    up_text = Image.new("RGBA", (w, h))
    up_text_draw = ImageDraw.Draw(up_text)
    up_text_draw.text((0, 0), "LEVEL UP!", fill="black", font=font_xp)
    background.paste(up_text, (8, 91), up_text)

    x, y = 0, 0
    if len(str(level)) == 1:
        x, y = 37, 110
    elif len(str(level)) == 2:
        x, y = 30, 110
    else:
        x, y = 23, 110

    lvl_text = Image.new("RGBA", (130, 140))
    lvl_text_draw = ImageDraw.Draw(lvl_text)
    lvl_text_draw.text((0, 0), f"LVL {level}", fill="black", font=font_name)
    background.paste(lvl_text, (x, y), lvl_text)

    background.save(f"app/images/lvlups/{uid}.png")
    
    
def draw_profile(uid: int, name:str, lvl: int, current_exp: int, next_lvl_exp: int, place: int, reps: int, description: str):
    W, H = 580, 580
    standard_text_color = (80,80,80)
    # Fonts
    font_xp = ImageFont.truetype("app/fonts/Roboto-Regular.ttf", 16)
    font_name = ImageFont.truetype("app/fonts/Roboto-Bold.ttf", 50)
    font_rep = ImageFont.truetype("app/fonts/Roboto-Regular.ttf", 38)
    font_levelt = ImageFont.truetype("app/fonts/Roboto-Regular.ttf", 30)
    font_level = ImageFont.truetype("app/fonts/Roboto-Bold.ttf", 60)
    font_info = ImageFont.truetype("app/fonts/Roboto-Regular.ttf", 22)
    font_abtme_title = ImageFont.truetype("app/fonts/Roboto-Bold.ttf", 22)
    font_abtme_text = ImageFont.truetype("app/fonts/Roboto-Regular.ttf", 16)
    # ---------------------------
    # User avatar
    pfp_img = Image.open(f"app/images/avatars/{uid}.png").resize((148, 148))
    # ---------------------------
    # Background and lvlup element images
    bg_img = Image.open("app/images/backgrounds/profile/default_profile.png").convert("RGBA")
    # ---------------------------
    
    background = Image.new("RGBA", (W, H))
    background.paste(bg_img, (0, 0), bg_img)
    
    rectangle = Image.new("RGBA", (W, H))
    rdraw = ImageDraw.Draw(rectangle)
    rdraw.rectangle((10, 267, 569, 200), fill=(5,5,5,200), outline=None) # nickname and title bar
    rdraw.rectangle((10, 268, 184, 327), fill=(153,255,170,200), outline=None) # reputation bar
    rdraw.rectangle((10, 328, 184, 569), fill=(80,80,80,200), outline=None) # achievements bar
    rdraw.rectangle((185, 268, 569, 569), fill=(255, 255, 255, 210), outline=None) # info tab
    rdraw.rectangle((198, 436, 556, 438), fill=standard_text_color, outline=None)
    rdraw.rectangle((22, 274, 171, 125), fill="white", outline=None) # avatar holder
    rectangle.paste(pfp_img, (23, 126)) # avatar
    background.paste(rectangle, mask=rectangle)
    
    lvl_progress = Image.new("RGBA", (359, 32))
    lvl_prog_draw = ImageDraw.Draw(lvl_progress)
    lvl_prog_draw.rectangle((0, 0, 358, 31), fill="white", outline=(120,120,120), width=2) # level progress bar
    percentage = round(current_exp / next_lvl_exp, 2)
    percentage = 0.02 if percentage == 0.0 or percentage == 0.01 else percentage # fix of filler going out of bounds backwards
    width = percentage * 358 if percentage != 1 else 353
    lvl_prog_draw.rectangle((5, 5, width, 26), fill=(153,255,170), outline=None) # level progress filler
    xp_text = f"XP: {current_exp}/{next_lvl_exp}"
    w, h = lvl_prog_draw.textsize(xp_text, font=font_xp)
    lvl_prog_draw.text(((359 - w) / 2, (31 - h) / 2), xp_text, fill=standard_text_color, font=font_xp) 
    background.paste(lvl_progress, (198, 284))
    
    nickname = Image.new("RGBA", (W, H))
    nickname_draw = ImageDraw.Draw(nickname)
    name = f"{name[:11]}..." if len(name) > 11 else name
    nickname_draw.text((190, 205), name, fill="white", font=font_name)
    background.paste(nickname, mask=nickname)
    
    rep = Image.new("RGBA", (184, 327))
    rep_draw = ImageDraw.Draw(rep)
    rep_text = f"REP {reps}"
    w, h = rep_draw.textsize(rep_text, font=font_rep)
    rep_draw.text(((195 - w) / 2, 275), rep_text, fill="white", font=font_rep)
    background.paste(rep, mask=rep)
    
    infotab_text = Image.new("RGBA", (569, 569))
    infotab_text_draw = ImageDraw.Draw(infotab_text)
    infotab_text_draw.text((12, 67), text="LEVEL", fill=standard_text_color, font=font_levelt)
    infotab_text_draw.text((50, 110), text=str(lvl), fill=standard_text_color, font=font_level, anchor="mt")
    infotab_text_draw.text((110, 70), text="Server Rank", fill=standard_text_color, font=font_info)
    infotab_text_draw.text((110, 100), text="Achievements", fill=standard_text_color, font=font_info)
    infotab_text_draw.text((110, 130), text="XP Till Next LVL", fill=standard_text_color, font=font_info)
    infotab_text_draw.text((375, 90), text=f"# {place}", fill=standard_text_color, font=font_info, anchor="rs")
    infotab_text_draw.text((375, 120), text="Soon", fill=standard_text_color, font=font_info, anchor="rs")
    infotab_text_draw.text((375, 150), text=f"{next_lvl_exp - current_exp}", fill=standard_text_color, font=font_info, anchor="rs")
    infotab_text_draw.text((12, 173), text="About me", fill=standard_text_color, font=font_abtme_title)
    # TODO: Make new limit of 255 characters
    description = "Beep Boop, description!" if description == None else description
    textwraped = wrap(description, width=54)
    infotab_text_draw.text((193, 213), text="\n".join(textwraped), fill=standard_text_color, font=font_abtme_text, anchor="ms")
    background.paste(infotab_text, (185, 268), mask=infotab_text)
    
    background.save(f"app/images/profiles/{uid}.png")