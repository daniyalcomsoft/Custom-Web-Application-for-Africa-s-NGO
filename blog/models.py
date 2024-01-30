from django.db import models
from django.db.models.base import Model, ModelState
from django.db.models.fields.files import ImageField
from django.utils.html import format_html


# Create your models here.

class Video(models.Model):
    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to="video/%y")
    def __str__(self):
        return self.caption

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:40px; height:40px;border-radius:50%;"/  >'.format(self.image))

    def __str__(self):
        return self.title

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)    
    image = models.ImageField(upload_to='post/')   

    def __str__(self):
        return self.title

class IndexTopHeading(models.Model):
    image = models.ImageField(upload_to='post/')
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.description

class IndexOfSecondHeading(models.Model):
    heading = models.CharField(max_length=50)
    image = models.ImageField(upload_to='post/')
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.heading

class IndexOfThirdHeading(models.Model):
    heading = models.CharField(max_length=50)
    image = models.ImageField(upload_to='post/')
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.heading

class IndexOfFourthHeading(models.Model):
    heading = models.CharField(max_length=50)  
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.heading

class MainVideo(models.Model): 
    heading = models.CharField(max_length=50)   
    video = models.FileField(upload_to="video/%y")
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.heading

class IndexOfCommunityHelp(models.Model):
    image = models.ImageField(upload_to='post/')    
    raisedcommunity = models.CharField(max_length=500)
    amount = models.CharField(max_length=50, default="$")
    heading = models.CharField(max_length=50)  
    description = models.CharField(max_length=500)
    date = models.CharField(max_length=100, default="Date & Day")

    def __str__(self):
        return self.heading

class IndexReviewsHeading(models.Model):
    heading = models.CharField(max_length=500)
    sponsorname = models.CharField(max_length=100)

    def __str__(self):
        return self.heading

class DonateFirstHeading(models.Model):
    heading = models.CharField(max_length=50)  
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.heading


class DonateSecHeading(models.Model):
    heading = models.CharField(max_length=50)
    image = models.ImageField(upload_to='post/')
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.heading

class DonateThirdHeading(models.Model):
    image = models.ImageField(upload_to='post/')
    description = models.CharField(max_length=500)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class DonateBigImage(models.Model):
    image = models.ImageField(upload_to='post/')
    description = models.CharField(max_length=500)    

    def __str__(self):
        return self.description

class ContactUs(models.Model):
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    email = models.CharField(max_length=500)    
    
    def __str__(self):
        return self.email

#------------------------------------- About------------------------------------------------

class ABFirstHeading(models.Model):
    image = models.ImageField(upload_to='post/')
    description = models.CharField(max_length=500)    

    def __str__(self):
        return self.description

class ABSecondHeading(models.Model):
    logo = models.ImageField(upload_to='post/')
    description = models.CharField(max_length=500)    

    def __str__(self):
        return self.description

class ABThirdHeading(models.Model):
    heading = models.CharField(max_length=50)
    description = models.CharField(max_length=500)    

    def __str__(self):
        return self.heading

class ABFourthHeading(models.Model):
    image = models.ImageField(upload_to='post/')
    description = models.CharField(max_length=500)    

    def __str__(self):
        return self.description

class ABFifthHeading(models.Model):
    heading = models.CharField(max_length=50)
    description1 = models.CharField(max_length=500)   
    description2 = models.CharField(max_length=500) 

    def __str__(self):
        return self.heading

class ABSupportImage(models.Model):
    supporterimage = models.ImageField(upload_to='post/')
    description = models.CharField(max_length=500)    

    def __str__(self):
        return self.description
    
class ABSixthHeading(models.Model):
    heading = models.CharField(max_length=50)
    description1 = models.CharField(max_length=500)   
    description2 = models.CharField(max_length=500) 

    def __str__(self):
        return self.heading

class ABSeventhHeading(models.Model):
    image = models.ImageField(upload_to='post/')
    description = models.CharField(max_length=500)    

    def __str__(self):
        return self.description

# -----------------------------finanace-----------------------------------------
class FHeadingOne(models.Model):
    image = models.ImageField(upload_to='post/')  
    description = models.CharField(max_length=500)    

    def __str__(self):
        return self.description

class FHeadingTwo(models.Model):
    image = models.ImageField(upload_to='post/')  
    description = models.CharField(max_length=500)    

    def __str__(self):
        return self.description

class FHeadingThree(models.Model): 
    heading = models.CharField(max_length=50)    
    reportdescription = models.CharField(max_length=500)    

    def __str__(self):
        return self.heading

class FHeadingFour(models.Model):
    image = models.ImageField(upload_to='post/')  
    description = models.CharField(max_length=500)    

    def __str__(self):
        return self.description

