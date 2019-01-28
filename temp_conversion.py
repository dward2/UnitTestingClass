def convert_c_to_f(temp_c):
    temp_f = 1.8 * temp_c + 32
    return temp_f


def main_code():
    temp_c_str = input("Enter temperature in degC: ")
    temp_c = float(temp_c_str)
    temp_f = convert_c_to_f(temp_c)
    print("The temperature is {} degF".format(temp_f))


def fever_detection(temperatures):

    largest_temp = max(temperatures)
    has_fever = False
    fever_threshold = 100.5
    for temp in temperatures:
        if temp >= fever_threshold:
            has_fever = True
    return largest_temp, has_fever


if __name__ == "__main__":
    main_code()
