import plotly.express as px

# Sample data for ASGS regions and mean percentages of indigenous students
data = {
    'ASGS Region': ['MC', 'IR', 'OR', 'R', 'VR'],
    'Mean Percentage of Indigenous Students': [65.4, 45.8, 31.2, 22.7, 9.3]
}

# Create a DataFrame from the sample data (you can replace this with your data source)
import pandas as pd
df = pd.DataFrame(data)

# Function to get ASGS region input from the user
def get_user_input():
    while True:
        codes = input("Enter ASGS region codes (e.g., MC IR OR): ").split()
        # Check if at least two valid codes are entered
        if len(codes) >= 2 and all(code in data['ASGS Region'] for code in codes):
            return codes
        else:
            print("Invalid input. Please enter at least two valid ASGS region codes.")

# Get ASGS region input from the user
selected_regions = get_user_input()

# Filter the DataFrame based on the selected regions
filtered_df = df[df['ASGS Region'].isin(selected_regions)]
print(filtered_df)
# Create the bar plot using Plotly
fig = px.bar(
    filtered_df,
    x='ASGS Region',
    y='Mean Percentage of Indigenous Students',
    title='Mean Percentage of Indigenous Students by ASGS Region'
)

# Show the plot
if len(selected_regions) >= 2:
    fig.show()
else:
    print("Two or more valid ASGS region codes are required to create the plot.")
