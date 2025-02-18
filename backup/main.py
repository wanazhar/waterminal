# main.py
import os
import datetime
from historical import fetch_historical_prices
from exporter import export_to_excel
from profile_viewer import view_company_profile

def display_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(r"""
     __      __  _______  _______  __    _  _______  ___      _______  __   __ 
    |  |    |  ||   _   ||       ||  |  | ||       ||   |    |       ||  | |  |
    |   \  /   ||  |_|  ||_     _||   |_| ||    ___||   |    |   _   ||  |_|  |
    |    \/    ||       |  |   |  |       ||   | __ |   |    |  | |  ||       |
    |  |\  /|  ||       |  |   |  |  _    ||   ||  ||   |___ |  |_|  ||       |
    |__| \/ |__||   _   |  |   |  | | |   ||   |_| ||       ||       ||   _   |
                |__| |__|  |___|  |_|  |__||_______||_______||_______||__| |__|
    """)
    print("1. Get Historical Stock Prices")
    print("2. Export Historical Data to Excel")
    print("3. View Company Profile")
    print("4. Exit")
    print("\n" + "="*60)
    print("vibecoded by wanazhar on deepthink r1. 2025".center(60))
    print("="*60)

def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            tickers = input("Enter tickers (comma-separated): ").upper().split(',')
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            fetch_historical_prices(tickers, start_date, end_date)
            
        elif choice == '2':
            tickers = input("Enter tickers (comma-separated): ").upper().split(',')
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            export_to_excel(tickers, start_date, end_date)
            
        elif choice == '3':
            ticker = input("Enter ticker: ").upper()
            view_company_profile(ticker)
            
        elif choice == '4':
            print("Exiting Waterminal...")
            break
            
        else:
            print("Invalid choice. Please try again.")
            
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()