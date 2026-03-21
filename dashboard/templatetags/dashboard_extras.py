import hashlib
from django import template

register = template.Library()

@register.filter
def string_to_color(value):
    """Generate a consistent pastel color from any string."""
    if not value:
        return "hsl(0, 70%, 70%)"
    hash_object = hashlib.md5(value.encode())
    hex_dig = hash_object.hexdigest()
    hue = int(hex_dig[:2], 16) % 360
    return f"hsl({hue}, 70%, 70%)"

@register.filter
def has_group(user, group_name):
    """Check if a user belongs to a specific group."""
    return user.groups.filter(name=group_name).exists()