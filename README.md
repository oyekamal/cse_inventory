# Inventory

This is a basic Django project.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have Python and pip installed. You can download Python from [here](https://www.python.org/downloads/).

### Installation

1. **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <project_directory>
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

5. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    The project should now be running at `http://127.0.0.1:8000/`.

## Running the Tests

To run tests, execute:

```bash
python manage.py test
