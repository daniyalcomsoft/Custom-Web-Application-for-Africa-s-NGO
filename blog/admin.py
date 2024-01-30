from django.contrib import admin
from django.db.models.lookups import In
from .models import *
# Register your models here.

#or configuration of category admin 
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag','description','url','add_date')
    search_fields = ('title',)

class PostAdminn(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('tittle',)
    list_filter = ('cat',)
    list_per_page = 50

    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js','js/script.js',)

class IndexTopHeadingAdmin(admin.ModelAdmin):
    list_display = ('description','image')

class IndexOfSecondHeadingAdmin(admin.ModelAdmin):
    list_display = ('heading','image','description')
    search_fields = ('heading',)

class IndexOfThirdHeadingAdmin(admin.ModelAdmin):
    list_display = ('heading','image','description')
    search_fields = ('heading',)

class IndexOfFourthHeadingAdmin(admin.ModelAdmin):
    list_display = ('heading','description')
    search_fields = ('heading',)

class MainVideoAdmin(admin.ModelAdmin):
    list_display = ('heading','video','description')
    search_fields = ('heading',)

class IndexOfCommunityHelpAdmin(admin.ModelAdmin):
    list_display = ('heading','image','raisedcommunity','amount','description','date')
    search_fields = ('heading',)

class IndexReviewsHeadingAdmin(admin.ModelAdmin):
    list_display = ('heading','sponsorname')
    search_fields = ('heading',)




class DonateFirstHeadingAdmin(admin.ModelAdmin):
    list_display = ('heading','description')
    search_fields = ('heading',)

class DonateSecHeadingAdmin(admin.ModelAdmin):
    list_display = ('heading','image','description')
    search_fields = ('heading',)

class DonateThirdHeadingAdmin(admin.ModelAdmin):
    list_display = ('name','description','image')
    search_fields = ('name',)

class DonateBigImageAdmin(admin.ModelAdmin):
    list_display = ('description','image')
    search_fields = ('description',)

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('address','phone','email')
    search_fields = ('phone',)

# ------------------------------------About-------------------------------------------------------------------------

class ABFirstHeadingAdmin(admin.ModelAdmin):
    list_display = ('description','image')
    search_fields = ('description',)

class ABSecondHeadingAdmin(admin.ModelAdmin):
    list_display = ('description','logo')
    search_fields = ('description',)

class ABThirdHeadingAdmin(admin.ModelAdmin):
    list_display = ('heading','description')
    search_fields = ('heading',)

class ABFourthHeadingAdmin(admin.ModelAdmin):
    list_display = ('description','image')
    search_fields = ('description',)

class ABFifthHeadingAdmin(admin.ModelAdmin):
    list_display = ('heading','description1','description2')
    search_fields = ('heading',)

class ABSupportImageAdmin(admin.ModelAdmin):
    list_display = ('description','supporterimage')
    search_fields = ('description',)

class ABSixthHeadingAdmin(admin.ModelAdmin):
    list_display = ('heading','description1','description2')
    search_fields = ('heading',)

class ABSeventhHeadingAdmin(admin.ModelAdmin):
    list_display = ('description','image')
    search_fields = ('description',)

class FHeadingOneAdmin(admin.ModelAdmin):
    list_display = ('description','image')
    search_fields = ('description',)

class FHeadingTwoAdmin(admin.ModelAdmin):
    list_display = ('description','image')
    search_fields = ('description',)

class FHeadingThreeAdmin(admin.ModelAdmin):
    list_display = ('heading','reportdescription')
    search_fields = ('heading',)

class FHeadingFourAdmin(admin.ModelAdmin):
    list_display = ('description','image')
    search_fields = ('description',)

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name','image','description')
    search_fields = ('name',)

class VideoAdmin(admin.ModelAdmin):
    list_display = ('caption','video')
    search_fields = ('caption',)

class StoriesAdmin(admin.ModelAdmin):
    list_display = ('name','image', 'description')
    search_fields = ('name',)

# ------------------Sovle Water Crisis----------------

class SCHeadingOneAdmin(admin.ModelAdmin):
    list_display = ('heading', 'description')
    search_fields = ('heading',)

class SCHeadingTwoAdmin(admin.ModelAdmin):
    list_display = ('heading', 'description')
    search_fields = ('heading',)

class SCHeadingThreeAdmin(admin.ModelAdmin):
    list_display = ('heading','image', 'description')
    search_fields = ('heading',)

class SCHeadingFourAdmin(admin.ModelAdmin):
    list_display = ('heading','image', 'description')
    search_fields = ('heading',)

class SCHeadingFiveAdmin(admin.ModelAdmin):
    list_display = ('heading', 'description')
    search_fields = ('heading',)

class SCHeadingSixAdmin(admin.ModelAdmin):
    list_display = ('heading','image', 'description')
    search_fields = ('heading',)

class SCHeadingSevenAdmin(admin.ModelAdmin):
    list_display = ('heading','description1', 'description2')
    search_fields = ('heading',)

class SCHeadingEightAdmin(admin.ModelAdmin):
    list_display = ('heading', 'description')
    search_fields = ('heading',)

    # -----------------------------------------water promise---------------------------------

class WPHeadingOneAdmin(admin.ModelAdmin):
    list_display = ('heading', 'description')
    search_fields = ('heading',)

class WPHeadingTwoAdmin(admin.ModelAdmin):
    list_display = ('heading','image', 'description')
    search_fields = ('heading',)

class WPHeadingThreeAdmin(admin.ModelAdmin):
    list_display = ('heading','image', 'description')
    search_fields = ('heading',)

class WPHeadingFourAdmin(admin.ModelAdmin):
    list_display = ('heading','image', 'description')
    search_fields = ('heading',)

class WPHeadingFiveAdmin(admin.ModelAdmin):
    list_display = ('heading','image', 'description')
    search_fields = ('heading',)

class WPHeadingSixAdmin(admin.ModelAdmin):
    list_display = ('heading', 'description')
    search_fields = ('heading',)

    # ------------------------------------------------make a donation

class MDHeadingOneAdmin(admin.ModelAdmin):
    list_display = ('heading', 'description')
    search_fields = ('heading',)

class MDHeadingTwoAdmin(admin.ModelAdmin):
    list_display = ('heading','image', 'description')
    search_fields = ('heading',)

class MDHeadingThreeAdmin(admin.ModelAdmin):
    list_display = ('heading', 'description')
    search_fields = ('heading',)


    # ------------------------------------------------give monthly

class GMHeadingOneAdmin(admin.ModelAdmin):
    list_display = ('heading', 'description')
    search_fields = ('heading',)

class GMHeadingTwoAdmin(admin.ModelAdmin):
    list_display = ('heading','image', 'description')
    search_fields = ('heading',)

class GMHeadingThreeAdmin(admin.ModelAdmin):
    list_display = ('heading', 'description')
    search_fields = ('heading',)



    # ------------------------------------------------Sponsor Community

class SCMHeadingOneAdmin(admin.ModelAdmin):
    list_display = ('heading', 'description')
    search_fields = ('heading',)

class SCMHeadingTwoAdmin(admin.ModelAdmin):
    list_display = ('heading','image', 'amount')
    search_fields = ('heading',)

class SCMHeadingThreeAdmin(admin.ModelAdmin):
    list_display = ('heading', 'description')
    search_fields = ('heading',)

class SCMHeadingFourAdmin(admin.ModelAdmin):
    list_display = ('heading', 'description')
    search_fields = ('heading',)


# ---------------------------------------------------Corporate Sponsorship

class CSHeadingOneAdmin(admin.ModelAdmin):
    list_display = ('heading', 'description')
    search_fields = ('heading',)

# -------------------------------------------water crisis------------------------------

class WCHeadingOneAdmin(admin.ModelAdmin):
    list_display = ('heading', 'description')
    search_fields = ('heading',)

class WCHeadingTwoAdmin(admin.ModelAdmin):
    list_display = ('heading', 'description')
    search_fields = ('heading',)

class WCHeadingThreeAdmin(admin.ModelAdmin):
    list_display = ('heading','image', 'description')
    search_fields = ('heading',)

class WCHeadingFourAdmin(admin.ModelAdmin):
    list_display = ('heading','image', 'description')
    search_fields = ('heading',)

class WCHeadingFiveAdmin(admin.ModelAdmin):
    list_display = ('heading', 'education', 'health', 'hunger', 'poverty')
    search_fields = ('heading',)

class WCHeadingSixAdmin(admin.ModelAdmin):
    list_display = ('heading', 'description')
    search_fields = ('heading',)

class WCHeadingSevenAdmin(admin.ModelAdmin):
    list_display = ('heading','image', 'description')
    search_fields = ('heading',)

class WCHeadingEightAdmin(admin.ModelAdmin):
    list_display = ('caption','heading', 'video')
    search_fields = ('caption',)

# -----------------------------------------------covid-19-----------------------------------------------

class CDHeadingOneAdmin(admin.ModelAdmin):
    list_display = ('heading', 'description')
    search_fields = ('heading',)

class CDHeadingTwoAdmin(admin.ModelAdmin):
    list_display = ('heading','image', 'description')
    search_fields = ('heading',)

class CDHeadingThreeAdmin(admin.ModelAdmin):
    list_display = ('heading', 'description')
    search_fields = ('heading',)

class CDHeadingFourAdmin(admin.ModelAdmin):
    list_display = ('heading','description')
    search_fields = ('heading',)

class CDHeadingFiveAdmin(admin.ModelAdmin):
    list_display = ('heading','image', 'description','dateandday')
    search_fields = ('heading',)

# ------------------------------------------water and Health------------------------------------------

class WHHeadingOneAdmin(admin.ModelAdmin):
    list_display = ('heading','description1', 'description2')
    search_fields = ('heading',)

class WHHeadingTwoAdmin(admin.ModelAdmin):
    list_display = ('heading','description')
    search_fields = ('heading',)

class WHHeadingThreeAdmin(admin.ModelAdmin):
    list_display = ('heading','image','description')
    search_fields = ('heading',)

class WHHeadingFourAdmin(admin.ModelAdmin):
    list_display = ('heading','description1','description2')
    search_fields = ('heading',)

class WHHeadingFiveAdmin(admin.ModelAdmin):
    list_display = ('heading','description')
    search_fields = ('heading',)

class WHHeadingSixAdmin(admin.ModelAdmin):
    list_display = ('heading','description')
    search_fields = ('heading',)

# --------------------------------------------------Water and Education

class WEHeadingOneAdmin(admin.ModelAdmin):
    list_display = ('heading','image','description')
    search_fields = ('heading',)

class WEHeadingTwoAdmin(admin.ModelAdmin):
    list_display = ('heading','description')
    search_fields = ('heading',)

class WEHeadingThreeAdmin(admin.ModelAdmin):
    list_display = ('heading','description')
    search_fields = ('heading',)

# --------------------------------water and hunger------------------


class HUNHeadingOneAdmin(admin.ModelAdmin):
    list_display = ('heading','description')
    search_fields = ('heading',)

class HUNHeadingTwoAdmin(admin.ModelAdmin):
    list_display = ('heading','description')
    search_fields = ('heading',)


class HUNHeadingThreeAdmin(admin.ModelAdmin):
    list_display = ('heading','description')
    search_fields = ('heading',)

class HUNHeadingFourAdmin(admin.ModelAdmin):
    list_display = ('heading','description')
    search_fields = ('heading',)




class PWHeadingOneAdmin(admin.ModelAdmin):
    list_display = ('heading','description1','description2')
    search_fields = ('heading',)

class PWHeadingTwoAdmin(admin.ModelAdmin):
    list_display = ('heading','description')
    search_fields = ('heading',)

class PWHeadingThreeAdmin(admin.ModelAdmin):
    list_display = ('heading','description1','description2')
    search_fields = ('heading',)

class PWHeadingFourAdmin(admin.ModelAdmin):
    list_display = ('heading','description')
    search_fields = ('heading',)

class PWHeadingFiveAdmin(admin.ModelAdmin):
    list_display = ('heading','description1','description2')
    search_fields = ('heading',)

class PWHeadingSixAdmin(admin.ModelAdmin):
    list_display = ('heading','description')
    search_fields = ('heading',)

class PWHeadingSevenAdmin(admin.ModelAdmin):
    list_display = ('heading','description1','description2')
    search_fields = ('heading',)

class PWMidImageAdmin(admin.ModelAdmin):
    list_display = ('heading','image')
    search_fields = ('heading',)

class PWBottomImageAdmin(admin.ModelAdmin):
    list_display = ('heading','image')
    search_fields = ('heading',)

class WSHeadingOneAdmin(admin.ModelAdmin):
    list_display = ('heading','description')
    search_fields = ('heading',)

class WSTopImageAdmin(admin.ModelAdmin):
    list_display = ('heading','image')
    search_fields = ('heading',)

class WSBottomImageAdmin(admin.ModelAdmin):
    list_display = ('heading','image')
    search_fields = ('heading',)

class SSHeadingOneAdmin(admin.ModelAdmin):
    list_display = ('heading','video','description')
    search_fields = ('heading',)

class SSHeadingTwoAdmin(admin.ModelAdmin):
    list_display = ('heading','description')
    search_fields = ('heading',)

class SSHeadingThreeAdmin(admin.ModelAdmin):
    list_display = ('heading','description1','description2')
    search_fields = ('heading',)

class SSHeadingFourAdmin(admin.ModelAdmin):
    list_display = ('heading','description')
    search_fields = ('heading',)

class OurImagesAdmin(admin.ModelAdmin):
    list_display = ('heading','image')
    search_fields = ('heading',)

class PaymentPageAdmin(admin.ModelAdmin):
    list_display = ('heading','description')
    search_fields = ('heading',)

class LSHeadingOneAdmin(admin.ModelAdmin):
    list_display = ('heading','image','description')
    search_fields = ('heading',)

class EMHeadingOneAdmin(admin.ModelAdmin):
    list_display = ('heading','description')
    search_fields = ('heading',)

class EMHeadingTwoAdmin(admin.ModelAdmin):
    list_display = ('heading','video','description')
    search_fields = ('heading',)

class RRHeadingOneAdmin(admin.ModelAdmin):
    list_display = ('heading','description')
    search_fields = ('heading',)

class RRHeadingTwoAdmin(admin.ModelAdmin):
    list_display = ('heading','image','description')
    search_fields = ('heading',)

class TTHeadingOneAdmin(admin.ModelAdmin):
    list_display = ('heading','video','description')
    search_fields = ('heading',)

class TTHeadingTwoAdmin(admin.ModelAdmin):
    list_display = ('heading','description1','description2')
    search_fields = ('heading',)

class RCHeadingOneAdmin(admin.ModelAdmin):
    list_display = ('heading','description')
    search_fields = ('heading',)

class RCHeadingTwoAdmin(admin.ModelAdmin):
    list_display = ('heading','description')
    search_fields = ('heading',)

class FRHeadingOneAdmin(admin.ModelAdmin):
    list_display = ('heading','description')
    search_fields = ('heading',)

class FRHeadingTwoAdmin(admin.ModelAdmin):
    list_display = ('heading','image','description')
    search_fields = ('heading',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdminn)
admin.site.register(IndexTopHeading, IndexTopHeadingAdmin)
admin.site.register(IndexOfSecondHeading, IndexOfSecondHeadingAdmin)
admin.site.register(IndexOfThirdHeading, IndexOfThirdHeadingAdmin)
admin.site.register(MainVideo, MainVideoAdmin)
admin.site.register(IndexOfFourthHeading, IndexOfFourthHeadingAdmin)
admin.site.register(IndexOfCommunityHelp, IndexOfCommunityHelpAdmin)
admin.site.register(IndexReviewsHeading, IndexReviewsHeadingAdmin)
admin.site.register(DonateFirstHeading, DonateFirstHeadingAdmin)
admin.site.register(DonateSecHeading, DonateSecHeadingAdmin)
admin.site.register(DonateThirdHeading, DonateThirdHeadingAdmin)
admin.site.register(DonateBigImage, DonateBigImageAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(ABFirstHeading, ABFirstHeadingAdmin)

admin.site.register(ABSecondHeading, ABSecondHeadingAdmin)
admin.site.register(ABThirdHeading, ABThirdHeadingAdmin)
admin.site.register(ABFourthHeading, ABFourthHeadingAdmin)
admin.site.register(ABFifthHeading, ABFifthHeadingAdmin)
admin.site.register(ABSupportImage, ABSupportImageAdmin)
admin.site.register(ABSixthHeading, ABSixthHeadingAdmin)
admin.site.register(ABSeventhHeading, ABSeventhHeadingAdmin)

admin.site.register(FHeadingOne, FHeadingOneAdmin)
admin.site.register(FHeadingTwo, FHeadingTwoAdmin)
admin.site.register(FHeadingThree, FHeadingThreeAdmin)
admin.site.register(FHeadingFour, FHeadingFourAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Stories, StoriesAdmin)

admin.site.register(SCHeadingOne, SCHeadingOneAdmin)
admin.site.register(SCHeadingTwo, SCHeadingTwoAdmin)
admin.site.register(SCHeadingThree, SCHeadingThreeAdmin)
admin.site.register(SCHeadingFour, SCHeadingFourAdmin)
admin.site.register(SCHeadingFive, SCHeadingFiveAdmin)
admin.site.register(SCHeadingSix, SCHeadingSixAdmin)
admin.site.register(SCHeadingSeven, SCHeadingSevenAdmin)
admin.site.register(SCHeadingEight, SCHeadingEightAdmin)

admin.site.register(WPHeadingOne, WPHeadingOneAdmin)
admin.site.register(WPHeadingTwo, WPHeadingTwoAdmin)
admin.site.register(WPHeadingThree, WPHeadingThreeAdmin)
admin.site.register(WPHeadingFour, WPHeadingFourAdmin)
admin.site.register(WPHeadingFive, WPHeadingFiveAdmin)
admin.site.register(WPHeadingSix, WPHeadingSixAdmin)

admin.site.register(MDHeadingOne, MDHeadingOneAdmin)
admin.site.register(MDHeadingTwo, MDHeadingTwoAdmin)
admin.site.register(MDHeadingThree, MDHeadingThreeAdmin)

admin.site.register(GMHeadingOne, GMHeadingOneAdmin)
admin.site.register(GMHeadingTwo, GMHeadingTwoAdmin)
admin.site.register(GMHeadingThree, GMHeadingThreeAdmin)

admin.site.register(SCMHeadingOne, SCMHeadingOneAdmin)
admin.site.register(SCMHeadingTwo, SCMHeadingTwoAdmin)
admin.site.register(SCMHeadingThree, SCMHeadingThreeAdmin)
admin.site.register(SCMHeadingFour, SCMHeadingFourAdmin)

admin.site.register(CSHeadingOne, CSHeadingOneAdmin)

admin.site.register(WCHeadingOne, WCHeadingOneAdmin)
admin.site.register(WCHeadingTwo, WCHeadingTwoAdmin)
admin.site.register(WCHeadingThree, WCHeadingThreeAdmin)
admin.site.register(WCHeadingFour, WCHeadingFourAdmin)
admin.site.register(WCHeadingFive, WCHeadingFiveAdmin)
admin.site.register(WCHeadingSix, WCHeadingSixAdmin)
admin.site.register(WCHeadingSeven, WCHeadingSevenAdmin)
admin.site.register(WCHeadingEight, WCHeadingEightAdmin)

admin.site.register(CDHeadingOne, CDHeadingOneAdmin)
admin.site.register(CDHeadingTwo, CDHeadingTwoAdmin)
admin.site.register(CDHeadingThree, CDHeadingThreeAdmin)
admin.site.register(CDHeadingFour, CDHeadingFourAdmin)
admin.site.register(CDHeadingFive, CDHeadingFiveAdmin)

admin.site.register(WHHeadingOne,WHHeadingOneAdmin)
admin.site.register(WHHeadingTwo,WHHeadingTwoAdmin)
admin.site.register(WHHeadingThree,WHHeadingThreeAdmin)
admin.site.register(WHHeadingFour,WHHeadingFourAdmin)
admin.site.register(WHHeadingFive,WHHeadingFiveAdmin)
admin.site.register(WHHeadingSix,WHHeadingSixAdmin)

admin.site.register(WEHeadingOne, WEHeadingOneAdmin)
admin.site.register(WEHeadingTwo, WEHeadingTwoAdmin)
admin.site.register(WEHeadingThree, WEHeadingThreeAdmin)

admin.site.register(HUNHeadingOne, HUNHeadingOneAdmin)
admin.site.register(HUNHeadingTwo, HUNHeadingTwoAdmin)
admin.site.register(HUNHeadingThree, HUNHeadingThreeAdmin)
admin.site.register(HUNHeadingFour, HUNHeadingFourAdmin)


admin.site.register(PWHeadingOne, PWHeadingOneAdmin)
admin.site.register(PWHeadingTwo, PWHeadingTwoAdmin)
admin.site.register(PWHeadingThree, PWHeadingThreeAdmin)
admin.site.register(PWHeadingFour, PWHeadingFourAdmin)
admin.site.register(PWHeadingFive, PWHeadingFiveAdmin)
admin.site.register(PWHeadingSix, PWHeadingSixAdmin)
admin.site.register(PWHeadingSeven, PWHeadingSevenAdmin)
admin.site.register(PWMidImage, PWMidImageAdmin)
admin.site.register(PWBottomImage, PWBottomImageAdmin)

admin.site.register(WSTopImage, WSTopImageAdmin)
admin.site.register(WSBottomImage, WSBottomImageAdmin)
admin.site.register(WSHeadingOne, WSHeadingOneAdmin)

admin.site.register(SSHeadingOne, SSHeadingOneAdmin)
admin.site.register(SSHeadingTwo, SSHeadingTwoAdmin)
admin.site.register(SSHeadingThree, SSHeadingThreeAdmin)
admin.site.register(SSHeadingFour, SSHeadingFourAdmin)


admin.site.register(OurImages, OurImagesAdmin)
admin.site.register(PaymentPage, PaymentPageAdmin)
admin.site.register(LSHeadingOne, LSHeadingOneAdmin)
admin.site.register(EMHeadingOne, EMHeadingOneAdmin)
admin.site.register(EMHeadingTwo, EMHeadingTwoAdmin)
admin.site.register(RRHeadingOne, RRHeadingOneAdmin)
admin.site.register(RRHeadingTwo, RRHeadingTwoAdmin)
admin.site.register(TTHeadingOne, TTHeadingOneAdmin)
admin.site.register(TTHeadingTwo, TTHeadingTwoAdmin)

admin.site.register(RCHeadingOne, RCHeadingOneAdmin)
admin.site.register(RCHeadingTwo, RCHeadingTwoAdmin)

admin.site.register(FRHeadingOne, FRHeadingOneAdmin)
admin.site.register(FRHeadingTwo, FRHeadingTwoAdmin)