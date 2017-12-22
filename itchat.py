import itchat

itchat.auto_login(enableCmdQR=2)

import itchat, time
from itchat.content import *

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    msg.user.send('%s: %s' % (msg.type, msg.text))


itchat.auto_login(enableCmdQR=2)
itchat.run()
