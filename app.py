from instagrapi import Client
import os
import time
from keepalive import keep_alive

keep_alive()

my_bot = Client()


ins_caption = "-\n-\nπ’π¬π»πΈπ΅π΅ β\n\n\n(Β―Β΄β’._.β’ π πΈπβπΏπΎ β π β’._.β’Β΄Β―( \n\nβLβoβaβdβiβnβgβ \n\n_____πΌπ  ΞΉαΆ°Ε£πβδΉβ’π­π¦ΕαΆ  ππ­______ \n.\n. \nο½ο½ο½ο½ο½ο½ο½ο½ \n- \n- \n- \n#trending #viral #instagram #explore #instagood #love #tiktok #explorepage #fashion #tiktok #reels #beautiful #cute #follow #selfie #art #friends #nature #girl #style #blogger #food #travel #photography #photooftheday #instadaily #fitness #me #fun #smile "

my_bot.login(username="*****", password="*****")

img_dir = "imgs"

for i in os.listdir(img_dir):
    img_path = os.path.join(img_dir, i)
    my_bot.photo_upload(path=f'{img_path}', caption=ins_caption)
    # Delete Uploaded File
    try:
        os.remove(img_path)
    except:
        pass
    #sleep For 4 Hours
    time.sleep(14400)
