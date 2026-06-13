from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import subprocess
import platform
import webbrowser
from datetime import datetime

# Initialize the Flask app and enable CORS
app = Flask(__name__)
CORS(app)

# Define the API endpoint that will process commands
@app.route('/process-command', methods=['POST'])
def process_command():
    data = request.get_json()
    command = data.get('command', '').lower()

    response_message = ""
    print(f"✅ Received command: {command}")

    # --- Command Processing Logic ---
    if "open notepad" in command or "open text editor" in command:
        response_message = "Opening the text editor."
        try:
            if platform.system() == "Windows":
                os.system("start notepad")
            elif platform.system() == "Darwin":  # macOS
                subprocess.run(["open", "-a", "TextEdit"])
            else:  # Linux
                subprocess.run(["xdg-open", "gedit"])
        except Exception as e:
            response_message = f"Error opening text editor: {e}"

    elif "open chrome" in command:
        response_message = "Opening Google Chrome."
        webbrowser.open("https://www.google.com")

    elif "what is the time" in command:
        now = datetime.now()
        current_time = now.strftime("%I:%M %p")
        response_message = f"The current time is {current_time}."

    else:
        response_message = "Sorry, I don't know that command."
    
    # Return the response to the webpage
    return jsonify({'message': response_message})

# Run the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)