from instagrapi import Client
import os
import time

my_bot = Client()

ins_caption = "-\n-\n𝓢𝓬𝓻𝓸𝓵𝓵 →\n\n\n(¯´•._.• 🎀 𝐸𝓂❀𝒿𝒾 → 🎀 •._.•´¯( \n\n░L░o░a░d░i░n░g░ \n\n_____🐼👊  ιᶰţ𝒆Ⓡ乇ⓢ𝐭𝔦ŇᎶ  🏆🍭______ \n.\n. \nｈａｓｈｔａｇｓ \n- \n- \n- \n#trending #viral #instagram #explore #instagood #love #tiktok #explorepage #fashion #tiktok #reels #beautiful #cute #follow #selfie #art #friends #nature #girl #style #blogger #food #travel #photography #photooftheday #instadaily #fitness #me #fun #smile "
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
    #sleep For 4.8 Hours
    time.sleep(17280)
