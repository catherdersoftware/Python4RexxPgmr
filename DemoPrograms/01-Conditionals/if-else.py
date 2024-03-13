mood = "anxious" 

if mood == "happy":
    print("I'm very pleased your're in good mood")
elif mood == "sad":
    print("Cheer up!")
elif mood in ("anxious", "worried"):
    print("Take a chill pill bro!")
else:
    print("I'll put the kettle on!")

match (mood):
    case "happy":
        print("I'm very pleased your're in good mood")
    case "sad":
        print("Cheer up")
    case "anxious" | "worried":
        print("Take a chill pill bro!")
    case _:
        print("I'll put the kettle on!")

    