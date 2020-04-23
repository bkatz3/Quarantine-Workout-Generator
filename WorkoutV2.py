import random
import datetime
import csv

todays_date=datetime.datetime.today()
todays_date=todays_date.strftime('%m/%d/%Y')



def generate_upper():
    lucky_number=random.randint(1,6)
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
    elif lucky_number == 6:
        sets = random.randint(4, 8)
        exercise = f"{sets} sets of Shoulder Presses"
    return exercise


def generate_legs():
    lucky_number = random.randint(1, 5)
    exercise = ""
    if lucky_number == 1:
        reps = random.randint(3, 10)
        exercise = f"{reps} Minutes of Wall Sits"
    elif lucky_number == 2:
        sets = random.randint(3, 7)
        exercise = f"{sets} sets of Calf Raises"
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


def generate_wild_card():
    lucky_number = random.randint(1,6)
    exercise = ""
    if lucky_number == 1:
        reps = random.randint(50, 300)
        exercise = f"{reps} Pushups"
    elif lucky_number == 2:
        reps = random.randint(30, 150)
        exercise = f"{reps} Pullups"
    elif lucky_number == 3:
        sets = random.randint(4,8)
        exercise = f"{sets} sets of rows"
    elif lucky_number == 4:
        miles = random.randint(2, 5)
        exercise = f"{miles} mile Run"
    elif lucky_number == 5:
        exercise = "Rest Day!"
    elif lucky_number == 6:
        exercise = "20 minutes of stretching"
    return exercise


def generate_workout():
    upper=generate_upper()
    lower=generate_legs()
    core=generate_core()
    wild_card=generate_wild_card()

    workout_dict={}
    workout_dict['Date']=todays_date
    workout_dict['Upper']=upper
    workout_dict['Lower']=lower
    workout_dict['Core']=core
    workout_dict['Wild Card']=wild_card

    print(f'\n{todays_date}\'s workout is as follows:')
    print(f'{upper} \n{lower} \n{core} \n{wild_card}')


    with open('/Users/BenKatz/Documents/environments/project1_env/bin/workoutlog.csv','a') as csv_file:
        fields=['Date','Upper','Lower','Core','Wild Card']
        output_writer=csv.DictWriter(csv_file,fieldnames=fields)
        # output_writer.writeheader()     <---- Use this when starting a new csv - will write the headers into the doc.
        output_writer.writerow(workout_dict)


generate_workout()
