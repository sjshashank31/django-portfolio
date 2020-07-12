from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, get_list_or_404
from .models import UserInfo, Study, Skill, Service, Work, Experience
from .forms import InfoForm, SkillForm, EducationForm, ServiceForm, WorkForm, ExperienceForm, GetUserForm
from .util import render_to_pdf
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request, slug):
    try:
        context = {}
        context['info'] = UserInfo.objects.get(slug=slug)
        name = UserInfo.objects.get(slug=slug)
        context['education'] = Study.objects.filter(slug=name).all()
        context['skill'] = Skill.objects.filter(slug=name).all()
        context['service'] = Service.objects.filter(slug=name).all()
        context['work'] = Work.objects.filter(slug=name).all()
        context['experience'] = Experience.objects.filter(slug=name).all()
        context['exp_count'] = len(context['experience'])
        context['project_count'] = len(context['work'])

        return render(request, 'index.html',  context)
    except:
        return  HttpResponse("Portfolio Not Found with this Url")

def home(request):
    context = {}
    if request.user.is_authenticated:
        context['portfolio'] = UserInfo.objects.filter(user=request.user).all()
    return render(request, 'home.html', context)


@login_required
def detail_view(request, slug):
    context = {}
    context['details'] = UserInfo.objects.get(slug=slug)
    return render(request, 'details.html', context)


@login_required
def skill_detail_view(request, slug):
    try:
        details = Skill.objects.filter(slug__slug=slug).all()
        return render(request, 'skills_details.html', {'details': details, 'slug': slug})
    except Exception as e:
        print(e)
        return HttpResponse("User  not found or has been deleted ")


@login_required
def education_detail_view(request, slug):
    try:
        details = Study.objects.filter(slug__slug=slug).all()
        return render(request, 'education_details.html', {'details': details, 'slug': slug})
    except:
        return HttpResponse("USER NOT FOUND")


@login_required
def service_detail_view(request, slug):
    try:
        details = Service.objects.filter(slug__slug=slug).all()
        return render(request, 'service_details.html', {'details': details, 'slug': slug})
    except:
        return HttpResponse("User Not Found")


@login_required
def work_detail_view(request, slug):
    try:
        details = Work.objects.filter(slug__slug=slug).all()
        return render(request, 'work_details.html', {'details': details, 'slug': slug})
    except:
        return HttpResponse("User Not Found")


@login_required
def experience_detail_view(request, slug):
    try:
        details = Experience.objects.filter(slug__slug=slug).all()
        return render(request, 'experience_details.html', {'details': details, 'slug': slug})
    except:
        HttpResponse("User Not Found")


@login_required
def create_info(request):
    # add the dictionary during initialization
    try:
        if request.method == "POST":
            form = InfoForm(request.POST, request.FILES)
            if form.is_valid():
                name = form.cleaned_data.get('name')
                profile_picture = form.cleaned_data.get('profile_picture')
                email = form.cleaned_data.get('email')
                about = form.cleaned_data.get('about')
                mobile_no = form.cleaned_data.get('mobile_no')
                profession = form.cleaned_data.get('profession')
                place = form.cleaned_data.get('place')

                user = UserInfo.objects.create(user=request.user,
                                               name=name,
                                               profile_picture=profile_picture,
                                               email=email,
                                               about=about,
                                               mobile_no=mobile_no,
                                               profession=profession,
                                               place=place,

                                               )

                user.slug_save()
                messages.success(request, "Your profile is Created")
                return redirect('home:detail', slug=user.get_slug())

        form = InfoForm()
        return render(request, "infoform.html", {'form': form})
    except:
        return HttpResponse("Something wen wrong")


@login_required
def skill_info(request, slug):
    try:
        if request.method == "POST":
            form = SkillForm(request.POST)
            slug = UserInfo.objects.get(user=request.user, slug=slug)
            if form.is_valid():
                skill = form.cleaned_data.get('skill')
                percent = form.cleaned_data.get('percent')
                if not Skill.objects.filter(user=request.user, slug__slug=slug, skill=skill):
                    skills = Skill(user=request.user, slug=slug, skill=skill, percent=percent)
                    skills.save()
                    messages.success(request, "Your skill is registered")
                    return redirect('home:skill-details', slug=slug)
                else:
                    return HttpResponse("<h3>You already have registered this skill"
                                        " go and edit if you want......go back</h3>")
            else:
                messages.error(request, "You filled wrong information")

        form = SkillForm()
        return render(request, "skill_form.html", {'form': form, 'slug': slug})
    except Exception as e:
        print(e)
        return HttpResponse("Something went wrong")


