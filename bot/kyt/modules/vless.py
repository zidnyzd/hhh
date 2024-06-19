from kyt import *

import subprocess
import datetime as DT
import re
from telethon import events, Button
from kyt import bot, valid

@bot.on(events.CallbackQuery(data=b'create-vless'))
async def create_vless(event):
    async def create_vless_(event):
        try:
            async with bot.conversation(chat) as user:
                await event.respond('**Username:**')
                user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
                user = (await user).raw_text
            async with bot.conversation(chat) as pw:
                await event.respond("**Quota:**")
                pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
                pw = (await pw).raw_text
            async with bot.conversation(chat) as exp:
                await event.respond("**Choose Expiry Day**", buttons=[
                    [Button.inline(" 3 Day ", "3"),
                     Button.inline(" 7 Day ", "7")],
                    [Button.inline(" 30 Day ", "30"),
                     Button.inline(" 60 Day ", "60")]])
                exp = exp.wait_event(events.CallbackQuery)
                exp = (await exp).data.decode("ascii")
            async with bot.conversation(chat) as ip_limit:
                await event.respond("**Limit User (IP):**")
                ip_limit = ip_limit.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
                ip_limit = (await ip_limit).raw_text

            await event.edit("Processing.")
            await event.edit("Processing..")
            await event.edit("Processing...")
            await event.edit("Processing....")
            time.sleep(3)
            await event.edit("`Processing Create Premium Account`")
            time.sleep(1)
            await event.edit("`Processing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
            time.sleep(1)
            await event.edit("`Processing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
            time.sleep(2)
            await event.edit("`Processing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
            time.sleep(3)
            await event.edit("`Processing... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
            time.sleep(2)
            await event.edit("`Processing... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
            time.sleep(1)
            await event.edit("`Processing... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `")
            time.sleep(1)
            await event.edit("`Processing... 84%\n█████████████████████▒▒▒▒ `")
            time.sleep(0)
            await event.edit("`Processing... 100%\n█████████████████████████ `")
            time.sleep(1)
            await event.edit("`Wait.. Setting up an Account`")

            # Run the addvless script
            cmd = f'printf "%s\n" "{user}" "{exp}" "{pw}" "{ip_limit}" | addvless'
            print(f"Executing command: {cmd}")  # Debugging
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                shell=True
            )
            a = result.stdout
            print(f"Command output: {a}")  # Debugging

            # Check if user already exists
            if "already exists" in a.lower():
                await event.respond("**User Already Exist**")
                return
            elif "error" in a.lower():
                await event.respond("**Error Occurred**")
                return

            # Process output
            today = DT.date.today()
            later = today + DT.timedelta(days=int(exp))
            x = [x.group() for x in re.finditer("vless://(.*)", a)]
            print(f"Parsed URLs: {x}")
            uuid = re.search("vless://(.*?)@", x[0]).group(1)

            msg = f"""
**━━━━━━━━━━━━━━━━━**
**🇬🇧 Xray/Vless Account 🇬🇧**
**━━━━━━━━━━━━━━━━━**
**» Remarks     :** `{user}`
**» Host Server :** `{DOMAIN}`
**» User Quota  :** `{pw} GB`
**» port TLS    :** `443, 8443`
**» Port NTLS   :** `80, 8080, 2082`
**» NetWork     :** `(WS) or (gRPC)`
**» User ID     :** `{uuid}`
**» Path Vless  :** `(/multi path)/vless`
**» Path Dynamic:** `http://BUG.COM/vless`
**━━━━━━━━━━━━━━━━━**
**» Link TLS   : **
`{x[0]}`
**━━━━━━━━━━━━━━━━━**
**» Link NTLS  :**
`{x[1].replace(" ","")}`
**━━━━━━━━━━━━━━━━━**
**» Link GRPC  :**
`{x[2].replace(" ","")}`
**━━━━━━━━━━━━━━━━━**
**» Format OpenClash :** https://{DOMAIN}:81/vless-{user}.txt
**━━━━━━━━━━━━━━━━━**
**» Expired Until:** `{later}`
**» 🤖@storezid**
"""
            await event.respond(msg)

        except subprocess.CalledProcessError as e:
            await event.respond("**Error Occurred**")
            print(f"Error output: {e.stderr}")  # Debugging

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))
    if a == "true":
        await create_vless_(event)
    else:
        await event.answer("Akses Ditolak", alert=True)

@bot.on(events.CallbackQuery(data=b'cek-vless'))
async def cek_vless(event):
    async def cek_vless_(event):
        cmd = 'bot-cek-vless'.strip()
        x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        print(x)
        z = subprocess.check_output(cmd, shell=True).decode("utf-8")
        await event.respond(f"""
{z}

**Shows Logged In Users Vless**
**» 🤖@ghoibvpnn**
""", buttons=[[Button.inline("‹ Main Menu ›", "menu")]])
    sender = await event.get_sender()
    a = valid(str(sender.id))
    if a == "true":
        await cek_vless_(event)
    else:
        await event.answer("Access Denied", alert=True)

@bot.on(events.CallbackQuery(data=b'delete-vless'))
async def delete_vless(event):
    async def delete_vless_(event):
        async with bot.conversation(chat) as user:
            await event.respond('**Username:**')
            user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = (await user).raw_text
        cmd = f'printf "%s\n" "{user}" | delvless'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except:
            await event.respond("**User Not Found**")
        else:
            msg = f"""**Successfully Deleted**"""
            await event.respond(msg)
    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))
    if a == "true":
        await delete_vless_(event)
    else:
        await event.answer("Akses Ditolak", alert=True)

