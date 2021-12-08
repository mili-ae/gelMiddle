from io import BytesIO
import operator

import requests
from PIL import Image


def image_check(url):
    file_name_for_regular_data = url.replace("https://", "").split("/")[2]
    
    resp = requests.get(url)
    img = Image.open(BytesIO(resp.content)).convert("RGB")
    file_name = file_name_for_regular_data + ".png"
    img.save(f"images/avatars/{file_name}", "png")
    
def calculate_place(db, user_id, guild_id):
        guild_db = db[str(guild_id)]
        userlist = list(guild_db.find())
        users = []
        
        for i in range(len(userlist)):
            try:
                uid = userlist[i]["_id"]
                level = userlist[i]["level"]
                users.append((uid, level))
            except:
                return "FTGPerr" #failed to get place

        sorted_list = sorted(users, key=operator.itemgetter(1), reverse=True)
 
        rank = 1
        for stats in sorted_list:
            if stats[0] == user_id:
                return rank
            rank += 1
