
import requests
import time
while True:
    payload = {
        'content': "Automate ur message and send offers every 3 mins for 24/7 \n| NEW Program, 100% working, DM me"
    }

    header = {
        'authorization': 'NzA3NTQ1MDExMTY3ODIxODM2.GALws2.bwvgs8H-8tKREM3B5D15KsuBRkqyaLuDk6P6IU'
    }

    r = requests.post("https://discord.com/api/v9/channels/1512305081008128091/messages",

                        data=payload, headers=header)
    r = requests.post("https://discord.com/api/v9/channels/812908225405255703/messages",

    data=payload, headers=header)
    
    time.sleep(10)
      # https://discord.com/api/v9/channels/1512305081008128091/messages
