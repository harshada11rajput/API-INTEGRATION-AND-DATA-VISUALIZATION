import requests
import matplotlib.pyplot as plt

# Ask user for student_input of interest
student_input = input("What are you interested in (Science, Arts, Commerce)? ")

# Suggest courses based on field
if student_input.lower() == "science":
    courses = ["Mechanical Engineering", "Civil Engineering","MBBS","etc"]
elif student_input.lower() == "arts":
    courses = ["Graphic Design", "Fine Arts", "Music","etc"]
elif student_input.lower() == "commerce":
    courses = ["Bcom","BBA","etc"]
else:
    print("something went wrong")

print("some course suggestions for you:")
for course in courses:
    print(course)

# Fetch the university data from API
url = "http://universities.hipolabs.com/search"
params = {
    "country": "India"
}

try:
    response = requests.get(url, params=params)
    universities = response.json()

    university_names = [uni["name"] for uni in universities[:5]]
    print("\nHere are some universities:")
    for university in university_names:
        print(university)

    # Create a bar chart
    plt.bar(university_names, [2]*len(university_names))
    plt.xlabel("University")
    plt.ylabel("Number of Suggestions")
    plt.title("University Suggestions")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f"An error occurred: {e}")
