import random
from datetime import datetime
age = []
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "black", "white", "gray", "turquoise", "chartreuse", "lime", "darker grey", "really dark grey", "cyan", "magenta"]
tim_fav_color = random.choice(colors)
result = 0
def responses(name):
# VARIABLES --------------------------------------------------------------
    player_input = input(f"{name}: ").lower()
    current_time = datetime.now().strftime("%I:%M %p")
    split_input = player_input.split()
    past_input = ""
    global age
    global result
    name_lower = name.lower()
    has_number = any(char.isdigit() for char in player_input)
# VOICE LINES -------------------------------------------------------------
    hello_response_list = ["Hello, I'm timmy", "Hi", "I'm timmy, do you need anything", "Hello", "Back in my day we didn't have chat bots", "HI"]
    weather_words = ["Its a bit cloudy out", "It seems to be storming right now, at least where I live", "How do you expect me to know the weather where you live"]
    hello_words = ["hi", "hello", "sup", "what's up"]
    call_name_responses = ["Yeah?", "?", "What do you want now", "WHAT DO YOU WANT FROM ME", "What", "Yeah", "Sup", "Present", "At your service", "Uh huh", "Yes", "yeah", "yes", "Huh", "Wat", "Hi"]
    timmy_name_responses = ["Call me Big Tim from now on", "I'm timmy", "My name is timmy", "They call me the timinator in these parts", "My name, seriously it's literally right\n  ⬆︎  there"]
    game_list1 = ["I play", "I like to play", "I love playing", "I have 1241 hours playing", ]
    game_list2 = ["CS2", "with my toes", "Terraria", "Cult of the Lamb", "Helldivers II", "in the mud", "Fortnite", "Minecraft"]
    youre_welcome_list = ["No problem just doing my job", "No problemo", "Your welcome", "Of course","The thanks is yours"]
    age_list = ["Why are you trying to talk to a child", "I'd prefer not to say my age to a stranger", "I'm 0 years old", "Why do you want to know"]
    feeling_list = ["I'm doing great how about you", "I'm doing horrible, you keep on asking me question after question just like google it I don't even know that much why do you torture me", "I am a chatbot I don't have feelings", "I feel fine", "I'm okay", "I feel tired"]
    gender_responses = ["I identify as he/him", "That is so rude, I take offense", "What does gender mean"]
    or_question_list = ["If I had to I'd choose", "I guess I'd choose", "If you're really making me, I guess I'd choose", "Easy,", "I'd choose"]
    credits_responses = ["I was created by Emerson", "I was made with the power of friendship", "I was made in China", "Code: Emerson, Voicelines: Emerson, Cool awesome amazing dude: Emerson(not biased)", "Made with love and care", "I was made by Emerson Sher"]
    idk_words = ["Sorry I didn't catch that", "Huh?", "wat those words", "Me no understand", "射么？", "?", "我不知道", "I don't understand", "I haven't learned those words yet", "Idk google it urself", "Go here: google.com", f"{player_input}?", f"{player_input}, wdym"]
    your_name_responses = ["Seriously, how do you not know your own name did you hit your head too hard", f"Your name is {name}" ]
    mean_responses = ["That's not very kind", "F### you", "I hate you too", "Think of better insults", f"{player_input}, really, those words don't even move me 1 milimeter"]
    math_easy_responses = [f"Easy {result}", f"Too easy, it's {result}", f"Erm actually if you don't know this you are actually intellectually lacking, but if you really need the answer, the answer is {result}", f"It's {result}", f"Simple, {result}", f"{result}"] 
    math_medium_responses = [f"The answer would be {result}", f"This one is a bit difficult, well atleast for you, anyways the answer is {result}", f"Umm... hmm.. it's {result + random.randint(-5, 5)}" , f"Okay, it's... {result}"]
    math_hard_responses = [f"You gave me a tricky one, but thats not going to stop me, The answer is {result}", f"According to my calculations it's {result}", f"This one is quite simple, you need to dome simple maths and you get {result}", f"Umm... Hmm... this one is quite tricky, hmm... uh I think the answer is {result+ random.randint(-100, 100)}", f"Too Easy, it's {result}", "idk just use a calculator atp"]


