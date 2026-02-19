from django.core.validators import RegexValidator

uz_phone_validator = RegexValidator(
    regex=r'^(\+998|998)?[0-9]{9}$',
    message="Telefon raqam +998901234567 formatida bo‘lishi kerak"
)