@login_required
def education_info(request, slug):
    try:
        if request.method == "POST":
            form = EducationForm(request.POST)
            slug = UserInfo.objects.get(user=request.user, slug=slug)
            if form.is_valid():
                board = form.cleaned_data.get('board_or_univ')
                course = form.cleaned_data.get('course')
                school_clg = form.cleaned_data.get('school_or_college')
                cgpa_percent = form.cleaned_data.get('cgpa_or_percent')
                cgpa = form.cleaned_data.get('cgpa')
                education = Study(user=request.user,
                                  slug=slug,
                                  board_or_univ=board,
                                  course=course,
                                  school_or_college=school_clg,
                                  cgpa_or_percent=cgpa_percent,
                                  cgpa=cgpa)
                education.save()
                messages.success(request, "Your Qualification detail is registered")
                return redirect('home:education-details', slug=slug)

        form = EducationForm()
        return render(request, "education_form.html", {'form': form, 'slug':slug})
    except Exception as e:
        print(e)
        return HttpResponse("Something went wrong")


@login_required
def service_info(request, slug):
    try:
        if request.method == "POST":
            form = ServiceForm(request.POST)
            slug = UserInfo.objects.get(user=request.user, slug=slug)
            if form.is_valid():
                service_name = form.cleaned_data.get('service_name')
                description = form.cleaned_data.get('description')
                service = Service(user=request.user, slug=slug, service_name=service_name, description=description )
                service.save()
                messages.success(request, "Your service detail is registered")
                return redirect('home:service-details', slug=slug)

        form = ServiceForm()
        return render(request, "service_form.html", {'form': form, 'slug': slug})
    except Exception as e:
        print(e)
        return HttpResponse("Something went wrong")


@login_required
def work_info(request, slug):
    try:
        if request.method == "POST":
            form = WorkForm(request.POST, request.FILES)
            slug = UserInfo.objects.get(user=request.user, slug=slug)
            if form.is_valid():
                project_name = form.cleaned_data.get('project_name')
                project_type = form.cleaned_data.get('project_type')
                project_link = form.cleaned_data.get('project_link')
                project_image = form.cleaned_data.get('project_image')
                work = Work(user=request.user,
                            slug=slug,
                            project_name=project_name,
                            project_type=project_type,
                            project_link=project_link,
                            project_image=project_image)
                work.save()
                messages.success(request, "Your work is registered")
                return redirect('home:work-details', slug=slug)

        form = WorkForm()
        return render(request, "work_form.html", {'form': form, 'slug':slug})

    except Exception as e:
        print(e)
        return HttpResponse("Something went wrong")


@login_required
def experience_info(request, slug):
    try:
        if request.method == "POST":
            form = ExperienceForm(request.POST, request.FILES)
            slug = UserInfo.objects.get(user=request.user, slug=slug)
            if form.is_valid():
                organisation_name = form.cleaned_data.get('organisation_name')
                post = form.cleaned_data.get('post')
                joining_date = form.cleaned_data.get('joining_date')
                ending_date = form.cleaned_data.get('ending_date')
                work_experience = form.cleaned_data.get('work_experience')
                if not Experience.objects.filter(user=request.user, slug__slug=slug, organisation_name=organisation_name):
                    exp = Experience(user=request.user,
                                     slug=slug,
                                     organisation_name=organisation_name,
                                     post=post,
                                     joining_date=joining_date,
                                     ending_date=ending_date,
                                     work_experience=work_experience)
                    exp.save()
                    messages.success(request, "Your Experienceis registered")
                    return redirect('home:experience-details', slug=slug)
                else:
                    return HttpResponse("You are already registered with this company go back")

        form = ExperienceForm()
        return render(request, "experience_form.html", {'form': form, 'slug':slug})
    except Exception as e:
        print(e)
        return HttpResponse("Something went wrong")


@login_required
def get_user(request):
    try:
        context = {}
        context['details'] = UserInfo.objects.filter(user=request.user).all()
        return render(request, 'already_user.html', context)
    except:
        return HttpResponse("User is not registered")


@login_required
def update_info(request, slug):

        obj = get_object_or_404(UserInfo, slug=slug)
        form = InfoForm(request.POST or None, request.FILES, instance=obj)
        # save the data from the form and
        # redirect to detail_view
        if form.is_valid():
            form.save()
            messages.success(request, "Your Information is updated")
            return redirect('home:detail', slug=slug)

            # add form dictionary to context
        form = InfoForm(request.POST and request.FILES or None, instance=obj)
        return render(request, "update_info.html", {'form': form})



