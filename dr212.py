#RENGGA===Version SB

import linepy
from linepy import *
from akad.ttypes import *
from datetime import datetime
import pytz, pafy, time, asyncio, random, multiprocessing, timeit, sys, json, ctypes, codecs, tweepy, threading, glob, re, ast, six, os, subprocess, wikipedia, atexit, urllib, urllib.parse, urllib3, string, tempfile, shutil, unicodedata
from humanfriendly import format_timespan, format_size, format_number, format_length
import html5lib
import requests,json,urllib3
from random import randint
from bs4 import BeautifulSoup
#from gtts import gTTS
from googletrans import Translator
import youtube_dl
from time import sleep
from zalgo_text import zalgo
from threading import Thread,Event
import requests,uvloop
import wikipedia as wiki
requests.packages.urllib3.disable_warnings()
loop = uvloop.new_event_loop()
#==============================================================================#
botStart = time.time()
msg_dict = {}
msg_dict1 = {}
#==============[ token 1 ]==============#
cl = LINE("EGfpnNRfSbvaL2z6ohu5.waHPajN9z7cwv0IV5lq1zq.gPqV6274k7c48DbmK9njHeGKpusf8hBehMKGLesR+Xo=")
cl.log("Auth Token : " + str(cl.authToken))
cl.log("Timeline Token : " + str(cl.tl.channelAccessToken))

#ki = LINE("ECdm6SBDFcSQbB92wzX5.1PdWISfJEQ4F83O0j89lDq.JodVBppuZDrGubzT5z2f0aDSMKYdjL8JVkK68+IV8Dk=")
#ki.log("Auth Token : " + str(ki.authToken))
#ki.log("Timeline Token : " + str(ki.tl.channelAccessToken))

#kk = LINE("ECAwXp5sPIBzbr4OUbLc.hWg0o07213VLVCn7xM25Ra.baCad+HAHXkLT+fvWaAiMb1XpJhX1WslmRPBrm3r1d8=")
#kk.log("Auth Token : " + str(kk.authToken))
#kk.log("Timeline Token : " + str(kk.tl.channelAccessToken))

#kc = LINE("ECsvzXirmdEkBI6I05q2.8MR2Nwc8pKJ7uYeNTWsieG.1SCO8Kgzzd6xIpvc/5Kf5VbszTV4IIQv244nW1uH0Ac=")
#kc.log("Auth Token : " + str(kc.authToken))

#ko = LINE("ECT0USVbXIyy6LG2LSo9.ldVvgada5Tbn2m08z3h2kq.+PtjyMtcVdEGS1rHhAOkhqBFJ2WrwVSk9oeSIxZs7sc=")
#ko.log("Auth Token : " + str(ko.authToken))

#jk = LINE("ECW6O4s19hZIZrkUAji8.bds4TzCfqnYz5+yCG41iAa.MyfOJlBtObcxpKpAkn/l5rHAZremhCFmFA1kG7MZkn0=")
#jk.log("Auth Token : " + str(jk.authToken))

#sw = LINE("ECQAqe2syyJWB4P8Omk7.gRXSPo8nFcRN2ReIOJpnPW.QLsJW4YQfEUD3P1L0EBxDtOIW7LvfpflPnLgRvgh3rc=")
#sw.log("Auth Token : " + str(sw.authToken))
#==============[●●●●●●]==============#
print ("\n\
                     ========     \n\
                      ======     \n\
                       ====     \n")
print (" ======== THANKS TO ALLOH SWT --------")
print (" ======== THANKS TO PY3 ========")
print (" ======== KEEP STAY AND RULLES ========")
print ("\n\
   =======================    =======    ===========          \n\
   =======================      ====    =============      \n\
           ========              ==    ======    =====      \n\
           ========                   ======      ======    \n\
           ========                  ======        ======   \n\
           ========                 ======          ======  \n\
           ========                ======================== \n\
           ========               ========================== \n\
           ========              ======                ======\n\
         ============          =========              =========\n")
print ("=========== LOGIN SUCSES ==========")

oepoll = OEPoll(cl)

mid = cl.profile.mid
mid = cl.getProfile().mid
#Amid = ki.getProfile().mid
#Bmid = kk.getProfile().mid
#Cmid = kc.getProfile().mid
#Dmid = ko.getProfile().mid
#Emid = jk.getProfile().mid
#Zmid = sw.getProfile().mid
#===========================================================================================
KAC = [cl]
ABC = [cl]
Bots = [mid]
creator = ["u5808690099fd67b0965748afe4b43565"]
owner = ["u5808690099fd67b0965748afe4b43565"]
admin = ["u5808690099fd67b0965748afe4b43565"]
staff = ["u5808690099fd67b0965748afe4b43565"]
Saints = admin + staff

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
welcome = []

#responsename1 = ki.getProfile().displayName
#responsename2 = kk.getProfile().displayName
#responsename3 = kc.getProfile().displayName
#responsename4 = ko.getProfile().displayName
#responsename5 = jk.getProfile().displayName

settings = {
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "comment":"╔═════════════════════\n║ 🐯@💫🔥Mikha_Lee🔥💫 🐯\n║💣OPEN ORDER💣\n╠═════════════════════\n╠➩SELFTBOT ONLY\n╠➩SELFTBOT + ASIST\n╠➩1 AKUN UTAMA    75K\n╠➩1AKUN UTAMA + 2 ASIST 150K\n╠➩1AKUN UTAMA + 3 ASIST 175K\n╠➩1AKUN UTAMA + 4 ASIST 200K\n╠➩1AKUN UTAMA  + 5 ASIST 225K\n╠➩1 AKUN UTAMA + 9 BOT +1 SIRI LUAR 300K\n╠➩ ProtectBot 3-20 Bot Assist\n╠═════════════════════\n║     [👇 Minat Silahan hub👇]\n╠➩line://ti/p/~rozikeane\n╠➩line://ti/p/~keyla_77\n╠➩line://ti/p/~keyla_77\n╠➩TERIMAKASIH\n║═════════════════════\n╠➩C̽̅̈́̅ŕ̛̋͛e͛̃̾̍ǻ̕͘t͒̉̈̎o͊̓̌͠r̐̇̾̐ B̝̪̭͓͍̺͐͂̑̅̓͗͗̈́͢y͚͔̝͖̮̤͚̅̉̑̐̓̀̋̊͂͜͜͢͞:̶̨̻̪͓̦̻̋̾̂̽̎͘͜͜WIRO_212>༻>\n║ ═════════════════════\n╠➩ Support By: keyla_77\n╚══════════════════════",
    "autoJoinTicket":False,
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

wait = {
    "limit": 1,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":True,
    "contact":False,
    'autoJoin':True,
    'autoAdd':True,
    'left':False,
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":False,
    "Mentionkick":False,
    "welcomeOn":False,
    "sticker":False,
    "selfbot":True,
    "likeOn":True,
    'autoBlock':False,
    "unsend":True,
    "arespon":True,
    "mention":"Tuh Yang ngintip mending Gabung Chat sini -_-",
    "Respontag":"YANG NGETAG2 GAK JELAS TENGGELAMKAN -_-",
    "welcome":"Selamat datang & semoga betah n bahagia",
    "message":"──────┅❇͜͡❇͜͡☆͜͡❇͜͡❇┅──────\nᴼᴾᴱᴺ ᴼᴿᴰᴱᴿ\n────────┅┅───────\n➣ꜱᴇʟꜰʙᴏᴛ ᴏɴʟʏ\n➣ꜱᴇʟꜰʙᴏᴛ + ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 2 ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 3 ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 4 ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 5 ᴀꜱɪꜱᴛ\n➣ʙᴏᴛᴘʀᴏᴛᴇᴄᴛ 3-30 ʙᴏᴛ ᴀꜱɪꜱᴛ\n➣ɴᴇᴡ ꜱᴄʀɪᴘᴛ\n➣ʜʀɢᴀ ʙɪꜱᴀ ɴᴇɢᴏ\n─────────┅┅─────────\n  ✯❇͜͡❇͜͡C͜͡r͜͡e͜͡a͜͡t͜͡o͜͡r✯͜͡$͜͡ë͜͡I͜͡F͜͡-͜͡฿͜͜͡͡o͜͡t͜͡ ͜͡❇͜͡❇✯\nline.me/ti/p/~keyla_77\n➣ѕєʟғвот κɪcκєʀ_+_ᴘʀᴏᴛᴇᴄᴛ\n────────┅❇͜͡❇͜͡☆͜͡❇͜͡❇┅────────",
    }

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)

Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Mention User「{}」\n\n  [ Mention ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += settings["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n???[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n???[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to,"Hay kk")

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += "welcome"
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n???[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n???[ Success ]"
      #  client.sendMessage(to, textx)
    except Exception as error:
        cl.sendMessage(to)
        
def executeCmd(msg, text, txt, cmd, msg_id, receiver, sender, to, setKey):
    if cmd.startswith('ex\n'):
      if sender in clientMid:
        try:
            sep = text.split('\n')
            ryn = text.replace(sep[0] + '\n','')
            f = open('exec.txt', 'w')
            sys.stdout = f
            print(' ')
            exec(ryn)
            print('\n%s' % str(datetime.now()))
            f.close()
            sys.stdout = sys.__stdout__
            with open('exec.txt','r') as r:
                txt = r.read()
            cl.sendMessage(to, txt)
        except Exception as e:
            pass
      else:
        cl.sendMessage(to, 'Apalo !')
    elif cmd.startswith('exc\n'):
      if sender in clientMid:
        sep = text.split('\n')
        ryn = text.replace(sep[0] + '\n','')
        if 'print' in ryn:
        	ryn = ryn.replace('print(','cl.sendExecMessage(to,')
        	exec(ryn)
        else:
        	exec(ryn)
      else:
        cl.sendMessage(to, 'Apalo !')        

def logError(text):
    cl.log("[@💫🔥Mikha_Lee🔥💫 ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Makassar")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("errorLog.txt","a") as error:
        error.write("\n[{}] {}".format(str(time), text))
        
def sendTemplates(to, data):
    data = data
    url = "https://api.line.me/message/v3/share"
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi Note 5 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36 Line/8.1.1'  
    headers['Content-Type'] = 'application/json'  
    headers['Authorization'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.5uMcEEHahauPb5_MKAArvGzEP8dFOeVQeaMEUSjtlvMV9uuGpj827IGArKqVJhiGJy4vs8lkkseiNd-3lqST14THW-SlwGkIRZOrruV4genyXbiEEqZHfoztZbi5kTp9NFf2cxSxPt8YBUW1udeqKu2uRCApqJKzQFfYu3cveyk.GoRKUnfzfj7P2uAX9vYQf9WzVZi8MFcmJk8uFrLtTqU'
    sendPost = requests.post(url, data=json.dumps(data), headers=headers)
    print(sendPost)
    return sendPost
def sendTextTemplate(to, text):
    data = {
            "type": "flex",
            "altText": "@💫🔥Mikha_Lee🔥💫 ",
            "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": text,
                "size": "md",
                "margin": "none",
                "color": "#F0F8FF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  }
}
}
    cl.postTemplate(to, data)
 
def sendTextTemplate8(to, text):
    data = {
                                "type": "flex",
                                "altText": "{} menghapus anda dari grup".format(cl.getProfile().displayName),
                                "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#40E0D0",
            "align": "center"
          },
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00008B"
    },
    "header": {
      "backgroundColor": "#00008B"
    }
  },  
  "hero": {
    "type": "image",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "url": "https://media.tenor.com/images/842c542426869f999afaeb7d8c7940b3/tenor.gif",
    "size": "full",
    "margin": "xl"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "CREATOR",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#7CFC00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/keyla_77"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#E5E4E2"
      },
      {
        "type": "text",
        "text": "ORDER",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "action": {
          "type": "uri",
          "uri": "line://app/1602687308-GXq4Vvk9/?type=text&text=Order"
        },
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "💫🔥Mikha_Lee🔥💫",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#F0F8FF",
        "align": "center"
      }
    ]
  }
}
}
    cl.postTemplate(to, data)
    
def sendTextTemplate7(to, text):
    data = {
                                "type": "flex",
                                "altText": "{} menghapus anda dari grup".format(cl.getProfile().displayName),
                                "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#40E0D0",
            "align": "center"
          },
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00008B"
    },
    "header": {
      "backgroundColor": "#00008B"
    }
  },  
  "hero": {
    "type": "image",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "url": "https://media.giphy.com/media/NTj6PZtxqt6U91ksRZ/giphy.gif",
    "size": "full",
    "margin": "xl"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "CREATOR",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#7CFC00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/keyla_77"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#E5E4E2"
      },
      {
        "type": "text",
        "text": "ORDER",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "action": {
          "type": "uri",
          "uri": "line://app/1602687308-GXq4Vvk9/?type=text&text=Order"
        },
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "💫🔥Mikha_Lee🔥💫",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#F0F8FF",
        "align": "center"
      }
    ]
  }
}
}
    cl.postTemplate(to, data)
    
