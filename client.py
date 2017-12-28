# Echo client program
import socket
import json

HOST = 'localhost'
PORT = 3000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

dj = json.dumps({
    "stage": "run",
    "mime": "text/x-c++src",
    "filename": "a.cpp",
    "stdin": "asdf",
    "source": "#include <iostream>\nusing namespace std;\n\nint main() {\n\tcout<<\"Hello\";\n\treturn 0;\n}"
})
s.sendall(dj)
data = s.recv(1024)
s.close()
print 'Received', repr(data)
