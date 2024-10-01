# Personal Blog

A personal blog web application built with Flask that allows you to write, publish, and manage articles. The application is divided into two main sections: a guest section for public viewing and an admin section for content management.

## Features

### Guest Section
- View a list of published articles on the home page
- Read individual articles in detail
- Responsive design for optimal viewing on various devices

### Admin Section
- Secure login system
- Dashboard to manage articles
- Create new articles
- Edit existing articles
- Delete articles
- Logout functionality

## Technical Details

### Backend
- Built with Flask, a lightweight WSGI web application framework in Python
- Uses JSON files to store article data
- Implements session-based authentication for admin access

### Frontend
- HTML templates using Jinja2 templating engine
- CSS for styling, with a focus on a clean and readable design
- Responsive layout for mobile and desktop viewing

### File Structure
- `app.py`: Main application file containing route definitions and core logic
- `templates/`: Directory containing HTML templates
- `static/`: Directory for static assets like CSS files
- `articles/`: Directory to store article data as JSON files

### Key Components
- `load_articles()`: Function to load and sort articles from JSON files
- `login_required`: Decorator to protect admin routes
- CRUD operations for articles (Create, Read, Update, Delete)

## Setup and Running
1. Ensure Python and Flask are installed
2. Clone the repository
3. Navigate to the project directory
4. Run `flask run` to start the development server
5. Access the blog at `http://localhost:5000`

## Security Note
The current implementation uses a hardcoded username and password for admin access. In a production environment, this should be replaced with a more secure authentication system.

## Future Improvements
- Implement a database for better data management
- Add user registration and multiple user support
- Implement a rich text editor for article creation and editing
- Add categories and tags for articles
- Implement a search functionality

src: https://roadmap.sh/projects/personal-blog