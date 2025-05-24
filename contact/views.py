from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
import json
from .forms import ContactForm
from .models import Contact


class ContactFormView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:contact_success')
    
    def form_valid(self, form):
        # Save contact with IP address
        contact = form.save(commit=False)
        contact.ip_address = self.get_client_ip()
        contact.save()
        
        # Send email notification (optional)
        self.send_email_notification(contact)
        
        messages.success(self.request, 'Your message has been sent successfully!')
        return super().form_valid(form)
    
    def get_client_ip(self):
        """Get client IP address from request."""
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        return ip
    
    def send_email_notification(self, contact):
        """Send email notification to admin (if configured)."""
        if hasattr(settings, 'CONTACT_EMAIL'):
            try:
                send_mail(
                    f'New Contact Form Submission: {contact.subject}',
                    f'From: {contact.name} ({contact.email})\n\n{contact.message}',
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.CONTACT_EMAIL],
                    fail_silently=True,
                )
            except Exception:
                pass  # Fail silently


class ContactSuccessView(TemplateView):
    template_name = 'contact/success.html'


@require_POST
@csrf_protect
def contact_submit_ajax(request):
    """AJAX endpoint for contact form submission."""
    try:
        # Check rate limiting (simple implementation)
        if not check_rate_limit(request):
            return JsonResponse({
                'success': False,
                'errors': {'__all__': 'Too many submissions. Please try again later.'}
            }, status=429)
        
        # Parse JSON data
        data = json.loads(request.body)
        form = ContactForm(data)
        
        if form.is_valid():
            # Save contact
            contact = form.save(commit=False)
            contact.ip_address = get_client_ip(request)
            contact.save()
            
            # Send email notification
            send_email_notification_ajax(contact)
            
            return JsonResponse({
                'success': True,
                'message': 'Your message has been sent successfully!'
            })
        else:
            return JsonResponse({
                'success': False,
                'errors': form.errors
            }, status=400)
    
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'errors': {'__all__': 'Invalid data format.'}
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'errors': {'__all__': 'An error occurred. Please try again.'}
        }, status=500)


def check_rate_limit(request):
    """Simple rate limiting check (5 submissions per hour per IP)."""
    ip = get_client_ip(request)
    one_hour_ago = timezone.now() - timezone.timedelta(hours=1)
    
    recent_submissions = Contact.objects.filter(
        ip_address=ip,
        created_at__gte=one_hour_ago
    ).count()
    
    return recent_submissions < 5


def get_client_ip(request):
    """Get client IP address from request."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def send_email_notification_ajax(contact):
    """Send email notification for AJAX submissions."""
    if hasattr(settings, 'CONTACT_EMAIL'):
        try:
            send_mail(
                f'New Contact Form Submission: {contact.subject}',
                f'From: {contact.name} ({contact.email})\n\n{contact.message}',
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],
                fail_silently=True,
            )
        except Exception:
            pass
