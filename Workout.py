import random

def generate_upper():
    lucky_number=random.randint(1,5)
    exercise=""
    if lucky_number==1:
        reps=random.randint(2,7)
        exercise=f"{reps} Sets of Curls"
    elif lucky_number==2:
        reps = random.randint(2, 7)
        exercise=f"{reps} Sets of Curl Holds"
    elif lucky_number==3:
        reps = random.randint(50, 250)
        exercise = f"{reps} Tricep Presses"
    elif lucky_number==4:
        reps = random.randint(50, 250)
        exercise = f"{reps} Tricep Extensions"
    elif lucky_number==5:
        reps = random.randint(50, 250)
        exercise=f"{reps} Shrugs"
    return exercise


def generate_legs():
    lucky_number = random.randint(1, 5)
    exercise = ""
    if lucky_number == 1:
        reps = random.randint(3, 10)
        exercise = f"{reps} Minutes of Wall Sits"
    elif lucky_number == 2:
        reps = random.randint(100, 300)
        exercise = f"{reps} Calf Raises"
    elif lucky_number == 3:
        reps = random.randint(50, 200)
        exercise = f"{reps} Lunges"
    elif lucky_number == 4:
        reps = random.randint(25, 100)
        exercise = f"{reps} Box Jumps"
    elif lucky_number == 5:
        reps = random.randint(50, 250)
        exercise = f"{reps} Squats"
    return exercise


def generate_core():
    lucky_number = random.randint(1,5)
    exercise = ""
    if lucky_number == 1:
        reps = random.randint(50, 250)
        exercise = f"{reps} Situps"
    elif lucky_number == 2:
        reps = random.randint(50, 250)
        exercise = f"{reps} Leg Lifts"
    elif lucky_number == 3:
        reps = random.randint(3, 10)
        exercise = f"{reps} Min of Planks"
    elif lucky_number == 4:
        reps = random.randint(50, 250)
        exercise = f"{reps} Russian Twists"
    elif lucky_number == 5:
        reps = random.randint(2, 5)
        exercise = f"{reps} Sets of alphabet Leg Lifts"
    return exercise


def generate_wild_Card():
    lucky_number = random.randint(1,5)
    exercise = ""
    if lucky_number == 1:
        reps = random.randint(50, 300)
        exercise = f"{reps} Pushups"
    elif lucky_number == 2:
        reps = random.randint(30, 150)
        exercise = f"{reps} Pullups"
    elif lucky_number == 3:
        reps = random.randint(50, 200)
        exercise = f"{reps} Dips"
    elif lucky_number == 4:
        miles = random.randint(2, 5)
        exercise = f"{miles} mile Run"
    elif lucky_number == 5:
        exercise = "Rest Day!"
    return exercise


def generate_workout():
    print("Today's workout is as follows:")
    print(generate_upper())
    print(generate_legs())
    print(generate_core())
    print(generate_wild_Card())

generate_workout()

