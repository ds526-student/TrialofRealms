def get_valid_int(prompt, min_value=None, max_value=None, return_zero_based=False):
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Invalid response please try again")
                continue
            if max_value is not None and value > max_value:
                print(f"Invalid response please try again")
                continue
            return value - 1 if return_zero_based else value
        except ValueError:
            print("Invalid response please try again")

def confirm(prompt="Would you like to proceed? (y/n)"):
    x = input(prompt).strip().lower()
    return x

def enter():
    print("Press enter to continue")
    input()