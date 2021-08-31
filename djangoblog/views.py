from django.core.files.storage import FileSystemStorage
from djangoblog.models import categories,blog
from django.contrib.auth.models import User, auth
from django.db.models.manager import EmptyManager
from django.shortcuts import redirect, render
from django.contrib import messages



# Create your views here.
def index(req):
    firstblog = blog.objects.all().last()
    allblogs = blog.objects.all()
    allcategories = categories.objects.all()

    return render(req, 'index.html',{'cat':allcategories,'blogs':allblogs,'firstblog':firstblog})

def login(req):
    if req.method == "POST":

        uname=req.POST['UserName']
        upass=req.POST['Userpass']

        if uname!='' or upass!='':
            user = auth.authenticate(username=uname, password = upass)
            if user is not None :
                auth.login(req,user)
                return redirect('profile/'+str(user.id)) 
            else:
                messages.info(req,'Login Failed')   
                return redirect('login') 

        else:
            messages.error(req, 'Please fill out the * fields')
            return redirect('login')
            
    else:  
        return render(req, 'login.html')


def signup(req):
        if req.method == "POST":
            uname = req.POST['Username']
            uemail = req.POST['Useremail']
            upass = req.POST['Userpass']
            urepass = req.POST['Userrepass']
            uimage = req.POST['Userimage']
            if uimage is None:
                uimage = "No Imahe Choosed"
            
            if uname == '' or uemail == '' or upass == '' or urepass == '':
                messages.error(req, 'Please fill out the * fields')
                return redirect('signup')
            
            elif upass != urepass:
                messages.error(req, 'PAssword not matching')
                return redirect('signup')
            elif upass == urepass:
                if User.objects.filter(username = uname).exists():
                    messages.info(req, 'Username '+uname+' already exist, Try Something else')
                    return redirect('signup')     
                elif User.objects.filter(email = uemail).exists():
                    messages.info(req, 'User Email '+uemail+' already exist, Try Something else') 
                    return redirect('signup')     
                else:
                    user = User.objects.create_user(username = uname,email = uemail, password = upass)
                    user.save()
                    messages.info(req, 'Your Account has been created You can login now')
                    return redirect('login')        
        else:
            return render(req, 'signup.html')
            
        return render(req, 'signup.html')
    


def profile(req,pk):
    if req.user.is_authenticated:
        userr = User.objects.filter(id=pk).first()
        if userr is None:
            return redirect('/')
        else:
            specificblogs = blog.objects.filter(userid=pk).all()
            totalspecificblogs = blog.objects.filter(userid=pk).count()

            return render(req, 'profile.html', {'user':userr,'sblogs':specificblogs,'totalcount':totalspecificblogs})
    else:
        return redirect('/')

def addblog(req,pk):
    if req.method == "POST":
        title = req.POST['title']
        desc = req.POST.get('desc')
        cat = req.POST['Category']
        usernamee = req.user.username
        userid = req.user.id
        # date = datetime.now()
        if len(req.FILES['blogimage']) ==0:
            blogimage = "No Image has selected"
        else:
            blogimage = req.FILES['blogimage']
        fs = FileSystemStorage()
        filename = fs.save(blogimage.name, blogimage)
        photo = fs.url(filename)

        if title == '' or desc == '' or cat == '':
            messages.info(req, 'Fields with * are Required')
            return redirect('/profile/'+str(req.user.id)+'/addblog')  
        else:
            blogg = blog.objects.create(title=title, desc = desc, category = cat,photo = photo, username = usernamee, userid= userid)
            blogg.save()
            messages.info(req, 'Your Blog  has been Published')
            return redirect('/profile/'+str(req.user.id))  
    else:    
        allcat = categories.objects.all()
        return render(req,'addblog.html',{'pk':pk, 'allcat':allcat})


def logout(req):
    auth.logout(req)
    return redirect('login')