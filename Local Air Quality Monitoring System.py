# Local Air Quality Monitoring System
# Beginner-friendly (Fresher level)

# Function to classify air quality based on AQI value
def classify_aqi(aqi):
    if aqi <= 50:
        return "Good – Air quality is pretty decent."
    elif aqi <= 100:
        return "Moderate – Acceptable but some  sensitive people might get affected by the pollutants."
    elif aqi <= 200:
        return "Poor – Breathing discomfort for people with health issues."
    elif aqi <= 300:
        return "Very Poor –  Everyone faces breathing problems when outside."
    else:
        return "Severe –  Even healthy people face respiratory issues and lung diseases."

# Function to give suggestions
def suggestions(aqi):
    if aqi <= 100:
        return "No major precautions needed as such."
    elif aqi <= 200:
        return "Wear a mask if outdoors."
    elif aqi <= 300:
        return "Avoid outdoor activities and keep doors and windows closed."
    else:
        return "Prefer to stay indoors and use air purifiers if available."

# Main program loop
print("------ Local Air Quality Monitoring System ------")

city = input("Enter your city name: ")
aqi = int(input("Enter the AQI value (Air Quality Index): "))

status = classify_aqi(aqi)
advice = suggestions(aqi)

print("\n--- Air Quality Report ---")
print("City:", city)
print("AQI :", aqi)
print("Status:", status)
print("Health Advice:", advice)

# Save report to a file
with open("air_quality_report.txt", "w") as file:
    file.write("Air Quality Report\n")
    file.write(f"City: {city}\n")
    file.write(f"AQI : {aqi}\n")
    file.write(f"Status: {status}\n")
    file.write(f"Health Advice: {advice}\n")


print("\nReport saved as 'air_quality_report.txt'")

