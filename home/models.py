from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    objective = models.TextField()
    address = models.CharField(max_length=200)
    phoneno = models.CharField(max_length=12)
    email = models.EmailField(max_length=100)
    linkedin = models.URLField(blank=True)
    university1 = models.CharField(max_length=100, blank=True)
    degree1 = models.CharField(max_length=50, blank=True)
    stream1 = models.CharField(max_length=100, blank=True)
    currentYear1 = models.CharField(max_length=50, blank=True)
    univStartingYear1 = models.CharField(max_length=20, blank=True)
    univPassingYear1 = models.CharField(max_length=20, blank=True)
    univResult1 = models.CharField(max_length=20, blank=True)
    university2 = models.CharField(max_length=100, blank=True)
    degree2 = models.CharField(max_length=50, blank=True)
    stream2 = models.CharField(max_length=100, blank=True)
    currentYear2 = models.CharField(max_length=50, blank=True)
    univStartingYear2 = models.CharField(max_length=20, blank=True)
    univPassingYear2 = models.CharField(max_length=20, blank=True)
    univResult2 = models.CharField(max_length=20, blank=True)
    intermediateSchool = models.CharField(max_length=100, blank=True)
    intermediateStartingYear = models.CharField(max_length=20, blank=True)
    intermediatePassingYear = models.CharField(max_length=20, blank=True)
    intermediateMarks = models.CharField(max_length=15, blank=True)
    highSchool = models.CharField(max_length=100, blank=True)
    highSchoolStartingYear = models.CharField(max_length=20, blank=True)
    highSchoolPassingYear = models.CharField(max_length=20, blank=True)
    highSchoolMarks = models.CharField(max_length=20, blank=True)
    jobTitle1 = models.CharField(max_length=100, blank=True)
    jobStartDate1 = models.CharField(max_length=20, blank=True)
    jobEndDate1 = models.CharField(max_length=20, blank=True)
    jobDescription1 = models.TextField(blank=True, null=True)
    jobTitle2 = models.CharField(max_length=100, blank=True)
    jobStartDate2 = models.CharField(max_length=20, blank=True)
    jobEndDate2 = models.CharField(max_length=20, blank=True)
    jobDescription2 = models.TextField(blank=True, null=True)
    jobTitle3 = models.CharField(max_length=100, blank=True)
    jobStartDate3 = models.CharField(max_length=20, blank=True)
    jobEndDate3 = models.CharField(max_length=20, blank=True)
    jobDescription3 = models.TextField(blank=True, null=True)
    projectTitle1 = models.CharField(max_length=100, blank=True)
    projectStartDate1 = models.CharField(max_length=20, blank=True)
    projectEndDate1 = models.CharField(max_length=20, blank=True)
    projectDescription1 = models.TextField(blank=True, null=True)
    projectTitle2 = models.CharField(max_length=100, blank=True)
    projectStartDate2 = models.CharField(max_length=20, blank=True)
    projectEndDate2 = models.CharField(max_length=20, blank=True)
    projectDescription2 = models.TextField(blank=True, null=True)
    projectTitle3 = models.CharField(max_length=100, blank=True)
    projectStartDate3 = models.CharField(max_length=20, blank=True)
    projectEndDate3 = models.CharField(max_length=20, blank=True)
    projectDescription3 = models.TextField(blank=True, null=True)
    skillDetail = models.TextField()
    languageDetail = models.TextField()   
    areaOfInterest = models.CharField(max_length=200, blank=True)
    extracurricularDetail = models.CharField(max_length=200, blank=True)    

    def __str__(self):
        return self.name