# PERSONAL BUDGET TRACKER

#### VIDEO DEMO: https://www.youtube.com/watch?v=QWoLzGsDOJ4

### Description:

The Personal Budget Tracker is a simple Python application that helps users manage their personal finances by tracking expenses across various categories. It allows users to add expenses, view total expenditures, and filter expenses by specific categories, making it easier to monitor and control spending habits.

### Features

- **Add Expense**: Easily add an expense by entering the amount and selecting a category.
- **View Total Expenses**: Quickly see the total amount of money spent across all expenses.
- **Filter by Category**: Filter and view expenses based on specific categories, such as 'Food', 'Transport', etc.

### Project Structure

1. **project.py**:

This is the main Python script where the core functionality of your budget tracker is implemented.

2. **test_project.py**:

This is the test script for your project.
It contains test functions that are prefixed with test_ (e.g., test_add_expense, test_get_total_expenses, test_get_expenses_by_category).


## Implementation Details

### `project.py`

#### `add_expense(expenses, amount, category)`
- **Purpose**: Adds an expense to the list.
- **Parameters**:
  - `expenses` (list): List of expenses.
  - `amount` (float): Amount of the expense.
  - `category` (str): Category of the expense.
- **Returns**: None (modifies the `expenses` list in place).

#### `get_total_expenses(expenses)`
- **Purpose**: Calculates the total amount of all expenses.
- **Parameters**:
  - `expenses` (list): List of expenses.
- **Returns**: Total amount (float).

#### `get_expenses_by_category(expenses, category)`
- **Purpose**: Filters expenses by a specified category.
- **Parameters**:
  - `expenses` (list): List of expenses.
  - `category` (str): Category to filter by.
- **Returns**: List of expenses that match the category.

#### `main()`
- **Purpose**: Provides a user interface to interact with the budget tracker.
- **Functionality**:
  - Allows users to add expenses, view total expenses, or filter expenses by category.
  - Continues running until the user chooses to exit.

## Installation

### Prerequisites
- Python 3.x
- `pip` (Python package installer)

### Steps
1. Clone the repository or download the project files.

2. Navigate to the project directory:
   ```bash
   cd path/to/budget_tracker
   ```

3. (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   ```
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1.To start the budget tracker application, run:
   ```bash
   python project.py
   ```
2.To run the tests using pytest, execute:
   ```bash
   pytest
   ```
