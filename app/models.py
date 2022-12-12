from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Level (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) :
        return str(self.name)



class Exam (models.Model) :
    user = models.ForeignKey(User,related_name='user_exam',on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total_points = models.CharField(null=True,blank=True,max_length=100)

    def __str__ (self) :
        return f'{self.user.username} Exam'

class Point (models.Model) :
    level = models.ForeignKey(Level,related_name='point_of_exam',on_delete=models.CASCADE,blank=True,null=True)
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

    def __str__(self) :
        return f"{self.question}"


class Leaderboard (models.Model) :
    user = models.ForeignKey(User,related_name='users_board',on_delete=models.CASCADE)
    rank = models.IntegerField(null=True,blank=True)
    points = models.IntegerField(default=0)

    def __str__(self) :
        if self.rank :
            t = f'#{self.rank} {self.user}'
        else:
            t = f"{self.user} NO RANK"
        
        return t


@receiver(post_save,sender=Exam)
def add_points(**kwargs) :
    if kwargs['created']:
        
        # fetch data
        exam = kwargs['instance']
        user = exam.user
        
        leader = Leaderboard.objects.get(user=user)
        point_of_exam = int(str(exam.total_points).split('/')[0])
        old_user_points = leader.points

        # insert new points
        leader.points = point_of_exam + old_user_points
        
        # save data
        leader.save()

        



@receiver(post_save,sender=User)
def create_leaderboards(**kwargs) :
    if kwargs['created']:
        Leaderboard.objects.create(user=kwargs['instance'])