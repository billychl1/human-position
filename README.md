## Human Position System

This project includes a Flask backend and a React frontend for a human position tracking system. The backend uses SQLite for data storage and provides APIs for data retrieval and heatmap generation. The frontend visualizes the data using charts and heatmaps.

### Backend (Flask)

#### Setup and Run

1. **Clone the repository:**
   ```sh
   git clone https://github.com/billychl1/human-position.git
   cd human-position/backend
   ```

2. **Create a virtual environment:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Flask application:**
   ```sh
   python app.py
   ```

The backend server runs on `http://localhost:5000` by default.

### Frontend (React)

#### Setup and Run

1. **Navigate to the frontend directory:**
   ```sh
   cd ../frontend
   ```

2. **Installation:**
   ```sh
   npx create-react-app human-data-v
   cd human-data-v
   npm install axios chart.js react-chartjs-2 heatmap.js 
   ```

3. **Update src folder:**
   Replace the auto-created src folder with Github src folder
   
4. **Start the React application:**
   ```sh
   npm start
   ```

The frontend application runs on `http://localhost:3000` by default.

### API Endpoints

#### Data Retrieval
- **Endpoint:** `/api/data`
- **Method:** `GET`
- **Parameters:**
  - `option`: Filter data by instance ID.
  - `timeframe`: Filter data by timeframe (in hours).

#### Heatmap Generation
- **Endpoint:** `/api/heatmap`
- **Method:** `GET`
- **Parameters:**
  - `timeframe`: Filter data by timeframe (in hours).

### Notes
- Ensure both backend and frontend servers are running simultaneously.