def sendTextTemplate6(to, text):
    data = {
                                "type": "flex",
                                "altText": "{} menghapus anda dari grup".format(cl.getProfile().displayName),
                                "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#40E0D0",
            "align": "center"
          },
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00008B"
    },
    "header": {
      "backgroundColor": "#00008B"
    }
  },  
  "hero": {
    "type": "image",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "url": "https://media.giphy.com/media/nbBbfmBVnuIYZ5itAc/giphy.gif",
    "size": "full",
    "margin": "xl"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "CREATOR",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#7CFC00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/keyla_77"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#E5E4E2"
      },
      {
        "type": "text",
        "text": "ORDER",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "action": {
          "type": "uri",
          "uri": "line://app/1602687308-GXq4Vvk9/?type=text&text=Order"
        },
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "💫🔥Mikha_Lee🔥💫",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#F0F8FF",
        "align": "center"
      }
    ]
  }
}
}
    cl.postTemplate(to, data)
    
def sendTextTemplate4(to, text):
    data = {
                                "type": "flex",
                                "altText": "{} menghapus anda dari grup".format(cl.getProfile().displayName),
                                "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#40E0D0",
            "align": "center"
          },
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00008B"
    },
    "header": {
      "backgroundColor": "#00008B"
    }
  },  
  "hero": {
    "type": "image",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "url": "https://3.bp.blogspot.com/-OfIz4mSIumw/WbLEZw7l6nI/AAAAAAARd6Y/Dxzos1SA_5MU32bXFTKToLDndM7YpV7WACLcBGAs/s1600/AW529310_04.gif",
    "size": "full",
    "margin": "xl"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "CREATOR",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#7CFC00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/keyla_77"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#E5E4E2"
      },
      {
        "type": "text",
        "text": "ORDER",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "action": {
          "type": "uri",
          "uri": "line://app/1602687308-GXq4Vvk9/?type=text&text=Order"
        },
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "💫🔥Mikha_Lee🔥💫",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#F0F8FF",
        "align": "center"
      }
    ]
  }
}
}
    cl.postTemplate(to, data)
    
def sendTextTemplate5(to, text):
    data = {
            "type": "flex",
            "altText": "💫🔥Mikha_Lee🔥💫",
            "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "sm",
            "weight": "bold",
            "wrap": True,
            "color": "#F0F8FF"
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00008B"
    },
    "header": {
      "backgroundColor": "#00008B"
    }
  },  
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "sÉªÊá´Êá´á´É´ á´ÉªÊÉªÊ",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "ð¶SOUNDCLOUDð¶",
        "size": "md",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "align": "center"
      }
    ]
  }
}
}
    cl.postTemplate(to, data)
    
def sendTextTemplate1(to, text):
    data = {
                "type": "template",
                "altText": "💫🔥Mikha_Lee🔥💫",
                "contents": {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                               "text": text,
                               "size": "sm",
                               "margin": "none",
                               "color": "#8B008B",
                               "wrap": True,
                               "weight": "regular",
                               "type": "text"
                            }
                        ]
                    }
                }
            }
    cl.postTemplate(to, data)
    
def sendTextTemplate2(to, text):
    data = {
            "type": "flex",
            "altText": "💫🔥Mikha_Lee🔥💫",
            "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#0000CD"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": text,
                "size": "md",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  }
}
}
    cl.postTemplate(to, data)
    
def sendTextTemplate3(to, text):
    data = {
            "type": "flex",
            "altText": "💫🔥Mikha_Lee🔥💫",
            "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "sm",
            "weight": "bold",
            "wrap": True,
            "color": "#00FF00"
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00FFFF"
    },
    "header": {
      "backgroundColor": "#00FFFF"
    }
    },  
     "hero": {
     "type": "image",
     "aspectRatio": "20:13",
     "aspectMode": "cover",
     "url": "https://media.giphy.com/media/67pVlH3LSLDjTBikzf/giphy.gif",
     "size": "full",
     "margin": "xl"
  },  
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "CREATOR",
        "size": "xxl",
        "wrap": True,
        "weight": "bold",
        "color": "#000000",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/keyla_77"
        },
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "💫🔥Mikha_Lee🔥💫 BOTS",
        "size": "md",
        "wrap": True,
        "weight": "bold",
        "color": "#000000",
        "align": "center"
      }
    ]
  }
}
}
    cl.postTemplate(to, data)
    
def sendStickerTemplate(to, text):
    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
    to = op.param1
    data = {
                          "type": "template",
                          "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                          "template": {
                             "type": "image_carousel",
                             "columns": [
                              {
                                  "imageUrl": text,
                                  "size": "full", 
                                  "action": {
                                      "type": "uri",
                                      "uri": "http://line.me/ti/p/keyla_77"
           }                                                
 }
]
                          }
                      }
    cl.postTemplate(to, data)
    
def sendStickerTemplate(to, text):
    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
    to = op.param1
    data = {
                          "type": "template",
                          "altText": "{} sent a sticker".format(client.getProfile().displayName),
                          "template": {
                             "type": "image_carousel",
                             "columns": [
                              {
                                  "imageUrl": text,
                                  "size": "full", 
                                  "action": {
                                      "type": "uri",
                                      "uri": "http://line.me/ti/p/~3q18091987"
           }                                                
 }
]
                          }
                      }
    cl.postTemplate(to, data)    
    
def youtubeMp3(to, link):
    subprocess.getoutput('youtube-dl --extract-audio --audio-format mp3 --output Team💫🔥Mikha_Lee🔥💫Bot.mp3 {}'.format(link))
    try:
        cl.sendAudio(to, 'Team Bots 💫🔥Mikha_Lee🔥💫.mp3')
        time.sleep(2)
        os.remove('Team Bots 💫🔥Mikha_Lee🔥💫.mp3')
    except Exception as e:
        cl.sendMessage(to, '💫🔥Mikha_Lee🔥💫 TEAM BOT\nMungkin Link salah cek lagi coba')
def youtubeMp4(to, link):
    subprocess.getoutput('youtube-dl --format mp4 --output Team Bots 💫🔥Mikha_Lee🔥💫.mp4 {}'.format(link))
    try:
        cl.sendVideo(to, "Team Bots 💫🔥Mikha_Lee🔥💫.mp4")
        time.sleep(2)
        os.remove('Team Bots 💫🔥Mikha_Lee🔥💫.mp4')
    except Exception as e:
        cl.sendMessage(to, ' ã ERROR ã\nMungkin Link Nya Salah GaN~', contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+client.getContact(clientMid).pictureStatus, 'AGENT_NAME': 'ã ERROR ã', 'AGENT_LINK': 'https://line.me/ti/p/~keyla_77'})

def delExpire():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                if time.time() - temp_flood[tmp]["time"] >= 3*10:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        veza = "ãBOT ACTIVE AGAINã"
                        cl.sendMessage(tmp, veza, {'AGENT_LINK': "https://line.me/ti/p/~keyla_77", 'AGENT_ICON': "http://klikuntung.com/images/messengers/line-logo.png", 'AGENT_NAME': "Detect Spam "})        
                    except Exception as error:
                        logError(error)

def delExpirev2():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        veza = "ãBOT ACTIVE AGAINã"
                        cl.sendMessage(tmp, veza, {'AGENT_LINK': "https://line.me/ti/p/~keyla_77", 'AGENT_ICON': "http://klikuntung.com/images/messengers/line-logo.png", 'AGENT_NAME': "Detect Spam "})        
                    except Exception as error:
                        logError(error)    

def musik(to):
    contentMetadata={'previewUrl': "http://dl.profile.line-cdn.net/"+cl.getContact(mid).picturePath, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': cl.getContact(mid).statusMessage if cl.getContact(mid).statusMessage != '' else 'http://line.me/ti/p/~dzul1991ji', 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': cl.getContact(mid).displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.cl.cl/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://os.me.naver.jp/os/p/"+mid,'MSG_SENDER_NAME':  cl.getContact(mid).displayName,}
    return cl.sendMessage(to, cl.getContact(mid).displayName, contentMetadata, 19)

def sendMention2(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))
    
def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "┏═════════════════┓" + "\n" + \
                  "   °❂°「 ------💫🔥Mikha_Lee🔥💫 ------ 」°❂°" + "\n" + \
                  "┗═════════════════┛" + "\n" + \
                  "╔═════════════════┓" + "\n" + \
                  "║°❂° " + key + "Me\n" + \
                  "║°❂° " + key + "Mid「@」\n" + \
                  "║°❂° " + key + "Info「@」\n" + \
                  "║°❂° " + key + "Restart\n" + \
                  "║°❂° " + key + "Runtime\n" + \
                  "║°❂° " + key + "Creator\n" + \
                  "║°❂° " + key + "Speed/Sp\n" + \
                  "║°❂° " + key + "Tag-Mention\n" + \
                  "║°❂° " + key + "Joinall(No Grup)\n" + \
                  "║°❂° " + key + "As1-4\n" + \
                  "║°❂° " + key + "Sein(Masukan Bot Via Invite)\n" + \
                  "║°❂° " + key + "Js stay [ aCtive Gs ]\n" + \
                  "║°❂° " + key + "Js in [ keluar Gs ]\n" + \
                  "║°❂° " + key + "Byeme\n" + \
                  "║°❂° " + key + "Leave「Namagrup」\n" + \
                  "║°❂° " + key + "Ginfo\n" + \
                  "║°❂° " + key + "Self on「@」\n" + \
                  "║°❂° " + key + "Open\n" + \
                  "║°❂° " + key + "Close\n" + \
                  "║°❂° " + key + "Url grup\n" + \
                  "║°❂° " + key + "Infogrup「angka」\n" + \
                  "║°❂° " + key + "Infomem「angka」\n" + \
                  "║°❂° " + key + "All clear\n" + \
                  "║°❂° " + key + "Hapus chat\n" + \
                  "║°❂° " + key + "Friendlist\n" + \
                  "║°❂° " + key + "Gruplist\n" + \
                  "║°❂° " + key + "Updatefoto\n" + \
                  "║°❂° " + key + "Updategrup\n" + \
                  "║°❂° " + key + "Updatebot\n" + \
                  "║°❂° " + key + "Setkey「New Key」\n" + \
                  "║°❂° " + key + "Mykey\n" + \
                  "║°❂° " + key + "Self 「on/off」\n" + \
                  "║°❂° " + key + "Ketik「 Refresh 」\n" + \
                  "╚═══════════════"
    return helpMessage

def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "┏═════════════════┓" + "\n" + \
                  "   °❂°「 ----💫🔥Mikha_Lee🔥💫------ 」°❂°" + "\n" + \
                  "┗═════════════════┛" + "\n" + \
                  "╔═════════════════┓" + "\n" + \
                  "║°❂° " + key + "Blc\n" + \
                  "║°❂° " + key + "Ban:on\n" + \
                  "║°❂° " + key + "Unban:on\n" + \
                  "║°❂° " + key + "Ban「@」\n" + \
                  "║°❂° " + key + "Unban「@」\n" + \
                  "║°❂° " + key + "Talkban「@」\n" + \
                  "║°❂° " + key + "Untalkban「@」\n" + \
                  "║°❂° " + key + "Talkban:on\n" + \
                  "║°❂° " + key + "Untalkban:on\n" + \
                  "║°❂° " + key + "Banlist\n" + \
                  "║°❂° " + key + "Talkbanlist\n" + \
                  "║°❂° " + key + "Clearban\n" + \
                  "║°❂° " + key + "Refresh\n║\n" + \
                  "║══⟦֮°❂°Command Menu°❂°⟧֮\n║\n" + \
                  "║°❂° " + key + "Cek sider\n" + \
                  "║°❂° " + key + "Cek spam\n" + \
                  "║°❂° " + key + "Cek pesan \n" + \
                  "║°❂° " + key + "Cek respon \n" + \
                  "║°❂° " + key + "Cek welcome\n" + \
                  "║°❂° " + key + "Set sider: (Text)\n" + \
                  "║°❂° " + key + "Set spam: (Text)\n" + \
                  "║°❂° " + key + "Set pesan: (Text)\n" + \
                  "║°❂° " + key + "Set respon: (Text)\n" + \
                  "║°❂° " + key + "Set welcome: (Text)\n" + \
                  "║°❂° " + key + "myname:「Nama」\n" + \
                  "║°❂° " + key + "Gift:「Mid 」「Jumlah」\n" + \
                  "║°❂° " + key + "Spam:「Mid」「Jumlah」\n" + \
                  "╚═══════════════" + "\n" + \
                  "╚═══════════════°❂°\n°❂° Suᴘᴘᴏʀᴛ:\n\n╔═ஜ°° Cʀᴇᴀᴛᴇᴅ Bʏ °°ஜ══╗\n╠\n╚═ஜ°° 💫🔥Mikha_Lee🔥💫°°ஜ═╝"
                  
    return helpMessage1

