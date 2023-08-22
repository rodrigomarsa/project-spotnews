from django.db import models
from news.validators import validate_date, validate_title


class News(models.Model):
    title = models.CharField(
        max_length=200,
        validators=[validate_title],
        blank=False,
        error_messages={
            "blank": "Este campo não pode estar vazio.",
        },
    )
    content = models.TextField(
        blank=False,
        error_messages={
            "blank": "Este campo não pode estar vazio.",
        },
    )
    author = models.ForeignKey(
        "Users", on_delete=models.CASCADE, related_name="news"
    )
    created_at = models.DateField(validators=[validate_date])
    image = models.ImageField(upload_to="img/", blank=True, null=True)
    categories = models.ManyToManyField("Categories", related_name="news")

    def __str__(self):
        return self.title
