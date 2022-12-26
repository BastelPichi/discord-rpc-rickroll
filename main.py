import time
from pypresence import Presence

client_id = "975411248105676901"
RPC = Presence(client_id)
RPC.connect()


i = 0
print("Ready. Closing this Window will kill your Status, so leave it open ;)")
while True:
    i += 1
    RPC.update(details="haha, I rickrolled you ;)", large_image=str(i), buttons=[{"label": "More Rickroll", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}, {"label": "Download this", "url": "https://rpcrickroll.aj.do/"}])
    if i > 8:
        i = 0
    time.sleep(1)