@bot.on(events.CallbackQuery(data=b'trial-vless'))
async def trial_vless(event):
    async def trial_vless_(event):
        async with bot.conversation(chat) as exp:
            await event.respond("**Choose Expiry Minutes**", buttons=[
                [Button.inline(" 10 Menit ", "10"),
                 Button.inline(" 15 Menit ", "15")],
                [Button.inline(" 30 Menit ", "30"),
                 Button.inline(" 60 Menit ", "60")]])
            exp = exp.wait_event(events.CallbackQuery)
            exp = (await exp).data.decode("ascii")
        async with bot.conversation(chat) as ip_limit:
            await event.respond("**Limit User (IP):**")
            ip_limit = ip_limit.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            ip_limit = (await ip_limit).raw_text

        await event.edit("Processing.")
        await event.edit("Processing..")
        await event.edit("Processing...")
        await event.edit("Processing....")
        time.sleep(3)
        await event.edit("`Processing Create Premium Account`")
        time.sleep(1)
        await event.edit("`Processing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(1)
        await event.edit("`Processing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(2)
        await event.edit("`Processing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(3)
        await event.edit("`Processing... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(2)
        await event.edit("`Processing... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(1)
        await event.edit("`Processing... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(1)
        await event.edit("`Processing... 84%\n█████████████████████▒▒▒▒ `")
        time.sleep(0)
        await event.edit("`Processing... 100%\n█████████████████████████ `")
        time.sleep(1)
        await event.edit("`Wait.. Setting up an Account`")
        try:
            cmd = f'printf "%s\n" "{exp}" "{ip_limit}" | trialvless'
            print("Executing command:", cmd)  # Debugging
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                shell=True,
                check=True
            )
            a = result.stdout
            print("Command output:", a)  # Debugging
        except subprocess.CalledProcessError as e:
            await event.respond("**User Already Exist or Error Occurred**")
            print(e.stderr)  # Debugging
            return
        
        x = [x.group() for x in re.finditer("vless://(.*)", a)]
        print(x)
        remarks = re.search("#(.*)", x[0]).group(1)
        uuid = re.search("vless://(.*?)@", x[0]).group(1)
        msg = f"""
**━━━━━━━━━━━━━━━━━**
**🇬🇧 Xray/Vless Account 🇬🇧**
**━━━━━━━━━━━━━━━━━**
**» Remarks     :** `{remarks}`
**» Host Server :** `{DOMAIN}`
**» User Quota  :** `Unlimited`
**» Port DNS    :** `443, 53`
**» port TLS    :** `222-1000`
**» Port NTLS   :** `80, 8080, 8081-9999`
**» NetWork     :** `(WS) or (gRPC)`
**» User ID     :** `{uuid}`
**» Path Vless  :** `(/multi path)/vless `
**» Path Dynamic:** `http://BUG.COM/vless `
**━━━━━━━━━━━━━━━━━**
**» Link TLS   : **
`{x[0]}`
**━━━━━━━━━━━━━━━━━**
**» Link NTLS  :**
`{x[1].replace(" ","")}`
**━━━━━━━━━━━━━━━━━**
**» Link GRPC  :**
`{x[2].replace(" ","")}`
**━━━━━━━━━━━━━━━━━**
**» Expired Until :** `{exp} Minutes`
**» 🤖@ghoibvpnn**
"""
        await event.respond(msg)
    
    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))
    if a == "true":
        await trial_vless_(event)
    else:
        await event.answer("Akses Ditolak", alert=True)

@bot.on(events.CallbackQuery(data=b'vless'))
async def vless(event):
    async def vless_(event):
        inline = [
            [Button.inline(" TRIAL VLESS ", "trial-vless"), Button.inline(" CREATE VLESS ", "create-vless")],
            [Button.inline(" CHECK VLESS ", "cek-vless"), Button.inline(" DELETE VLESS ", "delete-vless")],
            [Button.inline("‹ Main Menu ›", "menu")]
        ]
        z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
        msg = f"""
━━━━━━━━━━━━━━━━━━━━━━━ 
**🇬🇧 VLESS MANAGER 🇬🇧**
━━━━━━━━━━━━━━━━━━━━━━━ 
🔰 **» Service:** `VLESS`
🔰 **» Hostname:** `{DOMAIN}`
🔰 **» ISP:** `{z["isp"]}`
🔰 **» Country:** `{z["country"]}`
━━━━━━━━━━━━━━━━━━━━━━━ 
"""
        await event.edit(msg, buttons=inline)
    sender = await event.get_sender()
    a = valid(str(sender.id))
    if a == "true":
        await vless_(event)
    else:
        await event.answer("Access Denied", alert=True)

