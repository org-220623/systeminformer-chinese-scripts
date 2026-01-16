import os

data = {
    "push": "push.bat",
    "mrnd": "main_nodebug.bat",
    "gaph": "gitea-push.bat",
    "burl": ["build-release.bat", "restore.bat"],
    "rste": "restore.bat",
    # number
    "0": ["build-release.bat", "restore.bat"],
    "1": "push.bat",
    "2": "gitea-push.bat",
    "3": "restore.bat",
}

def print_info():
    print("Internal Tool")

print_info()

try:
    while True:
        command = input("=" * 30 + "\nEnter command: ").strip()
        if command in ["cls", "clear"]:
            os.system("cls")
            print_info()
            continue
        if command in ["quit", "exit", "die"]:
            exit()
        try:
            file = data[command]
            if command in ["burl", "0"]:
                os.system(r"..\build\build_thirdparty.cmd")
            if isinstance(file, str):
                os.system("misc\\Batch\\" + file)
            elif isinstance(file, list):
                for i in file:
                    if isinstance(i, str):
                        os.system("misc\\Batch\\" + i)
                    else:
                        print("Unknown type. [0x1]")
            else:
                print("Unknown type. [0x2]")
        except Exception as error:
            print("Unknown command.")
except KeyboardInterrupt:
    exit()
except SystemError:
    exit()
except SystemExit:
    exit()
else:
    exit()