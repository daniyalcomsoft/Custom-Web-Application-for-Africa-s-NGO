from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import *
from paypal.standard.forms import PayPalPaymentsForm
from django.shortcuts import reverse

# Create your views here.
def index(request):
    ith = IndexTopHeading.objects.all()
    ish = IndexOfSecondHeading.objects.all()
    ithd = IndexOfThirdHeading.objects.all()
    videos=MainVideo.objects.all()
    ifh = IndexOfFourthHeading.objects.all()
    chelp = IndexOfCommunityHelp.objects.all()
    irh = IndexReviewsHeading.objects.all()
    pp = PaymentPage.objects.all()
    return render(request, 'index.html',{'ith':ith, 'ish':ish, 'ithd':ithd, 'videos':videos, 'ifh':ifh, 'chelp':chelp,'irh':irh, 'pp':pp})



def home(request):
    #load all the post from databse
    posts = Post.objects.all()[:11]
    cats = Category.objects.all()
    data = {
        'posts' : posts,
        'cats' : cats
    }
    return render(request, 'home.html', data)

def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()
    return render(request, 'posts.html', {'post':post, 'cats':cats})

def category(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat = cat)
    return render(request, "category.html", {'cat':cat,'posts':posts})

def blogs(request):
    #load all the post from databse
    posts = Post.objects.all()[:11]
    cats = Category.objects.all()
    data = {
        'posts' : posts,
        'cats' : cats
    }
    return render(request, 'blogs.html', data)

def donate(request):
    dfh = DonateFirstHeading.objects.all()
    dsh = DonateSecHeading.objects.all()
    dth = DonateThirdHeading.objects.all()
    dbi = DonateBigImage.objects.all()
    pp = PaymentPage.objects.all()
    return render(request, 'donate.html', {'dfh': dfh,'dsh': dsh, 'dth':dth, 'dbi':dbi, 'pp':pp})

def contact(request):
    con = ContactUs.objects.all()
    return render(request, 'contact.html', {'con':con}) 

def about(request):
    ab1 = ABFirstHeading.objects.all()
    ab2 = ABSecondHeading.objects.all()
    ab3 = ABThirdHeading.objects.all()
    ab4 = ABFourthHeading.objects.all()
    ab5 = ABFifthHeading.objects.all()
    supp = ABSupportImage.objects.all()
    ab6 = ABSixthHeading.objects.all()
    ab7 = ABSeventhHeading.objects.all()
    return render(request, 'about.html', {'ab1':ab1, 'ab2':ab2, 'ab3':ab3, 'ab4':ab4, 'ab5':ab5, 'supp':supp, 'ab6':ab6, 'ab7':ab7})

def financials(request):
    fh1 = FHeadingOne.objects.all()
    fh2 = FHeadingTwo.objects.all()
    fh3 = FHeadingThree.objects.all()
    fh4 = FHeadingFour.objects.all()     
    return render(request, 'financials.html', {'fh1':fh1,'fh2':fh2, 'fh3':fh3, 'fh4':fh4})

def ourteam(request):
    tem = Team.objects.all()
    return render(request, 'ourteam.html', {'tem':tem})

def video(request):
    videos=Video.objects.all()
    return render(request, 'video.html', {'videos':videos})

def stories(request):
    story = Stories.objects.all()
    return render(request, 'stories.html', {'story':story})

def solvecrisis(request):
    sc1 = SCHeadingOne.objects.all()
    sc2 = SCHeadingTwo.objects.all()
    sc3 = SCHeadingThree.objects.all()
    sc4 = SCHeadingFour.objects.all()
    sc5 = SCHeadingFive.objects.all()
    sc6 = SCHeadingSix.objects.all()
    sc7 = SCHeadingSeven.objects.all()
    sc8 = SCHeadingEight.objects.all()
    return render(request, 'solvecrisis.html', {'sc1':sc1,'sc2':sc2,'sc3':sc3,'sc4':sc4,'sc5':sc5,'sc6':sc6,'sc7':sc7,'sc8':sc8})

def promise(request):
    wp1  = WPHeadingOne.objects.all()
    wp2  = WPHeadingTwo.objects.all()
    wp3  = WPHeadingThree.objects.all()
    wp4  = WPHeadingFour.objects.all()
    wp5  = WPHeadingFive.objects.all()
    wp6  = WPHeadingSix.objects.all()
    return render(request, 'promise.html', {'wp1':wp1,'wp2':wp2,'wp3':wp3,'wp4':wp4,'wp5':wp5,'wp6':wp6})



def donation(request):
    md1 = MDHeadingOne.objects.all()
    md2 = MDHeadingTwo.objects.all()
    md3 = MDHeadingThree.objects.all()
    pp = PaymentPage.objects.all()
    return render(request, 'donation.html', {'md1':md1,'md2':md2,'md3':md3, 'pp':pp})



def monthly(request):
    gm1 = GMHeadingOne.objects.all()
    gm2 = GMHeadingTwo.objects.all()
    gm3 = GMHeadingThree.objects.all()
    pp = PaymentPage.objects.all()
    return render(request, 'monthly.html', {'gm1':gm1,'gm2':gm2,'gm3':gm3,'pp':pp})

def community(request):
    scm1 = SCMHeadingOne.objects.all()
    scm2 = SCMHeadingTwo.objects.all()
    scm3 = SCMHeadingThree.objects.all()
    scm4 = SCMHeadingFour.objects.all()
    return render(request, 'community.html', {'scm1':scm1,'scm2':scm2,'scm3':scm3,'scm4':scm4})

