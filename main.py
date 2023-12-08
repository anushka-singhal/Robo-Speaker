import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker")
    x = input("Enter what you want me to pronounce")
    command = f"say {x}"
    os.system(command)