class Team(models.Model):
    image = models.ImageField(upload_to='post/') 
    name = models.CharField(max_length=50)   
    description = models.CharField(max_length=500)    

    def __str__(self):
        return self.name

class Stories(models.Model):
    image = models.ImageField(upload_to='post/') 
    name = models.CharField(max_length=50)   
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.name




# ----------------------Solve Water Crisis----------------------

class SCHeadingOne(models.Model):   
    heading = models.CharField(max_length=100)   
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class SCHeadingTwo(models.Model):   
    heading = models.CharField(max_length=100)   
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class SCHeadingThree(models.Model):
    image = models.ImageField(upload_to='post/') 
    heading = models.CharField(max_length=100)   
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class SCHeadingFour(models.Model):
    image = models.ImageField(upload_to='post/') 
    heading = models.CharField(max_length=100)   
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class SCHeadingFive(models.Model):   
    heading = models.CharField(max_length=100)   
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class SCHeadingSix(models.Model):
    image = models.ImageField(upload_to='post/') 
    heading = models.CharField(max_length=100)   
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class SCHeadingSeven(models.Model):
    heading = models.CharField(max_length=100)
    description1 = models.CharField(max_length=500)   
    description2 = models.CharField(max_length=500) 

    def __str__(self):
        return self.heading

class SCHeadingEight(models.Model):   
    heading = models.CharField(max_length=100)   
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class WPHeadingOne(models.Model):
    heading = models.CharField(max_length=100)         
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class WPHeadingTwo(models.Model):
    heading = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post/')       
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class WPHeadingThree(models.Model):
    heading = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post/')       
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class WPHeadingFour(models.Model):
    heading = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post/')       
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class WPHeadingFive(models.Model):
    heading = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post/')       
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class WPHeadingSix(models.Model):
    heading = models.CharField(max_length=100)         
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

        # _--------------------------------------------------make a donation

class MDHeadingOne(models.Model):
    heading = models.CharField(max_length=100)         
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class MDHeadingTwo(models.Model):
    heading = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post/')       
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class MDHeadingThree(models.Model):
    heading = models.CharField(max_length=100)         
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading


        # _--------------------------------------------------Give Monthly

class GMHeadingOne(models.Model):
    heading = models.CharField(max_length=100)         
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class GMHeadingTwo(models.Model):
    heading = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post/')       
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class GMHeadingThree(models.Model):
    heading = models.CharField(max_length=100)         
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

# ------------------------------sponsor a community---------------------------


class SCMHeadingOne(models.Model):
    heading = models.CharField(max_length=100)         
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class SCMHeadingTwo(models.Model):
    heading = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post/')       
    amount = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading


class SCMHeadingThree(models.Model):
    heading = models.CharField(max_length=100)         
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading


class SCMHeadingFour(models.Model):
    heading = models.CharField(max_length=100)         
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class CSHeadingOne(models.Model):
    heading = models.CharField(max_length=100)         
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading


# ----------------------------------------------water crisis

class WCHeadingOne(models.Model):
    heading = models.CharField(max_length=100)         
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class WCHeadingTwo(models.Model):
    heading = models.CharField(max_length=100)         
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class WCHeadingThree(models.Model):
    heading = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post/')       
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class WCHeadingFour(models.Model):
    heading = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post/')       
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class WCHeadingFive(models.Model):
    heading = models.CharField(max_length=100)         
    education = models.CharField(max_length=1000)   
    health = models.CharField(max_length=1000) 
    hunger = models.CharField(max_length=1000) 
    poverty = models.CharField(max_length=1000)  

    def __str__(self):
        return self.heading

class WCHeadingSix(models.Model):
    heading = models.CharField(max_length=100)         
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class WCHeadingSeven(models.Model):
    heading = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post/')       
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class WCHeadingEight(models.Model):
    caption = models.CharField(max_length=100)
    heading = models.CharField(max_length=100)
    video = models.FileField(upload_to="video/%y")
    def __str__(self):
        return self.caption 

        # ------------------------------COVID-19-------------------------------------------------

class CDHeadingOne(models.Model):
    heading = models.CharField(max_length=100)         
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class CDHeadingTwo(models.Model):
    heading = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post/')       
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class CDHeadingThree(models.Model):
    heading = models.CharField(max_length=100)         
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class CDHeadingFour(models.Model):
    heading = models.CharField(max_length=100)         
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading


class CDHeadingFive(models.Model):
    heading = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post/')       
    description = models.CharField(max_length=1000) 
    dateandday = models.CharField(max_length=50)

    def __str__(self):
        return self.heading

                # ------------------------------ Water and Health-------------------------------------------------

class WHHeadingOne(models.Model):
    heading = models.CharField(max_length=100)
    description1 = models.CharField(max_length=1000) 
    description2 = models.CharField(max_length=1000)

    def __str__(self):
        return self.heading

