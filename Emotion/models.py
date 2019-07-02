from django.db import models


# Create your models here.
class Nations(models.Model):
    nno = models.CharField(primary_key=True, max_length=4)
    nation_chinese = models.CharField(max_length=255)
    nation_english = models.CharField(max_length=255)
    geographical_position = models.CharField(max_length=255)
    economic_situation = models.CharField(max_length=255)


class Organization(models.Model):
    ono = models.CharField(primary_key=True, max_length=5)
    organization_chinese = models.CharField(max_length=255)
    organization_english = models.CharField(max_length=255)
    nno = models.ForeignKey('Nations', on_delete=models.CASCADE)
    main_duty = models.CharField(max_length=255)
    organization_type = models.CharField(max_length=255)
    setup_time = models.DateField(null=True)


class User(models.Model):
    userid = models.CharField(primary_key=True, max_length=255)
    password = models.CharField(max_length=255)
    permissions = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=1)
    national = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


'''
class National_operation(models.Model):
    userid = models.ForeignKey('User', on_delete=models.CASCADE)
    # nno = models.ForeignKey('Nations', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    operation_type = models.CharField(max_length=255)

    class Meta:
        # unique_together = ("userid", "nno", "time")
        unique_together = ("userid", "time")
'''


class Basic_information(models.Model):
    """docstring for character_information"""
    cno = models.CharField(primary_key=True, max_length=5)
    chinese_name = models.CharField(max_length=255)
    english_name = models.CharField(max_length=255, null=True)
    nno = models.ForeignKey('Nations', on_delete=models.CASCADE)
    actor = models.CharField(max_length=255)
    sex = models.CharField(max_length=1, null=True)
    birth = models.CharField(max_length=255, null=True)
    death = models.CharField(max_length=255, null=True)


class Agname(models.Model):
    cno = models.ForeignKey(Basic_information, on_delete=models.CASCADE)
    agname_chinese = models.CharField(max_length=255, null=True)
    agname_english = models.CharField(max_length=255, null=True)

    class Meta:
        unique_together = ("cno", "agname_chinese")


class Character_subjects(models.Model):
    cno = models.ForeignKey('Basic_information', on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)

    class Meta:
        unique_together = ("cno", "subject")


class Contact(models.Model):
    cno = models.ForeignKey('Basic_information', on_delete=models.CASCADE)
    contact = models.CharField(max_length=255)
    contact_type = models.CharField(max_length=255)

    class Meta:
        unique_together = ("cno", "contact")


class Figure_operation(models.Model):
    userid = models.ForeignKey('User', on_delete=models.CASCADE)
    # cno = models.ForeignKey('Basic_information', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    operation_object = models.CharField(max_length=255,default=None)
    operation_type = models.CharField(max_length=255)

    class Meta:
        # unique_together = ("userid", "cno", "time")
        unique_together = ("userid", "time")


class S_organization(models.Model):
    sono = models.CharField(primary_key=True, max_length=7)
    ono = models.ForeignKey('Organization', on_delete=models.CASCADE)
    name_chinese = models.CharField(max_length=255)
    name_english = models.CharField(max_length=255)
    main_duty = models.CharField(max_length=255, null=True)


class S_contact(models.Model):
    sono = models.ForeignKey('S_organization', on_delete=models.CASCADE)
    contact = models.CharField(max_length=255)
    contact_type = models.CharField(max_length=255)

    class Meta:
        unique_together = ("sono", "contact")


class Positions(models.Model):
    cno = models.ForeignKey('Basic_information', on_delete=models.CASCADE)
    ono = models.ForeignKey('Organization', on_delete=models.CASCADE)
    sono = models.ForeignKey('S_organization', on_delete=models.CASCADE, null=True)
    position = models.CharField(max_length=255)
    position_start = models.DateField(default=None)
    position_end = models.DateField(null=True)

    class Meta:
        unique_together = ("cno", "ono", "sono", "position", "position_start")


'''
class Organization_operation(models.Model):
    userid = models.ForeignKey('User', on_delete=models.CASCADE)
    # ono = models.ForeignKey('Organization', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    operation_type = models.CharField(max_length=255)

    class Meta:
        # unique_together = ("userid", "ono", "time")
        unique_together = ("userid", "time")
'''


class Agname_o(models.Model):
    ono = models.ForeignKey('Organization', on_delete=models.CASCADE)
    agname = models.CharField(max_length=255)

    class Meta:
        unique_together = ("ono", "agname")


class Agname_os(models.Model):
    sono = models.ForeignKey('S_organization', on_delete=models.CASCADE)
    agname = models.CharField(max_length=255)

    class Meta:
        unique_together = ("sono", "agname")
