import crypt

def crackpass(crypted_pass):
   flag = 0
   file = open('pass.txt','r')
   if crypted_pass == None:
      print('You didn\'t give the password')
      return
   salt = crypted_pass[0:2]
   for dic in file.readlines():
       word = dic.strip()
       cryptWord = crypt.crypt(word,salt = salt)
       if cryptWord == crypted_pass:
           print(f'[+] Password Found: {word}\nHash: {cryptWord}')
           flag+=10
           break
   if flag == 0:
        print('[-] Password Not Found:',crypted_pass)


mode = input('1. pre hashed passwords or\n2. letter based passwords\n(1/2) ')
while True:
   try:
     if "2" in mode:
        s = input('Password: ')
        slt = input('Salt: ')
        crypted = crypt.crypt(s,salt = slt)
     elif "1" in mode:
        crypted = input("Hashed password: ")
     else:
       break
     crackpass(crypted)
   except (KeyboardInterrupt, EOFError):
     break
