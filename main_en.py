import time
import random

# Define the correct password
Password = "123"

# Global variable initialization
Global_TimesTry = 0  # Number of attempts
Global_TimeNeedToWait = 0  # Time needed to wait
Global_ReInputCtrl = False  # Control whether the correct password is entered again
Global_TurnToReturnFakeTrue = random.randint(0, 1400)  # Randomly generate a count to fake a correct response


def GiveRandomFakeTrueTurns(NowTurn):
    """
    Prepare for the next random fake correct result
    """
    global Global_TurnToReturnFakeTrue
    Global_TurnToReturnFakeTrue = NowTurn + random.randint(0, 1400)


def CheckPassword_Main(Password_input):

    global Password
    global Global_TimesTry
    global Global_TimeNeedToWait
    global Global_ReInputCtrl
    global Global_TurnToReturnFakeTrue

    # Increment the total number of attempts
    Global_TimesTry += 1

    # Calculate how long to wait for this attempt based on the total number of attempts
    Global_TimeNeedToWait = round(Global_TimeNeedToWait + (Global_TimesTry / 50), 1)

    # If the wait time exceeds 10 seconds, enforce it to 10 seconds to prevent legitimate users from being unable to log in due to excessive wait time caused by brute force attempts
    if Global_TimeNeedToWait > 10:
        Global_TimeNeedToWait = 10
        print("Your password is being brute-forced. We are protecting your account security. Please wait 10 seconds.")

    # Wait to increase the difficulty of brute-force attempts
    time.sleep(Global_TimeNeedToWait)

    # Check if the entered password is correct
    if Password == Password_input:
        if Global_ReInputCtrl:
            # If it's the second time entering the correct password, return a true correct result
            return (True, True, True)
        else:
            # If it's the first time entering the correct password, return a fake incorrect result
            Global_ReInputCtrl = True
            return (False, False, False)
    else:
        # If the number of attempts reaches the count to return a fake correct result, fake a correct return
        if Global_TimesTry == Global_TurnToReturnFakeTrue:
            GiveRandomFakeTrueTurns(Global_TimesTry)
            return (False, False, True)  # Fake a correct return
        else:
            # If the input is incorrect, return a fake incorrect result
            return (False, False, False)


def True_Login():
    """
    Operations after the user successfully logs in
    """
    print("Login successful, entering the system...")
    return 0


# Main loop, continuously prompting the user to enter the password
while True:
    # User input for the password
    Password_input = str(input("Please enter the password:"))

    # Check the password and get the result status
    True_Status, Sec_True, Show_True = CheckPassword_Main(Password_input)

    if True_Status:
        if Sec_True:
            # Second correct password entry, truly log in
            print("Password correct! Verification successful, logging in, please wait...")
            True_Login()
        elif Show_True:
            # Fake a correct return, not truly logging in
            print("Password correct! Verification successful, logging in, please wait...")
    elif Show_True:
        # Random fake correct, prompt the user as if they are logging in
        print("Password correct! Verification successful, logging in, please wait...")
    else:
        # Incorrect password input, prompt to re-enter
        print("Password incorrect! Please try again.")
