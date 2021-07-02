from django.db import models

# List parent
class List(models.Model):
  list_name = models.CharField(max_length=200)

  def __str__(self):
    return "%s" % (self.list_name)

# Items in list
class listItem(models.Model):
  item = models.CharField(max_length=200)
  isDone = models.BooleanField(default=False)
  list_name = models.ForeignKey(
    List, 
    on_delete=models.CASCADE,
    related_name='items'
  )
    
  def __str__(self):
    return self.item
