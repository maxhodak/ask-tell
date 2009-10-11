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
logfile = open('/tmp/asktell.log','a+')
while 1:
  client, address = s.accept()
  data = client.recv(size)
  if data:
    if len(data) > 300:
      logfile.write("Rejected due to length\n")
      logfile.flush()
      client.send("false")
    else:
      if data == '<ask>':
        client.send(next_msg)
        if len(messages) > 0:
          if len(messages) > 5:
            denom = 5.0
          else:
            if float(len(messages)-1) < 1e-2:
              denom = 1.0
            else:
              denom = float(len(messages)-1)
          ind = int(round(random.expovariate(1.0/denom),0))
          ind = len(messages)-ind
          if ind > len(messages)-1 or ind < 0:
            ind = len(messages)-1
          next_msg = messages[ind]
      else:
        logfile.write(data+"\n")
        logfile.flush()
        messages.append(data)
        client.send("true")
  client.close()