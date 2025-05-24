# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview
Django CMS with Jinja2 templates and Tailwind CSS v4, following Brad Frost's Atomic Design pattern. The project includes a landing page for Tina Kylau's Happy Leadership coaching business and a blog/pages system.

## Development Commands

### Python/Django (using Poetry)
```bash
# Install dependencies
poetry install

# Run development server
poetry run python manage.py runserver

# Database migrations
poetry run python manage.py makemigrations
poetry run python manage.py migrate

# Create superuser
poetry run python manage.py createsuperuser

# Run tests
poetry run pytest
poetry run pytest -v  # verbose
poetry run pytest -k test_name  # run specific test

# Code quality
poetry run black .  # format code
poetry run flake8  # lint code
poetry run isort .  # sort imports

# Django shell
poetry run python manage.py shell
```

### CSS/Frontend (using npm)
```bash
# Install dependencies
npm install

# Build CSS (Tailwind)
npm run build-css  # one-time build
npm run dev        # watch mode for development

# The CSS pipeline: static/css/main.css → PostCSS/Tailwind → static/css/output.css
```

## Architecture

### Django Apps
- **pages**: Content management system with Page, Category, Tag models. Landing page at `/`, blog at `/blog/`
- **contact**: Contact form with JavaScript validation, rate limiting, and email notifications

### Template System
- Uses **Jinja2** (not Django templates) configured in `cms_project/jinja2.py`
- Custom filters: `date`, `truncate`, `default`
- Global functions: `static()`, `url()`, `now()`
- Templates follow Atomic Design:
  - `templates/atoms/`: Basic UI elements
  - `templates/molecules/`: Component groups (page-card, pagination, form fields)
  - `templates/organisms/`: Complex sections (header, footer, hero sections)
  - `pages/jinja2/pages/`: Page-specific templates
  - `contact/jinja2/contact/`: Contact form templates

### CSS Architecture
- Tailwind CSS v4 with PostCSS
- Atomic Design structure in `static/css/`:
  - `main.css`: Entry point with Tailwind imports and custom brand colors
  - Organized by atoms → molecules → organisms → templates → pages
- Brand colors defined for Tina Kylau theme

### Key Configuration Files
- `cms_project/settings.py`: Django settings with Jinja2 configuration
- `cms_project/jinja2.py`: Jinja2 environment setup with custom filters
- `tailwind.config.js`: Tailwind content paths
- `postcss.config.js`: PostCSS plugins configuration

### JavaScript
- Contact form validation in `static/js/contact-validation.js`
- Real-time field validation with visual feedback
- AJAX form submission with CSRF token handling

## Important Notes
- Always use Poetry for Python dependencies
- CSS changes require rebuild: `npm run build-css`
- Jinja2 syntax differs from Django templates (e.g., `{{ url('name') }}` not `{% url 'name' %}`)
- The landing page uses a separate base template (`base-landing.html`) with custom styling
- Contact form has rate limiting (5 submissions per hour per IP)