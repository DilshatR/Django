from django.db import models

class Languages(models.Model):
    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'
    title = models.CharField(max_length=128)
    active = models.BooleanField()

    def __str__(self):
        return self.title

class News(models.Model):
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    lang_id = models.ForeignKey(to=Languages, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to="news")
    active = models.BooleanField()

    def __str__(self):
        return f'{self.title} | {self.lang_id.title}'

class Pages(models.Model):
    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'
    lang_id = models.ForeignKey(to=Languages, on_delete=models.CASCADE)
    page_name = models.CharField(max_length=128)
    description = models.TextField(null=True)
    key_works = models.TextField(null=True)
    content = models.TextField()
    active = models.BooleanField()

    def __str__(self):
        return self.page_name

class MainMenu(models.Model):
    class Meta:
        verbose_name = 'Main Menu'
        verbose_name_plural = 'Main Menu'
    lang_id = models.ForeignKey(to=Languages, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.CharField(max_length=256)
    position = models.IntegerField()
    active = models.BooleanField()

    def __str__(self):
        return self.title

class FooterMenu(models.Model):
    class Meta:
        verbose_name = 'Footer Menu'
        verbose_name_plural = 'Footer Menu'
    lang_id = models.ForeignKey(to=Languages, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.CharField(max_length=256)
    position = models.IntegerField()
    active = models.BooleanField()


class Slider(models.Model):
    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Slider'

    lang_id = models.ForeignKey(to=Languages, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to="slider")
    active = models.BooleanField()

    def __str__(self):
        return f'{self.title} | {self.lang_id.title}'
