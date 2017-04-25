

# Create your models here.
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django.db import models

# Create your models here.

from django.core.urlresolvers import reverse
from django.db import models

state_choice=(("AL","Alabama"),("AK","Alaska"),("AZ","Arizona"),("AR","Arkansas"),("CA","California"),("CO","Colorado"),("CT","Connecticut"),
              ("DE","Delaware"),("DC","District Of Columbia"),("FL","Florida"),("GA","Georgia"),("HI","Hawaii"),("ID","Idaho"),("IL","Illinois"),
              ("IN","Indiana"),("IA","Iowa"),("KS","Kansas"),("KY","Kentucky"),("LA","Louisiana"),("ME","Maine"),("MD","Maryland"),("MA","Massachusetts"),
              ("MI","Michigan"),("MN","Minnesota"),("MS","Mississippi"),("MO","Missouri"),("MT","Montana"),("NE","Nebraska"),("NV","Nevada"),("NH","New Hampshire"),
              ("NJ","New Jersey"),("NM","New Mexico"),("NY","New York"),("NC","North Carolina"),("ND","North Dakota"),("OH","Ohio"),("OK","Oklahoma"),
              ("OR","Oregon"),("PA","Pennsylvania"),("RI","Rhode Island"),("SC","South Carolina"),("SD","South Dakota"),("TN","Tennessee"),("TX","Texas"),
              ("UT","Utah"),("VT","Vermont"),("VA","Virginia"),("WA","Washington"),("WV","West Virginia"),("WI","Wisconsin"),("WY","Wyoming"))
# Create your models here.
# Create your models here.
class Coach(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, unique=True, related_name='profile')
    city = models.CharField(max_length=21)
    state = models.CharField(max_length=20, choices=state_choice)
    resume = models.FileField(blank=True, null=True)
    certification = models.FileField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='Coach/profile_image',null=True,blank=True)


    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = Coach.objects.create(user=kwargs['instance'])

    post_save.connect(create_profile, sender=User)
    def __str__(self):
        return self.user.username

class Team(models.Model):
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=40)
    mascot = models.CharField(max_length=15)
    city = models.CharField(max_length=21)
    state = models.CharField(max_length=20,choices=state_choice)

    def __str__(self):
        return self.team_name
class Player(models.Model):
    predominate_hand_choices=(('left','left'),('right','right'))
    baseball_positions=(('pitcher','pitcher'),('catcher','catcher'),('first base','first base'),('second base','second base')
                        ,('third base','third base'),('shortstop','shortstop'),('right fielder','right fielder'),
                        ('left fielder','left fielder'),('center fielder','center fielder'))
    type_choices=(("independent","independent"),("Coach-Dependent","Coach-Dependent"))
    height_feet_choices=(("1ft","1ft"),("2ft","2ft"),("3ft","3ft"),("4ft","4ft"),("5ft","5ft"),("6ft","6ft"))
    height_inches_choices=(("1in","1in"),("2in","2in"),("3in","3in"),("4in","4in"),("5in","5in"),("6in","6in"),
                           ("7in", "7in"),("8in","8in"),("9in","9in"),("10in","10in"),("11in","11in"),("12in","12in"))
    email=models.CharField(max_length=200)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=8)
    type = models.CharField(max_length=50, choices=type_choices)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    hometown = models.CharField(max_length=21)
    homestate = models.CharField(max_length=20,choices=state_choice)
    height_feet = models.CharField(max_length=3, choices=height_feet_choices)
    height_inches = models.CharField(max_length=4, choices=height_inches_choices)
    weight = models.CharField(max_length=3)
    batting_orientation = models.CharField(max_length=50,choices=predominate_hand_choices)
    position=models.CharField(max_length=50,choices=baseball_positions)
    player_number=models.IntegerField()

    #player number
    def __str__(self):
        return self.first_name + '\n'+self.last_name

class Swing(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    swing_name = models.CharField(max_length=50)
    start_rot_x = models.DecimalField(max_digits=200, decimal_places=3)
    end_rot_x = models.DecimalField(max_digits=200, decimal_places=3)
    start_rot_y = models.DecimalField(max_digits=200, decimal_places=3)
    end_rot_y = models.DecimalField(max_digits=200, decimal_places=3)
    start_rot_z = models.DecimalField(max_digits=200, decimal_places=3)
    end_rot_z = models.DecimalField(max_digits=200, decimal_places=3)
    start_pos_x = models.DecimalField(max_digits=200, decimal_places=3)
    end_pos_x = models.DecimalField(max_digits=200, decimal_places=3)
    start_pos_y = models.DecimalField(max_digits=200, decimal_places=3)
    end_pos_y = models.DecimalField(max_digits=200, decimal_places=3)
    start_pos_z = models.DecimalField(max_digits=200, decimal_places=3)
    end_pos_z = models.DecimalField(max_digits=200, decimal_places=3)
    speed = models.DecimalField(max_digits=300, decimal_places=3)
    def __str__(self):
        return self.player.first_name + '\n'+self.player.last_name + '\n' + self.swing_name