# Random Voiceline Variables
    your_name_response = random.choice(your_name_responses)
    mean_response = random.choice(mean_responses)
    idk_response = random.choice(idk_words)
    credits_response = random.choice(credits_responses)
    or_question_response = random.choice(or_question_list)
    gender_response = random.choice(gender_responses)
    age_response = random.choice(age_list)
    call_name_response = random.choice(call_name_responses)
    feeling_response = random.choice(feeling_list)
    youre_welcome_response = random.choice(youre_welcome_list)
    game_list1_response = random.choice(game_list1)
    game_list2_response = random.choice(game_list2)
    hello_response = random.choice(hello_response_list)
    weather_response = random.choice(weather_words)
    timmy_name_response = random.choice(timmy_name_responses)
    math_easy_response = random.choice(math_easy_responses)
    math_medium_response = random.choice(math_medium_responses)
    math_hard_response = random.choice(math_hard_responses)

# ALL OF THE CODE ----------------------------------------------
    for i in hello_words:
        if i in player_input:
            print(f"\nTimmy: {hello_response}\n")
            break
        else:  
            if " or " in player_input:
                or_position = split_input.index("or")
                random_integer = random.randint(1, 2)
                if random_integer == 2:
                    if split_input[or_position-1] == "me":
                        print(f"\nTimmy: {or_question_response} you\n")
                    elif split_input[or_position-1] == "you":
                        print(f"\nTimmy: {or_question_response} me\n")
                    else:
                        print(f"\nTimmy: {or_question_response} {split_input[or_position-1]}\n")
                else:
                    if split_input[or_position+1] == "me":
                        print(f"\nTimmy: {or_question_response} you\n")
                    elif split_input[or_position+1] == "you":
                        print(f"\nTimmy: {or_question_response} me\n")
                    else:
                        print(f"\nTimmy: {or_question_response} {split_input[or_position+1]}\n")
            
            elif " * " in player_input and has_number == True or " • " in player_input and has_number == True :
                math_input = player_input.split()
                if "*" in player_input:
                    times_pos = math_input.index("*")
                elif "•" in player_input:
                    times_pos = math_input.index("•")
                result = (float(math_input[times_pos-1]) * float(math_input[times_pos+1]))
                math_easy_responses = [f"Easy {result}", f"Too easy, it's {result}", f"Erm actually if you don't know this you are actually intellectually lacking, but if you really need the answer, the answer is {result}", f"It's {result}", f"Simple, {result}", f"{result}"] 
                math_medium_responses = [f"The answer would be {result}", f"This one is a bit difficult, well atleast for you, anyways the answer is {result}", f"Umm... hmm.. it's {result + random.randint(-5, 5)}" , f"Okay, it's... {result}"]
                math_hard_responses = [f"You gave me a tricky one, but thats not going to stop me, The answer is {result}", f"According to my calculations it's {result}", f"This one is quite simple, you need to dome simple maths and you get {result}", f"Umm... Hmm... this one is quite tricky, hmm... uh I think the answer is {result+ random.randint(-100, 100)}", f"Too Easy, it's {result}", "idk just use a calculator atp"]
                math_easy_response = random.choice(math_easy_responses)
                math_medium_response = random.choice(math_medium_responses)
                math_hard_response = random.choice(math_hard_responses)
                if result < 100 or result > -100:
                    print(f"\nTimmy: {math_easy_response}\n")
                elif result < 1000 and result > 100 or result > -1000 and result < -100:
                    print(f"\nTimmy: {math_medium_response}\n")
                elif result > 1000 or result < -1000:
                    print(f"\nTimmy: {math_hard_response}\n")           
            elif "*" in player_input or "•" in player_input:
                print(f"\nTimmy: Sorry, I can't understand math when do don't put spacing between stuff\n")
            elif " / " in player_input and has_number == True or " ÷ " in player_input and has_number == True :
                math_input = player_input.split()
                if "/" in player_input:
                    divide_pos = math_input.index("/")
                elif "÷" in player_input:
                    divide_pos = math_input.index("÷")
                result = (float(math_input[divide_pos-1]) / float(math_input[divide_pos+1]))
                math_easy_responses = [f"Easy {result}", f"Too easy, it's {result}", f"Erm actually if you don't know this you are actually intellectually lacking, but if you really need the answer, the answer is {result}", f"It's {result}", f"Simple, {result}", f"{result}"] 
                math_medium_responses = [f"The answer would be {result}", f"This one is a bit difficult, well atleast for you, anyways the answer is {result}", f"Umm... hmm.. it's {result + random.randint(-5, 5)}" , f"Okay, it's... {result}"]
                math_hard_responses = [f"You gave me a tricky one, but thats not going to stop me, The answer is {result}", f"According to my calculations it's {result}", f"This one is quite simple, you need to dome simple maths and you get {result}", f"Umm... Hmm... this one is quite tricky, hmm... uh I think the answer is {result+ random.randint(-100, 100)}", f"Too Easy, it's {result}", "idk just use a calculator atp"]
                math_easy_response = random.choice(math_easy_responses)
                math_medium_response = random.choice(math_medium_responses)
                math_hard_response = random.choice(math_hard_responses)
                if result < 100 or result > -100:
                    print(f"\nTimmy: {math_easy_response}\n")
                elif result < 1000 and result > 100 or result > -1000 and result < -100:
                    print(f"\nTimmy: {math_medium_response}\n")
                elif result > 1000 or result < -1000:
                    print(f"\nTimmy: {math_hard_response}\n")   
            elif "/" in player_input or "÷" in player_input:
                print(f"\nTimmy: Sorry, I can't understand math when do don't put spacing between stuff\n")
            elif " + " in player_input and has_number == True :
                math_input = player_input.split()
                plus_pos = math_input.index("+")
            
                result = (float(math_input[plus_pos-1]) + float(math_input[plus_pos+1]))
                math_easy_responses = [f"Easy {result}", f"Too easy, it's {result}", f"Erm actually if you don't know this you are actually intellectually lacking, but if you really need the answer, the answer is {result}", f"It's {result}", f"Simple, {result}", f"{result}"] 
                math_medium_responses = [f"The answer would be {result}", f"This one is a bit difficult, well atleast for you, anyways the answer is {result}", f"Umm... hmm.. it's {result + random.randint(-5, 5)}" , f"Okay, it's... {result}"]
                math_hard_responses = [f"You gave me a tricky one, but thats not going to stop me, The answer is {result}", f"According to my calculations it's {result}", f"This one is quite simple, you need to dome simple maths and you get {result}", f"Umm... Hmm... this one is quite tricky, hmm... uh I think the answer is {result+ random.randint(-100, 100)}", f"Too Easy, it's {result}", "idk just use a calculator atp"]
                math_easy_response = random.choice(math_easy_responses)
                math_medium_response = random.choice(math_medium_responses)
                math_hard_response = random.choice(math_hard_responses)
                if result < 100 or result > -100:
                    print(f"\nTimmy: {math_easy_response}\n")
                elif result < 1000 and result > 100 or result > -1000 and result < -100:
                    print(f"\nTimmy: {math_medium_response}\n")
                elif result > 1000 or result < -1000:
                    print(f"\nTimmy: {math_hard_response}\n")
            elif "+" in player_input:
                print(f"\nTimmy: Sorry, I can't understand math when do don't put spacing between stuff\n")          
            elif " - " in player_input and has_number == True :
                math_input = player_input.split()
                minus_pos = math_input.index("-")
                result = 0
                result = (float(math_input[minus_pos-1]) - float(math_input[minus_pos+1]))
                math_easy_responses = [f"Easy {result}", f"Too easy, it's {result}", f"Erm actually if you don't know this you are actually intellectually lacking, but if you really need the answer, the answer is {result}", f"It's {result}", f"Simple, {result}", f"{result}"] 
                math_medium_responses = [f"The answer would be {result}", f"This one is a bit difficult, well atleast for you, anyways the answer is {result}", f"Umm... hmm.. it's {result + random.randint(-5, 5)}" , f"Okay, it's... {result}"]
                math_hard_responses = [f"You gave me a tricky one, but thats not going to stop me, The answer is {result}", f"According to my calculations it's {result}", f"This one is quite simple, you need to dome simple maths and you get {result}", f"Umm... Hmm... this one is quite tricky, hmm... uh I think the answer is {result+ random.randint(-100, 100)}", f"Too Easy, it's {result}", "idk just use a calculator atp"]
                math_easy_response = random.choice(math_easy_responses)
                math_medium_response = random.choice(math_medium_responses)
                math_hard_response = random.choice(math_hard_responses)
                if result < 100 or result > -100:
                    print(f"\nTimmy: {math_easy_response}\n")
                elif result < 1000 and result > 100 or result > -1000 and result < -100:
                    print(f"\nTimmy: {math_medium_response}\n")
                elif result > 1000 or result < -1000:
                    print(f"\nTimmy: {math_hard_response}\n")
            elif "-" in player_input:
                print(f"\nTimmy: Sorry, I can't understand math when do don't put spacing between stuff\n")            

            elif "timmy" in player_input or "hey" in player_input:
                print(f"\nTimmy: {call_name_response}\n")

            elif "name" in player_input and "my" in player_input and "what" in player_input:
                print(f"\nTimmy: {your_name_response}\n")

            elif "time" in player_input and "what" in player_input:
                print(f"\nTimmy: It's aproximatly {current_time}\n")

            elif "what" in player_input and "weather" in player_input or "how" in player_input and "weather" in player_input:
                print(f"\nTimmy: {weather_response}\n")

            elif "name" in player_input and "your" in player_input and "what" in player_input or "name" in player_input and "ur" in player_input and "what" in player_input:
                print(f"\nTimmy: {timmy_name_response}\n")

            elif "game" in player_input and "what" in player_input and "you" in player_input and "play" in player_input or "game" in player_input and "what" in player_input and "you" in player_input and "like" in player_input:
                print(f"\nTimmy: {game_list1_response} {game_list2_response}\n")
            
            elif "name" in player_input and "my" in player_input and name_lower not in player_input and "is" in player_input:
                print(f"\nTimmy: That's not your name, your name is {name}\n")

            elif "how" in player_input and "egg" in player_input and "to" in player_input:
                print(f"\nTimmy: First you have to crack a egg on the pan then you have to turn up the heat and then you have to wait for the egg to release itself from the pan then you must either flip the egg or take it off the pan and your done -timmycooks.com \n")

            elif "thank" in player_input and "you" in player_input or "thank" in player_input:
                print(f"\nTimmy: {youre_welcome_response}\n")

            elif "what" in player_input and "gender" in player_input or "identify" in player_input and "you" in player_input:
                print(f"\nTimmy: {gender_response}\n")

            elif "where" in player_input and "live" in player_input and "you" in player_input:
                print(f"\nTimmy: My mom told me not to tell strangers where I live but I don't think of you as a strager so I live on 1532 Timmyland ave California\n")

            elif "you" in player_input and "suck" in player_input or "i" in player_input and "hate" in player_input and "you" in player_input or "i" in player_input and "die" in player_input and "hope" in player_input or "f " in player_input and " you" in player_input or "screw" in player_input and "you" in player_input:
                print(f"\nTimmy: {mean_response}\n")

            elif "what" in player_input and "age" in player_input and "you" in player_input or "how" in player_input and "old" in player_input and "you" in player_input:
                print(f"\nTimmy: {age_response}\n")

            elif "how" in player_input and "are" in player_input and "you" in player_input or "are" in player_input and "you" in player_input and "okay" in player_input or "how" in player_input and "you" in player_input and "feel" in player_input:
                print(f"\nTimmy: {feeling_response}\n")
            
            elif player_input == "help":
                print("\nTimmy: Some things to try:\n\n1. Say: Hi, Hello.\n\n2. Ask: Whats the time\n\n3. Ask: Whats the weather\n\n4. Ask: What's my name\n\n5. Say: Hey timmy, timmy\n\n6. Restart and name yourself timmy or Timmy\n\n7. Ask: Whats your name\n\n8. Ask: How old are you\n\n10. Ask: Whats your gender\n\n11. Ask: How are you, are you okay, how do you feel\n\n12. Ask: How to cook a egg\n\n13. Ask any or questions, ex: timmy whats better oled or lcd\n\n14. Say your name is something that isn't your name, ex: Emerson: My name is bob\n\n15. Say your age\n\n16 Ask: Whats my name\n\n17. Say: Credits, Who made you, Who created you", "Say: knock knock")

            elif "old" in player_input and "i" in player_input and "am" in player_input and has_number == True or "i" in player_input and "am" in player_input and has_number == True:
                print(f"\nTimmy: Nice I'm 0 years old\n")
                age = [int(item) for item in split_input if item.isdigit()]

            elif "knock knock" in player_input:
                print("\nTimmy: Who's there\n")

            elif "you" in player_input and "are" in player_input and "cool" in player_input or "you" in player_input and "are" in player_input and "nice" in player_input or "you" in player_input and "are" in player_input and "funny" in player_input:
                print(f"\nTimmy: Why thanks\n")
            
            elif "how" in player_input and "old" in player_input and "i" in player_input and has_number == False or "what" in player_input and "my" in player_input and "age" in player_input and has_number == False:
                
                print(f"\nTimmy: You are {age[0]} years old\n")

            elif "credit" in player_input or "created" in player_input and "you" in player_input or "made" in player_input and "you" in player_input:
                print(f"\nTimmy: {credits_response}\n")

            elif "favorite" in player_input and "what" in player_input and "color" in player_input and "your" in player_input:
                print(f"\nTimmy: My favorite color is {tim_fav_color}\n")
            
            elif name_lower in player_input:
                print(f"\nTimmy: That's you\n")

            elif "you" in player_input and "are" in player_input:
                print(f"\nTimmy: Don't say that about me\n")

            elif "repeat" in player_input:
                print(f"\nTimmy: {past_input}\n")

            elif "what" in player_input:
                print(f"\nTimmy: {idk_response}\n")
            else:
                print(f"")
            break

