from flask import Flask, render_template, request
from main import plrs,plrStats,plrFirstName,plrLastName
import subprocess

app = Flask(__name__, static_url_path='/static') 

@app.route("/")
def connect():
    return render_template('coolstuf.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
    
def display_results():
    # Execute the "helloworld.py" file to get the inputs
    process = subprocess.Popen(['python', 'helloworld.py'], stdout=subprocess.PIPE)
    output, error = process.communicate()

    # Parse the output to get the inputs
    inputs = {}
    exec(output.decode(), inputs)

    # Pass inputs to the HTML template for display
    return render_template('display_results.html', inputs=inputs)
