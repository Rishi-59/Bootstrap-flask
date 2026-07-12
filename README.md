# Day 61 - WTForms

A Flask application demonstrating form handling and validation using **WTForms** and **Flask-WTF**.

## Overview

This project is part of the #100DaysOfCode challenge (Day 61). It showcases how to build secure web forms with built-in validation using Flask, WTForms, and Bootstrap for responsive UI design.

## Features

- **Form Validation**: Email and password validation using WTForms validators
- **CSRF Protection**: Integrated CSRF token protection via Flask-WTF
- **Responsive UI**: Bootstrap 4 styling for mobile-friendly design
- **Login System**: Demo login with hardcoded credentials for testing
- **Custom Validators**: Support for custom validation logic

## Project Structure

```
├── main.py              # Flask application and form definitions
├── requirements.txt     # Project dependencies
├── pyproject.toml       # Project metadata and configuration
├── templates/           # HTML templates
│   ├── base.html        # Base template with Bootstrap layout
│   ├── index.html       # Home page
│   ├── login.html       # Login form page
│   ├── success.html     # Success page (after valid login)
│   └── denied.html      # Denied page (after invalid login)
└── README.md           # This file
```

## Installation

### Prerequisites

- Python 3.12 or higher
- pip or UV package manager

### Setup Instructions

1. **Clone or navigate to the project directory**:
   ```bash
   cd "Day 61 - WTForms"
   ```

2. **Install dependencies**:
   
   On macOS/Linux:
   ```bash
   pip3 install -r requirements.txt
   ```
   
   On Windows:
   ```bash
   python -m pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```

4. **Access the application**:
   Open your browser and navigate to `http://localhost:5000`

## Usage

### Pages

- **Home Page** (`/`): Landing page with link to login
- **Login Page** (`/login`): Form for entering email and password
- **Success Page**: Displayed on successful login
- **Denied Page**: Displayed on failed login

### Test Credentials

- **Email**: `admin@email.com`
- **Password**: `12345678`

## Form Validation

The application uses WTForms with the following validators:

### Email Field
- **Required**: Must be filled
- **Email Format**: Must be a valid email address (contains @ and .)

### Password Field
- **Required**: Must be filled
- **Minimum Length**: At least 8 characters

### Custom Validators

The project includes commented-out code for custom email validation. You can uncomment and use it if needed:

```python
def validate_email():
    def _validate_email(form, field):
        if '@' not in field.data or '.' not in field.data:
            raise ValidationError('Please enter a valid email address')
    return _validate_email
```

## Technologies Used

- **Flask**: Web framework
- **Flask-WTF**: CSRF protection for Flask
- **WTForms**: Form handling and validation library
- **Flask-Bootstrap**: Bootstrap integration for Flask
- **Werkzeug**: WSGI utility library

## Dependencies

See `requirements.txt` for the complete list:
- bootstrap-flask==2.2.0
- flask==2.3.2
- flask-wtf==1.2.1
- wtforms==3.0.1
- werkzeug==3.0.0
- And other supporting packages

## Key Concepts Demonstrated

1. **Form Creation**: Building forms with WTForms
2. **Validation**: Built-in and custom validators
3. **CSRF Protection**: Securing forms against CSRF attacks
4. **Template Inheritance**: Using Jinja2 templates with Bootstrap
5. **HTTP Methods**: Handling GET and POST requests

## Security Notes

⚠️ **Important**: This is a demo application. In production:
- Use a proper authentication system (e.g., Flask-Login)
- Hash passwords with bcrypt or similar
- Store credentials in a database, not hardcoded
- Use environment variables for sensitive data
- Implement proper session management

## Future Enhancements

- Add database integration for user storage
- Implement user registration
- Add password hashing with bcrypt
- Create password reset functionality
- Add user authentication with Flask-Login
- Implement email verification

## Author

Created as part of the #100DaysOfCode challenge.

## License

This project is open source and available for educational purposes.
