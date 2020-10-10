import pyttsx3

# instantiate object from pyttsx3 module
machine = pyttsx3.init()

machine.say("Welcome to text to speech conversion!:")
machine.runAndWait()

machine.say("Would you like me to read a file? Enter yes or no down below.")
machine.runAndWait()
response = input("Enter yes or no: ")

while response == "yes":
    machine.say("Enter down below how fast you want me to speak (180 is fairly good):")
    machine.runAndWait()

    # set speech speed rate
    speechRate = int(input("Enter speech rate (180 is fairly good): "))
    machine.setProperty('rate', speechRate)

    machine.say("Enter down below the volume you want me to speak "
                "with from 0.0 to 1.0 being the loudest.")
    machine.runAndWait()

    # set volume
    volume = float(input("Enter volume down below (0.0 to 1.0 being the loudest): "))
    machine.setProperty('volume', volume)

    machine.say("Enter the full file name down below including its extension. For example, file dot t x t: ")
    machine.runAndWait()

    # user inputs file to be read
    file = input("Enter the file name: ")

    machine.say("I will start reading the file shortly.")
    machine.runAndWait()

    # reads file line by line where each line is read out loud
    with open(file, 'r') as f:
        for line in f:
            machine.say(line)
            machine.runAndWait()

    machine.say("File reading has ended. Would you like me to read another file?")
    machine.runAndWait()
    response = input("Enter yes or no: ")

machine.say("Thank you for using speech to text "
            "conversion. I hope it was useful!")
machine.runAndWait()

# stop text to speech conversion
machine.stop()
