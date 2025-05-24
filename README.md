# Django CMS Project TODO

## Project Overview
Build a simple Content Management System using Django with Jinja2 templates, locally served Tailwind CSS, and Brad Frost's Atomic Design pattern for custom CSS organization.

## Setup Tasks

### 1. Project Initialization
- [ ] Create Django project: `django-admin startproject cms_project .`
- [ ] Create pages app: `python manage.py startapp pages`
- [ ] Create contact app: `python manage.py startapp contact`
- [ ] Add 'pages' and 'contact' to INSTALLED_APPS in settings.py
- [ ] Run initial migrations: `python manage.py migrate`
- [ ] Create superuser: `python manage.py createsuperuser`

### 2. Configure Jinja2 Templates
- [ ] Install Jinja2: `pip install Jinja2`
- [ ] Configure Jinja2 in settings.py TEMPLATES setting
- [ ] Create jinja2.py configuration file for environment setup
- [ ] Set up template directories structure

### 3. Setup Tailwind CSS (Local)
- [ ] Download Tailwind CSS standalone CLI
- [ ] Create input.css file with Tailwind directives
- [ ] Configure tailwind.config.js
- [ ] Set up build process for CSS compilation
- [ ] Create npm scripts or Makefile for CSS building
- [ ] Configure Django static files to serve compiled CSS

### 4. Implement Atomic Design Pattern
- [ ] Create CSS directory structure:
  ```
  static/css/
  ├── atoms/
  │   ├── _buttons.css
  │   ├── _typography.css
  │   └── _forms.css
  ├── molecules/
  │   ├── _cards.css
  │   ├── _navigation.css
  │   ├── _search.css
  │   └── _form-fields.css
  ├── organisms/
  │   ├── _header.css
  │   ├── _footer.css
  │   └── _sidebar.css
  ├── templates/
  │   ├── _page-layouts.css
  │   └── _grid.css
  └── pages/
      ├── _home.css
      ├── _article.css
      └── _contact.css
  ```
- [ ] Create main.css to import all partials
- [ ] Set up CSS compilation workflow

## Pages App Development

### 5. Models
- [ ] Create Page model with fields:
  - title (CharField)
  - slug (SlugField)
  - content (TextField)
  - meta_description (TextField)
  - is_published (BooleanField)
  - created_at (DateTimeField)
  - updated_at (DateTimeField)
  - author (ForeignKey to User)
- [ ] Create Category model
- [ ] Create Tag model
- [ ] Run migrations

### 6. Admin Interface
- [ ] Register models in admin.py
- [ ] Customize admin interface with:
  - List display options
  - Search fields
  - Filters
  - Prepopulated slug field
  - Rich text editor for content

### 7. Views
- [ ] Create PageListView (homepage)
- [ ] Create PageDetailView
- [ ] Create CategoryListView
- [ ] Create TagListView
- [ ] Add pagination to list views
- [ ] Implement search functionality

### 8. URLs
- [ ] Configure main urls.py to include pages URLs
- [ ] Create pages/urls.py with patterns:
  - / (homepage)
  - /page/<slug>/ (page detail)
  - /category/<slug>/ (category pages)
  - /tag/<slug>/ (tag pages)
  - /search/ (search results)

### 9. Templates (Jinja2)
- [ ] Create base template structure following Atomic Design:
  ```
  templates/
  ├── base.html
  ├── atoms/
  │   ├── button.html
  │   └── heading.html
  ├── molecules/
  │   ├── card.html
  │   ├── pagination.html
  │   ├── search-form.html
  │   └── form-field.html
  ├── organisms/
  │   ├── header.html
  │   ├── footer.html
  │   └── sidebar.html
  ├── templates/
  │   └── default-layout.html
  └── pages/
      ├── home.html
      ├── detail.html
      ├── category.html
      ├── search.html
      └── contact.html
  ```
- [ ] Implement responsive design with Tailwind classes
- [ ] Add meta tags for SEO

### 10. Static Files & Assets
- [ ] Configure STATIC_URL and STATICFILES_DIRS
- [ ] Set up media files handling for uploads
- [ ] Create favicon and site logo
- [ ] Optimize images

## Contact Form App Development

### 11. Contact Models
- [ ] Create Contact model with fields:
  - name (CharField)
  - email (EmailField)
  - subject (CharField)
  - message (TextField)
  - created_at (DateTimeField)
  - is_read (BooleanField, default=False)
  - ip_address (GenericIPAddressField, optional)
- [ ] Run migrations for contact app

### 12. Contact Form Implementation
- [ ] Create Django form class with:
  - name field (required, min 2 chars, max 100 chars)
  - email field (required, valid email format)
  - subject field (required, min 5 chars, max 200 chars)
  - message field (required, min 10 chars, max 1000 chars)
- [ ] Add form cleaning methods
- [ ] Implement honeypot field for spam protection

