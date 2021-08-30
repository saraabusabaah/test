import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    while True:

      city = input("Enter one of the following cities: New York City, Chicago or Washington?\n")
      city = city.lower()
      if city not in ('new york city', 'chicago', 'washington'):
        print("invalid city, please enter valid city\n")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:

      month = input("Enter the specific month that you want or enter 'all':\n")
      month = month.lower()
      if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
        print("invalid month, please try again")
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:

      day = input(" Enter the specific day that you want \n")
      day = day.lower()
      if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
          print("invalid day, please enter a valid day")
          continue
      else:
        break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name


    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]


        if day != 'all':
           df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    print ("most common month :" , df['month'].mode().max())

    # TO DO: display the most common day of week

    print ("most common day :" , df['day_of_week'].mode().max())

    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    print("The most common start hour is ", df['hour'].mode()[0])



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    print("most common start station", df['Start Station'].mode().max())


    # TO DO: display most commonly used end station

    print("most common end station", df['End Station'].mode().max())

    # TO DO: display most frequent combination of start station and end station trip


    df['trip'] = df['Start Station'] + ' - ' + df['End Station']
    print("most common end station used :", df['trip'].mode().max())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    print("The total travel time = ", df['Trip Duration'].sum())

    # TO DO: display mean travel time

    print("The total mean time =", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    print('user types :',df['User Type'].value_counts())

    # TO DO: Display counts of gender

    try:
        print('gender types :', df['gender'].value_counts())
    except:
        print ('No data available')


    # TO DO: Display earliest, most recent, and most common year of birth

    try:
        print('the earliest year of birth:'(df['birth year'].min()))
        print('the most recent year of birth:'(df['birth year'].max()))
        print('the most common year of birth:'(df['birth year'].mode().max()))

    except:
        print('birth year not available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    x = 1
    while True:
        r = input('\nWould you like to see the raw data? please Enter yes or no.\n')
        if r.lower() == 'yes':
            print(df[x:x+5])
            x = x+5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)






        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
