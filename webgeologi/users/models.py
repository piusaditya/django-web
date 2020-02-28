from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# 28 Februari 2020, Pius
# Fungsi buat bikin models untuk profile buat hapus akun(cascade), upload foto


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

# Define hasil keluaran 'Nama orang Profile'
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)