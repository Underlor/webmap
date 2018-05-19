from django.db import models


class HDD(models.Model):
    name = models.CharField(max_length=255)


class CPU(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    core_count = models.CharField(max_length=255)
    clock_speed = models.CharField(max_length=255)
    architecture = models.CharField(max_length=255)


class OS(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    computer_name = models.CharField(max_length=255)
    current_user = models.CharField(max_length=255)
    install_date = models.CharField(max_length=255)
    build_number = models.CharField(max_length=255)
    boot_device = models.CharField(max_length=255)
    total_visible_memory = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255)


class GPU(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    adapter_ram = models.CharField(max_length=255)
    driver_version = models.CharField(max_length=255)
    video_processor = models.CharField(max_length=255)


class RAM(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    capacity = models.CharField(max_length=255)
    form_factor = models.CharField(max_length=255)
    clock_speed = models.CharField(max_length=255)


class MOTHERBOARD(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    chipset = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255)


# Create your models here.
class PC(models.Model):
    ip = models.CharField(max_length=255)
    bios_manufacturer = models.CharField(max_length=255)
    bios_version = models.CharField(max_length=255)
    motherboard = models.ManyToManyField(MOTHERBOARD)
    ram = models.ManyToManyField(RAM)
    gpu = models.ManyToManyField(GPU)
    os = models.ManyToManyField(OS)
    cpu = models.ManyToManyField(CPU)
    hdd = models.ManyToManyField(HDD)
    actual = models.BooleanField(default=True)
    update_dt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Рабочая станция'
        verbose_name_plural = 'Рабочии станции'
