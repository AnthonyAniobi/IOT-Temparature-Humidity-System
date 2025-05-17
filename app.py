from flask import Flask, request, render_template_string

app = Flask(__name__)

# Store the latest iot data in memory
latest_iot_data = {}

# home page for get request
@app.route('/')
def hello_world():
    return 'Hello, IOT'

# route for recieving iot data
@app.route('/', methods=['POST'])
def home():
    data = request.json
    global latest_iot_data
    latest_iot_data = request.json
    print("Data received:", data)
    return "IOT Data received", 200

@app.route('/data')
def data():
    return latest_iot_data 

@app.route('/display')
def display():
    return render_template_string("""
        <h1>Latest IOT Data</h1>
        <pre id="iot-data">Loading...</pre>
        <script>
            async function fetchData() {
                const res = await fetch("/data");
                const json = await res.json();
                document.getElementById("iot-data").textContent = JSON.stringify(json, null, 2);
            }

            // Fetch every 3 seconds
            setInterval(fetchData, 3000);
            fetchData();  // Initial fetch
        </script>
    """)


@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Webhook received:", data)
    return "Webhook received", 200

if __name__ == '__main__':
    app.run(port=8000)
