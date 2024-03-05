from django.db import models

class Brand(models.Model):
    description=models.CharField(max_length=50,unique=True)
    
    def __str__(self) -> str:
        return str(self.description)
    
    class Meta:
        db_table="brand"
        verbose_name="Marca"
        verbose_name_plural="Marcas"

class Models(models.Model):
    description=models.CharField(
        max_length=50,
        db_comment="Descripcion del modelo de Vehiculo"
    )
    brand=models.ForeignKey(
        Brand,
        on_delete=models.PROTECT,
        )
    def __str__(self):
        return f"{self.brand} - {self.description}"
    class Meta:
        db_table="model"
        db_table_comment="Modelos de Vehiculos"
        verbose_name="Modelos"
        verbose_name_plural="Modelos"