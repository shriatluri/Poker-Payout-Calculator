# Poker Game Optimization App

This is a Flask-based web application for managing and optimizing poker game sessions. It allows players to input their buy-in amounts, track their final amounts, and calculate optimal payouts. The application also supports adding, editing, and removing buy-in amounts.

## Features

- Add new players with buy-in amounts
- Edit players' buy-in amounts
- Add and remove default buy-in amounts
- Calculate and display optimal payouts
- Download player information as an Excel file
- Responsive and user-friendly interface

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure you have the following installed on your local machine:

- Python 3.6+
- pip (Python package installer)
- Git

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/poker-game-optimization.git
    cd poker-game-optimization
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. **Set up environment variables:**

    Create a `.env` file in the root directory of your project and add the following:

    ```plaintext
    FLASK_APP=app.py
    FLASK_ENV=development
    SECRET_KEY=your_secret_key
    ```

2. **Run the application:**

    ```bash
    flask run
    ```

3. **Open your browser and navigate to:**

    ```
    http://127.0.0.1:5000
    ```

### Usage

1. **Add a Player:**

    - Enter the player's name and buy-in amount, then click "Add Player".

2. **Edit a Player's Buy-In Amount:**

    - Click the "Edit" button next to the player's name.
    - Enter the new buy-in amount and click "Save".

3. **Add Default Buy-In Amount:**

    - Click the "Add Default Buy-In" button next to the player's name.

4. **Remove Default Buy-In Amount:**

    - Click the "Remove Default Buy-In" button next to the player's name.

5. **Set Default Buy-In Amount:**

    - Enter a new default buy-in amount and click "Set Default Buy-In".

6. **Finalize Game:**

    - Enter the end amounts for each player.
    - Click "Finalize" to calculate and display the optimal payouts.

7. **Download Player Information:**

    - Click "Download Player Information" to download the data as an Excel file.

### Deployment

To deploy this application to Heroku, follow these steps:

1. **Log in to Heroku:**

    ```bash
    heroku login
    ```

2. **Create a new Heroku app:**

    ```bash
    heroku create your-app-name
    ```

3. **Add the Heroku remote:**

    ```bash
    git remote add heroku https://git.heroku.com/your-app-name.git
    ```

4. **Deploy the application:**

    ```bash
    git push heroku main
    ```

5. **Open your application in the browser:**

    ```bash
    heroku open
    ```

### File Structure

```plaintext
poker-game-optimization/
├── app.py
├── requirements.txt
├── Procfile
├── runtime.txt (optional)
├── static/
│   └── styles.css
└── templates/
    ├── index.html
    └── results.html
```

### Built With

- [Flask](https://flask.palletsprojects.com/) - Web framework for Python
- [Pandas](https://pandas.pydata.org/) - Data analysis and manipulation library
- [Gunicorn](https://gunicorn.org/) - Python WSGI HTTP Server for UNIX

### Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or enhancements.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
