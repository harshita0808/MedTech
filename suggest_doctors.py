import pymongo
import googlemaps

class Doctor:
    def __init__(self, name, specialty, address):
        self.name = name
        self.specialty = specialty
        self.address = address

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["doctor_db"]
doctors_collection = db["doctors"]

# Sample data of doctors with addresses
doctors_data = [

    # Add more doctors and addresses as needed
]

# Insert sample data into MongoDB
doctors_collection.insert_many(doctors_data)

def get_nearby_doctors(location, problem):
    recommended_doctors = []
    
    # Initialize Google Maps client with your API key
    gmaps = googlemaps.Client(key='YOUR_API_KEY')

    # Geocode the user's location to get latitude and longitude
    geocode_result = gmaps.geocode(location)

    if geocode_result:
        user_lat = geocode_result[0]['geometry']['location']['lat']
        user_lng = geocode_result[0]['geometry']['location']['lng']

        # Query MongoDB for doctors near the user's location
        for doctor in doctors_collection.find():
            doctor_address = doctor["address"]
            doctor_geocode_result = gmaps.geocode(doctor_address)

            if doctor_geocode_result:
                doctor_lat = doctor_geocode_result[0]['geometry']['location']['lat']
                doctor_lng = doctor_geocode_result[0]['geometry']['location']['lng']

                # Calculate distance using Haversine formula (you can use a library for this)
                # For simplicity, we'll use a placeholder distance here
                distance = 10  # Placeholder distance in miles

                if distance <= 10:  # Adjust the distance threshold as needed
                    if problem.lower() in doctor["specialty"].lower():
                        recommended_doctors.append(doctor["name"])

    return recommended_doctors

# Main program
if __name__ == "__main__":
    user_location = input("Enter your location (e.g., City, State): ")
    user_problem = input("Enter your medical problem: ")
    
    nearby_doctors = get_nearby_doctors(user_location, user_problem)
    
    if nearby_doctors:
        print("Recommended nearby doctors for your problem:")
        for doctor in nearby_doctors:
            print(doctor)
    else:
        print("No nearby doctors found for your problem. Please consult a general practitioner.")
