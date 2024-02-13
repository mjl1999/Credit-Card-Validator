def main():
    card = input("Please enter your 16 digit card number (no spaces or hyphens optional): ")
    card = card.translate(str.maketrans({" ": "", "-": ""}))
    card = check_card(card)
    validate(card)


def validate(card):
    r_card = card[::-1]
    total_of_n1 = sum_n1(r_card)
    total_of_n2 = sum_n2(r_card)
    total = total_of_n1 + total_of_n2
    if total % 10 == 0:
        print("Valid card")
    else:
        print("Invalid card")


def sum_n1(card):
    total = 0
    for num in card[::2]:
        total += int(num)
    return total


def sum_n2(card):
    total = 0
    for num in card[1::2]:
        num = int(num) * 2
        if num >= 10:
            num = (num // 10) + (num % 10)
        total += num
    return total


def check_card(card):
    retry_attempts = 4
    while retry_attempts != 0:
        if check_digits(card) and check_length(card):
            return card
        else:
            card = input(f"Warning {retry_attempts - 1} retries remaining!!! Please re-enter your card details:\n")
            card = card.translate(str.maketrans({" ": "", "-": ""}))
            retry_attempts -= 1
    print("Retry attempts exceeded. Your portal has been locked for 24 hours")
    quit()


def check_digits(card):
    try:
        int(card)
        return True
    except ValueError:
        print("Please enter digits only.")
        return False

def check_length(card):
    if len(card) == 16:
        return True
    else:
        print("Your card should only be 16 digits long")
        return False

main()