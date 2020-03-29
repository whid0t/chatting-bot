import time


#the worlist with the words
wordlist = ("hello", "hi", "greetings", "sup", "what's up",)


print('Hi! This is my first big project. Please if you find any problems let me know here or email me at andreiski@abv.bg. Thank you!')
print('If you want to see the wordlist for this bot type wordlist. More functions are coming soon.')


name = input("\n What's your name? ") 
def say_hello():
	print('Hi %s, nice to meet you!' %name)

def greeting_person():
	if name in wordlist:
		print('Test')

user_input = input("Try asking me or saying something.")
#The time saying section

vreme = time.asctime( time.localtime(time.time()) )
def say_time():
	if user_input == "What time is it":
		print ("Local current time is:", vreme)

     
    


say_hello()
greeting_person()
say_time()
