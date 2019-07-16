#! /usr/bin/python3
import smtplib, ssl, secrets, urllib.request

port = 465
password = secrets.password

context = ssl.create_default_context()

sender_email = "mailtestbart@gmail.com"
receiver_email = "joep_is_cool@hotmail.com"

external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

path = 'ip.txt'
ip_file_r = open(path, 'r')
ip_check = ip_file_r.read()

ip_file_r.close()

message = """\
Subject: IP

Extern IP adres is: %s""" % external_ip

if external_ip != ip_check:

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("mailtestbart@gmail.com", password)
        server.sendmail(sender_email, receiver_email, message)

    ip_file_w = open(path, 'w')
    ip_file_w.write(external_ip)
    ip_file_w.close()