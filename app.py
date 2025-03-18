from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop_output():
    # Get system information
    name = "Sandeep"
    username = os.getenv("USER") or os.getenv("USERNAME")  # Get system username
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)  # Convert to IST
    ist_time_str = ist_time.strftime("%Y-%m-%d %H:%M:%S IST")

    # Run top command
    top_output = subprocess.getoutput("top -b -n 1")

    # Create response
    response = f"""
    <h1>Name: {name}</h1>
    <h2>Username: {username}</h2>
    <h3>Server Time (IST): {ist_time_str}</h3>
    <pre>{top_output}</pre>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
