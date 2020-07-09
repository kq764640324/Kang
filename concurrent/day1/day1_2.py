from socket import *

f = socket()
f.bind(("0.0.0.0",8000))
f.listen(5)

c,addr = f.accept()
print("Connect from",addr)

data = c.recv(4096)
print(data)

data = """HTTP/1.1 200 OK
Content-Type:text/html
<h1>hello world<h1>
"""

c.send(data.encode())


c.close()
f.close()

