import time, sys, os, webbrowser


delay = 3

def main():
  name = input('Name -> ')
  age = input('Age -> ')
  reason = input('Reason -> ')
  email = input('Enter email -> ')
  ip = input('Enter Ip -> ')
  addy = input("Enter address -> ")
  relatives = input("Relatives -> ")
  number = input("Enter phone number -> ")
  social = input('Enter social accounts -> ')
  twitter = input('Enter YOUR twitter account -> ')
  discord = input('Enter YOUR discord account -> ')
  with open('doxpaste.dp', 'w') as f:
    f.write(f'''➤ Name: {name}
➤ Age: {age}
➤ Reason: {reason}
————————————————————————

➤                            Emails
➤ {email}
————————————————————————
➤                            Ip 
➤ {ip}
————————————————————————
➤                            Addy

➤ {addy}
————————————————————————
➤                            Additional info
➤ Relatives: {relatives}
➤ Phone number: {number}
➤ Social media: {social}
————————————————————————
➤                            Doxxers info
➤ Twitter: {twitter}
➤ Discord: {discord}
''')

print("Welcome to my Automatic Dox Paster!")

main()
