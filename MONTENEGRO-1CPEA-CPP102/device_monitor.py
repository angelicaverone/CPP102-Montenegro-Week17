def get_initial_readings():
    readings = []

    while True:
        text = input("How many readings will you enter? ")

        if is_whole_number(text):
            number = int(text)

            if number > 0:
                break

        print("Invalid input. Enter a positive whole number.")

    for index in range(number):
        while True:
            text = input(
                f"Enter temperature reading {index + 1}: "
            )

            if is_whole_number(text):
                reading = int(text)

                if 0 <= reading <= 100:
                    readings.append(reading)
                    break

            print("Invalid input. Enter a whole number from 0 to 100.")

    return readings


def is_whole_number(text):
    if len(text) == 0:
        return False

    for character in text:
        if character not in "0123456789":
            return False

    return True


def display_menu():
    print("\nSIMULATED DEVICE MONITORING SYSTEM")
    print("----------------------------------")
    print("[1] View Readings")
    print("[2] Add Reading")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")


def display_readings(readings):
    print("\nCURRENT READINGS")
    print("----------------")

    for index in range(len(readings)):
        print(f"Reading {index + 1}: {readings[index]} °C")


def add_reading(readings):
    while True:
        text = input("Enter new temperature reading: ")

        if is_whole_number(text):
            reading = int(text)

            if 0 <= reading <= 100:
                readings.append(reading)
                print("Reading added successfully.")
                break

        print("Invalid input. Enter a whole number from 0 to 100.")


def classify_reading(reading):
    if reading < 30:
        return "NORMAL"
    elif reading <= 35:
        return "WARNING"
    else:
        return "CRITICAL"


def classify_readings(readings):
    print("\nREADING CLASSIFICATION")
    print("----------------------")

    for reading in readings:
        status = classify_reading(reading)
        print(f"{reading} °C -> {status}")


def compute_total(readings):
    total = 0

    for reading in readings:
        total += reading

    return total


def compute_average(readings):
    if len(readings) == 0:
        return 0.0

    return compute_total(readings) / len(readings)


def find_minimum(readings):
    minimum = readings[0]

    for reading in readings:
        if reading < minimum:
            minimum = reading

    return minimum


def find_maximum(readings):
    maximum = readings[0]

    for reading in readings:
        if reading > maximum:
            maximum = reading

    return maximum


def count_category(readings, category):
    count = 0

    for reading in readings:
        if classify_reading(reading) == category:
            count += 1

    return count


def determine_overall_status(warning_count, critical_count):
    if critical_count > 0:
        return "ATTENTION REQUIRED"
    elif warning_count > 0:
        return "MONITOR"
    else:
        return "NORMAL"


def display_summary(readings):
    total = compute_total(readings)
    number = len(readings)
    average = compute_average(readings)

    normal = count_category(readings, "NORMAL")
    warning = count_category(readings, "WARNING")
    critical = count_category(readings, "CRITICAL")

    print("\nMONITORING SUMMARY")
    print("------------------")
    print(f"Number of readings: {number}")
    print(f"Total of readings: {total}")
    print(f"Average temperature: {average:.2f} °C")

    if number > 0:
        print(f"Minimum temperature: {find_minimum(readings)} °C")
        print(f"Maximum temperature: {find_maximum(readings)} °C")

        print(f"\nNORMAL: {normal} ({normal / number * 100:.2f}%)")
        print(f"WARNING: {warning} ({warning / number * 100:.2f}%)")
        print(f"CRITICAL: {critical} ({critical / number * 100:.2f}%)")

    status = determine_overall_status(warning, critical)
    print(f"\nOverall Status: {status}")


def main():
    readings = get_initial_readings()

    while True:
        display_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            display_readings(readings)

        elif choice == "2":
            add_reading(readings)

        elif choice == "3":
            classify_readings(readings)

        elif choice == "4":
            display_summary(readings)

        elif choice == "5":
            print("Thank you for using the Device Monitoring System.")
            break

        else:
            print("Invalid choice. Please enter 1 to 5.")


main()