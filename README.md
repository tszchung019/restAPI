# restAPI
Python restAPI with FastAPI

# Set up
for pip and virtualenv
pip install -r requirements.txt

# Start the server
uvicorn main:app --reload

# Explore the web application
Method:
get 127.0.0.1:8000 (index.html)
Description:
- An input field to input the length of password to be generated (minimum 12 as per security best practice, otherwise, an error is returned)
- An checkbox to determine whether the password is returned as hashed password (In data transmission, it is preferred to hash the data to protect sensitive data from exposure)

Method:
get 127.0.0.1:8000/speech (index.html)
Description:
- An input field to upload a audio file (.wav) format (You can record an audio within 20 seconds)
- After clicking the "Send" button, the transcript of the audio is generated and if one of the following intents is matched, a response is generated:
    - intent (greeting) -- "Hello, nice to meet you!"
    - intent (wit/get_weather) -- "It is ${condition} in ${location}." If a location is not given in the speech, the dafault location is Sheffield (Sheffield is a nice city.)
    >> The ${condition} is retrieved from another API (https://api.weatherapi.com/v1/current.json)

Method:
post 127.0.0.1:8000/generate-password
Description:
- returns a string with the data provided in the request body in JSON
e.g. 
{
  "length":12,
  "hashing": false
}
