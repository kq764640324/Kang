from socket import *
import struct

sockfd = socket(AF_INET,SOCK_DGRAM)
sockfd.bind(("127.0.0.1",8000))

st = struct.Struct("i32sif")

f = open("student.txt","a")

while True:
    data,addr = sockfd.recvfrom(1024)

    data = st.unpack(data)

    info = "%d %s %d %.2f\n"%(data[0],data[1].decode(),data[2],data[3])

    f.write(info)
    f.flush()

f.close()
sockfd.close()