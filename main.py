import keyboard
import time
import inquirer
import sys
import configparser
import os
from pynput import keyboard as pynput_keyboard
from win10toast import ToastNotifier
import itertools


def writter(filename, key, value):
    with open(filename, 'r+') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if (str(key)) in line:
                lines[i] = str(key) + " " + str(value) + "\n"
        f.seek(0)
        f.writelines(lines)


def reader(filename, key):
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if key in line:
                return line.split(": ")[1].strip()


def on_press(key):
    global right_i
    if key == pynput_keyboard.Key.pause:
        toaster = ToastNotifier()
        toaster.show_toast("Forza Horizon 5 Skill Points Macro",
                           "Macro stopped.", duration=0)
        os._exit(0)
    if key == pynput_keyboard.Key.right:
        right_i += 1
        print(f'\rYou have {str(right_i * 2)} Tridents: ', end='')


def countdown(t):
    while (t):
        mins, secs = divmod(t, 60)
        timer = 'Starting in: {:2d}'.format(secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("\n")


def press(key, delay):
    keyboard.press_and_release(key)
    time.sleep(delay)


def press_and_release_amount(amount, key):
    for i in range(0, amount):
        keyboard.press_and_release(key)
        time.sleep(0.5)


def upgrades_navigator():
    press('enter', 1)
    press('right', 1)
    press('right', 1)
    press('down', 1)
    press('enter', 1)


def paint_navigator():
    press('left', 1)
    press('down', 1)
    press('enter', 1)


def car_mastery():
    press('enter', 2)
    press('right', 2)
    press('enter', 2)
    press('right', 2)
    press('enter', 2)
    press('up', 2)
    press('enter', 2)
    press('right', 2)
    press('enter', 2)


# Man = Manufacturer Go To Brand Select
def applier(man_row_amt, man_col_amt, loop_amt):
    right_amt_store = 1
    keyboard.press_and_release('backspace')
    time.sleep(0.8)
    press_and_release_amount(man_row_amt, 'right')
    time.sleep(0.5)
    press_and_release_amount(man_col_amt, 'down')
    press('enter', 1)
    # car select nav goes here
    press('enter', 5)
    press('esc', 2)
    press('up', 1)
    upgrades_navigator()
    time.sleep(1)
    car_mastery()
    press('esc', 2)
    press('esc', 2)
    press('down', 1)
    press('enter', 1)
    paint_navigator()
    for i in range(0, (loop_amt//2)):
        for i in range(0, 2):
            keyboard.press_and_release('backspace')
            time.sleep(0.8)
            press_and_release_amount(man_row_amt, 'right')
            time.sleep(0.5)
            press_and_release_amount(man_col_amt, 'down')
            press('enter', 1)
            press_and_release_amount(right_amt_store, 'right')
            press('enter', 5)
            press('esc', 2)
            press('up', 1)
            upgrades_navigator()
            time.sleep(1)
            car_mastery()
            press('esc', 2)
            press('esc', 2)
            press('down', 1)
            press('enter', 1)
            paint_navigator()
        right_amt_store += 1


def replayer():
    total = (int(reader("history.txt", macro_runs_total)))
    potential_sp_total = int(reader("history.txt", sp_earned_total))
    run = 0
    sp = 0
    for i in itertools.count(start=1):
        keyboard.press_and_release('enter')
        time.sleep(8)
        keyboard.press("w")
        time.sleep(45)
        keyboard.release("w")
        time.sleep(1)
        keyboard.press_and_release('x')
        time.sleep(1)
        keyboard.press_and_release('enter')
        time.sleep(12)
        total += 1
        run += 1
        potential_sp_total += 9
        sp += 9
        writter("history.txt", macro_runs, run)
        writter("history.txt", macro_runs_total, total)
        writter("history.txt", sp_earned, sp)
        writter("history.txt", sp_earned_total, potential_sp_total)
    os._exit(0)


def purchaser(num):
    tridents2 = 0
    total_tridents = (int(reader("history.txt", tridents_total)))
    for i in range(0, num):
        # keyboard.press_and_release('y')
        # time.sleep(1)
        # keyboard.press_and_release('enter')
        time.sleep(0.4)
        total_tridents += 1
        tridents2 += 1
        writter("history.txt", tridents, tridents2)
        writter("history.txt", tridents_total, total_tridents)
        print('success')
    os._exit(0)


def formatter(num):
    return "{:,}".format(num)


def main():
    global macro_runs
    global macro_runs_total
    global sp_earned
    global sp_earned_total
    global tridents
    global tridents_total
    global sp_used
    global wheelspin_earned

    macro_runs = "Last macro runs:"
    macro_runs_total = "Total runs:"
    sp_earned = "Potential skill points earned from the last run:"
    sp_earned_total = "Total potential skill points earned:"
    tridents = "Total Peel Tridents purchased from the last macro:"
    tridents_total = "Total Peel Tridents purchased:"
    sp_used = "Total Skill Points applied and used:"
    wheelspin_earned = "Total Wheel Spins earned: 32"
    if not os.path.exists("history.txt"):
        with open("history.txt", 'w') as f:
            f.write("""### 10SP 30S Skill Points Statistics:\nLast macro runs: 0\nTotal runs: 0\nPotential skill points earned from the last run: 0\nTotal potential skill points earned: 0\n\n### Peel Trident Purchaser:\nTotal Peel Tridents purchased from the last macro: 0\nTotal Peel Tridents purchased: 0\n\n### Skill Points Applier:\nTotal Skill Points applied and used: 0\nTotal Wheel Spins earned: 0""")

    app_question = [
        inquirer.List(
            "action",
            message="Select",
            choices=["10SP 30S Replayer", "Peel Trident Purchaser",
                     "Peel Trident Super Wheel Spin Applier"],
        ),
    ]
    config_question = [
        inquirer.List(
            "action",
            message="Select",
            choices=["Yes", "No (create new)"],
        ),
    ]
    print("Forza Horizon 5 Skill Point Macro Tool\nAfter selecting an option the countdown will start, please quickly switch to the Forza Horizon window.")
    print("Tip: Press right key to count how many Tridents you have, stop pressing right just until the excess Trident where the bottom column is empty.\nRestart program after done counting.")
    app_answers = inquirer.prompt(app_question)
    if (app_answers["action"] == "10SP 30S Replayer"):
        input("Please note that this will run indefinitely. Press Pause Break to exit out.\nPress enter to continue:")
        countdown(5)
        while (True):
            replayer()
    elif (app_answers["action"] == "Peel Trident Purchaser"):
        num_input = int(input("Enter the number of Peel Tridents to buy: "))
        total_price = num_input * 25000
        total_sp = num_input * 9
        input(f"You will be purchasing {str(formatter(total_price))} credits worth of Peel Tridents costing {
              str(total_sp)} Skill Points for {str(num_input)} Super Wheelspins. Confirm? (Press enter to continue): ")
        countdown(5)
        purchaser(num_input)
    elif (app_answers["action"] == "Peel Trident Super Wheel Spin Applier"):
        num_input_amt = int(
            input("Enter the number of Peel Tridents to apply (value needs to be greater than 1):\n "))
        if not os.path.exists('config.ini'):
            config = configparser.ConfigParser()
            num_input_row = int(
                input("Enter how many right keypress for jumping to manufacturer Peel: "))
            num_input_col = int(
                input("Enter how many down keypress for jumping to manufacturer Peel: "))
            config['DEFAULT'] = {
                'manufacturerrowamount': num_input_row, 'ManufacturerColAmount': num_input_col}
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
        elif os.path.exists('config.ini'):
            config_read = configparser.ConfigParser()
            # Load the file into the config_read object
            config_read.read('config.ini')
            num_input_row = int(
                config_read['DEFAULT']['manufacturerrowamount'])
            num_input_col = int(
                config_read['DEFAULT']['ManufacturerColAmount'])
            print(f"Use the last manufacturer selection settings?:\nRight Keypress: {
                  num_input_row}\nDown Keypress:{num_input_col}")
            config_answers = inquirer.prompt(config_question)
            if (config_answers["action"] == "Yes"):
                pass
            elif (config_answers["action"] == "No (create new)"):
                config = configparser.ConfigParser()
                num_input_row = int(
                    input("Enter how many right keypress for jumping to manufacturer Peel: "))
                num_input_col = int(
                    input("Enter how many down keypress for jumping to manufacturer Peel: "))
                config['DEFAULT'] = {
                    'manufacturerrowamount': num_input_row, 'ManufacturerColAmount': num_input_col}
                with open('config.ini', 'w') as configfile:
                    config.write(configfile)
        print(f'complete: row: {num_input_row} col:{
              num_input_col} loop: {num_input_amt}')
        countdown(5)
        applier(num_input_row, num_input_col, num_input_amt)


def on_press(key):
    global right_i
    if key == pynput_keyboard.Key.pause:
        toaster = ToastNotifier()
        toaster.show_toast("Forza Horizon 5 Skill Points Macro",
                           "Macro stopped.", duration=0)
        os._exit(0)
    if key == pynput_keyboard.Key.right:
        right_i += 1
        print(f'\rYou have {str(right_i * 2)} Tridents: ', end='')


if __name__ == '__main__':
    sys.set_int_max_str_digits(0)
    os.system('cls')
    global right_i
    right_i = 0
    with pynput_keyboard.Listener(on_press=on_press) as listener:
        main()
        listener.join()