def bot(op):
    global time
    global ast
    global groupParam
    try:   
    	#if op.type == 0:
            #return
            
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            Ticket = cl.reissueGroupTicket(op.param1)
                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                            sw.kickoutFromGroup(op.param1,[op.param2])
                            sw.leaveGroup(op.param1) 
                            cl.updateGroup(X)
                            random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                except:
                    try:
                        if ki.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                ki.reissueGroupTicket(op.param1)
                                X = ki.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                Ticket = ki.reissueGroupTicket(op.param1)
                                sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                sw.kickoutFromGroup(op.param1,[op.param2])
                                sw.leaveGroup(op.param1)
                                ki.updateGroup(X)
                                ki.inviteIntoGroup(op.param1,[Zmid])
                                cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                    except:
                        try:
                            if kk.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    kk.reissueGroupTicket(op.param1)
                                    X = kk.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    Ticket = kk.reissueGroupTicket(op.param1)
                                    sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    sw.kickoutFromGroup(op.param1,[op.param2])
                                    kk.updateGroup(X)
                                    kk.inviteIntoGroup(op.param1,[Zmid])
                                    cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                        except:
                            try:
                                if kc.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        kc.reissueGroupTicket(op.param1)
                                        X = kc.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        Ticket = kc.reissueGroupTicket(op.param1)
                                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        sw.kickoutFromGroup(op.param1,[op.param2])
                                        kc.updateGroup(X)
                                        kc.inviteIntoGroup(op.param1,[Zmid])
                                        cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                            except:
                                try:
                                    if ko.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            ko.reissueGroupTicket(op.param1)
                                            X = ko.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            Ticket = ko.reissueGroupTicket(op.param1)
                                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            sw.kickoutFromGroup(op.param1,[op.param2])
                                            ko.updateGroup(X)
                                            ko.inviteIntoGroup(op.param1,[Zmid])
                                            cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)                                        
                                except:
                                    try:
                                        if cl.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                cl.reissueGroupTicket(op.param1)
                                                X = cl.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                Ticket = cl.reissueGroupTicket(op.param1)
                                                sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                sw.kickoutFromGroup(op.param1,[op.param2])
                                                sw.leaveGroup(op.param1)
                                                cl.updateGroup(X)
                                                cl.inviteIntoGroup(op.param1,[Zmid])
                                                cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                    except:
                                        try:
                                            if ki.getGroup(op.param1).preventedJoinByTicket == False:
                                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                    ki.reissueGroupTicket(op.param1)
                                                    X = ki.getGroup(op.param1)
                                                    X.preventedJoinByTicket = True
                                                    Ticket = ki.reissueGroupTicket(op.param1)
                                                    sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                    sw.kickoutFromGroup(op.param1,[op.param2])
                                                    sw.leaveGroup(op.param1)
                                                    ki.updateGroup(X)
                                                    ki.inviteIntoGroup(op.param1,[Zmid])
                                                    cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                        except:
                                            pass
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        sendTextTemplate4(op.param1,"á´ÊÉªá´á´á´á´sÉªÊÂ sá´á´á´ÊÂ ÉªÉ´á´ Éªá´á´Â á´á´\n Group " +str(ginfo.name))
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        sendTextTemplate4(op.param1,"Trimakasih sudah invite " + str(ginfo.name))
                  
        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        sendTextTemplate8(op.param1,"Haii " +str(ginfo.name))
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        sendTextTemplate8(op.param1,"Haii " + str(ginfo.name))
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.leaveGroup(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        kk.leaveGroup(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.leaveGroup(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ko.acceptGroupInvitation(op.param1)
                        ginfo = ko.getGroup(op.param1)
                        ko.leaveGroup(op.param1)
                    else:
                        ko.acceptGroupInvitation(op.param1)
                        ginfo = ko.getGroup(op.param1)
            if Emid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        jk.acceptGroupInvitation(op.param1)
                        ginfo = jk.getGroup(op.param1)
                        jk.leaveGroup(op.param1)
                    else:
                        jk.acceptGroupInvitation(op.param1)
                        ginfo = jk.getGroup(op.param1)
                        
        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        jk.findAndAddContactsByMid(op.param3)
                        jk.kickoutFromGroup(op.param1,[op.param2])
                        jk.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            ki.findAndAddContactsByMid(op.param3)
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                kk.findAndAddContactsByMid(op.param3)
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    kc.findAndAddContactsByMid(op.param3)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.inviteIntoGroup(op.param1,[op.param3])    
                                except:
                                    try:
                                        ko.findAndAddContactsByMid(op.param3)
                                        ko.kickoutFromGroup(op.param1,[op.param2])
                                        ko.inviteIntoGroup(op.param1,[op.param3])        
                                    except:
                                        try:
                                            random.choice(ABC).findAndAddContactsByMid(op.param3)
                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            pass                
                        

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass
              
        if op.type == 17:
            if op.param1 in welcome:
                ginfo = cl.getGroup(op.param1)
                welcomeMembers(op.param1, [op.param2])
                contact = cl.getContact(op.param2)
                data = {
                        "type": "flex",
                        "altText": "💫🔥Mikha_Lee🔥💫 bots",
                        "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "flex": 2,
            "text": "{}".format(cl.getContact(op.param2).displayName),
            "size": "md",
            "wrap": True,
            "weight": "bold",
            "gravity": "center",
            "color": "#FF0000"
          },
          {
            "type": "separator",
            "color": "#6F4E37"
          },
          {
            "type": "text",
            "text": "WELCOME TO THE ROOM",
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#FFD700"
          },
          {
            "type": "text",
            "text": "â£ Jangan Lupa Cek Note\nâ£ Ciptakan Keamanan Room,\nâ£ Dan Harmoni Persahabatan\nâ£ Karena Kita Semua\nâ£ Sahabat Disini\nâ£ Terimakasih",
            "size": "md",
            "weight": "bold",
            "color": "#ADFF2F",
            "wrap": True
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#0000FF"
    },
    "footer": {
      "backgroundColor": "#DC143C"
    }
  },
  
  "hero": {
    "type": "image",
    "aspectRatio": "20:13",
    "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
    "size": "full",
    "margin": "xxl"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "BOSS",
        "size": "xxl",
        "wrap": True,
        "weight": "bold",
        "color": "#7CFC00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/keyla_77"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#E5E4E2"
      },
      {
        "type": "text",
        "text": "ORDER",
        "size": "xxl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "action": {
          "type": "uri",
          "uri": "line://app/1603968955-ORWb9RdY/?type=text&text=Order"
        },
        "align": "center"
      }
    ]
  }
}
}
                cl.postTemplate(op.param1, data)
                sendStickerTemplate(op.param1, "https://i.ibb.co/rGSVfNg/89933.gif")
        if op.type == 5:
            print ("[ 5 ] NOTIFIED AUTO BLOCK CONTACT")
            if wait["autoBlock"] == True:
                cl.blockContact(op.param1)
                cl.sendMessage(op.param1, wait["Sory aim bclock u"])
                
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendMessage(op.param1, wait["message"])
        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Gambar Dihapus 」\n°❂° Pengirim : "
                                ret_ = "°❂° Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n°❂° Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                cl.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "°❂°Pesan Dihapus°❂°\n"
                                ret_ += "°❂° Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\n°❂° Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n°❂° Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n°❂° Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                cl.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "°❂° Sticker Dihapus °❂°\n"
                                ret_ += "°❂° Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\n°❂° Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n°❂° Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                cl.sendMessage(at, str(ret_))
                                cl.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)
                
        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        sw.acceptGroupInvitation(op.param1)
                        sw.findAndAddContactsByMid(op.param3)
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        sw.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                        x = sw.getGroup(op.param1)
                        x.preventedJoinByTicket = False
                        sw.updateGroup(x)
                        invsend = 0
                        Ti = sw.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ti)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        ko.acceptGroupInvitationByTicket(op.param1,Ti)
                        jk.acceptGroupInvitationByTicket(op.param1,Ti)
                        Ticket = sw.reissueGroupTicket(op.param1)
                        sw.leaveGroup(op.param1)
                        random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                    except:
                        random.choice(ABC).findAndAddContactsByMid(op.param3)
                        random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])        
            
        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                cl.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    x = ki.getGroup(op.param1)
                                    x.preventedJoinByTicket = False
                                    ki.updateGroup(x)
                                    invsend = 0
                                    Ti = ki.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                                    sw.acceptGroupInvitationByTicket(op.param1,Ti)
                                    sw.kickoutFromGroup(op.param1,[op.param2])
                                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                                    ko.kickoutFromGroup(op.param1,[op.param2])
                                    jk.acceptGroupInvitationByTicket(op.param1,Ti)
                                    jk.kickoutFromGroup(op.param1,[op.param2])
                                    G = sw.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    sw.updateGroup(G)
                                    sw.leaveGroup(op.param1)
                                    random.choice(KAC).inviteIntoGroup(op.param1,[Zmid])
                                except:
                                    try:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                        cl.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                            kk.inviteIntoGroup(op.param1,[op.param3])
                                            cl.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                random.choice(ABC).findAndAddContactsByMid(op.param3)
                                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                cl.acceptGroupInvitation(op.param1)    
                                            except:
                                                pass
                return

            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kk.inviteIntoGroup(op.param1,[op.param3])
                        ki.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            ki.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                jk.kickoutFromGroup(op.param1,[op.param2])
                                jk.inviteIntoGroup(op.param1,[op.param3])
                                ki.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    x = kk.getGroup(op.param1)
                                    x.preventedJoinByTicket = False
                                    kk.updateGroup(x)
                                    invsend = 0
                                    Ti = kk.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                                    sw.acceptGroupInvitationByTicket(op.param1,Ti)
                                    sw.kickoutFromGroup(op.param1,[op.param2])
                                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                                    ko.kickoutFromGroup(op.param1,[op.param2])
                                    jk.acceptGroupInvitationByTicket(op.param1,Ti)
                                    jk.kickoutFromGroup(op.param1,[op.param2])
                                    G = sw.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    sw.updateGroup(G)
                                    sw.leaveGroup(op.param1)
                                    random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                                except:
                                    try:
                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                        ki.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                            ki.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                random.choice(ABC).findAndAddContactsByMid(op.param3)
                                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                ki.acceptGroupInvitation(op.param1)        
                                            except:
                                                pass
                return

            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        kk.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            jk.kickoutFromGroup(op.param1,[op.param2])
                            jk.inviteIntoGroup(op.param1,[op.param3])
                            kk.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                kk.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    x = kc.getGroup(op.param1)
                                    x.preventedJoinByTicket = False
                                    kc.updateGroup(x)
                                    invsend = 0
                                    Ti = kc.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                                    sw.acceptGroupInvitationByTicket(op.param1,Ti)
                                    sw.kickoutFromGroup(op.param1,[op.param2])
                                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                                    ko.kickoutFromGroup(op.param1,[op.param2])
                                    jk.acceptGroupInvitationByTicket(op.param1,Ti)
                                    jk.kickoutFromGroup(op.param1,[op.param2])
                                    G = sw.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    sw.updateGroup(G)
                                    sw.leaveGroup(op.param1)
                                    random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                                except:
                                    try:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                        kk.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                            kk.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                random.choice(ABC).findAndAddContactsByMid(op.param3)
                                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                kk.acceptGroupInvitation(op.param1)            
                                            except:
                                                pass
                return
                    
            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        jk.kickoutFromGroup(op.param1,[op.param2])
                        jk.inviteIntoGroup(op.param1,[op.param3])
                        kc.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            kc.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.inviteIntoGroup(op.param1,[op.param3])
                                kc.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    x = ko.getGroup(op.param1)
                                    x.preventedJoinByTicket = False
                                    ko.updateGroup(x)
                                    invsend = 0
                                    Ti = ko.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                                    sw.acceptGroupInvitationByTicket(op.param1,Ti)
                                    sw.kickoutFromGroup(op.param1,[op.param2])
                                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    jk.acceptGroupInvitationByTicket(op.param1,Ti)
                                    jk.kickoutFromGroup(op.param1,[op.param2])
                                    G = sw.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    sw.updateGroup(G)
                                    sw.leaveGroup(op.param1)
                                    random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                                except:
                                    try:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                        kc.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                            kk.inviteIntoGroup(op.param1,[op.param3])
                                            kc.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                random.choice(ABC).findAndAddContactsByMid(op.param3)
                                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                kc.acceptGroupInvitation(op.param1)                
                                            except:
                                                pass
                return

            if Dmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        jk.kickoutFromGroup(op.param1,[op.param2])
                        jk.inviteIntoGroup(op.param1,[op.param3])
                        ko.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            ko.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.inviteIntoGroup(op.param1,[op.param3])
                                ko.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    x = cl.getGroup(op.param1)
                                    x.preventedJoinByTicket = False
                                    cl.updateGroup(x)
                                    invsend = 0
                                    Ti = cl.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                                    sw.acceptGroupInvitationByTicket(op.param1,Ti)
                                    sw.kickoutFromGroup(op.param1,[op.param2])
                                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    jk.acceptGroupInvitationByTicket(op.param1,Ti)
                                    jk.kickoutFromGroup(op.param1,[op.param2])
                                    G = sw.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    sw.updateGroup(G)
                                    sw.leaveGroup(op.param1)
                                    random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                                except:
                                    try:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                        ko.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                            ko.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                random.choice(ABC).findAndAddContactsByMid(op.param3)
                                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                ko.acceptGroupInvitation(op.param1)                    
                                            except:
                                                pass
                return
                
            if Emid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ko.kickoutFromGroup(op.param1,[op.param2])
                        ko.inviteIntoGroup(op.param1,[op.param3])
                        jk.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            jk.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.inviteIntoGroup(op.param1,[op.param3])
                                jk.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    x = cl.getGroup(op.param1)
                                    x.preventedJoinByTicket = False
                                    cl.updateGroup(x)
                                    invsend = 0
                                    Ti = cl.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                                    sw.acceptGroupInvitationByTicket(op.param1,Ti)
                                    sw.kickoutFromGroup(op.param1,[op.param2])
                                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    jk.acceptGroupInvitationByTicket(op.param1,Ti)
                                    jk.kickoutFromGroup(op.param1,[op.param2])
                                    G = sw.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    sw.updateGroup(G)
                                    sw.leaveGroup(op.param1)
                                    random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                                except:
                                    try:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                        jk.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                            jk.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                random.choice(ABC).findAndAddContactsByMid(op.param3)
                                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                jk.acceptGroupInvitation(op.param1)                    
                                            except:
                                                pass
                return    
                
            if Zmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        jk.findAndAddContactsByMid(op.param3)
                        jk.kickoutFromGroup(op.param1,[op.param2])
                        jk.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            ki.findAndAddContactsByMid(op.param3)
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                kk.findAndAddContactsByMid(op.param3)
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    kc.findAndAddContactsByMid(op.param3)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.inviteIntoGroup(op.param1,[op.param3])    
                                except:
                                    try:
                                        ko.findAndAddContactsByMid(op.param3)
                                        ko.kickoutFromGroup(op.param1,[op.param2])
                                        ko.inviteIntoGroup(op.param1,[op.param3])        
                                    except:
                                        try:
                                            random.choice(ABC).findAndAddContactsByMid(op.param3)
                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            pass
                return    
                
            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        jk.kickoutFromGroup(op.param1,[op.param2])
                        jk.findAndAddContactsByMid(op.param1,admin)
                        jk.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.findAndAddContactsByMid(op.param3)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.inviteIntoGroup(op.param1,[op.param3])    
                                except:
                                    try:
                                        ko.findAndAddContactsByMid(op.param3)
                                        ko.kickoutFromGroup(op.param1,[op.param2])
                                        ko.inviteIntoGroup(op.param1,[op.param3])        
                                    except:
                                        try:
                                            random.choice(ABC).findAndAddContactsByMid(op.param3)
                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])    
                                        except:
                                            pass

                return

            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.findAndAddContactsByMid(op.param1,staff)
                        ki.inviteIntoGroup(op.param1,staff)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.findAndAddContactsByMid(op.param1,staff)
                            kk.inviteIntoGroup(op.param1,staff)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.findAndAddContactsByMid(op.param1,staff)
                                kc.inviteIntoGroup(op.param1,staff)
                            except:
                                try:
                                    ko.findAndAddContactsByMid(op.param3)
                                    ko.kickoutFromGroup(op.param1,[op.param2])
                                    ko.inviteIntoGroup(op.param1,[op.param3])        
                                except:
                                    try:
                                        random.choice(ABC).findAndAddContactsByMid(op.param3)
                                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                        random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])        
                                    except:
                                        pass

                return
              
        if op.type == 13:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(ABC).cancelGroupInvitation(op.param1,[op.param3])
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                      
        if op.type == 13:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        group = jk.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            jk.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = ki.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                ki.cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = kk.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    kk.cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = kc.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        kc.cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    try:
                                        group = ko.getGroup(op.param1)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        for _mid in gMembMids:
                                            ko.cancelGroupInvitation(op.param1,[_mid])        
                                    except:
                                        pass
        
        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        ko.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                jk.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                                          
        if op.type == 32:
            if Zmid in op.param3:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.inviteIntoGroup(op.param1,[Zmid])
                    except:
                        try:
                            kk.inviteIntoGroup(op.param1,[Zmid])
                        except:
                            try:
                                kc.inviteIntoGroup(op.param1,[Zmid])
                            except:
                                try:
                                    ko.inviteIntoGroup(op.param1,[Zmid])
                                except:
                                    try:
                                        jk.inviteIntoGroup(op.param1,[Zmid])
                                    except:
                                        try:
                                            random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                                        except:
                                            pass
            return
        if op.type == 55:
            try:
                if op.param1 in Setmain["RAreadPoint"]:
                   if op.param2 in Setmain["RAreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["RAreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 55:
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = cl.getContact(op.param2)
                        data = {
                                "type": "flex",
                                "altText": "sider",
                                "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": "Terciduk",
            "size": "xl",
            "weight": "bold",
            "wrap": True,
            "color": "#FFFF00",
            "align": "center"
          },
          {
            "type": "text",
            "text": "Asalamu.alaikum gabung sini kk chat..biar ramai nih room",
            "size": "md",
            "weight": "bold",
            "color": "#40E0D0",
            "wrap": True
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00008B"
    },
    "header": {
      "backgroundColor": "#00008B"
    }
  },  
  "hero": {
    "type": "image",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
    "size": "full",
    "margin": "xxl"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "CREATOR",
        "size": "xxl",
        "wrap": True,
        "weight": "bold",
        "color": "#F0F8FF",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/keyla_77"
        },
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "{}".format(cl.getContact(op.param2).displayName),
        "size": "md",
        "wrap": True,
        "weight": "bold",
        "color": "#F0F8FF",
        "align": "center"
      }
    ]
  }
}
}
                        cl.postTemplate(op.param1, data);
                
        if op.type == 25 or op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                              
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["arespon"] == True: 
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   lists = []
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           contact = cl.getContact(msg._from)
                           #cl.sendImageWithURL(msg._from, "http://dl.profile.line-cdn.net{}".format(contact.picturePath))
                           cl.sendMention3(sender, "Salken kk @!       ,  \n☻▬▬▬▬▬▬▬▬▬▬☻\n【Assalamualaikum】\n☻▬▬▬▬▬▬▬▬▬▬☻\n➸ @💫🔥Myojob🔥💫  masih sibuk\n☻▬▬▬▬▬▬▬▬▬▬☻\n【Ntar klo on pasti di respon,,】\n☻▬▬▬▬▬▬▬▬▬▬☻",[sender])
                           #cl.sendImageWithURL(msg.to, None, contentMetadata={"STKID":"14689864","STKPKGID":"1374347","STKVER":"1"}, contentType=7)
                           break
              
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   #contact = cl.getContact(msg._from)
                   #name = re.findall(r'@(\w+)', msg.text)
                   #image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           sendTextTemplate4(msg.to, wait["Respontag"])
                           #cl.sendImageWithURL(msg.to,image)
                           break
                           
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   #name = re.findall(r'@(\w+)', msg.text)
                   #mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   #mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:fb
                           #cl.mentiontag(msg.to,[msg._from])
                           #cl.sendMessage(msg.to, "Jangan tag saya....")
                           #cl.kickoutFromGroup(msg.to, [msg._from])
                           #break
                           
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"「Cek ID Sticker」\n°❂° STKID : " + msg.contentMetadata["STKID"] + "\n°❂° STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n°❂° STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"°❂° Nama : " + msg.contentMetadata["displayName"] + "\n°❂° MID : " + msg.contentMetadata["mid"] + "\n°❂° Status Msg : " + contact.statusMessage + "\n°❂° Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
                        
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 16:
                        url = msg.contentMetadata["postEndUrl"]
                        cl.likePost(url[25:58], url[66:], likeType=1004)
                        cl.createComment(url[25:58], url[66:], settings["comment"])
                        print ("Auto like done")
                        sendTextTemplate8(msg.to,"❂➤Like Success")
                        settings["likeOn"] = False
        if op.type == 25 or op.type == 26:	     
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    sendTextTemplate8(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        sendTextTemplate(msg.to,"°❂° Nama : " + msg.contentMetadata["displayName"] + "\n°❂° MID : " + msg.contentMetadata["mid"] + "\n°❂° Status Msg : " + contact.statusMessage + "\n°❂° Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
#===================================[ ] ADD Bots
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        sendTextTemplate(msg.to,"°❂°Contact itu sudah jadi anggota bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        sendTextTemplate(msg.to,"°❂°Berhasil menambahkan ke anggota bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        sendTextTemplate(msg.to,"°❂°Berhasil menghapus dari anggota bot")
                    else:
                        wait["dellbots"] = True
                        sendTextTemplate(msg.to,"°❂°Contact itu bukan anggota bot saints")
                        
#===================================[ ]  ADD STAFF
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        cl.sendMessage(msg.to,"°❂°Contact itu sudah jadi staff")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        sendTextTemplate(msg.to,"°❂°Berhasil menambahkan ke staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        sendTextTemplate(msg.to,"°❂°Berhasil menghapus dari staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        sendTextTemplate(msg.to,"°❂°Contact itu bukan staff")
#===================================[ ]  ADD ADMIN
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        sendTextTemplate(msg.to,"°❂°Contact itu sudah jadi admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        sendTextTemplate(msg.to,"°❂°Berhasil menambahkan ke admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        sendTextTemplate(msg.to,"°❂°Berhasil menghapus dari admin")
                    else:
                        wait["delladmin"] = True
                        sendTextTemplate(msg.to,"°❂°Contact itu bukan admin")
#===================================[ ]  ADD BLACKLIST
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        sendTextTemplate(msg.to,"°❂°Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        sendTextTemplate(msg.to,"°❂°Berhasil menambahkan ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        sendTextTemplate(msg.to,"°❂°Berhasil menghapus dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        sendTextTemplate(msg.to,"°❂°ontact itu tidak ada di blacklist")
#===================================[ ] TALKBAN
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        sendTextTemplate(msg.to,"°❂°Contact itu sudah ada di Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        sendTextTemplate(msg.to,"°❂°Berhasil menambahkan ke Talkban user")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                         sendTextTemplate(msg.to,"°❂°Berhasil menghapus dari Talkban user")
                    else:
                        wait["Talkdblacklist"] = True
                        sendTextTemplate(msg.to,"°❂°Contact itu tidak ada di Talkban")
#===================================[ ] UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = cl.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            sendTextTemplate(msg.to, "°❂°Berhasil menambahkan gambar")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     sendTextTemplate(msg.to, "°❂°Berhasil mengubah foto group")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["RAfoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][mid]
                            cl.updateProfilePicture(path)
                            sendTextTemplate(msg.to,"°❂°Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                        if Amid in Setmain["RAfoto"]:
                            path = ki.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Amid]
                            ki.updateProfilePicture(path)
                            ki.sendMessage(msg.to,"°❂°Foto berhasil dirubah")
                        elif Bmid in Setmain["RAfoto"]:
                            path = kk.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Bmid]
                            kk.updateProfilePicture(path)
                            kk.sendMessage(msg.to,"°❂°Foto berhasil dirubah")
                        elif Cmid in Setmain["RAfoto"]:
                            path = kc.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Cmid]
                            kc.updateProfilePicture(path)
                            kc.sendMessage(msg.to,"°❂°Foto berhasil dirubah")
                        elif Dmid in Setmain["RAfoto"]:
                            path = ko.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Cmid]
                            ko.updateProfilePicture(path)
                            ko.sendMessage(msg.to,"°❂°Foto berhasil dirubah")
                            
                        elif Zmid in Setmain["RAfoto"]:
                            path = sw.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Zmid]
                            sw.updateProfilePicture(path)
                            sw.sendMessage(msg.to,"°❂°Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = ki.downloadObjectMsg(msg_id)
                     path2 = kk.downloadObjectMsg(msg_id)
                     path3 = kc.downloadObjectMsg(msg_id)
                     path4 = ko.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     ki.updateProfilePicture(path1)
                     ki.sendMessage(msg.to, "°❂°Berhasil mengubah foto profile bot")
                     kk.updateProfilePicture(path2)
                     kk.sendMessage(msg.to, "°❂°Berhasil mengubah foto profile bot")
                     kc.updateProfilePicture(path3)
                     kc.sendMessage(msg.to, "°❂°Berhasil mengubah foto profile bot")
                     ko.updateProfilePicture(path4)
                     ko.sendMessage(msg.to, "°❂°erhasil mengubah foto profile bot")

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "menu":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = help()
                               sendTextTemplate3(msg.to, str(helpMessage))
                                                                                       
                        if cmd == "self on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                sendTextTemplate(msg.to, "°❂°Selfbot Turn On")
                           
                        elif cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               sendTextTemplate3(msg.to, "Help\nMenu\nHelp1\nHelp2\nHelp3\nHelp4\nHelp5\nMyset\nJoox-judul\nGs tag\nKc tag\nHere\nOut\nRs\nBc1:\nBroadcast:\nAbout\n\nTEMPLATE BY 💫🔥Mikha_Lee🔥💫")
 
                        elif cmd == "self off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                sendTextTemplate(msg.to, "°❂°Selfbot Turn Off")
                          
                        elif cmd == "help1":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               sendTextTemplate3(msg.to, "Notag on|off\nAllpro on|off\nProtecturl on|off\nProtectjoin on|off\nProtectkick on|off\nProtectcancel on|off\n\nTEMPLATE BY 💫🔥Mikha_Lee🔥💫")                 
                        elif cmd == "help2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage1 = helpbot()
                               sendTextTemplate3(msg.to, str(helpMessage1))
                        elif cmd == "help3":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               sendTextTemplate3(msg.to, "Hah\nSue\nKamvret\nSedih\nSepi\nHadeh\nJumlah:\nStag tag\nSpamcall:\nSpamcall\n\nTEMPLATE BY 💫🔥Mikha_Lee🔥💫")
                        elif cmd == "help4":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               sendTextTemplate3(msg.to, "Respon on|off\nContact on|off\nAutojoin on|off\nAutoadd on|off\nAutoleave on|off\nWelcome on|off\nSider on|off\n\nTEMPLET BY 💫🔥Mikha_Lee🔥💫")
                        elif cmd == "help5":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               sendTextTemplate3(msg.to, "Admin:on\nAdmin:repeat\nStaff:on\nStaff:repeat\nAdminadd tag\nAdmindell tag\nStaffadd tag\nStaffdell tag\nBotadd tag\nBotdell tag\nRefresh\nListbot\nListadmin\nListprotect\nSelf on|off\n\nTEMPLATE BY 💫🔥Mikha_Lee🔥💫")
                        
                        elif cmd == "promo1":
                            if msg._from in admin:
                                saya = cl.getGroupIdsJoined()
                                for groups in saya:
                                    data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://media0.giphy.com/media/xVxio2tNLAM5q/200w.webp?cid=u5808690099fd67b0965748afe4b43565",
        "action": {
          "uri": "http://line.me/ti/p/keyla_77",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#C0FF03"
        },
        "header": {
          "backgroundColor": "#C0FF03"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "text": "💫🔥Mikha_Lee🔥💫 BOTS",
            "color": "#00FFFF",
            "wrap": True,
            "weight": "bold",
            "type": "text",
            "size": "lg",
            "align": "center"
          },
          {
            "type": "separator",
            "color": "#6F4E37"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://media3.giphy.com/media/jLDTcbU89ZOW4/200.webp?cid=u5808690099fd67b0965748afe4b43565"
                  },
                  {
                    "text": "Pemasangan template ke SB",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          
          {
            "text": "160K/Bln",
            "size": "xs",
            "align": "end",
            "color": "#000000",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://media3.giphy.com/media/jLDTcbU89ZOW4/200.webp?cid=u5808690099fd67b0965748afe4b43565"
                  },
                  {
                    "text": "SBonly template",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "200K/Bln",
            "size": "xs",
            "align": "end",
            "color": "#000000",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://media3.giphy.com/media/jLDTcbU89ZOW4/200.webp?cid=u5808690099fd67b0965748afe4b43565"
                  },
                  {
                    "text": "SB 3asist template",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "250k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#000000",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://media3.giphy.com/media/jLDTcbU89ZOW4/200.webp?cid=19f5b51a5c449c5e414637706ff581fb"
                  },
                  {
                    "text": "SB 6asist template",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "500k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#000000",
            "wrap": True,
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "CREATOR",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#000000",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/keyla_77"
            },
            "align": "center"            
          }
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "KEPOIN SEKARANG\nhttp://line.me/ti/p/keyla_77",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#000000",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/keyla_77"
            },
            "align": "center"                            
          }
        ]
      }
    }
  ],
  "type": "carousel"
}

                                    cl.postFlex(groups, data)     
                        elif cmd == "me":
                                contact = cl.getProfile()
                                mids = [contact.mid]
                                status = cl.getContact(sender)                               	
                                data = {
                                        "type": "flex",
                                        "altText": "Me Message",
                                        "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": "💫🔥Mikha_Lee🔥💫 BOTS",
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#7FFF00"
          },
          {
            "type": "text",
            "text": "{}".format(status.statusMessage),
            "align": "center",
            "size": "sm",
            "weight": "bold",
            "color": "#FF00FF",
            "wrap": True
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00008B"
    },
    "header": {
      "backgroundColor": "#00008B"
    }
  },  
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "ORDER",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#F0F8FF",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/keyla_77"
        },
        "align": "center"
      }
    ]
  },
  "hero": {
    "aspectMode": "cover",
    "aspectRatio": "20:13",
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
    "size": "full",
    "align": "center",
  },
  "header": {
    "type": "box",   
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "{}".format(status.displayName),
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#7FFF00",
        "align": "center"
      }
    ]
  }
}
}
                                cl.postTemplate(to, data)
                            
                        elif cmd.startswith("krupuk"):
                            try:
                                proses = text.split(" ")
                                urutan = text.replace(proses[0] + " ","")
                                r = requests.get("http://api.zicor.ooo/joox.php?song={}".format(str(urllib.parse.quote(urutan))))
                                data = r.text
                                data = json.loads(data)
                                b = data
                                c = str(b["title"])
                                d = str(b["singer"])
                                e = str(b["url"])
                                g = str(b["image"])
                                hasil = "Penyanyi: "+str(d)
                                hasil += "\nJudul : "+str(c)
                                data = {
                                        "type": "flex",
                                        "altText": "Musik",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#9932CC"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": g,
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "text": "💫🔥Mikha_Lee🔥💫TEAM BOT\n\nMP3",
            "size": "sm",
            "color": "#FF0000",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#800080"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": hasil,
                "size": "xs",
                "margin": "none",
                "color": "#FF6347",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": "PLAY di bawah",
                "size": "xxl",
                "weight": "bold",
                "action": {
                  "uri": e,
                  "type": "uri",
                  "label": "Audio"
                },
                "margin": "xl",
                "align": "start",
                "color": "#FFD700",
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "horizontal"
      }
    ],
    "type": "box",
    "layout": "vertical"
  }
}
}
                                cl.postTemplate(to, data)
                                cl.sendAudioWithURL(to,e)
                            except Exception as error:
                                sendTextTemplate(to, "error\n" + str(error))
                                logError(error)
 
                        elif cmd == "set":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "           💫🔥Mikha_Lee🔥💫 - BOT\n"
                                if wait["sticker"] == True: md+="║⊛ Sticker On\n"
                                else: md+="║⊛ Sticker Off\n"
                                if wait["left"] == True: md+="║⊛ Left On\n"
                                else: md+="║⊛ Left Off\n"                        
                                if wait["contact"] == True: md+="║⊛ Contact On\n"
                                else: md+="║⊛ Contact Off\n"
                                if wait["talkban"] == True: md+="║⊛ Talkban「ON」\n"
                                else: md+="║⊛ Talkban On\n"
                                if wait["unsend"] == True: md+="║⊛ Unsend On\n"
                                else: md+="║⊛ Unsend Off\n"
                                if wait["Mentionkick"] == True: md+="║⊛ Notag On\n"
                                else: md+="║⊛ Notag Off\n"
                                if wait["detectMention"] == True: md+="║⊛ Respon On\n"
                                else: md+="║⊛ Respon Off\n"
                                if wait["autoJoin"] == True: md+="║⊛ Autojoin On\n"
                                else: md+="║⊛ Autojoin Off\n"
                                if wait["autoAdd"] == True: md+="║⊛ Autoadd On\n"
                                else: md+="║⊛ Autoadd On\n"
                                if msg.to in welcome: md+="║⊛ Welcome On\n"
                                else: md+="║⊛ Welcome Off\n"
                                if wait["autoLeave"] == True: md+="║⊛ Autoleave On\n"
                                else: md+="║⊛ Autoleave Off\n"
                                if msg.to in protectqr: md+="║⊛ Protecturl On\n"
                                else: md+="║⊛ Protecturl Off\n"
                                if msg.to in protectjoin: md+="║⊛ Protectjoin On\n"
                                else: md+="║⊛ Protectjoin Off\n"
                                if msg.to in protectkick: md+="⊛ Protectkick On\n"
                                else: md+="║⊛ Protectkick Off\n"
                                if msg.to in protectcancel: md+="║⊛ ProtectcancelOn\n"
                                else: md+="║⊛ Protectcancel Off\n╚════════════════╯\n"
                                sendTextTemplate3(msg.to, md+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                        elif cmd == "owner" or text.lower() == 'creator':
                            if msg._from in admin:
                                cl.sendMessage(msg.to, "u5808690099fd67b0965748afe4b43565") 
                                ma = ""
                                for i in creator:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'u5808690099fd67b0965748afe4b43565': i}, contentType=13)
                                    cl.sendMessage(msg.to, None, contentMetadata={"STKID":"16083749","STKPKGID":"1419343","STKVER":"1"}, contentType=7)


                        elif cmd == "about":
                                groups = cl.getGroupIdsJoined()
                                contacts = cl.getAllContactIds()
                                blockeds = cl.getBlockedContactIds()
                                crt = "u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540"
                                supp = "u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540"
                                suplist = []
                                lists = []
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                timeNoww = time.time()
                                for i in range(len(day)):
                                   if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                   if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nâ Jam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                data = {
                                        "type": "flex",
                                        "altText": "About",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#7CFC00"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "text": "    💫🔥Mikha_Lee🔥💫\nTEAM\n\nSELFBOT",
            "size": "sm",
            "color": "#FF0000",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#800080"
      },
      {
        "contents": [
          {
            "text": "💫🔥Mikha_Lee🔥💫 BOTS",
            "size": "xl",
            "align": "center",
            "color": "#00FFFF",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#800080"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "url": "https://i.ibb.co/27ZtgNz/20190105-183730.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "Myname: {}".format(cl.getProfile().displayName),
                "size": "md",
                "margin": "none",
                "color": "#ADFF2F",
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "type": "separator",
            "color": "#800080"
          },
          {
            "contents": [
              {
                "url": "https://i.ibb.co/27ZtgNz/20190105-183730.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "Waktu: {}".format(str(runtime)),
                "size": "xs",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://i.ibb.co/27ZtgNz/20190105-183730.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "Groups: {}".format(str(len(groups))),
                "size": "xs",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://i.ibb.co/27ZtgNz/20190105-183730.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "Friend: {}".format(str(len(contacts))),
                "size": "xs",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://i.ibb.co/27ZtgNz/20190105-183730.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "Block: {}".format(str(len(blockeds))),
                "size": "xs",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://i.ibb.co/27ZtgNz/20190105-183730.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "Versi",
                "size": "xs",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://i.ibb.co/27ZtgNz/20190105-183730.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "Support by\n💫🔥Mikha_Lee🔥💫 BOTS ",
                "size": "xs",
                "margin": "none",
                "color": "#FF6347",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": "          CREATOR",
                "size": "xxl",
                "weight": "bold",
                "action": {
                  "uri": "http://line.me/ti/p/keyla_77",
                  "type": "uri",
                  "label": "Add Creator"
                },
                "margin": "xl",
                "align": "start",
                "color": "#000000",
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FF0000"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": "           PROMO",
                "size": "xxl",
                "weight": "bold",
                "action": {
                  "uri": "line://app/1603968955-ORWb9RdY/?type=text&text=Promo",
                  "type": "uri",
                  "label": " ãOpen Orderã"
                },
                "margin": "xl",
                "align": "start",
                "color": "#000000",
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "horizontal"
      }
    ],
    "type": "box",
    "layout": "vertical"
  }
}
}
                                cl.postTemplate(to, data)

                        elif cmd == "aim":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                  musik(to)
                                  
                        elif cmd == ".me" or text.lower() == 'gue':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                msg.contentType = 13
                                msg.contentMetadata = {'mid': mid}
                                cl.sendContact(to, mid)

                        elif "autoreject " in msg.text.lower():
                            xpesan = msg.text.lower()
                            xres = xpesan.replace("autoreject ","")
                            if xres == "off":
                                settings['autorejc'] = False
                                sendTextTemplate(msg.to,"°❂°Auto Reject already Off")
                            elif xres == "on":
                                settings['autorejc'] = True
                                sendTextTemplate(msg.to,"°❂°Auto Reject already Onn")
                        
                        elif text.lower() == "mid":
                               cl.sendMessage(msg.to, msg._from)
                        elif text.lower() == "mymid":
                               cl.sendMessage(msg.to, msg._from)

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               cl.sendMessage(msg.to, None, contentMetadata={'u5808690099fd67b0965748afe4b43565': key1}, contentType=13)

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               sendTextTemplate8(msg.to, "?? Nama : "+str(mi.displayName)+"\n°❂°Mid : " +key1+"\n°❂° Status Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "mybot":
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in creator:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Amid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Bmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Cmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Dmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Emid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13 
                               msg.contentMetadata = {'mid': Zmid}
                               cl.sendMessage1(msg)

                        elif text.lower() == "hapus chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.removeAllMessages(op.param2)
                                   sendTextTemplate(msg.to,"°❂°Chat Done Clean")
                               except:
                                   pass

                        elif text.lower() == "hapus":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   ki.removeAllMessages(op.param2)
                                   ki.sendMessage(msg.to,"°❂°Chat Done Clean")
                                   kk.removeAllMessages(op.param2)
                                   kk.sendMessage(msg.to,"°❂°Chat Done Clean")
                                   kc.removeAllMessages(op.param2)
                                   kc.sendMessage(msg.to,"°❂°Chat Done Clean")
                                   ko.removeAllMessages(op.param2)
                                   ko.sendMessage(msg.to,"°❂°Chat Done Clean")
                                   jk.removeAllMessages(op.param2)
                                   jk.sendMessage(msg.to,"°❂°Chat Done Clean")
                                   sendTextTemplate(msg.to,"°❂°Chat Done Clean")
                               except:
                                   pass
                        
                        elif cmd.startswith("bs1: "):
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://media1.giphy.com/media/fnKtAO0GLeiD6/200w.webp?cid=19f5b51a5c454d542f704f7a6395da37",
        "action": {
          "uri": "http://line.me/ti/p/keyla_77",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#00008B"
        },
        "header": {
          "backgroundColor": "#00008B"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": pesan,
                    "color": "#FF0000",
                    "wrap": True,
                    "weight": "bold",
                    "type": "text",
                    "size": "lg",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "BRODCAST",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/keyla_77"
            },
            "align": "center"            
          }
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "💫🔥Mikha_Lee🔥💫 BOTS",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "align": "center"            
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                   cl.postFlex(group, data)
                                   
                        elif cmd.startswith("broadcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   sendTextTemplate8(group,"[ Broadcast ]\n" + str(pesan))

                        elif "zilong" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://4.bp.blogspot.com/-W_bn2qqdYXE/Wyhbjj2wqKI/AAAAAAANIz4/KQVsbq-aXm0kZNfFOS5SN8fqCvQ18xnUACLcBGAs/s1600/AW1238502_03.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/keyla_77"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
                        elif "natali" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://3.bp.blogspot.com/-OfIz4mSIumw/WbLEZw7l6nI/AAAAAAARd6Y/Dxzos1SA_5MU32bXFTKToLDndM7YpV7WACLcBGAs/s1600/AW529310_04.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/keyla_77"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data) 
                        elif "alucard" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.ibb.co/dJ1H13M/Benjol.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/keyla_77"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
                                    
                        elif "jhonson" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.ibb.co/y0wP3fJ/tai-line.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/keyla_77"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
                                    
                        elif "hayabusa" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://thumbs.gfycat.com/QuaintScornfulAmericanlobster-small.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/keyla_77"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
                                    
                        elif "lyla" in msg.text.lower():                     	
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.ibb.co/CVMQ40k/7c8ab257ee3b7e1ef283b7c0a35d9d2c.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/keyla_77"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
           
                        elif "grock" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://thumbs.gfycat.com/KlutzyUglyGelding-small.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/keyla_77"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
                                    
                        elif "tresla" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://thumbs.gfycat.com/BigIdealAsianelephant-small.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/keyla_77"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
                                    
                        elif "minotur" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.ibb.co/hHG5Mwb/AW316819-05.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/keyla_77"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "「Mykey」\nSetkey bot mu「 " + str(Setmain["keyCommand"]) + " 」")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendTextTemplate(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   sendTextTemplate(msg.to, "「Setkey」\nSetkey diganti jadi「{}」".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               sendTextTemplate(msg.to, "「Setkey」\nSetkey mu kembali ke awal")

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendTextTemplate8(msg.to, "°❂°Waittings 10 Seccond ....\n And You Klik Type [ Rs ]...")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                               sendTextTemplate(msg.to, "°❂°Done Restart...")
                            
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "°❂° Bot telah aktif selama °❂°\n" +waktu(eltime)
                               sendTextTemplate8(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "°❂°Tertutup"
                                    gTicket = "⚠Tidak ada"
                                else:
                                    gQr = "°❂°Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                sendTextTemplate8(msg.to, "{💫🔥Mikha_Lee🔥💫 TEAM BOTS}Grup Info\n\n°❂° Nama Group : {}".format(G.name)+ "\n°❂° ID Group : {}".format(G.id)+ "\n°❂° Pembuat : {}".format(G.creator.displayName)+ "\n°❂° Waktu Dibuat : {}".format(str(timeCreated))+ "\n°❂° Jumlah Member : {}".format(str(len(G.members)))+ "\n°❂° Jumlah Pending : {}".format(gPending)+ "\n°❂° Group Qr : {}".format(gQr)+ "\n°❂° Group Ticket : {}".format(gTicket))
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                            except Exception as e:
                                sendTextTemplate(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "°❂°Tertutup"
                                    gTicket = "⚠Tidak ada"
                                else:
                                    gQr = "°❂°Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "〘  COMMAND  〙Grup Info\n"
                                ret_ += "\n°❂° Nama Group : {}".format(G.name)
                                ret_ += "\n°❂° ID Group : {}".format(G.id)
                                ret_ += "\n°❂° Pembuat : {}".format(gCreator)
                                ret_ += "\n°❂° Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n°❂° Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n°❂° Jumlah Pending : {}".format(gPending)
                                ret_ += "\n°❂° Group Qr : {}".format(gQr)
                                ret_ += "\n°❂° Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                sendTextTemplate8(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "╠➩ "+ str(no) + ". " + mem.displayName
                                sendTextTemplate(to," ↪Group Name↩ : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n↪Total %i Members↩" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("leave: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = cl.getGroup(i)
                                if ginfo == group:
                                    ki.leaveGroup(i)
                                    kk.leaveGroup(i)
                                    kc.leaveGroup(i)
                                    km.leaveGroup(i)
                                    kb.leaveGroup(i)
                                    ko.leaveGroup(i)
                                    ke.leaveGroup(i)
                                    kf.leaveGroup(i)
                                    kg.leaveGroup(i)
                                    kh.leaveGroup(i)
                                    sendTextTemplate4(msg.to,"°❂°Berhasil keluar di grup " +str(ginfo.name))

                        elif cmd == "friendlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠➩ " + str(a) + ". " +G.displayName+ "\n"
                               sendTextTemplate3(msg.to,"╔══[ FRIEND LIST ]\n║\n"+ma+"║\n╚══[ Total↪"+str(len(gid))+"↩Friends ]")

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠➩ " + str(a) + ". " +G.name+ "\n"
                               sendTextTemplate3(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total↪"+str(len(gid))+"↩Groups ]")

                        elif cmd == "gruplist1":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = ki.getGroupIdsJoined()
                               for i in gid:
                                   G = ki.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠➩ " + str(a) + ". " +G.name+ "\n"
                               ki.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total↪"+str(len(gid))+"↩Groups ]")

                        elif cmd == "gruplist2":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kk.getGroupIdsJoined()
                               for i in gid:
                                   G = kk.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠➩ " + str(a) + ". " +G.name+ "\n"
                               kk.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total↪"+str(len(gid))+"↩Groups ]")

                        elif cmd == "gruplist3":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kc.getGroupIdsJoined()
                               for i in gid:
                                   G = kc.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠➩ " + str(a) + ". " +G.name+ "\n"
                               kc.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total↪"+str(len(gid))+"↩Groups ]")
                               
                        elif cmd == "gruplist4":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = ko.getGroupIdsJoined()
                               for i in gid:
                                   G = ko.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠➩ " + str(a) + ". " +G.name+ "\n"
                               ko.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total↪"+str(len(gid))+"↩Groups ]")                               

                        elif cmd == "open":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   cl.updateGroup(X)
                                   sendTextTemplate(msg.to, "°❂°Url Opened")

                        elif cmd == "close":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   sendTextTemplate(msg.to, "°❂°Url Closed")

                        elif cmd == "url grup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

#===========BOT UPDATE============#
                        elif cmd == "updategrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                sendTextTemplate(msg.to,"°❂°Kirim fotonya")

                        elif cmd == "updatebot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                sendTextTemplate(msg.to,"°❂°Kirim fotonya")
                                
                        elif cmd == "gantifoto":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["RAfoto"][mid] = True
                                sendTextTemplate(msg.to,"°❂°Kirim fotonya")
                                
                        elif cmd == "bot1cpp":
                            if msg._from in admin:
                                Setmain["RAfoto"][Amid] = True
                                ki.sendMessage(msg.to,"°❂°Kirim fotonya")
                                
                        elif cmd == "bot2cpp":
                            if msg._from in admin:
                                Setmain["RAfoto"][Bmid] = True
                                kk.sendMessage(msg.to,"°❂°Kirim fotonya")
                                
                        elif cmd == "bot3cpp":
                            if msg._from in admin:
                                Setmain["RAfoto"][Cmid] = True
                                kc.sendMessage(msg.to,"°❂°Kirim fotonya")
                                
                        elif cmd == "bot4cpp":
                            if msg._from in admin:
                                Setmain["RAfoto"][Dmid] = True
                                ko.sendMessage(msg.to,"°❂°Kirim fotonya")                                
                                
                        elif cmd == "bot5cpp":
                            if msg._from in admin:
                                Setmain["RAfoto"][Zmid] = True
                                sw.sendMessage(msg.to,"°❂°Kirim fotonya")

                        elif cmd.startswith("myname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                sendTextTemplate(msg.to,"°❂°Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot1gname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ki.getProfile()
                                profile.displayName = string
                                ki.updateProfile(profile)
                                ki.sendMessage(msg.to,"°❂°Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot2gname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kk.getProfile()
                                profile.displayName = string
                                kk.updateProfile(profile)
                                kk.sendMessage(msg.to,"°❂°Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot3gname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kc.getProfile()
                                profile.displayName = string
                                kc.updateProfile(profile)
                                kc.sendMessage(msg.to,"°❂°Nama diganti jadi " + string + "")
                                
                        elif cmd.startswith("bot4gname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ko.getProfile()
                                profile.displayName = string
                                ko.updateProfile(profile)
                                ko.sendMessage(msg.to,"°❂°Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot5gname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = sw.getProfile()
                                profile.displayName = string
                                sw.updateProfile(profile)
                                sw.sendMessage(msg.to,"°❂°Nama diganti jadi " + string + "")

#===========BOT UPDATE============#
                        elif cmd == "tag" or text.lower() == 'mention':
                           if wait["selfbot"] == True:
                            if msg._from in admin:
                             group = cl.getGroup(msg.to)
                            nama = [contact.mid for contact in group.members]
                            k = len(nama)//20
                            for a in range(k+1):
                                txt = u''
                                s=0
                                b=[]
                                for i in group.members[a*20 : (a+1)*20]:
                                    b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                    s += 7
                                    txt += u'@Zero \n'
                                cl.sendMessage(msg.to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)

                        elif cmd == "listbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                sendTextTemplate3(msg.to,"↪°❂°List Bot°❂°\n\n"+ma+"\n°❂°Jumlah Total Bot「%s」°❂°" %(str(len(Bots))))

                        elif cmd == "listadmin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getContact(m_id).displayName + "\n"
                                sendTextTemplate3(msg.to,"°❂°Daftar Admin°❂°\n\n°❂° Super admin:\n"+ma+"\n°❂°Admin:\n"+mb+"\n°❂° Staff:\n"+mc+"\n°❂° Jumlah Total Keseluruhan「%s」°❂°" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "listprotect":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getGroup(group).name + "\n"
                                sendTextTemplate3(msg.to,"°❂°Daftar Protection°❂°\n\n°❂° Protect URL :\n"+ma+"\n°❂° Protect KICK :\n"+mb+"\n°❂° Protect JOIN :\n"+md+"\n🔘 Protect CANCEL:\n"+mc+"\nTotal ↪%s↩ Grup yang dijaga" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel))))

                        elif cmd == "sk":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ki.sendMessage(msg.to,responsename1)
                                kk.sendMessage(msg.to,responsename2)
                                kc.sendMessage(msg.to,responsename3)
                                ko.sendMessage(msg.to,responsename4)
                                jk.sendMessage(msg.to,responsename5)   

                        elif cmd == "join":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Bmid,Cmid,Amid,Dmid,Emid,Zmid]
                                    cl.inviteIntoGroup(msg.to, anggota)
                                    kk.acceptGroupInvitation(msg.to)
                                    kc.acceptGroupInvitation(msg.to)
                                    ki.acceptGroupInvitation(msg.to)
                                    ko.acceptGroupInvitation(msg.to)
                                    jk.acceptGroupInvitation(msg.to)
                                except:
                                    pass
                                    
                        elif cmd == "sekarang":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = cl.getGroup(msg.to)
                                    cl.inviteIntoGroup(msg.to, [Zmid])
                                    sendTextTemplate(msg.to,"[ Group ]\n°❂°"+str(ginfo.name)+"\n°❂°Done Actived GS")
                                except:
                                    pass             
                            

                        elif cmd == "pulang":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ki.leaveGroup(msg.to)
                                ki.leaveGroup(msg.to)
                                kk.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                ko.leaveGroup(msg.to)
                                jk.leaveGroup(msg.to)
                                
                        elif cmd == "byeme":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                sendTextTemplate4(msg.to, "Bye_______\n       "+str(G.name))
                                cl.leaveGroup(msg.to)

                        elif cmd.startswith("joinall "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(group)
                                cl.acceptGroupInvitationByTicket(group,Ticket)
                                ki.acceptGroupInvitationByTicket(group,Ticket)
                                kk.acceptGroupInvitationByTicket(group,Ticket)
                                kc.acceptGroupInvitationByTicket(group,Ticket)
                                ko.acceptGroupInvitationByTicket(group,Ticket)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                                try:
                                    gCreator = G.creator.mid
                                    dia = cl.getContact(gCreator)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = '「 Sukses Masuk Group 」\n• Creator :  '
                                    diaa = str(dia.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@a\n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += xpesan+zxc
                                ret_ += "• Nama grup : {}".format(G.name)
                                ret_ += "\n• Group Qr : {}".format(gQr)
                                ret_ += "\n• Pendingan : {}".format(gPending)
                                ret_ += "\n• Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                sendTextTemplate3(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                            except:
                                pass

                        elif cmd.startswith("leave "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        ki.sendMessage(i, "Silahkan admin invite atau masukan kembali")
                                        ki.leaveGroup(i)
                                        kk.leaveGroup(i)
                                        kc.leaveGroup(i)
                                        ko.leaveGroup(i)                                        
                                        sendTextTemplate4(to,"°❂°Berhasil keluar dari grup " +h)

                        elif cmd == "as1":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)

                        elif cmd == "as2":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kk.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kk.updateGroup(G)

                        elif cmd == "as3":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kc.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kc.updateGroup(G)
                                
                        elif cmd == "as4":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ko.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ko.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ko.updateGroup(G)
                                
                        elif cmd == "js in":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = sw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                sw.updateGroup(G)

                        elif cmd == "js out":
                            if msg._from in admin:
                                G = sw.getGroup(msg.to)
                                sw.sendMessage(msg.to, "Bye_______\n       "+str(G.name))
                                sw.leaveGroup(msg.to)

                        elif cmd == "lali":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                sendTextTemplate(msg.to, " °❂°Kecepatan respon°❂°\n\n°❂°Get Profile\n°❂°   %.10f\n°❂°Get Contact\n°❂°   %.10f\n°❂°Get Group\n°❂°   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == ".speed" or cmd == "sp bot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               elapsed_time = time.time() - start
                               cl.sendMessage(msg.to, "{} detik".format(str(elapsed_time/10)))
                               ki.sendMessage(msg.to, "{} detik".format(str(elapsed_time/10)))
                               kk.sendMessage(msg.to, "{} detik".format(str(elapsed_time/10)))
                               kc.sendMessage(msg.to, "{} detik".format(str(elapsed_time/10)))
                               ko.sendMessage(msg.to, "{} detik".format(str(elapsed_time/10)))
                               jk.sendMessage(msg.to, "{} detik".format(str(elapsed_time/10)))
                               
                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                sendTextTemplate(msg.to, "Waittings")
                                sendTextTemplate(msg.to, "╭═══════════╮\n%.10f Seccond\n╰═══════════╯" % (get_profile_time/3))

                        elif cmd == "lurking on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['RAreadPoint'][msg.to] = msg_id
                                 Setmain['RAreadMember'][msg.to] = {}
                                 sendTextTemplate(msg.to, "°❂°Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurking off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['RAreadPoint'][msg.to]
                                 del Setmain['RAreadMember'][msg.to]
                                 sendTextTemplate(msg.to, "°❂°Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurkers":
                          if msg._from in admin:
                            if msg.to in Setmain['RAreadPoint']:
                                if Setmain['RAreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['RAreadMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Lurkers ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(cl.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        cl.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['RAreadPoint'][msg.to]
                                        del Setmain['RAreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['RAreadPoint'][msg.to] = msg.id
                                    Setmain['RAreadMember'][msg.to] = {}
                                else:
                                    sendTextTemplate(msg.to, "User kosong...")
                            else:
                                sendTextTemplate(msg.to, "Ketik lurking on dulu")

                        elif cmd == "kiss on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  sendTextTemplate(msg.to, "°❂°Cek sider diaktifkan\n\n°❂°Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n°❂°Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "kiss off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  sendTextTemplate(msg.to, "°❂°Cek sider dinonaktifkan\n\n°❂°Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n°❂°Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  sendTextTemplate(msg.to, "°❂°Sudak tidak aktif")

#===========Hiburan============#
                        elif cmd.startswith("sholat: "):
                          if msg._from in admin:
                             sep = text.split(" ")
                             location = text.replace(sep[0] + " ","")
                             with requests.session() as web:
                                  web.headers["user-agent"] = random.choice(settings["userAgent"])
                                  r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                                  data = r.text
                                  data = json.loads(data)
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                                         ret_ = "「Jadwal Sholat」"
                                         ret_ += "\n▶ Lokasi : " + data[0]
                                         ret_ += "\n▶ " + data[1]
                                         ret_ += "\n▶ " + data[2]
                                         ret_ += "\n▶ " + data[3]
                                         ret_ += "\n▶ " + data[4]
                                         ret_ += "\n▶ " + data[5]
                                         ret_ += "\n\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                         ret_ += "\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                  sendTextTemplate3(msg.to, str(ret_))

                        elif cmd.startswith("cuaca: "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            location = text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                if "result" not in data:
                                    ret_ = "°❂°Status Cuaca°❂°"
                                    ret_ += "\n°❂° Lokasi : " + data[0].replace("❄Temperatur di kota ","")
                                    ret_ += "\n°❂° Suhu : " + data[1].replace("⛄Suhu : ","") + " C"
                                    ret_ += "\n°❂° Kelembaban : " + data[2].replace("💧Kelembaban : ","") + " %"
                                    ret_ += "\n°❂° Tekanan udara : " + data[3].replace("☁Tekanan udara : ","") + " HPa"
                                    ret_ += "\n°❂° Kecepatan angin : " + data[4].replace("🌀Kecepatan angin : ","") + " m/s"
                                    ret_ += "\n\n°❂°Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\n°❂°Jam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                sendTextTemplate3(msg.to, str(ret_))

                        elif cmd.startswith("lokasi: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            location = msg.text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                if data[0] != "" and data[1] != "" and data[2] != "":
                                    link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                    ret_ = "°❂°Info Lokasi°❂°"
                                    ret_ += "\n °❂°Location : " + data[0]
                                    ret_ += "\n °❂°Google Maps : " + link
                                else:
                                    ret_ = "[Details Location] Error : Location not found"
                                sendTextTemplate3(msg.to,str(ret_))

                        elif cmd.startswith("lirik: "):
                           if msg._from in admin:
                               sep = msg.text.split(" ")
                               search = msg.text.replace(sep[0] + " ","")
                               params = {'songname': search}
                               with requests.session() as web:
                                   web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                   r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?{}".format(urllib.parse.urlencode(params)))
                                   try:
                                      data = json.loads(r.text)
                                      for song in data:
                                          songs = song[5]
                                          lyric = songs.replace('ti:','Title - ')
                                          lyric = lyric.replace('ar:','Artist - ')
                                          lyric = lyric.replace('al:','Album - ')
                                          removeString = "[1234567890.:]"
                                          for char in removeString:
                                              lyric = lyric.replace(char,'')
                                          ret_ = "╔══[ Lyric🎵 ]═════════"
                                          ret_ += "\n╠➩ Nama lagu : {}".format(str(song[0]))
                                          ret_ += "\n╠➩ Durasi : {}".format(str(song[1]))
                                          ret_ += "\n╠➩ Link : {}".format(str(song[3]))
                                          ret_ += "\n╚══[ Finish ]═════════\n\nLirik nya :\n{}".format(str(lyric))
                                          cl.sendMessage(msg.to, str(ret_))
                                   except:
                                       sendTextTemplate(to, "°❂°Lirik tidak ditemukan")

                        elif cmd.startswith("music "):
                            if msg._from in admin:
                               sep = msg.text.split(" ")
                               query = msg.text.replace(sep[0] + " ","")
                               cond = query.split("-")
                               search = str(cond[0])
                               with requests.session() as web:
                                   web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                   result = web.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                                   data = result.text
                                   data = json.loads(data)
                                   if len(cond) == 1:
                                      num = 0
                                      ret_ = "「 Pencarian Musik 」\n"
                                      for music in data["result"]:
                                          num += 1
                                          ret_ += "\n {}. {}".format(str(num), str(music["single"]))
                                      ret_ += "\n\n「 Total {} Pencarian 」".format(str(len(data["result"])))
                                      cl.sendMessage(to, str(ret_))
                                      sendMention(msg.to, msg._from,"","\nJika ingin menggunakan,\nSilahkan gunakan:\n\nMusik penyanyi-angka")
                                   if len(cond) == 2:
                                        num = int(cond[1])
                                        if num <= len(data["result"]):
                                               music = data["result"][num - 1]
                                               with requests.session() as web:
                                                    web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                                    result = web.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                                    data = result.text
                                                    data = json.loads(data)
                                                    if data["result"] != []:
                                                         ret_ = "「 Pencarian Musik 」"
                                                         ret_ += "\n°❂°Judul : {}".format(str(data["result"]["song"]))
                                                         ret_ += "\n°❂° Album : {}".format(str(data["result"]["album"]))
                                                         ret_ += "\n°❂° Ukuran : {}".format(str(data["result"]["size"]))
                                                         ret_ += " \n°❂° Link Musik : {}".format(str(data["result"]["mp3"]))
                                                         ret_ += "\n「 Tunggu Musiknya Keluar 」"
                                                         cl.sendImageWithURL(to, str(data["result"]["img"]))
                                                         cl.sendMessage(to, str(ret_))
                                                         cl.sendAudioWithURL(to, str(data["result"]["mp3"][0]))   
                     
                        elif cmd.startswith("music: "):
                           if msg._from in admin:
                              sep = msg.text.split(" ")
                              search = msg.text.replace(sep[0] + " ","")
                              params = {'songname': search}
                              with requests.session() as web:
                                  web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                  r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?{}".format(urllib.parse.urlencode(params)))
                                  try:
                                      data = json.loads(r.text)
                                      for song in data:
                                          ret_ = "╔══( 〘 Music 〙)═══════"
                                          ret_ += "\n╠°❂° Judul lagu : {}".format(str(song[0]))
                                          ret_ += "\n╠°❂° Durasi : {}".format(str(song[1]))
                                          ret_ += "\n╠°❂° Link : {}".format(str(song[3]))
                                          ret_ += "\n╚══(〘 Waiting Audio 〙)═══════"
                                      cl.sendMessage(msg.to, str(ret_))
                                      cl.sendMessage(msg.to, "°❂° Mohon bersabar musicnya lagi di upload")
                                      cl.sendAudioWithURL(msg.to, song[3])
                                  except:
                                      cl.sendMessage(to, "°❂° Musik tidak ditemukan")

                        elif cmd.startswith("gimage: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            search = msg.text.replace(sep[0] + " ","")
                            url = "https://api.xeonwz.ga/api/image/google?q={}".format(urllib.parse.quote(search))
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                r = web.get(url)
                                data = r.text
                                data = json.loads(data)
                                if data["data"] != []:
                                    start = timeit.timeit()
                                    items = data["data"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    cl.sendMessage(msg.to,"「Google Image」\nType : Search Image\nTime taken : %seconds" % (start))
                                    cl.sendImageWithURL(msg.to, str(path))

                        elif cmd.startswith("ytmp4: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "°❂° Judul °❂°〘 " + vid.title + " 〙"
                                    author = '\n\n°❂° Author : ' + str(vid.author)
                                    durasi = '\n°❂° Duration : ' + str(vid.duration)
                                    suka = '\n°❂° Likes : ' + str(vid.likes)
                                    rating = '\n°❂° Rating : ' + str(vid.rating)
                                    deskripsi = '\n°❂° Deskripsi : ' + str(vid.description)
                                cl.sendVideoWithURL(msg.to, me)
                                cl.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendMessage(msg.to,str(e))

                        elif cmd.startswith("ytmp3: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                bestaudio = vid.getbestaudio()
                                bestaudio.bitrate
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    shi = bestaudio.url
                                    me = best.url
                                    vin = s.url
                                    hasil = ""
                                    title = "°❂°Judul °❂°〘 " + vid.title + " 〙"
                                    author = '\n\n°❂° Author : ' + str(vid.author)
                                    durasi = '\n°❂° Duration : ' + str(vid.duration)
                                    suka = '\n°❂° Likes : ' + str(vid.likes)
                                    rating = '\n°❂° Rating : ' + str(vid.rating)
                                    deskripsi = '\n°❂° Deskripsi : ' + str(vid.description)
                                cl.sendImageWithURL(msg.to, me)
                                cl.sendAudioWithURL(msg.to, shi)
                                cl.sendText(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendText(msg.to,str(e))

                        elif cmd.startswith("profileig: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                                data = response.json()
                                namaIG = str(data['user']['full_name'])
                                bioIG = str(data['user']['biography'])
                                mediaIG = str(data['user']['media']['count'])
                                verifIG = str(data['user']['is_verified'])
                                usernameIG = str(data['user']['username'])
                                followerIG = str(data['user']['followed_by']['count'])
                                profileIG = data['user']['profile_pic_url_hd']
                                privateIG = str(data['user']['is_private'])
                                followIG = str(data['user']['follows']['count'])
                                link = "°❂° Link : " + "https://www.instagram.com/" + instagram
                                text = "°❂° Name : "+namaIG+"\n°❂° Username : "+usernameIG+"\n°❂° Biography : "+bioIG+"\n°❂° Follower : "+followerIG+"\n°❂° Following : "+followIG+"\n°❂° Post : "+mediaIG+"\n°❂° Verified : "+verifIG+"\n°❂° Private : "+privateIG+"" "\n" + link
                                cl.sendImageWithURL(msg.to, profileIG)
                                cl.sendMessage(msg.to, str(text))
                            except Exception as e:
                                    cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("cekdate: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            sendTextTemplate3(msg.to,"°❂° I N F O R M A S I °❂°\n\n"+"°❂° Date Of Birth : "+lahir+"\n°❂° Age : "+usia+"\n°❂° Ultah : "+ultah+"\n°❂° Zodiak : "+zodiak)

                        elif cmd.startswith("jumlah: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["RAlimit"] = num
                                sendTextTemplate(msg.to,"°❂° Total Spamtag Diubah Menjadi " +strnum)

                        elif cmd.startswith("naik: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                sendTextTemplate(msg.to,"°❂° Total Spamcall Diubah Menjadi " +strnum)

                        elif cmd.startswith("stag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["RAlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage(msg)
                                            except Exception as e:
                                                cl.sendMessage(msg.to,str(e))
                                    else:
                                        sendTextTemplate(msg.to,"Jumlah melebihi 1000")
                                        
                        elif cmd == "naik":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                cl.sendMessage(msg.to, "°❂°Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        cl.acquireGroupCallRoute(to)
                                        cl.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        cl.sendText(msg.to,str(e))
                                else:
                                    sendTextTemplate(msg.to,"Jumlah melebihi batas")

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      ki.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kk.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kc.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, str(Setmain["RAmessage1"]))
                                      ki.sendMessage(midd, str(Setmain["RAmessage1"]))
                                      kk.sendMessage(midd, str(Setmain["RAmessage1"]))
                                      kc.sendMessage(midd, str(Setmain["RAmessage1"]))

                        elif 'ID line: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              msgs = msg.text.replace('ID line: ','')
                              conn = cl.findContactsByUserid(msgs)
                              if True:
                                  cl.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  cl.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)

#===========Protection============#
                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg Done Active"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "°❂° Welcome Msg Done Active\n°❂°Di Group : " +str(ginfo.name)
                                  sendTextTemplate(msg.to, "°❂° Diaktifkan °❂°\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "°❂° Welcome Msg dinonaktifkan\n°❂°Di Group : " +str(ginfo.name)
                                    else:
                                         msgs = "°❂° Welcome Msg sudah tidak aktif"
                                    sendTextTemplate(msg.to, "°❂° Dinonaktifkan °❂°\n" + msgs)

                        elif 'Tisu ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Allprotect ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "°❂°Semua protect sudah on\n°❂°Di Group : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "°❂°Berhasil mengaktifkan semua protect\n°❂°Di Group : " +str(ginfo.name)
                                  sendTextTemplate(msg.to, "°❂°Diaktifkan°❂°\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "°❂°Berhasil menonaktifkan semua protect\n°❂°Di Group : " +str(ginfo.name)
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "°❂°Semua protect sudah off\n°❂°Di Group : " +str(ginfo.name)
                                    sendTextTemplate(msg.to, "°❂°Dinonaktifkan°❂°\n" + msgs)

#=========== KICKOUT ============#
                        elif ("pulang " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = cl.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           cl.updateGroup(G)
                                           invsend = 0
                                           Ticket = cl.reissueGroupTicket(msg.to)
                                           sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           sw.kickoutFromGroup(msg.to, [target])
                                           sw.leaveGroup(msg.to)
                                           X = cl.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           cl.updateGroup(X)
                                       except:
                                           pass
              
                        elif "Gusur" in msg.text:
                           if msg._from in Bots:
                            if msg.toType == 2:
                             #  print "Otw cleanse"
                               _name = msg.text.replace("Gusur","")
                               gs = ki.getGroup(msg.to)
                               gs = kk.getGroup(msg.to)
                               gs = kc.getGroup(msg.to)  
                               gs = ko.getGroup(msg.to)               
                               ki.sendMessage(msg.to,"Maap maap")
                               targets = []
                               for g in gs.members:
                                   if _name in g.displayName:
                                       targets.append(g.mid)
                               if targets == []:
                                  ki.sendMessage(msg.to,"Not found")
                              #    else:
                               for target in targets:
                                     if target not in Bots:
                                      try:
                                          klist=[ki,kk,kc,ko]
                                          kicker=random.choice(klist)
                                          kicker.kickoutFromGroup(msg.to,[target])
                                          print (msg.to,[g.mid])
                                      except:
                                          ki.sendMessage(msg.to,"wkwkwkwkwk")

                        elif ("Kick " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

#===========ADMIN ADD============#
                        elif ("Adminadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.append(target)
                                           sendTextTemplate(msg.to,"°❂°Berhasil menambahkan admin")
                                       except:
                                           pass

                        elif ("Staffadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           sendTextTemplate(msg.to,"°❂°Berhasil menambahkan staff")
                                       except:
                                           pass

                        elif ("Botadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           sendTextTemplate(msg.to,"°❂°Berhasil menambahkan bot")
                                       except:
                                           pass

                        elif ("Admindell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           admin.remove(target)
                                           sendTextTemplate(msg.to,"°❂°Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Staffdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           staff.remove(target)
                                           sendTextTemplate(msg.to,"°❂°Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Botdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           Bots.remove(target)
                                           sendTextTemplate(msg.to,"°❂°Berhasil menghapus admin")
                                       except:
                                           pass

                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in admin:
                                wait["addadmin"] = True
                                sebdTextTemplate(msg.to,"°❂°Kirim kontaknya")

                        elif cmd == "admin:repeat" or text.lower() == 'admin:repeat':
                            if msg._from in admin:
                                wait["delladmin"] = True
                                sendTextTemplate(msg.to,"°❂°Kirim kontaknya...")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in admin:
                                wait["addstaff"] = True
                                sendTextTemplate(msg.to,"°❂°Kirim kontaknya...")

                        elif cmd == "staff:repeat" or text.lower() == 'staff:repeat':
                            if msg._from in admin:
                                wait["dellstaff"] = True
                                sendTextTemplate(msg.to,"°❂°Kirim kontaknya...")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in admin:
                                wait["addbots"] = True
                                sendTextTemplate(msg.to,"°❂°Kirim kontaknya...")

                        elif cmd == "bot:repeat" or text.lower() == 'bot:repeat':
                            if msg._from in admin:
                                wait["dellbots"] = True
                                sendTextTemplate(msg.to,"°❂°Kirim kontaknya...")

                        elif cmd == "refresh" or text.lower() == 'sapu':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                sendTextTemplate(msg.to,"°❂°Berhasil di Refresh...")

                        elif cmd == "contact admin" or text.lower() == 'contact admin':
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact staff" or text.lower() == 'contact staff':
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact bot" or text.lower() == 'contact bot':
                            if msg._from in admin:
                                ma = ""
                                for i in Bots:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "unsend on" or text.lower() == 'unsend on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["unsend"] = True
                                sendTextTemplate(msg.to,"°❂°Deteksi unsend diaktifkan")

                        elif cmd == "unsend off" or text.lower() == 'unsend off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["unsend"] = False
                                sendTextTemplate(msg.to,"°❂°Deteksi unsend dinonaktifkan")
                                
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                sendTextTemplate(msg.to,"°❂°Notag diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["MentionKick"] = False
                                sendTextTemplate(msg.to,"°❂°Notag dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                sendTextTemplate(msg.to,"°❂°Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                sendTextTemplate(msg.to,"°❂°Deteksi contact dinonaktifkan")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                sendTextTemplate(msg.to,"°❂°Auto respon diaktifkan")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                sendTextTemplate(msg.to,"°❂°Auto respon dinonaktifkan")
                                
                        elif cmd == "responpm on" or text.lower() == 'responpm on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["arespon"] = True
                                sendTextTemplate(msg.to,"°❂°Auto respon pm diaktifkan")

                        elif cmd == "responpm off" or text.lower() == 'responpm off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["arespon"] = False
                                sendTextTemplate(msg.to,"°❂°Auto respon pm dinonaktifkan")          

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                sendTextTemplate(msg.to,"°❂°Autojoin diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                sendTextTemplate(msg.to,"°❂°Autojoin dinonaktifkan")
                                
                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                sendTextTemplate(msg.to,"°❂°Deteksi sticker diaktifkan")            
                                
                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                sendTextTemplate(msg.to,"°❂°Deteksi sticker dinonaktifkan")         

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                sendTextTemplate(msg.to,"°❂°Autoleave diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                sendTextTemplate(msg.to,"°❂°Autoleave dinonaktifkan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                sendTextTemplate(msg.to,"°❂°Auto add diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                sendTextTemplate(msg.to,"°❂°Auto add dinonaktifkan")
                                
                        elif cmd == "left on" or text.lower() == 'left on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["left"] = True
                                sendTextTemplate(msg.to,"°❂°Left diaktifkan")

                        elif cmd == "left off" or text.lower() == 'left off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["left"] = False
                                sendTextTemplate(msg.to,"°❂°left dinonaktifkan")
                                
                        elif cmd == "autoblock on" or text.lower() == 'autoblock on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoBlock"] = True
                                sendTextTemplate(msg.to,"°❂°AutoBlock diaktifkan")
                                
                        elif cmd == "autoblock off" or text.lower() == 'autoblock off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoBlock"] = True
                                sendTextTemplate(msg.to,"°❂°AutoBlock dinonaktifkan")          

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = True
                                sendTextTemplate(msg.to,"°❂°Join ticket diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = False
                                sendTextTemplate(msg.to,"°❂°Notag dinonaktifkan")

#===========COMMAND BLACKLIST============#
                        elif ("Talkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           sendTextTemplate(msg.to,"°❂°Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Untalkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           sendTextTemplate(msg.to,"°❂°Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                sendTextTemplate(msg.to,"°❂°Kirim kontaknya...")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                sendTextTemplate(msg.to,"°❂°Kirim kontaknya...")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           sendTextTemplate(msg.to,"°❂°Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           sendTextTemplate(msg.to,"°❂°Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                sendTextTemplate(msg.to,"°❂°Kirim kontaknya...")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                sendTextTemplate(msg.to,"°❂°Kirim kontaknya...")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                sendTextTemplate(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                sendTextTemplate3(msg.to,"〘 Blacklist User 〙\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                sendTextTemplate(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                sendTextTemplate(msg.to,"〘 Blacklist User 〙Talkban User\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "buron" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    sendTextTemplate(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "panu" or text.lower() == 'panu':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = cl.getContacts(wait["blacklist"])
                              mc = "「%i」User Blacklist" % len(ragets)
                              sendTextTemplate(msg.to,"°❂° Done Clear BL \n  "    +mc)
#===========COMMAND SET============#
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "°❂°Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  sendTextTemplate(msg.to, "°❂°Pesan Msg°❂°\n°❂°Pesan Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "°❂°Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  sendTextTemplate(msg.to, "°❂°Welcome Msg°❂°\n°❂°Welcome Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "°❂°Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  sendTextTemplate(msg.to, "°❂°Respon Msg°❂°\n°❂°Respon Msg diganti jadi :\n\n「{}」".format(str(spl)))
                        elif 'Set left: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set left: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "°❂°Gagal mengganti Respon Msg")
                              else:
                                  wait["left"] = spl
                                  sendTextTemplate(msg.to, "°❂°Respon Left°❂°\n°❂°Respon left diganti jadi :\n\n「{}」".format(str(spl)))
                        elif 'Set spam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "°❂°Gagal mengganti Spam")
                              else:
                                  Setmain["RAmessage1"] = spl
                                  sendTextTemplate(msg.to, "°❂°Spam Msg°❂°\n°❂°Spam Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "°❂°Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  sendTextTemplate(msg.to, "°❂°Sider Msg°❂°\n°❂°Sider Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "°❂°Pesan Msg°❂°\n°❂°Pesan Msg mu :\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "cek left":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "°❂°left Msg°❂°\n°❂°Left Msg mu :\n\n「 " + str(wait["left"]) + " 」")

                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "°❂°Welcome Msg°❂°\n°❂°Welcome Msg mu :\n\n「 " + str(wait["welcome"]) + " 」")

                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "°❂°Respon Msg°❂°\n°❂°Respon Msg mu :\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "°❂°Spam Msg°❂°\n°❂°Spam Msg mu :\n\n「 " + str(Setmain["RAmessage1"]) + " 」")

                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "°❂°Sider Msg°❂°\n°❂°Sider Msg mu :\n\n「 " + str(wait["mention"]) + " 」")

#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     cl.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group1 = ki.findGroupByTicket(ticket_id)
                                     ki.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     ki.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group2 = kk.findGroupByTicket(ticket_id)
                                     kk.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                     kk.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group3 = kc.findGroupByTicket(ticket_id)
                                     kc.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     kc.sendMessage(msg.to, "Masuk : %s" % str(group.name))

    except Exception as error:
        print (error)

while True:
  try:
      Ops = cl.poll.fetchOperations(cl.revision, 50)
      for op in Ops:
        if op.type != 0:
          cl.revision = max(cl.revision, op.revision)
          bot(op)
  except Exception as E:
    E = str(E)
    if "reason=None" in E:
      print (E)
      time.sleep(60)
      restart_program()
      
