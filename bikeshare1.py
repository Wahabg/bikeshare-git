import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january','february','march','april','may','june','all']
days = ['monday','tuesday','wedensday','thursday','friday','saturday','sunday','all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Choose the city you want to explore: {'chicago,washington,new york city'} ")


        if city.lower()  not in CITY_DATA:
            print('Please write a valid city')
            continue
        else:
            print(f'You entered {city.lower()}')
            break
            
    while True:
        month = input("Choose which month you want to explore: {'january,february,march,april,may,june,all'}")


        if month.lower()  not in months:
            print('Please write a valid month')
            continue
        else:
            print(f'You entered {month.lower()}')
            break
            
    while True:
        day = input("Choose the day you want to explore: {'monday,tuesday,wedensday,thursday,friday,saturday,all'}")


        if day.lower()  not in days:
            print('Please write a valid day')
            continue
        else:
            print(f'You entered {day.lower()}')
            break
            
    


    # get user input for month (all, january, february, ... , june)


    # get user input for day of week (all, monday, tuesday, ... sunday)


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

    
        # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_of_week

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        day = days.index(day) + 1
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    # extract month from the Start Time column to create an month column
    df['month'] = df['Start Time'].dt.month

    # find the most popular hour
    popular_month = df['month'].mode()[0]

    print('Most Popular  month:', popular_month)

    # display the most common day of week
    # extract day from the Start Time column to create an day column
    df['day'] = df['Start Time'].dt.day_of_week

    # find the most popular hour
    popular_day = df['day'].mode()[0]

    print('Most Popular  day:', popular_day)

    # display the most common start hour
    
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]

    print('Most Popular start station:', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    print('Most Popular end station:', popular_end_station)

    # display most frequent combination of start station and end station trip
    
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    popular_comb_station = df['Start To End'].mode()[0]
    print('Most Popular combination station:', popular_comb_station)
    



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    
    total_duration = df['Trip Duration'].sum()
    
    #Finds out the duration in minutes and seconds format    

    
    #Finds out the duration in hour and minutes format
 
    print(f"The total trip duration is {total_duration//3600} hours, {total_duration%3600//60} minutes and {total_duration%60} seconds.")

    #Calculating the average trip duration using mean method
    average_duration = round(df['Trip Duration'].mean())
    #Finds the average duration in minutes and seconds format
    print(f"The total trip duration is {average_duration//3600} hours, {average_duration//60} minutes and {average_duration%60} seconds.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()

    print(f"The types of users by number are :\n\n{user_type}")

    # Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print(f"\nThe types of users by gender are given below:\n\n{gender}")
    except:
        print("\nThere is no 'Gender' column in this file.")

    # Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print(f"\nThe earliest year of birth: {earliest}\n\nThe most recent year of birth: {recent}\n\nThe most common year of birth: {common_year}")
    except:
        print("There are no birth year details in this file.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def display_data(df):
    more = ''

    response = ['yes','no']
    count = 5

    counter = 0
    while True:
        answer = input("Would you like to see the raw data? {'yes,no'}")


        if answer.lower() not in response:
            print('Please write a valid answer')
            continue
        else:
            print(f'You entered {answer.lower()}')
            break

    if answer == 'yes':
        print(df[0:count])
        while more =='':
            
            while True:
                more = input("Would you like to see more raw data? press enter or write no to exit ")


                if more  not in ['','no']:
                    print('Please write a valid answer')
                    continue
                else:
                    
                    break
            
            if more =='':
                print(df[count:count+5])
                print('-'*100)

                count+=count
                continue
                
            else:
                print("end of program")
                print('-'*100)
                break
    else:
        print("end of program")


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
