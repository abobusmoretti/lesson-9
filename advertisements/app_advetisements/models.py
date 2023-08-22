from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model

User = get_user_model()

class Advertisements(models.Model):
    tittle = models.CharField('заголовок', max_length = 128)
    description = models.TextField('описание')
    price = models.DecimalField('цена', max_digits = 10, decimal_places = 2)
    auction = models.BooleanField('торг', help_text = 'Отметьте, если торг уместен')
    created_at = models.DateTimeField(auto_now_add = True)
    updeted_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, verbose_name = 'Пользователь', on_delete = models.CASCADE)
    image = models.ImageField('Изображение', upload_to = 'advertisements/',)

    class Meta:
        db_table = "advertisements"
    def __str__(self):
        return f"Advertisement(id = {self.id}, title = {self.tittle}, price = {self.price}"
    
    @admin.display(description = 'Дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style = "color: green; font-weight: bold;"> Сегодня В {} </span>', created_time
            )
        return self.created_at.strftime('%d.%m.%Y в %H:%M:%S')
    
    @admin.display(description = 'Дата изменения')
    def updated_date(self):
        from django.utils import timezone
        if self.updeted_at.date() == timezone.now().date():
            updated_time = self.updeted_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style = "color: red; font-weight: bold;"> Сегодня В {} </span>', updated_time
            )
        return self.updeted_at.strftime('%d.%m.%Y в %H:%M:%S')\
        
    @admin.display(description = 'Изображение')
    def created_image(self):
        if self.image:
            return format_html(
                '<img src = "{url}"  width="50" height="50">', url = self.image.url
        )

# Create your models here.
