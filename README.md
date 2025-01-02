# Blog API with Django Rest Framework

This project is a **Blog API** built using **Django Rest Framework (DRF)**. It allows users to register, log in, and manage their book categories and books. Each user can only view and manage their own categories and books.

## Features

- **User Authentication**:
  - User registration
  - User login (using JSON Web Tokens - JWT)
  - User profile management
- **Category Management**:
  - Users can view their own categories.
- **Book Management**:
  - Users can view books, with category names displayed instead of IDs.

## Endpoints

### Authentication
- **Register**: `/api/register/`
- **Login**: `/api/login/`

### Profile
- **User Profile**: `/api/profile/`
  - Returns the user's categories and books.

## Installation and Setup

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- pip (Python package installer)
- virtualenv (optional but recommended)

### Steps

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the API at:
   - `http://127.0.0.1:8000/api/`

## Usage

1. **Register** a user by making a POST request to `/api/register/` with the required details (e.g., `username`, `email`, `password`).
2. **Log in** to receive a JWT token using `/api/login/`.
3. Use the token in the Authorization header (e.g., `Authorization: Bearer <token>`) for authenticated requests.
4. Access the user profile at `/api/profile/` to view categories and books.

## Project Structure

- `app/`:
  - Contains the core app with models, serializers, views, and URLs.
- `manage.py`:
  - Django's management script for running commands.



## License
This project is open-source and available under the MIT License.

## Contributions
Contributions are welcome! Please fork the repository and submit a pull request.
