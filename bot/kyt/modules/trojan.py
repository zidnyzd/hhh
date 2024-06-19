from kyt import *

# CREATE TROJAN
@bot.on(events.CallbackQuery(data=b'create-trojan'))
async def create_trojan(event):
    async def create_trojan_(event):
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
                [Button.inline(" 3 Day ", "3"), Button.inline(" 7 Day ", "7")],
                [Button.inline(" 30 Day ", "30"), Button.inline(" 60 Day ", "60")]
            ])
            exp = exp.wait_event(events.CallbackQuery)
            exp = (await exp).data.decode("ascii")
        async with bot.conversation(chat) as ip_limit:
            await event.respond("**IP Limit:**")
            ip_limit = ip_limit.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            ip_limit = (await ip_limit).raw_text
        await event.edit("Processing...")
        time.sleep(3)
        cmd = f'printf "%s\n" "{user}" "{exp}" "{pw}" "{ip_limit}" | addtr'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
            print(f"Command output: {a}")  # Debug print
        except subprocess.CalledProcessError:
            await event.respond("**User Already Exist or Error Occurred**")
            return
        today = DT.date.today()
        later = today + DT.timedelta(days=int(exp))
        b = [x.group() for x in re.finditer("trojan://(.*)", a)]
        print(f"Regex matches: {b}")  # Debug print
        if not b:
            await event.respond("**Error: No matches found in the command output**")
            return
        remarks_match = re.search("#(.*)", b[0])
        domain_match = re.search("@(.*?):", b[0])
        uuid_match = re.search("trojan://(.*?)@", b[0])
        if not remarks_match or not domain_match or not uuid_match:
            await event.respond("**Error: Expected data not found in the command output**")
            return
        remarks = remarks_match.group(1)
        domain = domain_match.group(1)
        uuid = uuid_match.group(1)
        msg = f"""
**━━━━━━━━━━━━━━━━━**
**🇬🇧 Xray/Trojan Account 🇬🇧**
**━━━━━━━━━━━━━━━━━**
**» Remarks     :** `{remarks}`
**» Host Server :** `{domain}`
**» Host XrayDNS:** `{HOST}`
**» User Quota  :** `{pw} GB`
**» Port DNS    :** `443, 53`
**» port TLS    :** `222-1000`
**» Port NTLS   :** `80, 8080, 8081-9999`
**» NetWork     :** `(WS) or (gRPC)`
**» User ID     :** `{uuid}`
**» Path Trojan :** `(/multi path)/trojan-ws`
**» Path Dynamic:** `http://BUG.COM/trojan-ws`
**━━━━━━━━━━━━━━━━━**
**» Link TLS   : **
`{b[0]}`
**━━━━━━━━━━━━━━━━━**
**» Link NTLS  :**
`{b[1].replace(" ","")}`
**━━━━━━━━━━━━━━━━━**
**» Link GRPC  :**
`{b[2].replace(" ","")}`
**━━━━━━━━━━━━━━━━━**
**» Format OpenClash :** https://{DOMAIN}:81/trojan-{user}.txt
**━━━━━━━━━━━━━━━━━**
**» Expired Until:** `{later}`
**» 🤖@ghoibvpnn**
"""
        await event.respond(msg)
    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))
    if a == "true":
        await create_trojan_(event)
    else:
        await event.answer("Akses Ditolak", alert=True)


#CEK TROJAN
@bot.on(events.CallbackQuery(data=b'cek-trojan'))
async def cek_trojan(event):
    async def cek_trojan_(event):
        cmd = 'bot-cek-tr'.strip()
        x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        print(x)
        z = subprocess.check_output(cmd, shell=True).decode("utf-8")
        await event.respond(f"""
{z}
**Shows Logged In Users Trojan**
**» 🤖@ghoibvpnn**
""", buttons=[[Button.inline("‹ Main Menu ›", "menu")]])
    sender = await event.get_sender()
    a = valid(str(sender.id))
    if a == "true":
        await cek_trojan_(event)
    else:
        await event.answer("Access Denied", alert=True)

@bot.on(events.CallbackQuery(data=b'delete-trojan'))
async def delete_trojan(event):
    async def delete_trojan_(event):
        async with bot.conversation(chat) as user:
            await event.respond('**Username:**')
            user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = (await user).raw_text
        cmd = f'printf "%s\n" "{user}" | deltr'
        try:
            a = subprocess.check_output(cmd, shell=True, env=os.environ).decode("utf-8")
        except subprocess.CalledProcessError:
            await event.respond("**User Not Found**")
        else:
            msg = f"""**Successfully Deleted**"""
            await event.respond(msg)
    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))
    if a == "true":
        await delete_trojan_(event)
    else:
        await event.answer("Akses Ditolak", alert=True)

@bot.on(events.CallbackQuery(data=b'trojan'))
async def trojan(event):
    async def trojan_(event):
        inline = [
            [Button.inline(" TRIAL TROJAN ", "trial-trojan"),
             Button.inline(" CREATE TROJAN ", "create-trojan")],
            [Button.inline(" CHECK TROJAN ", "cek-trojan"),
             Button.inline(" DELETE TROJAN ", "delete-trojan")],
            [Button.inline("‹ Main Menu ›", "menu")]
        ]
        z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
        msg = f"""
━━━━━━━━━━━━━━━━━━━━━━━ 
**🇬🇧 TROJAN MANAGER 🇬🇧**
━━━━━━━━━━━━━━━━━━━━━━━ 
🔰 **» Service:** `TROJAN`
🔰 **» Hostname** `{DOMAIN}`
🔰 **» ISP:** `{z["isp"]}`
🔰 **» Country:** `{z["country"]}`
━━━━━━━━━━━━━━━━━━━━━━━ 
"""
        await event.edit(msg, buttons=inline)
    sender = await event.get_sender()
    a = valid(str(sender.id))
    if a == "true":
        await trojan_(event)
    else:
        await event.answer("Access Denied", alert=True)

