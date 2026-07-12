# 🏋️ Workout Tracker

A simple Workout Tracker built using Python that records daily exercises and stores them in a Google Sheet using the Nutritionix and Sheety APIs.

Built as part of the **100 Days of Code: The Complete Python Pro Bootcamp**.

## ✨ Features

- Accepts exercise details in natural language.
- Calculates exercise duration and calories burned.
- Records workout data in a Google Sheet.
- Automatically stores the date and time of each workout.

## 🛠️ Technologies Used

- Python
- Requests
- Nutritionix API
- Sheety API
- Datetime

## 📁 Project Structure

```text
Workout-Tracker/
│── main.py
│── README.md
│── .gitignore
```

## ▶️ How to Run

1. Clone the repository.

```bash
git clone https://github.com/Prathammunot73/Workout-Tracker.git
```

2. Install the required package.

```bash
pip install requests
```

3. Replace the placeholders in `main.py` with your own:

- Nutritionix App ID
- Nutritionix API Key
- Sheety Endpoint

4. Run the project.

```bash
python main.py
```

## 📚 What I Learned

- Working with REST APIs
- Sending HTTP POST requests using the Requests library
- Parsing JSON responses
- Working with dates and times using the `datetime` module
- Automating data entry into Google Sheets
- Using API authentication with request headers
