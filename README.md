# Ticket to Anywhere

Ticket to Anywhere is a web application that allows users to book tickets for various destinations. The application uses modern web technologies for a seamless experience for both front-end and back-end operations.

## Technologies Used

### Frontend:
- **HTML** - Used to structure the web pages.
- **CSS** - Applied for styling and layout of the pages.
- **JavaScript** - Added interactivity and dynamic content.

### Backend:
- **Django** - The primary backend framework, used for handling the logic, routes, and views of the web application.

### Database:
- **Django ORM** - Integrated with relational databases such as PostgreSQL, MySQL, or SQLite to store user and ticket-related data.

### User Authentication:
- **Django Authentication System** - Provides secure user login, registration, and session management features.

### APIs:
- **RESTful APIs** - For communication between the frontend and backend or integration with third-party services.

## Features

- **User Registration**: Users can sign up with their personal details.
- **Login/Logout**: Secure user authentication for logging in and out.
- **Ticket Booking**: Book tickets to various destinations.
- **Profile Management**: Update user details and view booking history.

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Lucky-Fulara/Ticket-to-Anywhere.git
   cd Ticket-to-Anywhere
   ```

2. **Install dependencies:**

   Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

   Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the database:**

   Apply migrations to set up the database schema:

   ```bash
   python manage.py migrate
   ```

4. **Run the development server:**

   Start the development server:

   ```bash
   python manage.py runserver
   ```

   Now, open your browser and go to `http://127.0.0.1:8000/` to view the application.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -am 'Add new feature'`).
4. Push the branch (`git push origin feature/your-feature`).
5. Open a pull request.
