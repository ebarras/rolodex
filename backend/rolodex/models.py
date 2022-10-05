from django.db import models

class Contact(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=70)
    birth_date = models.DateField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name


class Address(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    line1 = models.CharField(max_length=1024)
    line2 = models.CharField(max_length=1024, default=None, blank=True, null=True)
    line3 = models.CharField(max_length=1024, default=None, blank=True, null=True)
    city = models.CharField(max_length=50)
    zip_or_post_code = models.CharField(max_length=12)
    state_province_county = models.CharField(max_length=50)
    country_code = models.CharField(max_length=3)
    other_address_details = models.TextField(default=None, blank=True, null=True)
    contacts = models.ManyToManyField(Contact, blank=True)

    def __str__(self):
        return f'{self.line1}, {self.city}, {self.state_province_county} {self.zip_or_post_code}'


class PhoneNumber(models.Model):
    class PhoneNumberType(models.TextChoices):
        CELL = 'Cellular'
        WORK = 'Work'
        HOME = 'Home'
        BUSINESS = 'Business'
        OFFICE = 'Office'
    
    type = models.CharField(
        max_length=8,
        choices=PhoneNumberType.choices
    )
    number = models.CharField(max_length=26)

    contact = models.ForeignKey(
        'Contact',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.number


class Email(models.Model):
    class EmailType(models.TextChoices):
        WORK = 'Work'
        PERSONAL = 'Personal'
        BUSINESS = 'Business'
        SUPPORT = 'Support'
    
    type = models.CharField(
        max_length=8,
        choices=EmailType.choices
    )
    address = models.CharField(max_length=255)

    contact = models.ForeignKey(
        'Contact',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.address


class SocialMedia(models.Model):
    class SocialMediaType(models.TextChoices):
        FACEBOOK = 'Facebook'
        INSTAGRAM = 'Instagram'
        TWITTER = 'Twitter'
        LINKEDIN = 'LinkedIn'
        GITHUB = 'Github'

    type = models.CharField(
        max_length=9,
        choices=SocialMediaType.choices
    )

    username = models.CharField(max_length=305)
    url = models.TextField()

    contact = models.ForeignKey(
        'Contact',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.type}, {self.username}'

class Note(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    note = models.TextField()

    contact = models.ForeignKey(
        'Contact',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.note[:50]
