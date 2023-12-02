import subprocess
import time

def run_command(command):
    subprocess.run(command, shell=True)

def install_threader3000():
    print("\nInstalling threader3000")
    run_command("sudo pip3 install threader3000")
    print("threader3000 installed")
    time.sleep(0.5)

def install_dirsearch():
    print("\nInstalling dirsearch....")
    run_command("sudo apt install dirsearch")
    print("dirsearch installed")
    time.sleep(0.5)

def install_terminator():
    print("\nInstalling terminator")
    run_command("sudo apt install terminator")
    print("TERMINATOR INSTALLED")

def clean_up():
    print("\nCleaning stuff up now")
    run_command("sudo apt autoremove")

def run_the_works():
    print("\nRunning The Works!")
    run_command("sudo apt update")
    install_threader3000()
    install_dirsearch()
    install_terminator()
    clean_up()
    print("All packages cleaned up. Happy hunting!")
    time.sleep(0.5)

print("""\
 _  __     _ _ ____  _             _            
| |/ /__ _| (_) ___|| |_ __ _ _ __| |_ ___ _ __ 
| ' // _` | | \___ \| __/ _` | '__| __/ _ \ '__|
| . \ (_| | | |___) | || (_| | |  | ||  __/ |   
|_|\_\__,_|_|_|____/ \__\__,_|_|   \__\___|_|   


""")
print("Welcome to the installer, We're about to install some good stuff for you")

while True:
    print("\nChoose an option:")
    print("1. Update packages")
    print("2. Install threader3000")
    print("3. Install dirsearch")
    print("4. Install terminator")
    print("5. Clean up")
    print("6. Run The Works")
    print("7. Exit")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        run_command("sudo apt update")
    elif choice == "2":
        install_threader3000()
    elif choice == "3":
        install_dirsearch()
    elif choice == "4":
        install_terminator()
    elif choice == "5":
        clean_up()
    elif choice == "6":
        run_the_works()
    elif choice == "7":
        print("Goodbye! Happy hunting!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