class WHHeadingTwo(models.Model):
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class WHHeadingThree(models.Model):
    heading = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post/')       
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class WHHeadingFour(models.Model):
    heading = models.CharField(max_length=100)
    description1 = models.CharField(max_length=1000) 
    description2 = models.CharField(max_length=1000)

    def __str__(self):
        return self.heading

class WHHeadingFive(models.Model):
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class WHHeadingSix(models.Model):
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

        # ----------------------------------water and Education------------------------------------------

class WEHeadingOne(models.Model):
    heading = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post/')       
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class WEHeadingTwo(models.Model):
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class WEHeadingThree(models.Model):
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading


# -----------------------------------------------water and hunger -----------------------------------------------

class HUNHeadingOne(models.Model):
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class HUNHeadingTwo(models.Model):
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class HUNHeadingThree(models.Model):
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class HUNHeadingFour(models.Model):
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

# -------------------------------------------------Water And Poverty------------------------------------

class PWHeadingOne(models.Model):
    heading = models.CharField(max_length=100)
    description1 = models.CharField(max_length=1000) 
    description2 = models.CharField(max_length=1000)

    def __str__(self):
        return self.heading

class PWHeadingTwo(models.Model):
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class PWHeadingThree(models.Model):
    heading = models.CharField(max_length=100)
    description1 = models.CharField(max_length=1000) 
    description2 = models.CharField(max_length=1000)

    def __str__(self):
        return self.heading

class PWHeadingFour(models.Model):
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class PWHeadingFive(models.Model):
    heading = models.CharField(max_length=100)
    description1 = models.CharField(max_length=1000) 
    description2 = models.CharField(max_length=1000)

    def __str__(self):
        return self.heading

class PWHeadingSix(models.Model):
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class PWHeadingSeven(models.Model):
    heading = models.CharField(max_length=100)
    description1 = models.CharField(max_length=1000) 
    description2 = models.CharField(max_length=1000)

    def __str__(self):
        return self.heading

class PWMidImage(models.Model):
    heading = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post/')      

    def __str__(self):
        return self.heading

class PWBottomImage(models.Model):
    heading = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post/')      

    def __str__(self):
        return self.heading


        # -------------================================-=-=-==========Scarcity

class WSTopImage(models.Model):
    heading = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post/')      

    def __str__(self):
        return self.heading

class WSHeadingOne(models.Model):
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class WSBottomImage(models.Model):
    heading = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post/')  
    description = models.CharField(max_length=1000) 


    def __str__(self):
        return self.heading


class SSHeadingOne(models.Model):    
    heading = models.CharField(max_length=100)
    video = models.FileField(upload_to="video/%y")
    description = models.CharField(max_length=1000) 

    def __str__(self):
        return self.heading 

class SSHeadingTwo(models.Model):
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class SSHeadingThree(models.Model):
    heading = models.CharField(max_length=100)
    description1 = models.CharField(max_length=1000) 
    description2 = models.CharField(max_length=1000)

    def __str__(self):
        return self.heading

class SSHeadingFour(models.Model):
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading


class OurImages(models.Model):
    heading = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post/')      

    def __str__(self):
        return self.heading

class PaymentPage(models.Model):
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)      

    def __str__(self):
        return self.heading


class LSHeadingOne(models.Model):    
    heading = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post/')     
    description = models.CharField(max_length=1000)  

    def __str__(self):
        return self.heading


        # --------------------------------employment 

class EMHeadingOne(models.Model):
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)      

    def __str__(self):
        return self.heading


class EMHeadingTwo(models.Model):    
    heading = models.CharField(max_length=100)
    video = models.FileField(upload_to="video/%y", default="Add Your Video Here")     
    description = models.CharField(max_length=1000)  

    def __str__(self):
        return self.heading


        # --------------------------------Read Reviews 

class RRHeadingOne(models.Model):
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)      

    def __str__(self):
        return self.heading


class RRHeadingTwo(models.Model):    
    heading = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post/')     
    description = models.CharField(max_length=1000)  

    def __str__(self):
        return self.heading


class TTHeadingOne(models.Model):    
    heading = models.CharField(max_length=100)
    video = models.FileField(upload_to="video/%y", default="Add Your Video Here")     
    description = models.CharField(max_length=1000)  

    def __str__(self):
        return self.heading

class TTHeadingTwo(models.Model):
    heading = models.CharField(max_length=100)
    description1 = models.CharField(max_length=1000) 
    description2 = models.CharField(max_length=1000)   

    def __str__(self):
        return self.heading

class RCHeadingOne(models.Model):
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.heading

class RCHeadingTwo(models.Model):
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class FRHeadingOne(models.Model):
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading

class FRHeadingTwo(models.Model):
    heading = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post/') 
    description = models.CharField(max_length=1000)    

    def __str__(self):
        return self.heading