from django.core.exceptions import ValidationError
from datetime import datetime


def validate_date(value):
    if (
        not datetime.strptime(str(value), "%Y-%m-%d")
        or value > datetime.now().date()
    ):
        raise ValidationError(
            "Use o formato AAAA-MM-DD e uma data igual ou anterior a hoje."
        )


def validate_title(value):
    if len(value.split()) < 2:
        raise ValidationError("O título deve conter pelo menos 2 palavras.")
    if len(value) > 200:
        raise ValidationError(
            "Certifique-se de que o valor tenha no máximo 200 caracteres"
            f" (ele possui {len(value)})."
        )
