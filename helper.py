import os

data = {
    "push": "push.bat",
    "mrnd": "main_nodebug.bat",
    "gaph": "gitea-push.bat",
    # number
    "1": "push.bat",
    "2": "gitea-push.bat",
}

def print_info():
    print("Internal Tool")

print_info()

while True:
    command = input("=" * 30 + "\nEnter command: ").strip()
    if command in ["cls", "clear"]:
        os.system("cls")
        print_info()
        continue
    try:
        file = data[command]
        os.system("misc\\Batch\\" + file)
    except Exception as error:
        print("Unknown command.")