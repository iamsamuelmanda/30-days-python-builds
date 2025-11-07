import time

print("Welcome Passenger No 8")
name = input('What is your name, traveller? ')
choice = input(f'Welcome, {name}. Would you like to read the poem or skip the flight? ').lower()

if choice == 'read':
    print("I want to interest you with my new poem entitled Passenger")
    time.sleep(2)
    print('It reads')
    time.sleep(2)
    print('Am I a passenger like any other? In this seat I am just another Passenger floating through life like a stranger')
    time.sleep(3)
    print('As I stare through this small mirror I cannot help but imagine how beautiful this view is from the balcony of my subconscious')
    time.sleep(3)
    print('Oh, I am curious')
    time.sleep(2)
    print('If I said I was the pilot would you believe me? Since I am just another Passenger seated next to you?')
    time.sleep(3)
    print('I see the look in your eyes, you are so drawn to me but I cannot help it but ask')
    time.sleep(2)
    print('Do you recognize that I am never here but on another plane because of my mental platitude, which you just assume is just my attitude?')
    time.sleep(3)
    print('I cannot resist the urge but I should mention this is not another episode since the last diagnosis I took of myself')
    time.sleep(3)
    print('There is something about me which I also try to understand but I cannot since I am unable to tell the space or the color in my childhood')
    time.sleep(3)
    print('I see you are fatigued and tired, do you even want to listen?')
    time.sleep(2)
    print('Don\'t lean but fasten your belt, this plane is experiencing high turbulence')
else:
    print('The flight departs without you, traveller. Some journeys must wait...')
    print("\n" + "="*50)
journey_count = 1

while True:  # 'while' must be lowercase, not 'While'
    another = input(f"\n{name}, would you like to hear another passenger's story? (yes/no): ").lower()
    
    if another == 'yes':
        journey_count += 1
        print(f"\n--- Journey #{journey_count} ---")
        time.sleep(2)
        print("To be alive is indeed a choice, while many think they have free choice")
        time.sleep(2)
        print("Knowledge about their future should be progressive and much more incremental")
        time.sleep(2)
        print("While we are both strangers. Passenger, the greatest gift a creator can ever confer upon His creation is the ability to choose")
        time.sleep(3)
        print("This sentiment has shaped history as we know it today and for a generation to come")
        time.sleep(2)
        print("They can be right but others will always not question life itself but choose to live it blindly")
        time.sleep(2)
        print("One can wonder if to choose wisely is conditional that a stitch in time saves 9?")
        time.sleep(2)
        print("Moreover, Passenger we are all main characters in this story we are choosing to play in.")
        time.sleep(2)
        print("Oh, truly an emotion picture")
        time.sleep(2)
        print("Hey, stranger. What a time to be alive")
        time.sleep(2)
        print("Every Passenger carries a story...")
        time.sleep(2)
        print("Some are running from their past.")
        time.sleep(2)
        print("Others are racing towards their future.")
        time.sleep(2)
        print("But you, " + name + ", you are building your own plane.")
        time.sleep(3)
    elif another == 'no':
        print(f"\n{name}, you've completed {journey_count} journey(s) today.")
        print(f"The pilot remembers all {journey_count} passengers.")
        print("\nRemember: You're not just a passenger. You're the architect of your flight.")
        print("\nUntil we meet again. Keep building.")
        break
    else:
        print("Please answer 'yes' or 'no'")
   
