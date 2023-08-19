import schedule
import time

def my_function():
    print("Running my_function")

# Schedule the function to run every x minutes
interval_minutes = 5  # Change this to the desired interval in minutes
schedule.every(interval_minutes).minutes.do(my_function)

while True:
    schedule.run_pending()
    time.sleep(1)