### 13. JavaScript Live Validation
- [ ] Create validation.js file with validation logic
- [ ] Implement validation functions:
  ```javascript
  // Validation states and functions
  - validateName(value) - min 2 chars, only letters and spaces
  - validateEmail(value) - valid email format
  - validateSubject(value) - min 5 chars
  - validateMessage(value) - min 10 chars
  ```
- [ ] Add real-time validation on:
  - input event (while typing)
  - blur event (when leaving field)
  - submit event (final validation)
- [ ] Implement visual feedback:
  - Green border + checkmark icon for valid fields
  - Red border + error message for invalid fields
  - Default gray border for untouched fields
- [ ] Create error message display system:
  ```javascript
  // Error messages
  - "Name must be at least 2 characters"
  - "Please enter a valid email address"
  - "Subject must be at least 5 characters"
  - "Message must be at least 10 characters"
  ```

### 14. Contact Form Styling
- [ ] Create form field states in CSS:
  ```css
  /* Default state */
  .form-field-default {
    @apply border-gray-300 focus:border-blue-500;
  }
  
  /* Valid state */
  .form-field-valid {
    @apply border-green-500 bg-green-50;
  }
  
  /* Invalid state */
  .form-field-invalid {
    @apply border-red-500 bg-red-50;
  }
  ```
- [ ] Style error messages:
  - Red text color
  - Small font size
  - Smooth fade-in animation
- [ ] Add success checkmark icon (SVG)
- [ ] Create loading state for form submission
- [ ] Design success/error notification messages

### 15. Contact Views & URLs
- [ ] Create ContactFormView (FormView)
- [ ] Create ContactSuccessView
- [ ] Create ContactListView (admin only)
- [ ] Add AJAX endpoint for form submission
- [ ] Configure URLs:
  - /contact/ (contact form page)
  - /contact/success/ (success page)
  - /contact/submit/ (AJAX endpoint)
  - /admin/contact/messages/ (admin view)

### 16. Contact Form Templates
- [ ] Create contact form template with:
  - Proper form structure
  - CSRF token
  - Field containers for validation feedback
  - Error message containers
  - Submit button with loading state
- [ ] Create form field component template
- [ ] Create success message template
- [ ] Add no-JavaScript fallback

### 17. Backend Processing
- [ ] Implement email notification on form submission
- [ ] Add rate limiting (max 5 submissions per hour per IP)
- [ ] Store submissions in database
- [ ] Create admin interface for viewing messages
- [ ] Add CSV export functionality for contact messages

### 18. Contact Form Testing
- [ ] Write JavaScript validation tests
- [ ] Test form submission (valid/invalid data)
- [ ] Test rate limiting
- [ ] Test email notifications
- [ ] Test accessibility (keyboard navigation, screen readers)
- [ ] Cross-browser testing

## Additional Features

### 19. User Features
- [ ] Add user registration
- [ ] Add user login/logout
- [ ] Create user profile pages
- [ ] Implement permissions for content creation

### 20. CMS Features
- [ ] Add WYSIWYG editor (TinyMCE or CKEditor)
- [ ] Implement draft/publish workflow
- [ ] Add revision history
- [ ] Create sitemap.xml
- [ ] Add RSS feed
- [ ] Implement commenting system

### 21. Performance & Security
- [ ] Configure caching
- [ ] Add CSRF protection
- [ ] Implement rate limiting
- [ ] Set up proper security headers
- [ ] Configure allowed hosts
- [ ] Add SSL/HTTPS support

### 22. Testing
- [ ] Write model tests
- [ ] Write view tests
- [ ] Write template tests
- [ ] Add integration tests
- [ ] Configure test coverage

### 23. Deployment Preparation
- [ ] Create requirements.txt
- [ ] Add environment variables support
- [ ] Create .env.example
- [ ] Write deployment documentation
- [ ] Configure production settings
- [ ] Set up static files serving for production

## Development Workflow

1. **CSS Development**:
   - Edit atomic CSS files
   - Run Tailwind build process
   - Test responsive design
   - Implement form validation states

2. **Template Development**:
   - Create reusable Jinja2 components
   - Follow Atomic Design hierarchy
   - Maintain consistent naming conventions
   - Ensure progressive enhancement for forms

3. **Backend Development**:
   - Follow Django best practices
   - Write tests alongside features
   - Document code and APIs
   - Implement proper form validation

4. **JavaScript Development**:
   - Write modular, reusable validation code
   - Ensure no-JS fallback functionality
   - Test across browsers
   - Follow accessibility guidelines

## Commands Reference

```bash
# Start development server
python manage.py runserver

# Build Tailwind CSS
npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic

# Run tests
python manage.py test

# Run contact app tests
python manage.py test contact

# Watch JavaScript files (if using build process)
npm run watch
```

## Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Jinja2 Documentation](https://jinja.palletsprojects.com/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [Atomic Design Methodology](https://bradfrost.com/blog/post/atomic-web-design/)
- [JavaScript Form Validation Best Practices](https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation)
- [Web Accessibility Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