def main():
    # Starting Voice Things ----------------------
    name_questions = ["What's your name?", "What was your name again?", "What should I call you by?", "Huh, who are you", "Who are you, and what are you doing in my swamp"]
    name_question = random.choice(name_questions)
    name = input(f"\nTimmy: {name_question}\n\nName: ")
    timmy_name_responses = [f"{name}, I really like your name, anyone with that name is super hansome and charizmatic", f"{name}, that name sounds familiar", "That's a really awesome amazing great name", "You copycat thats my name not yours, I won't let you taint my name"]
    timmy_name_response = random.choice(timmy_name_responses)
    name_response_list1 = [f"Hello {name} I'm timmy", f"Hi {name}", f"Ah {name} was it, I think I've heard that name before", f"Hey {name} I'm Timmy", f"Whats up {name}", f"Sup {name}", f"Nice to meet you {name}", f"It's a pleasure to meet you {name}", f"Well well well, {name} we meet again"]
    name_response1 = random.choice(name_response_list1)
    emerson_name_responses = [f"Don't even think it't funny to use my creators name, to make sure it's you type in the correct password", f"That's a amazing name, anyone with that name is super awesome, cool, funny, charming name(I was definetly not programed to say thay), \nwait you could be lying, type password to confirm it's you"]
    emerson_name_response = random.choice(emerson_name_responses)
    password = "1234"
    if name.lower() == "timmy":
        if timmy_name_response == "You copycat thats my name not yours, I won't let you taint my name":
            print(f"\nTimmy: {timmy_name_response}\n")
            name = "[]"
            print(f"Timmy: Ha, how do you like it now, no name\n")
        else:
            print(f"\nTimmy: {timmy_name_response}\n")
    elif name.lower() == "mybutt":
        print(f"\nTimmy: Haha your so funny\n")

    elif name.lower() == "emerson":
        print(f"\nTimmy: {emerson_name_response}\n")
        password_input = input("Password: ")
        if password_input == password:
            print(f"\nPassword Accepted, Hello Emerson\n")
        else:
            print(f"\nPassword DENIED, Changing name\n")
            name = "[]"

    else: 
        print(f"\nTimmy: {name_response1}\n")
    while True:
        responses(name)


if __name__ == "__main__":
    main()