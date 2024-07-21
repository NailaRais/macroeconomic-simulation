Macroeconomic Simulation

This is a web-based application for simulating a macroeconomic model, designed to be deployed on Heroku. The application allows users to interact with a graphical representation of the model and input data to perform simulations.

Features

- Visual representation of the macroeconomic model.
- User-friendly interface for uploading data and running simulations.
- Deployment-ready for Heroku.

Project Structure

- `app.py`: The Flask application script.
- `templates/index.html`: The HTML template for the web interface.
- `requirements.txt`: The list of required Python packages.
- `Procfile`: The configuration file for Heroku.

## Setup

### Prerequisites

- Python 3.7 or higher
- Flask
- Heroku CLI

### Installation

1. Clone the repository or download the ZIP file and extract it.
2. Navigate to the project directory in your terminal.

### Running Locally

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask application:
   ```bash
   python app.py
   ```

### Deploying to Heroku

1. Log in to Heroku:
   ```bash
   heroku login
   ```
2. Create a new Heroku app:
   ```bash
   heroku create your-app-name
   ```
3. Initialize a Git repository and commit the code:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```
4. Set the Heroku remote:
   ```bash
   heroku git:remote -a your-app-name
   ```
5. Push the code to Heroku:
   ```bash
   git push heroku master
   ```

6. Open the application in your browser:
   ```bash
   heroku open
   ```

## Usage

- Open the application in your web browser.
- Upload your data file using the provided interface.
- Run the simulation and view the results.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
```

Download Updated ZIP with README

I have included the `README.md` file in the project directory and created a new ZIP file for you:

[Download macroeconomic_simulation_with_readme.zip](sandbox:/mnt/data/macroeconomic_simulation_with_readme.zip)

This ZIP file includes the `README.md` file along with the rest of the project files. You can proceed with the deployment as described.
