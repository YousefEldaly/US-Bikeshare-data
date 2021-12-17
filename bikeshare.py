import time
import pandas as pd
import numpy as np

C_DATA = { 'chicago': 'chicago.csv',
              'new York City': 'new_york_city.csv',
              'washington': 'washington.csv' }

def filtering():

    print('Hello! this program explor\'s the US bikeshare data!')
    while True:
        city = input("\nWhich city would you like to see its data?\nNew York City.\nChicago.\nWashington\n").strip().lower()
        if city not in ('new york city', 'chicago', 'washington'):
          print("Sorry, The selected city is not in our data set. Please try again.")
          continue
        else:
          break

    while True:
            month = input("\nWhich month would you like to explore? \nJanuary, February, March, April, May, June \nor type 'all' if you do not have any preference?\n").strip().lower()
            if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
              print("\nwrong selection, please type a valid month name or all.")
              continue
            else:
             break

    while True:
          day = input("\nchoose a specific day if you want to or choose all? \n(Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or  'all'.)\n").strip().lower()
          if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
            print("\nWrong selection, please type a valid day name or all.")
            continue
          else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
 
    df = pd.read_csv(C_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        n_month = ['january', 'february', 'march', 'april', 'may', 'june']
        month = n_month.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df




def timing(df):

    print('\nCalculating The Most Frequent Times of Travel...\n')
    starting_t = time.time()

    M_C_M= df['month'].mode()[0]
    print('Most Common Month:', M_C_M)


    M_C_D= df['day_of_week'].mode()[0]
    print('Most Common day of week:', M_C_D)


    df['Start_hour'] = df['Start Time'].dt.hour
    M_C_H = df['Start_hour'].mode()[0]
    print('Most Common Hour:', M_C_H)
    print("\nThis took %s seconds." % (time.time() - starting_t))
    print('-'*40)




def stationinning(df):

    print('\nCalculating The Most Popular Stations and Trip...\n')
    starting_t = time.time()

    M_C_S_S = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station :", M_C_S_S)

    M_C_E_S = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station :", M_C_E_S)

    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nThe Most Commonly used combination of start station and end station trip:', M_C_S_S, " & ", M_C_E_S)
    print("\nThis took %s seconds." % (time.time() - starting_t))
    print('-'*40)


def duration(df):

    print('\nCalculating Trip Duration...\n')
    starting_t = time.time()

    Total_Time=60*60*24
    Total_Travel_Time = df['Trip Duration'].sum()
    print('Total travel time:', Total_Travel_Time/Total_Time, " Days")

    Avarage_T=60
    Avarage_Travel_T = df['Trip Duration'].mean()
    print('Avarage travel time:', Avarage_Travel_T/Avarage_T, " Minutes")

    print("\nThis took %s seconds." % (time.time() - starting_t))
    print('-'*40)


def user_stats(df):
    print('\nCalculating User Stats...\n')
    starting_t = time.time()

    user_types = df['User Type'].value_counts().to_frame()
    print('User types:\n', user_types)


    try:    
       gender_count = df['Gender'].value_counts().to_frame()
       print('Riders gender:\n' ,gender_count)
    except KeyError:
       print("\nGender:\nno data here to be explored.")

    try:
       Earliest_Year = df['Birth Year'].min()
       print('\nEarliest Year:', Earliest_Year)
       Most_Recent_Year = df['Birth Year'].max()
       print('\nMost Recent Year:', Most_Recent_Year)
       M_C_Y = df['Birth Year'].value_counts().idxmax()
       print('\nMost Common Year:', M_C_Y)
    except KeyError:
       print("\n\nSorry, No data available for this month.")


       print("\nThis took %s seconds." % (time.time() - starting_t))
       print('-'*40)


def displaying(city):

    print('\nRaw data is available here\n')

    display_raw = input("more raw data? write down Yes or No\n").strip().lower()
    
    while display_raw == 'yes':
          try:
          
             for chunk in pd.read_csv(C_DATA[city], chunksize=5):
                print(chunk) 
                
                display_raw = input("you want to have a look on more raw data? write down Yes or No\n").strip().lower()
                if display_raw != 'yes':
                    print('Thank You')
                    break
             break
          except KeyboardInterrupt:
            clear()
            print('Thanks.')

def main():
    while True:
        city, month, day = filtering()
        df = load_data(city, month, day)

        timing(df)
        stationinning(df)
        duration(df)
        user_stats(df)
        displaying(city)

        restart = input('\nRestart? write down yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == '__main__':
      main()