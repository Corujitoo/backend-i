# Expense Manager CLI 💰

A simple command-line interface (CLI) system for managing financial income and expenses, developed in Python using the **Typer** library.

## 🚀 How to Run

### Prerequisites
1. Install `uv`:
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
2. Create environment: `uv venv`
3. Activate it: `.venv\Scripts\activate`
4. Install dependencies: `uv pip install typer`


💰 Expense Manager CLI
📝 Problem Description
It is often difficult to maintain strict control over small daily financial inflows and outflows without a simple and immediate tool. This application solves the problem of the lack of organized transaction tracking by allowing the user to quickly record income and expenses via the terminal. The system ensures data persistence in a JSON file, preventing the loss of information when closing the program and allowing future analysis of financial history with exact date and time.



## 🚀 How to Run


Installation and Dependencies
This project uses uv, the fastest package manager in the Python ecosystem. Follow these steps to set up the environment from scratch:

1. Install uv. In the terminal type the command: powershell -c "irm https://astral.sh/uv/install.ps1 | iex" 
2. Inside the root folder (ProjetoCLI) type the command in the terminal: uv venv
3. Now we will activate the Virtual Environment so our project can run: In the terminal type: .venv\Scripts\activate 
4. With the virtual environment active, install the Typer interface library by typing the following command in the terminal: uv pip install typer 



💻 How to Use (Commands)
To use the application, navigate to the source code folder (src) and start the interactive menu:
1. In the terminal type: cd src (this will open the folder that contains all the program logic and intelligence (The Brain 🧠))
2. Then type the following command: python main.py menu 


Examples of Use inside the Menu:
Option 1 (Add money): Enter the amount (e.g., 100.50) and the description (e.g., Salary). The system will save it as "income".

Option 2 (Register an expense): Enter the amount (e.g., 15.00) and the description (e.g., Lunch). The system will save it as "expense".

Option 3 (View balance): Shows the current calculation based on the operations performed during the session.

Option 4 (Exit): Safely closes the application.