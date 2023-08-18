import selectors
import sys

def read_input():
    # Create a selector object
    selector = selectors.DefaultSelector()

    # Register the standard input (sys.stdin) for reading with a timeout
    selector.register(sys.stdin, selectors.EVENT_READ)

    try:
        print("Enter something (or press Enter to skip):")
        events = selector.select(timeout=30)  # Wait for input for 30 seconds

        if events:
            # User provided input within the timeout
            user_input = sys.stdin.readline().strip()
            return user_input
        else:
            print("No input received. Skipping.")
            return None

    except KeyboardInterrupt:
        return None

if __name__ == "__main__":
    user_input = read_input()

    if user_input is not None:
        print("You entered:", user_input)
    else:
        print("No input received.")
