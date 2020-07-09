"""
聊天室练习客服端
"""
from socket import *
import struct

# 服务器地址
ADDR = ("127.0.0.1",8800)
def send_msg(sockfd,name):
    while True:
        text = input("发言：")
        msg = "C %s %s"%(name,text)
        sockfd.recvfrom(msg,ADDR)

def recv_msg(sockfd,name):
    pass

def main():
    sockfd = socket(AF_INET, SOCK_DGRAM)
    while True:
        name = input("NAME:")
        msg = "L " + name
        sockfd.sendto(msg.encode(),ADDR)
        # 等待回应
        data,addr = sockfd.recvfrom(1024)
        if data.decode() == "OK":
            print("您已经进入聊天室")
            break
        else:
            print(data.decode())

    # 创建新的进程
    pid = os.fork()

    if pid <0:
        sys.exit("Error!")
    elif pid == 0:
        send_msg(sockfd)
    else:
        recv_msg(sockfd,name)


if __name__ == "__main__":
    main()
