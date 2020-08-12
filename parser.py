import sys
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evaluateLecture.settings.local')
import django
django.setup()

import openpyxl
import csv
from lecture.models import Lecture


def saveCrawling ():
    data_list = []
    
    f = open('saveDatas.csv', 'r')
    rdr = csv.reader(f)
    for line in rdr:
        if not line:
            continue
        class_eval=line.pop()
        class_prog=line.pop()
        grade=line.pop()
        prof=line.pop()
        unit=line.pop()
        category=line.pop()
        department_title=line.pop()
        session=line.pop()
        est_year=line.pop()
        title=line.pop()
        score=0        

        print(title)

        Lecture(title=title, est_year=est_year, department_title=department_title, score=0, session=session, category=category, unit=unit, prof=prof, grade=grade, class_prog=class_prog, class_eval=class_eval).save()


    # return data_list

# i=0
# while i <3000:
saveCrawling()
#     i+=1

# if __name__=='__main__':

#     data_list = saveCrawling()
#     print(data_list)
#     print(data_list[0])

#     for i in range(0,3000) :
#         for title ,est_year, session, department_title, category, unit, prof, grade, class_prog, class_eval in data_list[i]:
#             Lecture(title=title, est_year=est_year, score=30, department_title=department_title, session=session, category=category, unit=unit, prof=prof, grade=grade, class_prog=class_prog, class_eval=class_eval).save()
