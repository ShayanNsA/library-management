from django.db import models
from django.core.exceptions import ValidationError # این رو ایمپورت میکنیم تا فراخوانی درست انجام شود

# Create your models here.

class Book(models.Model):

    title = models.CharField(max_length=50)
    publish_date = models.DateField()
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='books', null=True)
    authors = models.ManyToManyField("Author", related_name="books")

class Author(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    class Meta:
        # این جادوی اصلی است!
        # می‌گوید ترکیب این دو فیلد باید در کل دیتابیس یکتا باشد.
        constraints = [
            models.UniqueConstraint(
                fields=['first_name', 'last_name'],
                name='unique_author_full_name'
            )
        ]

    def clean(self):
        # اعمال همان منطق تمیزکاری که یاد گرفتی
        if self.first_name:
            self.first_name = self.first_name.strip()
        if self.last_name:
            self.last_name = self.last_name.strip()

    def save(self, *args, **kwargs):
        # تضمین نهایی برای تمیز بودن داده‌ها
        if self.first_name:
            self.first_name = self.first_name.strip()
        if self.last_name:
            self.last_name = self.last_name.strip()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Category(models.Model):

    title = models.CharField(max_length=50, unique=True,error_messages={
            'unique': 'این دسته‌بندی قبلاً وجود دارد' # این پیامِ استانداردِ جنگو را فارسی می‌کند
        })

    def clean(self):
        """
        پاکسازی داده قبل از اعتبارسنجی (مناسب برای فرم‌ها و پنل ادمین)
        """
        if self.title:
            self.title = self.title.strip()

    def save(self, *args, **kwargs):
        """
        ضمانت نهایی پاکسازی (مناسب برای همه حالات ذخیره‌سازی)
        """
        if self.title:
            self.title = self.title.strip()
        super().save(*args, **kwargs)


    # def clean(self):
    #     if Category.objects.filter(title__iexact=self.title).exclude(pk=self.pk).exists():
    #         raise ValidationError("خطا: این دسته بندی قبلاً وجود دارد!")
    # in zamani be dard mikhore ke uniqe=true is not defined !!!!!!!!!!!

    def __str__(self):
        return f"{self.title}"
