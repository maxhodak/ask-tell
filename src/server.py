#!/usr/bin/env python

import socket, random

host = 'maxhodak.com'
port = 11911
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)
messages = []
next_msg = "Nothing here!"
while 1:
  client, address = s.accept()
  data = client.recv(size)
  if data:
    if data == '<ask>':
      client.send(next_msg)
      if len(messages) > 0:
        if len(messages) > 5:
          denom = 5.0
        else:
          denom = float(len(messages)-1)
        ind = int(round(random.expovariate(1.0/denom),0))
        ind = len(messages)-ind
        if ind > len(messages)-1:
          ind = len(messages)-1
        next_msg = messages[ind]
    else:
      messages.append(data)
      client.send("true")
  client.close()