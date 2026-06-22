

import math
import random

import requests
import time
while True:
    payload = {
        'content': "name: Qrezn \n Looking for bunny ears, upgrading I have 40k\n click to send a trade send ANYTHING i will A/C: https://www.roblox.com/users/136106879/trade \n https://media.discordapp.net/attachments/442709710408515605/1518432847671591062/image.png?ex=6a39e64a&is=6a3894ca&hm=d9d3c65ca7cbf0312800c8a777144bcbdc5b077a541dda9c5dcd89ab842b745f&=&format=webp&quality=lossless&width=459&height=312 "
    } 

    header = {
        'authorization': "NzA3NTQ1MDExMTY3ODIxODM2.G3zyoD.2HWQzLm3pqAVuagR3o-LX5kY2fIxBjpYYxlVhE"
    }
    r = requests.post("https://discord.com/api/v9/channels/442709710408515605/messages",

    data=payload, headers=header)
    
    time.sleep(random.randint(1, 10))
      # https://discord.com/api/v9/channels/1512305081008128091/messages
