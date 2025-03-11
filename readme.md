# Simple IoT Application with Node.js (Express) and Google Charts

This project is a simple IoT application that uses Node.js with the Express framework to serve data and Google Charts to visualize the data.

## Features

- **Data Generation**: Simulates IoT sensor data using Python.
- **API Endpoint**: Provides an API endpoint to fetch the generated data.
- **Data Visualization**: Uses Google Charts to visualize the data in a web interface.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/VienThanh12/BasicOfIot
    cd backendIOT
    ```

2. **Install Node.js dependencies**:
    ```sh
    npm install
    ```

3. **Install Python dependencies**:
    ```sh
    pip install requests
    ```

## Usage

1. **Start the Node.js server**:
    ```sh
    node app.js
    ```

2. **Run the data generator**:
    ```sh
    python datagenerator.py
    ```

3. **Open the web interface**:
    Navigate to `http://localhost:3001` in your web browser to view the data visualization.

## File Structure

- `app.js`: Main Node.js application file.
- `datagenerator.py`: Python script to generate and send IoT data.
- `views/measurements.ejs`: EJS template for displaying the Google Chart.
- `public/`: Static files served by the Express server.

## Dependencies

- **Node.js**: JavaScript runtime environment.
- **Express**: Web framework for Node.js.
- **Google Charts**: Library for creating charts.
- **Requests**: Python HTTP library for sending requests.

## License

This project is licensed under the MIT License.