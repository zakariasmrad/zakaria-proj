guess=["lion","rabbit","monkey","crocodile","apple","pineapple","banana","watermelon","car","book","phone","bottle","carrot","onion","lettuce","tomato"]
import random
hidden=(random.choice(guess))
print("==>You have those hints to guess the hidden TREASURE chosen by the computer: ")
hlen=len(hidden)
if hidden==guess[0]:
  print("-->It is an animal")
  print("-->It lives in africa")
elif hidden==guess[1]:
  print("-->It is an animal")
  print("-->It lives in europe")
elif hidden==guess[2]:
  print("-->It is an animal")
  print("-->It lives in asia")
elif hidden==guess[3]:
  print("-->It is an animal")
  print("-->It lives in australia")  
elif hidden==guess[4] or hidden==guess[5] or hidden==guess[6] or hidden==guess[7]:
  print("-->It is a friut ")
elif hidden==guess[8] or hidden==guess[9] or hidden==guess[10] or hidden==guess[11]:
  print("-->It is a thing")
elif hidden==guess[12] or hidden==guess[13] or hidden==guess[14] or hidden==guess[-1]:
  print("-->It is a vegetable")
print("-->It starts with the letter: "+hidden[0:1])  
print("-->It contains: ",hlen,"letters")
i=0
xi=hidden[i:i+1]
vow=0
con=0
while i<hlen:
  xi=hidden[i:i+1]
  if xi=="a" or xi=="o" or xi=="e" or xi=="u" or xi=="i":
    vow=vow+1
    i+=1
  else:
    con=con+1
    i+=1
print("-->There are ",vow,"vowels in the hidden TREASURE")  
uguess=input("==>Now you have 3 attempts to guess this hidden TREASURE: ").lower()
j=3
while j!=0:
  if uguess!=hidden:
    print("Whoops that is wrong")
    j-=1
    print("Your current score is: ",j)
    if j==0:
     print("The hidden choice is: "+hidden)
     break
    uguess=input("Enter your guess")
  else:
    print("OOOh how smart you are!")
    break