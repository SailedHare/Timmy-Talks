import random
from datetime import datetime
import sys
age = []
def responses(name):
    hello_response_list = ["Hello, I'm timmy", "Hi", "I'm timmy, do you need anything", "Hello", "Back in my day we didn't have chat bots", "HI"]
    weather_words = ["Its a bit cloudy out.", "It seems to be storming right now, at least where I live.", "How do you expect me to know the weather where you live"]
    hello_words = ["hi", "hello", "sup", "what's up"]
    call_name_responses = ["Yeah?", "?", "What do you want now", "WHAT DO YOU WANT FROM ME", "What", "Yeah", "Sup", "Present", "At your service", "Uh huh", "Yes", "yeah", "yes", "Huh", "Wat", "Hi"]
    call_name_response = random.choice(call_name_responses)
    timmy_name_responses = ["Call me Big Tim from now on", "I'm timmy", "My name is timmy", "They call me the timinator in these parts", "My name, seriously it's literally right\n  ⬆︎  there"]
    timmy_name_response = random.choice(timmy_name_responses)
    game_list1 = ["I play", "I like to play", "I love playing", "I have 1241 hours playing", ]
    game_list2 = ["CS2", "with my toes", "Terraria", "Cult of the Lamb", "Helldivers II", "in the mud", "Fortnite", "Minecraft"]
    youre_welcome_list = ["No problem just doing my job", "No problemo", "Your welcome", "Of course","The thanks is yours"]
    age_list = ["Why are you trying to talk to a child", "I'd prefer not to say my age to a stranger", "I'm 0 years old", "Why do you want to know"]
    age_response = random.choice(age_list)
    feeling_list = ["I'm doing great how about you", "I'm doing horrible, you keep on asking me question after question just like google it I don't even know that much why do you torture me", "I am a chatbot I don't have feelings", "I feel fine", "I'm okay", "I feel tired"]
    gender_responses = ["I identify as he/him", "That is so rude, I take offense", "What does gender mean"]
    gender_response = random.choice(gender_responses)
    or_question_list = ["If I had to I'd choose", "I guess I'd choose", "If you're really making me, I guess I'd choose", "Easy,", "I'd choose", ""]
    or_question_response = random.choice(or_question_list)
    credits_responses = ["I was created by Emerson", "I was made with the power of friendship", "I was made in China", "Code: Emerson, Voicelines: Emerson, Cool awesome amazing dude: Emerson(not biased)", "Made with love and care", "I was made by Emerson Sher"]
    credits_response = random.choice(credits_responses)
    feeling_response = random.choice(feeling_list)
    youre_welcome_response = random.choice(youre_welcome_list)
    game_list1_response = random.choice(game_list1)
    game_list2_response = random.choice(game_list2)
    hello_response = random.choice(hello_response_list)
    weather_response = random.choice(weather_words)
    player_input = input(f"{name}: ").lower()
    current_time = datetime.now().strftime("%I:%M %p")
    idk_words = ["Sorry I didn't catch that", "Huh?", "wat those words", "Me no understand", "射么？", "?", "我不知道", "I don't understand", "I haven't learned those words yet", "Idk google it urself", "Go here: google.com"]
    idk_response = random.choice(idk_words)
    split_input = player_input.split()
    global age
    name_lower = name.lower()
    has_number = any(char.isdigit() for char in player_input)
    for i in hello_words:
        if i in player_input:
            print(f"\nTimmy: {hello_response}\n")
            break
        else:  
            if "or" in player_input:
                
                or_position = split_input.index("or")
                random_integer = random.randint(1, 2)
                if random_integer == 2:
                    print(f"\nTimmy: {or_question_response} {split_input[or_position-1]}\n")
                else:
                    print(f"\nTimmy: {or_question_response} {split_input[or_position+1]}\n")
            
            elif "timmy" in player_input or "hey" in player_input:
                print(f"\nTimmy: {call_name_response}\n")

            elif "name" in player_input and "my" in player_input and "what" in player_input:
                print(f"\nTimmy: Your name is {name}... I think.\n")

            elif "time" in player_input and "what" in player_input:
                print(f"\nTimmy: It's aproximatly {current_time}\n")

            elif "what" in player_input and "weather" in player_input or "how" in player_input and "weather" in player_input:
                print(f"\nTimmy: {weather_response}\n")

            elif "name" in player_input and "your" in player_input and "what" in player_input or "name" in player_input and "ur" in player_input and "what" in player_input:
                print(f"\nTimmy: {timmy_name_response}\n")

            elif "game" in player_input and "what" in player_input and "you" in player_input and "play" in player_input or "game" in player_input and "what" in player_input and "you" in player_input and "like" in player_input:
                print(f"\nTimmy: {game_list1_response} {game_list2_response}\n")
            
            elif "name" in player_input and "my" in player_input and name_lower not in player_input:
                print(f"\nTimmy: That's not your name, your name is {name}\n")

            elif "how" in player_input and "egg" in player_input and "to" in player_input:
                print(f"\nTimmy: First you have to crack a egg on the pan then you have to turn up the heat and then you have to wait for the egg to release itself from the pan then you must either flip the egg or take it off the pan and your done -timmycooks.com \n")

            elif "thank" in player_input and "you" in player_input or "thank" in player_input:
                print(f"\nTimmy: {youre_welcome_response}\n")

            elif "what" in player_input and "gender" in player_input or "identify" in player_input and "you" in player_input:
                print(f"\nTimmy: {gender_response}\n")

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
            
            elif "how" in player_input and "old" in player_input and "i" in player_input and has_number == False or "what" in player_input and "my" in player_input and "age" in player_input and has_number == False:
                
                print(f"\nTimmy: You are {age[0]} years old\n")

            elif "credit" in player_input or "created" in player_input and "you" in player_input or "made" in player_input and "you" in player_input:
                print(f"\nTimmy: {credits_response}\n")
            
            elif name_lower in player_input:
                print(f"\nTimmy: That's you\n")
            else:
                print(f"\nTimmy: {idk_response}\n")
            break
    
name_response_list1 = ["Hello", "Hi", "Ah", "Hey", "Whats up", "Sup", "Nice to meet you", "It's a pleasure to meet you"]
name_response_list2 = ["I'm timmy", "I'm dad", "thats your name I was right about to say it", "my name is timmy", "I KNOW WHAT YOU DID", "me is timmy", "me timmy"]
name_response1 = random.choice(name_response_list1)
name_response2 = random.choice(name_response_list2)
name_questions = ["What's your name?", "What was your name again?", "Hi my name is timmy whats yours?", "Huh, who are you", "Who the f@!# are you amd what are you doing in my lawn", "Who are you and what are you doing in my swamp"]
name_question = random.choice(name_questions)
name = input(f"\nTimmy: {name_question}\n\nName: ")
if name == "timmy" or name == "Timmy":
    print(f"\nTimmy: That's a really awesome amazing great name\n")
elif name == "Mybutt" or name == "mybutt" or name == "myButt" or name == "MyButt":
    print(f"\nTimmy: Haha your so funny and original\n")
else: 
    print(f"\nTimmy: {name_response1} {name} {name_response2}\n")
while True:
    responses(name)


