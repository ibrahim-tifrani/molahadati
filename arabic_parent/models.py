from django.db import models
class chat_model(models.Model):
    name_of_parent_chat=models.CharField(max_length=50,blank=True)
    name_of_child=models.CharField(max_length=50,blank=True)
    chats_words=models.TextField(null=True)
    def __str__(self):
        return self.name_of_parent_chat
# Create your models here.
