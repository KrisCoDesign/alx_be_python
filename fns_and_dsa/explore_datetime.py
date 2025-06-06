from datetime import datetime, timedelta, date

def display_current_datetime():
    current_date = datetime.now()
    print(f'Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}')

def calculate_future_date():
    user_days = int(input('Enter the number of days to add to the current date: '))
    current_date = date.today()
    future_date = current_date + timedelta(days=user_days)
    print(f'Futre date: {future_date}')

display_current_datetime()
calculate_future_date()