def get_time_duration():
    while True:
        try:
            # Prompt the user to enter a time
            hours = float(input("Enter a time duration in hours: "))
            if hours < 0:
                raise ValueError("The time duration must be a non-negative number.")
            return hours
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")


def convert_time(duration_hours):
    # Convert hours to minutes and seconds
    minutes = duration_hours * 60
    seconds = duration_hours * 3600
    return minutes, seconds


def main():
    # Get the time duration from the user
    hours = get_time_duration()

    # Convert the time duration to minutes and seconds
    minutes, seconds = convert_time(hours)

    # Display the converted time duration
    print(f"{hours} hours is equal to {minutes} minutes or {seconds} seconds.")


if __name__ == "__main__":
    main()
