command = ""
started = False
while command != "quit":
    command = input('>')
    if command == "start":
        if started:
            print('car has already started')
        else:
            started = True
            print("car started")
    elif command == "stop":
        if started:
            print('car stopped')
            started = False
        else:
            print("car is already stopped")
    elif command == "help":
        print("""
        Start - to start the car)
        stop- to stop the car
        quit - to exit""")
    elif command == "quit":
        break
    else:
        print('enter valid option')




