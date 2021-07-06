# -*- coding:utf8 -*- 
import socket

HOST = "irc.twitch.tv"
PORT = 6667
NICK = "TODO"
PASS = "TODO"

def send_message(message):
    sock.send(bytes("PRIVMSG #" + NICK + " :" + message + "\r\n", "UTF-8"))

sock = socket.socket()
sock.connect((HOST,PORT))

sock.send(bytes("PASS " + PASS + "\r\n", "UTF-8"))
sock.send(bytes("NICK " + NICK + "\r\n", "UTF-8"))
sock.send(bytes("JOIN #" + NICK + " \r\n", "UTF-8"))

while True:
    line = str(sock.recv(1024))
    
    if "End of /NAMES list" in line:
        break

print("Running...")

while True:
    for line in str(sock.recv(1024)).split('\\r\\n'):

        if "PING" in line:
            sock.send(bytes("PONG :tmi.twitch.tv\r\n","UTF-8"))
            sock.send(bytes("PING :tmi.twitch.tv\r\n","UTF-8"))
        
        parts = line.split(':')
        if len(parts) < 3:
            continue

        if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
            message = parts[2][:len(parts[2])]

        usernamesplit = parts[1].split("!")
        username = usernamesplit[0]

        print("Recv -> " + username + " : " + message)
        if message == "Hey":
            send_message("Hello " + username)
            print("Send -> " + "Hello " + username)
            
        if message == "!lights_on":
            send_message("Turning ON lights...")
            print("Send -> " + "Turning ON lights...")
            
        if message == "!lights_off":
            send_message("Turning OFF lights...")
            print("Send -> " + "Turning OFF lights...")
