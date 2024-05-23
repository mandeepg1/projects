# secret_number = 9
# guess_count = 0
# guess_limit = 3

# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print("You Win")
#         break
# else:
#     print('You failed')

# Car game

command = ""
started = False
stopped = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("got motion")
        else:
            started = True
            print('Car started...')
    elif command == "stop":
        print("Car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
              """)
    elif command == "quit":
        break
    else:
        print("Sorry me no hables englas")