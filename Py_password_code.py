import pyperclip

passwords = {
    
    "Facebook": "p@ssw0rd123",
    "Twitter": "Tw!tt3rP@ss",
    "Instagram": "gamer@1546",
    "Snapchat": "Sn@pch@t789",
    "LinkedIn": "L!nkedInP@ss",
    "TikTok": "T!kT0kS3cur3",
    "WhatsApp": "Wh@ts@pp2021",
    "Reddit": "R3dd!tP@ss",
    "Pinterest": "P!nterest123",
    "YouTube": "gamer@1546"
}

master_password = input("Enter Master Password to Access Locker: ")

def passdisplay():
    

    acc = input("Do you want to Access Locekr?  ")
    if acc.lower() == "yes":
        print("Access Granted!")
        for k, v in passwords.items():
            print(k, ":", v)
        passcopy = input("Which Password you want to copy, Enter its Name: ")
        if passcopy == "Facebook":
            pyperclip.copy(passwords["Facebook"])
        if passcopy == "Twitter":
            pyperclip.copy(passwords["Twitter"])
        if passcopy == "Instagram":
            pyperclip.copy(passwords["Instagram"])
        if passcopy == "Snapchat":
            pyperclip.copy(passwords["Snapchat"])
        if passcopy == "LinkedIn":
            pyperclip.copy(passwords["LinkedIn"])
        if passcopy == "TikTok":
            pyperclip.copy(passwords["TikTok"])
        if passcopy == "WhatsApp":
            pyperclip.copy(passwords["WhatsApp"])
        if passcopy == "Reddit":
            pyperclip.copy(passwords["Reddit"])
        if passcopy == "Pinterest":
            pyperclip.copy(passwords["Pinterest"])
        if passcopy == "YouTube":
            pyperclip.copy(passwords["YouTube"])
        print("Copied, Thank you!")
    else:
        print("No Worries, Thankyou!")

def masterpass(key):
    if key == "gamer@1546":
        passdisplay()
    else:
        print("Wrong Password!! Try Again")

masterpass(master_password)