# string concatenation (how to put string together)
# suppose we want to a create a string that says "Subscribe to _____"
# youtuber = "Shehab Sarker" 
# # some string variable

# # few ways to do this
# print("Subscribe to "+youtuber)
# print("Subscribe to {}".format(youtuber))
# print(f"Subscribe to {youtuber}")

adj=input("Adjective: ")
verb1=input("Verb1 : ")
verb2=input("Verb2 : ")
famous_person=input("Famous Person: ")
madlib=f"Computer progamming is so {adj}. It makes me so excited all the time because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}."

print(madlib)