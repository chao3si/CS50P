def main():
    time = input("What time is it? ").strip().lower()
    ans = convert(time)
    if 7 <= ans <= 8:
        print("Breakfast time")
    elif 12 <= ans <= 13:
        print("Lunch time")
    elif 18 <= ans <= 19:
        print("Dinner time")


def convert(time):
    time.replace("a.m.", "").replace("p.m.", "")
    # print(time)
    hours, minutes = time.split(":")
    hours, minutes = int(hours), int(minutes)
    if "p.m." in time and hours != 12:
        hours += 12
    if "a.m." in time and hours == 12:
        hours = 0
    return hours + minutes / 60


if __name__ == "__main__":
    main()
