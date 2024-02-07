from django.db import models

class Brand(models.Model):
    description=models.CharField(max_length=50,unique=True)
    
    def __str__(self) -> str:
        return str(self.description)
    
    class Meta:
        db_table="brand"
        verbose_name="Marca"
        verbose_name_plural="Marcas"

