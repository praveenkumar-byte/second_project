import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the CSV data
data = pd.read_csv('vehicle_Population.csv')

# Data Preprocessing: Convert 'County' column to strings
data['County'] = data['County'].astype(str)

# Filter the data to include only counties where there are electric vehicles (EVs)
filtered_data = data[data['Electric Vehicle (EV) Total'] > 0]

while True:
    print("Select a graph to view:")
    print("1. Histogram")
    print("2. Scatter Plot")
    print("3. Line Graph")
    # print("4. Bar Graph")
    print("4. Pie Chart")
    print("0. Exit")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        # Create a histogram
        plt.hist(filtered_data['Percent Electric Vehicles'], bins=20, color='b', alpha=0.7)
        plt.title('Histogram of Percent Electric Vehicles by County (Using EVs)')
        plt.xlabel('Percent Electric Vehicles (%)')
        plt.ylabel('Count of Counties')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    elif choice == "2":
        # Create a scatter plot
        plt.figure(figsize=(10, 6))
        # Modify this part to create your specific scatter plot
        plt.scatter(filtered_data['Battery Electric Vehicles (BEVs)'], filtered_data['Plug-In Hybrid Electric Vehicles (PHEVs)'], color='r')
        plt.title('Scatter Plot Example (Using EVs)')
        plt.xlabel('BEVs Total')
        plt.ylabel('PHEVs Total')
        plt.tight_layout()
        plt.show()
    elif choice == "3":
        # Create a line graph
        plt.figure(figsize=(10, 6))
        # Modify this part to create your specific line graph
        plt.plot(filtered_data['Date'], filtered_data['Electric Vehicle (EV) Total'], marker='o', linestyle='-', color='b')
        plt.title('Line Graph Example (Using EVs)')
        plt.xlabel('Date')
        plt.ylabel('EV Total')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    # elif choice == "4":
    #     # Create a bar graph
    #     plt.figure(figsize=(12, 6))
    #     total_electric_vehicles = filtered_data['Battery Electric Vehicles (BEVs)'] + filtered_data['Plug-In Hybrid Electric Vehicles (PHEVs)']
    #     plt.bar(filtered_data['County'], total_electric_vehicles, color='g')
    #     plt.title('Bar Graph of Total Electric Vehicles by County (Using EVs)')
    #     plt.xlabel('County')
    #     plt.ylabel('Total Electric Vehicles')
    #     plt.xticks(rotation=45)
    #     plt.tight_layout()
    #     plt.show()
    elif choice == "4":
        # Create a pie chart
        plt.figure(figsize=(8, 8))
        vehicle_use = filtered_data.groupby('Vehicle Primary Use')['Percent Electric Vehicles'].mean()
        vehicle_use.plot(kind='pie', autopct='%1.1f%%', startangle=90)
        plt.title('Pie Chart Example (Using EVs)')
        plt.ylabel('')
        plt.tight_layout()
        plt.show()
    elif choice == "0":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