def sponsorship(request):
    cs1 = CSHeadingOne.objects.all()
    return render(request, 'sponsorship.html', {'cs1':cs1})


def watercrisis(request):
    wc1 = WCHeadingOne.objects.all()
    wc2 = WCHeadingTwo.objects.all()
    wc3 = WCHeadingThree.objects.all()
    wc4 = WCHeadingFour.objects.all()
    wc5 = WCHeadingFive.objects.all()
    wc6 = WCHeadingSix.objects.all()
    wc7 = WCHeadingSeven.objects.all()
    wc8 = WCHeadingEight.objects.all()
    return render(request, 'watercrisis.html', {'wc1':wc1,'wc2':wc2,'wc3':wc3,'wc4':wc4,'wc5':wc5,'wc6':wc6,'wc7':wc7,'wc8':wc8,})
    

def covid(request):
    cd1 = CDHeadingOne.objects.all()
    cd2 = CDHeadingTwo.objects.all() 
    cd3 = CDHeadingThree.objects.all()
    cd4 = CDHeadingFour.objects.all()
    cd5 = CDHeadingFive.objects.all()    
    return render(request, 'covid.html', {'cd1':cd1,'cd2':cd2,'cd3':cd3,'cd4':cd4,'cd5':cd5})

def waterhealth(request):
    wh1 = WHHeadingOne.objects.all()
    wh2 = WHHeadingTwo.objects.all()
    wh3 = WHHeadingThree.objects.all()
    wh4 = WHHeadingFour.objects.all()
    wh5 = WHHeadingFive.objects.all()
    wh6 = WHHeadingSix.objects.all()
    return render(request, 'waterhealth.html', {'wh1':wh1,'wh2':wh2,'wh3':wh3,'wh4':wh4,'wh5':wh5,'wh6':wh6,})

def watereducation(request):
    we1 = WEHeadingOne.objects.all()
    we2 = WEHeadingTwo.objects.all()
    we3 = WEHeadingThree.objects.all()
    return render(request, 'watereducation.html', {'we1':we1,'we2':we2,'we3':we3})

def hunger(request):
    hun1 = HUNHeadingOne.objects.all()
    hun2 = HUNHeadingTwo.objects.all()
    hun3 = HUNHeadingThree.objects.all()
    hun4 = HUNHeadingFour.objects.all()
    return render(request, 'hunger.html', {'hun1':hun1, 'hun2':hun2, 'hun3':hun3, 'hun4':hun4})

def poverty(request):
    pw1 = PWHeadingOne.objects.all()
    pw2 = PWHeadingTwo.objects.all()
    pw3 = PWHeadingThree.objects.all()
    pw4 = PWHeadingFour.objects.all()
    pw5 = PWHeadingFive.objects.all()
    pw6 = PWHeadingSix.objects.all()
    pw7 = PWHeadingSeven.objects.all()
    pmi = PWMidImage.objects.all()
    pbi = PWBottomImage.objects.all()
    return render(request, 'poverty.html',{'pw1':pw1,'pw2':pw2,'pw3':pw3,'pw4':pw4,'pw5':pw5,'pw6':pw6,'pw7':pw7,'pmi':pmi,'pbi':pbi})
    
def scarcity(request):
    ws1 = WSHeadingOne.objects.all()
    wsti = WSTopImage.objects.all()
    wsbi = WSBottomImage.objects.all()
    return render(request, 'scarcity.html', {'ws1':ws1, 'wsti':wsti, 'wsbi':wsbi})

def statistics(request):
    ss1 = SSHeadingOne.objects.all()
    ss2 = SSHeadingTwo.objects.all()
    ss3 = SSHeadingThree.objects.all()
    ss4 = SSHeadingFour.objects.all()
    return render(request, 'statistics.html',{'ss1':ss1,'ss2':ss2,'ss3':ss3,'ss4':ss4})

def images(request):
    ou = OurImages.objects.all()
    return render(request, 'images.html', {'ou':ou})

def payment(request):
    return render(request, 'payment.html')

def process_payment(request):
    # order_id = request.session.get('order_id')
    # order = get_object_or_404(Order, id=order_id)
    # host = request.get_host()
    pp = PaymentPage.objects.all()
    paypal_dict = {
        'business': 'info@houseofgreensint.org',
        'amount': '',        
        'invoice': "",
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format('www.houseofgreensint.org',reverse('paypal-ipn')),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'process_payment.html', {'form': form, 'pp':pp})

def leader(request):
    ls = LSHeadingOne.objects.all()
    return render(request, 'leader.html', {'ls':ls})

def employment(request):
    em1 = EMHeadingOne.objects.all()
    em2 = EMHeadingTwo.objects.all()
    return render(request, 'employment.html', {'em1':em1, 'em2':em2})

def reviews(request):
    rr1 = RRHeadingOne.objects.all()
    rr2 = RRHeadingTwo.objects.all()
    return render(request, 'reviews.html', {'rr1':rr1, 'rr2':rr2})

def teaching(request):
    tt1 = TTHeadingOne.objects.all()
    tt2 = TTHeadingTwo.objects.all()
    return render(request, 'teaching.html', {'tt1':tt1, 'tt2':tt2})

def research(request): 
    rc1 = RCHeadingOne.objects.all()
    rc2 = RCHeadingTwo.objects.all()
    return render(request, 'research.html', {'rc1':rc1, 'rc2':rc2})

def fund(request):
    fr1 = FRHeadingOne.objects.all()
    fr2 = FRHeadingTwo.objects.all()
    return render(request, 'fund.html', {'fr1':fr1, 'fr2':fr2})
