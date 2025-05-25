# Django Simple CMS

A modern Content Management System built with Django, Django templates, and Tailwind CSS, following Brad Frost's Atomic Design pattern. Features a professional landing page and blog system with a contact form that includes real-time JavaScript validation.

## 🚀 Features

- **Landing Page**: Professional coaching business homepage with German content
- **Blog/Pages System**: Full-featured CMS with categories and tags
- **Contact Form**: Advanced form with real-time validation and rate limiting
- **Atomic Design Pattern**: Organized component architecture
- **Django Templates**: Standard Django templating system
- **Tailwind CSS v4**: Modern utility-first CSS framework
- **Responsive Design**: Mobile-first approach with smooth animations
- **Admin Interface**: Django admin for content management

## 📦 Project Structure

### Django Apps

#### Pages App
The `pages` app provides the core CMS functionality:
- **Models**: Page, Category, and Tag
- **Features**:
  - SEO-friendly URLs with automatic slug generation
  - Published/draft status for pages
  - Category and tag organization
  - Related pages functionality
  - Full-text search across pages
- **Views**:
  - Landing page (root URL)
  - Blog listing with pagination
  - Category and tag filtering
  - Search functionality

#### Contact App
The `contact` app handles form submissions:
- **Features**:
  - Real-time JavaScript field validation
  - Visual feedback (green for valid, red for invalid)
  - Rate limiting (5 submissions per hour per IP)
  - Email notifications (optional)
  - Spam protection with honeypot field
  - AJAX submission with fallback

### Atomic Design Pattern

The project follows Brad Frost's Atomic Design methodology:

```
templates/                  # Global templates
├── atoms/                  # Basic UI elements (buttons, headings)
├── molecules/              # Simple components (cards, form fields, search boxes)
├── organisms/              # Complex sections (header, footer, hero sections)
├── base.html              # Main base template
└── base-landing.html      # Landing page base template

pages/templates/pages/      # Pages app templates
├── landing.html           # Homepage/landing page
├── home.html              # Blog listing page
├── detail.html            # Individual page detail
├── category.html          # Category listing
├── tag.html               # Tag listing
└── search.html            # Search results

contact/templates/contact/  # Contact app templates
├── contact.html           # Contact form page
└── success.html           # Success message page

static/css/                 # CSS following Atomic Design
├── atoms/                  # Basic element styles
├── molecules/              # Component styles
├── organisms/              # Section styles
├── templates/              # Layout styles
├── pages/                  # Page-specific styles
└── main.css               # Main CSS entry point
```

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.11+
- Node.js 16+
- Poetry (Python package manager)
- npm (comes with Node.js)

### Step 1: Clone the Repository

```bash
git clone https://github.com/sostrowsk/django-simple-cms.git
cd django-simple-cms
```

### Step 2: Set Up Python Environment with Poetry

```bash
# Install Poetry if you haven't already
curl -sSL https://install.python-poetry.org | python3 -

# Install Python dependencies
poetry install

# Activate the virtual environment
poetry shell
```

### Step 3: Set Up the Database

```bash
# Run migrations
poetry run python manage.py migrate

# Create a superuser for admin access
poetry run python manage.py createsuperuser
```

### Step 4: Install Frontend Dependencies

```bash
# Install npm packages
npm install
```

### Step 5: Build CSS

```bash
# Build Tailwind CSS
npm run build-css

# Or run in watch mode for development
npm run dev
```

### Step 6: Run the Development Server

```bash
# Start Django server
poetry run python manage.py runserver
```

Visit `http://127.0.0.1:8000` to see the landing page.

## 🎨 Customization

### Adding Content

1. Go to `http://127.0.0.1:8000/admin`
2. Log in with your superuser credentials
3. Create categories and pages
4. Pages with slugs like 'angebot', 'about', 'impressum' will be linked from navigation

### Customizing the Landing Page

Edit the template files in:
- `templates/organisms/` - Individual sections (header, footer, hero, etc.)
- `pages/templates/pages/landing.html` - Main landing page structure
- `static/css/main.css` - Custom styles and brand colors

The templates use Django's template language with:
- `{% load static %}` - Load static files
- `{% static 'path/to/file' %}` - Reference static files
- `{% url 'app:view_name' %}` - Generate URLs
- `{% include 'template.html' %}` - Include other templates
- `{{ variable|filter }}` - Apply filters to variables

### Brand Colors

The project uses a custom color scheme:
- Primary: `#874645`
- Secondary: `#857074`
- Accent: `#CB9B9A`
- Dark: `#3D4752`
- Light backgrounds: `#ECE5DF`

## 📝 Development

### Running Tests

```bash
poetry run pytest
poetry run pytest -v  # verbose output
poetry run pytest -k test_name  # run specific test
```

### Code Quality

```bash
poetry run black .      # Format code
poetry run flake8       # Lint code
poetry run isort .      # Sort imports
```

### CSS Development

When making CSS changes:
1. Edit files in `static/css/`
2. Run `npm run build-css` to compile
3. Or use `npm run dev` for automatic rebuilding

### Adding New Templates

Follow the Atomic Design pattern:
1. Create atoms for basic elements
2. Combine atoms into molecules
3. Build organisms from molecules
4. Use organisms in page templates

Django template tips:
- Always add `{% load static %}` at the top when using static files
- Use `{% csrf_token %}` in forms
- Template inheritance: `{% extends 'base.html' %}`
- Block content: `{% block content %}...{% endblock %}`
- Context variables are automatically available from views

## 🌐 Deployment

For production deployment:

1. Set `DEBUG = False` in settings
2. Configure `ALLOWED_HOSTS`
3. Set up proper `SECRET_KEY`
4. Configure email settings for contact form
5. Run `poetry run python manage.py collectstatic`
6. Use a production server like Gunicorn with Nginx

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🆘 Support

For issues and questions:
- Open an issue on GitHub
- Check existing issues for solutions
- Ensure you've followed all setup steps

## 🏗️ Built With

- [Django](https://www.djangoproject.com/) - The web framework
- [Tailwind CSS](https://tailwindcss.com/) - CSS framework
- [Poetry](https://python-poetry.org/) - Python dependency management
- [PostCSS](https://postcss.org/) - CSS processing