"""
IO多路复用 select 实现多客户端通信

"""
from socket import *
from select import select

s= select()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind("0.0.0.0",8080)
s.listen(5)

rlist = [s]
wlist = []
xlist = []

while True:
    rs,ws,xs = select(rlist,wlist,xlist)

    for r in rs:
        if r is s:
            c,addr = r.accept()
            print("Connect from",addr)
            rlist.append(c)
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data.decode())
            wlist.append(r)

    for w in ws:
        w.send(b"OK,Thanks")
        wlist.remove(w)

    for x in xs:
        pass