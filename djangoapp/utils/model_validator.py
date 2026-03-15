from django.core.exceptions import ValidationError


def validate_png(image):
    if not image.name.lower().endswith(('.png', '.svg', '.ico',)):
        raise ValidationError(
            'Somente imagens PNG, SVG e ICO são aceitas.'
        )
