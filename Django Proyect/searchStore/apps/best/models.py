from django.db import models

# Create your models here.
class CategoryBest(models.Model):
    #id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 255, blank = False,null = False)
	#edad = models.IntegerField()
	category = models.CharField(max_length = 255, blank = False,null = False)
	active = models.BooleanField(default=False)
    #created_at = models.DateTimeField(default=timezone.now)
    #updated_at = models.DateTimeField(default=timezone.now)

	class Meta:
		verbose_name = 'categoryBest'
		verbose_name_plural = 'CategoryBests'

	def __str__(self):
		return self.name