from socket import *
import struct

sockfd = socket(AF_INET,SOCK_DGRAM)

DRAM = ("127.0.0.1",8000)
st = struct.Struct("i32sif")


while True:
    print("=================================")

    id = int(input("ID:"))
    name = input("请输入姓名：").encode()
    age = int(input("请输入年龄："))
    score = float(input("请输入成绩："))

    data = st.pack(id,name,age,score)

    sockfd.sendto(data,DRAM)

sockfd.close()




