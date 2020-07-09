"""
聊天室练习服务端
"""
from socket import *
import os,sys
ADDR = ("127.0.0.1",8800)

# 储存姓名
user = {}

def do_login(sockfd,name,addr):
    if name in user:
        sockfd.sendto("该用户已经存在".encode(),addr)
        return
    sockfd.sendto(b"OK",addr)
    msg = "欢迎%s进入聊天室"%name
    for i in user:
        sockfd.sendto(msg.encode(),user[i])
    # 将用户添加
    user[name] = addr

def do_request(sockfd):
    while True:
        data,addr = sockfd.recvfrom(1024)
        msg = data.decode().split(" ")
        # 区分请求类型
        if msg[0] == "L":
            do_login(sockfd,msg[1],addr)


def main():
    # 套接字
    sockfd = socket(AF_INET,SOCK_DGRAM)
    sockfd.bind(ADDR)
    do_request(sockfd)

if __name__ == "__main__":
    main()