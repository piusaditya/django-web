from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# Fungsi signals biar otomatis buat user profile dengan argumen info ke receiver

# FUNGSI CREATE PROFILE
# Membuat user profile untuk tiap user baru, tiap user menyimpan, send signal post_save
# signal diterima @receiver yaitu fungsi create profile
# create profile ambil semua argumen salah satunya instance user dan created
# jika created maka buat profile objects dengan user adalah instancenya

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# FUNGSI SAVE PROFILE

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()