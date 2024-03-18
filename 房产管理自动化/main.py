from Menu import Menu


menu = Menu()

menu.read_file()

while True:
    label = menu.choose_function()
    if not label:
        break
