from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
import re

def validate_file_size(value):
    """Validate file size is not more than 5MB"""
    filesize = value.size
    if filesize > 5 * 1024 * 1024:  # 5MB
        raise ValidationError("File size cannot exceed 5MB")

def validate_strong_password(password):
    """Custom password validator for minimum 12 characters with complexity"""
    if len(password) < 12:
        raise ValidationError("Password must be at least 12 characters long")
    
    if not re.search(r'[A-Z]', password):
        raise ValidationError("Password must contain at least one uppercase letter")
    
    if not re.search(r'[a-z]', password):
        raise ValidationError("Password must contain at least one lowercase letter")
    
    if not re.search(r'[0-9]', password):
        raise ValidationError("Password must contain at least one digit")
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        raise ValidationError("Password must contain at least one special character")