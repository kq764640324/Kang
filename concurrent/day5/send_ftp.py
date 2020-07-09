"""
ftp文件服务器
并发网络功能训练
"""

from socket import *
from threading import Thread

# 全局变量
HOST = "0.0.0.0"
PORT = 8008
ADDR = (HOST,PORT)
FTP = "F:\PY\fullstack\FTP"

f = socket()
f.bind(("0.0.0.0",8008))
f.listen(3)
# 将客户请求功能封装为类
class FtpServer:
    pass

def handle(connfd):
    print(connfd.recv())
# 网络搭建
def main():
    sockfd = socket()

    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(ADDR)
    sockfd.listen(5)
    print("Listen the port 8080...")
    while True:
        try:
            connfd,addr = sockfd.accept()
        except KeyboardInterrupt:
            print("退出服务程序")
            return
        except Exception as e:
            print(e)
            continue
        print("链接客户端：",addr)

        # client = Thread(target = handle,args(connfd,))
        client.setDaemon(True)
        client.start()