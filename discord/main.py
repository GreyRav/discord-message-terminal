import requests

#url du bot discord

webhook_url = 'https://discord.com/api/webhooks/1069029677160747068/OI-Yer5WEPldbNqcMU47Lv9hBfkD1hN76i3o472syULd3t0Zqq_H71VBZg70D9AcPMCt'

#composition des messages

message1 = {'content': 'Tu est vraiment pas doué !'}
message2 = {'content': 'message 2'}
message3 = {'content' : 'message 3 wouhou'}

#entrée utilisateur 

choix = input("choisi entre les 3 messages : 1, 2, 3\n")

#données differés de l'utilisateur

données_message_1 = ["message 1", "message1", "1"]
données_message_2 = ["message 2", "message2", "2"]
données_message_3 = ["message 3", "message3", "3"]

#réponse aprés entrées utilisateur

if choix in données_message_1:
    message = message1
elif choix in données_message_2:
    message = message2
elif choix in données_message_3:
   message = message3
else:
   print("t'abuse")
i = 1

#envoie 10 fois le message

while i <= 10:
    i = i + 1
    requests.post(webhook_url, json=message)


