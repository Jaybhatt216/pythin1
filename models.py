from django.db import models

# Create your models here.
#this is where you make objects
#pesudo code for polls app
'''
Question

Question_text
Publish_date

Choice

choice_text
number_of_votes
link_choice_to_questions
'''
#make a question class to questions also let Django 
#know that the type is model by doing models.Model
#this also makes it so that every question we create
#has a max lenght of 200 chars and a published date
class Question(models.Model):
    #now to give the class questions some question texts
    question_text = models.CharField(max_length=200)#you can only have 200 chars in a question
    pub_date = models.DateTimeField('date published')#get the date of question creation
    def _str_(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    number_of_votes = models.IntegerField(default=0)
    #now to link choice and question so every choice we
    #create links to only 1 question
    #passing in a question, its a foreign key of the question object
    #delete the answers votes etc when a question is deleted
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    def __str__(self):
        return self.choice_text
