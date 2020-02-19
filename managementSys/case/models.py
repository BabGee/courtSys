from django.db import models

STATUS = ((0, 'Pending'), (1, 'Solved'))

class CaseFile(models.Model):
    accuser_name = models.CharField(max_length=100)
    defendant_name = models.CharField(max_length=100)
    evidence = models.FileField(upload_to='caseFiles', auto_created=True)
    status = models.IntegerField(choices=STATUS, default=0)
    notes = models.TextField(default='The Case notes', help_text='Notes om the Case involving the Parties')

    def __str__(self):
        return f'{self.accuser_name} vs {self.defendant_name}'