@login_required
def update_skill(request, slug, skill):
    try:
        obj = get_object_or_404(Skill,user=request.user, slug__slug=slug, skill=skill)
        form = SkillForm(request.POST or None, instance=obj)
        if form.is_valid():
            skill = form.cleaned_data.get('skill')
            form.save()
            messages.success(request, "Your skill is updated")
            return redirect('home:skill-details', slug=slug)

        form = SkillForm(request.POST or None, instance=obj)
        return render(request, "update_skill.html", {'form': form})
    except:
        return HttpResponse("The content you want to updated has been deleted")


@login_required
def update_education(request, slug, course):
    try:
        user=request.user
        obj = get_object_or_404(Study, user=user, slug__slug=slug, course=course)
        form = EducationForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Qualification detail is updated")
            return redirect('home:education-details', slug=slug)

        form = EducationForm(request.POST or None, instance=obj)
        return render(request, "update_education.html", {'form': form})
    except:
        return HttpResponse("The content you want to updated has been deleted")


@login_required
def update_service(request, slug, service_name):
    try:
        user = request.user
        obj = get_object_or_404(Service, user=user, slug__slug=slug, service_name=service_name)
        form = ServiceForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Your service detail is updated")
            return redirect('home:service-details', slug=slug)

        form = ServiceForm(request.POST or None, instance=obj)
        return render(request, "update_service.html", {'form': form})
    except:
        return HttpResponse("The content you want to updated has been deleted")


@login_required
def update_work(request, slug, project_name):
    try:
        obj = get_object_or_404(Work,user=request.user, slug__slug=slug, project_name=project_name)
        form = WorkForm(request.POST or None and request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Your project detail  is updated")
            return redirect('home:work-details', slug=slug)
        form = WorkForm(instance=obj)
        return render(request, "update_work.html", {'form': form})
    except:
        return HttpResponse("The content you want to updated has been deleted")


@login_required
def update_experience(request, slug, organisation_name):
    try:
        obj = get_object_or_404(Experience, user=request.user, slug__slug=slug, organisation_name=organisation_name)
        form = ExperienceForm(request.POST or None, instance=obj)
        if form.is_valid():
            print(form)
            form.save()
            messages.success(request, "Your Work experience is updated")
            return redirect('home:experience-details', slug=slug)
        print(form)
        form = ExperienceForm(request.POST or None, instance=obj)
        return render(request, "update_experience.html", {'form': form})
    except:
        return HttpResponse("The content you want to updated has been deleted")


@login_required
def delete_skill(request, slug, skill):
    try:
        obj = Skill.objects.filter(user=request.user,slug__slug=slug, skill=skill)
        obj.delete()
        messages.success(request, "Your skill is deleted")
        return redirect("home:skill-details", slug=slug)
    except:
        return HttpResponse("The content you want to updated has been deleted")


@login_required
def delete_education(request, slug, course):
    try:
        obj = Study.objects.filter(user=request.user,slug__slug=slug, course=course)
        obj.delete()
        messages.success(request, "Your Qualification detail is deleted")
        return redirect("home:education-details", slug=slug)
    except:
        return HttpResponse("The content you want to updated has been deleted")


@login_required
def delete_service(request, slug, service_name):
    try:
        obj = Service.objects.filter(user=request.user, slug__slug=slug, service_name=service_name)
        obj.delete()
        messages.success(request, "Your service detail is deleted")
        return redirect("home:service-details", slug=slug)
    except:
        return HttpResponse("The content you want to updated has been deleted")


@login_required
def delete_work(request, slug, project_name):
    try:
        obj = Work.objects.filter(user=request.user, slug__slug=slug, project_name=project_name)
        obj.delete()
        messages.success(request, "Your project detail is deleted")
        return redirect("home:work-details", slug=slug)
    except:
        return HttpResponse("The content you want to updated has been deleted")


@login_required
def delete_experience(request, slug, post):
    try:
        obj = Experience.objects.filter(user=request.user,slug__slug=slug, post=post)
        obj.delete()
        messages.success(request, "Your work experience is deleted")
        return redirect("home:experience-details", slug=slug)
    except:
        return HttpResponse("The content you want to updated has been deleted")


def create_cv(request, slug):
    try:
        details = {}
        details['info'] = UserInfo.objects.get(slug=slug,)
        name = UserInfo.objects.get(slug=slug)
        details['education'] = Study.objects.filter(slug=name).all()
        details['skill'] = Skill.objects.filter(slug=name).all()
        details['service'] = Service.objects.filter(slug=name).all()
        details['work'] = Work.objects.filter(slug=name).all()
        details['experience'] = Experience.objects.filter(slug=name).all()
        details['count_exp'] = len(details['experience'])
        details['count_work'] = len(details['work'])
        print(details, 'test html')
        return render_to_pdf(
                'cv.html',
                {
                    'pagesize': 'A4',
                    'details': details,

                }
            )
    except:
        return HttpResponse("Something wen wrong")
