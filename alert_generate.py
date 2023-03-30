import os
import smtplib
from email.message import EmailMessage

def email_content(species):
    total_species = len(species)
    content = ""
    count = 1
    content += f"There are {total_species} dangerous aquatic species near your location. \n"

    os.chdir("Description")
    for i in species:
        content += f"{count}. {i}\n"
        file = open(f"{i}.txt")
        for j in file.readlines():
            content+=j
        file.close()
        content += "\n"
        count+=1
    content += "\n Images of the alerted species are attached with the mail for easier recognition."
    content += "\n https://drive.google.com/drive/folders/1vCw5zpHSFuU7r4TCZNtv47XpiG3-O7H1?usp=share_link"
    return content

def mail(receiver, species):
    e_add= 'mailtest0597@gmail.com'#senders email id
    e_pass = "dgnvvokxjohlebsr" #your gmail password

    msg=EmailMessage()
    msg["Subject"] = f"Aqualert Warning: {len(species)} dangerous aquatic species near you."#Enter the subject
    msg["From"]=e_add
    msg["To"]=receiver
    msg.set_content(email_content(species))#insert an f string here containing the warning
    with smtplib.SMTP_SSL("smtp.gmail.com",465) as s:
        s.login(e_add,e_pass)
        s.send_message(msg)