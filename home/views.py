from django.shortcuts import render
from .models import Profile

# Create your views here.
def home(request):
        return render(request,'home.html')

def resumedetails(request):
        return render(request,'resumedetails.html')   

def result(request):
        if request.method == "POST":
                name =request.POST["name"] 
        objective =request.POST["objective"] 
        address =request.POST["address"] 
        phoneno =request.POST["phoneno"] 
        email =request.POST["email"] 
        linkedin =request.POST["linkedin"]
        university1 =request.POST["university1"] 
        degree1 =request.POST["degree1"] 
        stream1 =request.POST["stream1"] 
        currentYear1 =request.POST["currentYear1"]
        univStartingYear1 =request.POST["univStartingYear1"]
        univPassingYear1 =request.POST["univPassingYear1"]
        univResult1 =request.POST["univResult1"]
        university2 =request.POST["university2"]
        degree2 =request.POST["degree2"]
        stream2 =request.POST["stream2"]
        currentYear2 =request.POST["currentYear2"]
        univStartingYear2 =request.POST["univStartingYear2"]
        univPassingYear2 =request.POST["univPassingYear2"]
        univResult2 =request.POST["univResult2"]
        intermediateSchool =request.POST["intermediateSchool"]
        intermediateStartingYear =request.POST["intermediateStartingYear"]
        intermediatePassingYear =request.POST["intermediatePassingYear"]
        intermediateMarks =request.POST["intermediateMarks"] 
        highSchool =request.POST["highSchool"] 
        highSchoolStartingYear =request.POST["highSchoolStartingYear"] 
        highSchoolPassingYear =request.POST["highSchoolPassingYear"]
        highSchoolMarks =request.POST["highSchoolMarks"] 
        jobTitle1 =request.POST["jobTitle1"]
        jobStartDate1 =request.POST["jobStartDate1"]
        jobEndDate1 =request.POST["jobEndDate1"]
        jobDescription1 =request.POST["jobDescription1"] 
        jobTitle2 =request.POST["jobTitle2"] 
        jobStartDate2 =request.POST["jobStartDate2"] 
        jobEndDate2 =request.POST["jobEndDate2"] 
        jobDescription2 =request.POST["jobDescription2"] 
        jobTitle3 =request.POST["jobTitle3"] 
        jobStartDate3 =request.POST["jobStartDate3"] 
        jobEndDate3 =request.POST["jobEndDate3"]
        jobDescription3 =request.POST["jobDescription3"]
        projectTitle1 =request.POST["projectTitle1"]
        projectStartDate1 =request.POST["projectStartDate1"] 
        projectEndDate1 =request.POST["projectEndDate1"]
        projectDescription1 =request.POST["projectDescription1"]
        projectTitle2 =request.POST["projectTitle2"]
        projectStartDate2 =request.POST["projectStartDate2"]
        projectEndDate2 =request.POST["projectEndDate2"]
        projectDescription2 =request.POST["projectDescription2"]
        projectTitle3 =request.POST["projectTitle3"]
        projectStartDate3 =request.POST["projectStartDate3"]
        projectEndDate3 =request.POST["projectEndDate3"]
        projectDescription3 =request.POST["projectDescription3"]
        skillDetail =request.POST["skillDetail"]
        languageDetail =request.POST["languageDetail"]
        areaOfInterest =request.POST["areaOfInterest"]
        extracurricularDetail =request.POST["extracurricularDetail"] 

        details = Profile (name=name, objective=objective, address=address, phoneno=phoneno, email=email, linkedin=linkedin, university1=university1, degree1=degree1, stream1=stream1, currentYear1=currentYear1, univStartingYear1=univStartingYear1, univPassingYear1=univPassingYear1, univResult1=univResult1, university2=university2, degree2=degree2, stream2=stream2, currentYear2=currentYear2, univStartingYear2=univStartingYear2, univPassingYear2=univPassingYear2, univResult2=univResult2, intermediateSchool=intermediateSchool, intermediateStartingYear=intermediateStartingYear, intermediatePassingYear=intermediatePassingYear,intermediateMarks=intermediateMarks, highSchool=highSchool, highSchoolStartingYear=highSchoolStartingYear, highSchoolPassingYear=highSchoolPassingYear, highSchoolMarks=highSchoolMarks, jobTitle1=jobTitle1, jobStartDate1=jobStartDate1, jobEndDate1=jobEndDate1, jobDescription1=jobDescription1, jobTitle2=jobTitle2, jobStartDate2=jobStartDate2, jobEndDate2=jobEndDate2, jobDescription2=jobDescription2, jobTitle3=jobTitle3, jobStartDate3=jobStartDate3, jobEndDate3=jobEndDate3, jobDescription3=jobDescription3, projectTitle1=projectTitle1, projectStartDate1=projectStartDate1, projectEndDate1=projectEndDate1, projectDescription1=projectDescription1, projectTitle2=projectTitle2, projectStartDate2=projectStartDate2, projectEndDate2=projectEndDate2, projectDescription2=projectDescription2, projectTitle3=projectTitle3, projectStartDate3=projectStartDate3, projectEndDate3=projectEndDate3, projectDescription3=projectDescription3, skillDetail=skillDetail, languageDetail=languageDetail, areaOfInterest=areaOfInterest, extracurricularDetail=extracurricularDetail)

        return render(request, "result.html", {'resume_details':details})