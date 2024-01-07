from django.db import models

class Key_Panel(models.Model):
    resident=models.CharField(max_length=100,blank=False,null=False)
    check_in=models.TimeField(auto_now_add=True)
    check_out=models.TimeField(null=True)

    def __str__(self):
        return f'{self.resident}, às {str(self.check_in)[:5]}'
