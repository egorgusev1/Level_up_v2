# LevelUp Project (CSC430)

![Screenshot of the frontpage.](level_up/images/front_page.png)

LevelUp is a web application designed for students and faculty to explore available internships and job opportunities. The platform offers user authentication features, including sign-in and sign-up options, facilitating a seamless experience for users seeking career advancement resources.

## Features
* **User Authentication**: Secure sign-in and sign-up functionalities for students and faculty members.
* **Internship & Job Listings**: Access to a curated list of available internships and job opportunities.
* **User-Friendly Interface**: An intuitive design ensuring easy navigation and usability.

## Technologies Used
The project leverages a combination of technologies to deliver its features:
* **Frontend**
  * HTML
  * TailwindCSS
* **Backend**
  * Python
  * AlpineJS
* **Frameworks**
  * Django
* **Others**
  * Docker/Docker Compose
## Dependencies

### Runtime Dependencies
   * django (>=5.2,<6.0): Provides the core framework for building the web application.
   * django-allauth[socialaccount] (>=65.7.0,<66.0.0): Handles user authentication, registration, and social account integration.
   * psycopg[binary] (>=3.2.8,<4.0.0): Enables PostgreSQL database connectivity with binary support.
   * dj-database-url (>=2.3.0,<3.0.0): Parses database URLs for easy configuration.
   * django-widget-tweaks (>=1.5.0,<2.0.0): Enhances form field rendering in Django templates.
   * django-anymail[mailgun] (>=13.0,<14.0): Integrates Mailgun for sending emails.
   * gunicorn (>=23.0.0,<24.0.0): Serves the Django application in a production environment.
   * whitenoise[brotli] (>=6.9.0,<7.0.0): Serves static files with Brotli compression support.

### Development Dependencies
   * django-debug-toolbar (^5.1.0): Provides debugging tools for Django development.
   * django-browser-reload (^1.18.0): Automatically reloads the browser during development.
   * pytest (^8.3.5): Runs and manages test suites.
   * pytest-django (^4.11.1): Integrates pytest with Django for testing.
   * playwright (^1.52.0): Automates browser interactions for end-to-end testing.
   * pytest-playwright (^0.7.0): Integrates Playwright with pytest for browser testing.
 
## Getting Started
To set up and run the project locally, follow these steps:

**1. Clone the Repository:**

`git clone https://github.com/egorgusev1/LevelUp_project_csc430.git`

**2. Navigate to the Project Directory:**

`cd LevelUp_project_csc430`

**3. Build and run the project in Docker Compose**

`docker compose up --build`

**4. Access the Application**

Open your browser and navigate to http://localhost:8000

## Testing

Run tests using pytest, make sure docker compose is running:
`docker compose exec web poetry run pytest`

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please fork the repository and submit a pull request. For major changes, kindly open an issue first to discuss the proposed changes.

## Acknowledgments

Developed as part of the CSC430 course project by:

* Egor
* Owen
* Matteo


