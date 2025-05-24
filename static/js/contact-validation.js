// Contact Form Validation
(function() {
    'use strict';

    // Validation rules
    const validators = {
        name: {
            validate: (value) => {
                const trimmed = value.trim();
                if (trimmed.length < 2) {
                    return { valid: false, message: 'Name must be at least 2 characters' };
                }
                if (!/^[a-zA-Z\s]+$/.test(trimmed)) {
                    return { valid: false, message: 'Name can only contain letters and spaces' };
                }
                return { valid: true };
            }
        },
        email: {
            validate: (value) => {
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!emailRegex.test(value)) {
                    return { valid: false, message: 'Please enter a valid email address' };
                }
                return { valid: true };
            }
        },
        subject: {
            validate: (value) => {
                const trimmed = value.trim();
                if (trimmed.length < 5) {
                    return { valid: false, message: 'Subject must be at least 5 characters' };
                }
                return { valid: true };
            }
        },
        message: {
            validate: (value) => {
                const trimmed = value.trim();
                if (trimmed.length < 10) {
                    return { valid: false, message: 'Message must be at least 10 characters' };
                }
                return { valid: true };
            }
        }
    };

    // CSS classes for field states
    const fieldClasses = {
        default: 'form-field-default border-gray-300 focus:border-blue-500',
        valid: 'form-field-valid border-green-500 bg-green-50',
        invalid: 'form-field-invalid border-red-500 bg-red-50'
    };

    // Initialize validation on page load
    document.addEventListener('DOMContentLoaded', function() {
        const form = document.getElementById('contact-form');
        if (!form) return;

        const fields = form.querySelectorAll('[data-validate]');
        const submitButton = form.querySelector('button[type="submit"]');

        // Add validation to each field
        fields.forEach(field => {
            const fieldName = field.getAttribute('data-validate');
            const formGroup = field.closest('.form-group');
            const errorElement = formGroup.querySelector('.error-message');
            const successIcon = formGroup.querySelector('.success-icon');

            // Validate on input (debounced)
            let inputTimeout;
            field.addEventListener('input', function() {
                clearTimeout(inputTimeout);
                inputTimeout = setTimeout(() => {
                    validateField(field, fieldName, errorElement, successIcon);
                }, 300);
            });

            // Validate on blur
            field.addEventListener('blur', function() {
                validateField(field, fieldName, errorElement, successIcon);
            });
        });

        // Form submission
        form.addEventListener('submit', function(e) {
            e.preventDefault();

            // Validate all fields
            let isValid = true;
            fields.forEach(field => {
                const fieldName = field.getAttribute('data-validate');
                const formGroup = field.closest('.form-group');
                const errorElement = formGroup.querySelector('.error-message');
                const successIcon = formGroup.querySelector('.success-icon');
                
                const result = validateField(field, fieldName, errorElement, successIcon);
                if (!result) isValid = false;
            });

            if (isValid) {
                submitForm(form, submitButton);
            }
        });
    });

    // Validate individual field
    function validateField(field, fieldName, errorElement, successIcon) {
        const value = field.value;
        const validator = validators[fieldName];
        
        if (!validator) return true;

        // Reset field state
        removeFieldState(field);
        errorElement.classList.add('hidden');
        errorElement.textContent = '';
        successIcon.classList.add('hidden');

        // Skip validation for empty untouched fields
        if (!value && !field.classList.contains('touched')) {
            return true;
        }

        // Mark field as touched
        field.classList.add('touched');

        // Validate
        const result = validator.validate(value);

        if (result.valid) {
            // Valid state
            field.classList.remove(...fieldClasses.default.split(' '));
            field.classList.remove(...fieldClasses.invalid.split(' '));
            field.classList.add(...fieldClasses.valid.split(' '));
            successIcon.classList.remove('hidden');
            return true;
        } else {
            // Invalid state
            field.classList.remove(...fieldClasses.default.split(' '));
            field.classList.remove(...fieldClasses.valid.split(' '));
            field.classList.add(...fieldClasses.invalid.split(' '));
            errorElement.textContent = result.message;
            errorElement.classList.remove('hidden');
            return false;
        }
    }

    // Remove all field states
    function removeFieldState(field) {
        field.classList.remove(...fieldClasses.valid.split(' '));
        field.classList.remove(...fieldClasses.invalid.split(' '));
        field.classList.add(...fieldClasses.default.split(' '));
    }

    // Submit form via AJAX
    function submitForm(form, submitButton) {
        const formData = new FormData(form);
        const data = {};
        
        // Convert FormData to JSON
        for (let [key, value] of formData.entries()) {
            if (key !== 'csrfmiddlewaretoken') {
                data[key] = value;
            }
        }

        // Show loading state
        submitButton.disabled = true;
        submitButton.querySelector('.button-text').classList.add('hidden');
        submitButton.querySelector('.loading-spinner').classList.remove('hidden');

        // Get CSRF token
        const csrfToken = form.querySelector('[name=csrfmiddlewaretoken]').value;

        // Submit via AJAX
        fetch('/contact/submit/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Show success message
                showMessage('success', data.message || 'Your message has been sent successfully!');
                form.reset();
                
                // Reset field states
                form.querySelectorAll('[data-validate]').forEach(field => {
                    removeFieldState(field);
                    field.classList.remove('touched');
                    const formGroup = field.closest('.form-group');
                    formGroup.querySelector('.success-icon').classList.add('hidden');
                });
            } else {
                // Show error message
                showMessage('error', 'There was an error sending your message. Please try again.');
                
                // Display field errors
                if (data.errors) {
                    Object.keys(data.errors).forEach(fieldName => {
                        const field = form.querySelector(`[name="${fieldName}"]`);
                        if (field) {
                            const formGroup = field.closest('.form-group');
                            const errorElement = formGroup.querySelector('.error-message');
                            errorElement.textContent = data.errors[fieldName][0];
                            errorElement.classList.remove('hidden');
                            
                            // Apply invalid state
                            field.classList.remove(...fieldClasses.default.split(' '));
                            field.classList.remove(...fieldClasses.valid.split(' '));
                            field.classList.add(...fieldClasses.invalid.split(' '));
                        }
                    });
                }
            }
        })
        .catch(error => {
            console.error('Error:', error);
            showMessage('error', 'An unexpected error occurred. Please try again.');
        })
        .finally(() => {
            // Reset button state
            submitButton.disabled = false;
            submitButton.querySelector('.button-text').classList.remove('hidden');
            submitButton.querySelector('.loading-spinner').classList.add('hidden');
        });
    }

    // Show success/error message
    function showMessage(type, message) {
        const messagesContainer = document.getElementById('form-messages');
        const successMessage = messagesContainer.querySelector('.success-message');
        const errorMessage = messagesContainer.querySelector('.error-message');

        // Hide all messages first
        messagesContainer.classList.add('hidden');
        successMessage.classList.add('hidden');
        errorMessage.classList.add('hidden');

        // Show appropriate message
        messagesContainer.classList.remove('hidden');
        if (type === 'success') {
            successMessage.querySelector('p:last-child').textContent = message;
            successMessage.classList.remove('hidden');
            
            // Auto-hide after 5 seconds
            setTimeout(() => {
                successMessage.classList.add('hidden');
                messagesContainer.classList.add('hidden');
            }, 5000);
        } else {
            errorMessage.querySelector('p:last-child').textContent = message;
            errorMessage.classList.remove('hidden');
        }

        // Scroll to message
        messagesContainer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

})();