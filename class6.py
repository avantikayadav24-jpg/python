print("=== smart school day planner ===")
print("Answer 3 quick questions and I will plan your day!\n")

day = input("What day is it? (monday to sunday): ").strip().capitalize()
weather = input("What is the weather? (sunny / rainy / cloudy) : ").strip().lower()
homework = input("Is your homework done? (yes / no): ").strip().lower()




if day in ("Saturday","Sunday"):
    print("weekend - enjoy your free time!")
elif day =="Monday":
    print("First day of the week. Pack your weekly planner.")
elif day =="Friday":
    print("Last school day. Return library school books today.")
elif day in ("Tuesday","Wednesday", "Thursday"):
    print("Regular school day. Stay focused!")
else:
    print("Day not recognised. Please check the spelling.")

if weather == "sunny" and homework =="yes":
    print("After school: Head to the park - great weather and homework is done!")

if not (homework == "yes"):
    print("homework   : not done yet.Finish it before going out!")

if weather == "rainy" or weather == "cloudy":
    print("weather tip : Pack your umbrella - it may get wet outside.")