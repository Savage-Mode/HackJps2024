print("""

█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█   ▀█▀ █░█ █▀▀   █▀ █▀▀ █▄░█ ▀█▀ █▀▀ █▄░█ █▀▀ █▀▀   █▀▀ ▄▀█ █▀▄▀█ █▀▀
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█   ░█░ █▀█ ██▄   ▄█ ██▄ █░▀█ ░█░ ██▄ █░▀█ █▄▄ ██▄   █▄█ █▀█ █░▀░█ ██▄
""")

plrs = input("How many players will be playing: " )
while not type(plrs) == int:
    if plrs.isnumeric():
        plrs = int(plrs)
        break
    else:
        print("Please type a valid number!")
        plrs = input("How many players will be playing: " )