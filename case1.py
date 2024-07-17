# Function to fetch weather data from OpenWeatherMap API
def fetch_weather_data(location):
    api_key = " yU4lMZH7wc1F1qbNVFhmaGGSVuQ46rPi"
    api_url = f" https://api.tomorrow.io/v4/weather/forecast?location=42.3478,-71.0466"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

# Function to display weather data to the user
def display_weather_data(data):
    if data:
        print(f"Current Weather in {data['name']}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather Conditions: {data['weather'][0]['description']}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("Error fetching weather data.")

# Main function to handle user input and display weather data
def main():
    location = input("Enter a city name or coordinates: ")
    data = fetch_weather_data(location)
    display_weather_data(data)

# Run the main function
if __name__ == "__main__":
    main()
