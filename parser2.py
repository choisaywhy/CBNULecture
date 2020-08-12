import openpyxl
import csv



def saveCrawling ():
    for i in range(0,4010) :
        # 파일 불러오기(수식이 아닌 값으로)
        
        try :
            report_name = './datas/report ('+str(i)+').xlsx'
            excelFile = openpyxl.load_workbook(filename = report_name)
            print(report_name)
        except FileNotFoundError:
            continue

        # 시트 불러오기
        sheet = excelFile['sheet 1']


        # 셀 주소로 값 출력
        # 강의명
        title = sheet['T6'].value
        # 개설연도
        est_year = sheet['E5'].value
        # 학기
        session = sheet['H5'].value
        # 개설학과
        department_title = sheet['T5'].value
        # 과목코드 / 분반
        category = sheet['E6'].value + sheet['H6'].value
        # 이수구분
        unit = sheet['E7'].value
        # 학점 / 시수
        # credit = sheet['T7'].value
        # 교수
        prof = sheet['T9'].value
        # 학년
        grade = sheet['T12'].value
        # 수업진행방식
        class_prog = str(sheet['D20'].value) + '&' + str(sheet['G20'].value) + '&' + str(sheet['J20'].value) + '&' + str(sheet['N20'].value) + '&' + str(sheet['U20'].value) + '&' + str(sheet['AA20'].value)

        # 평가방법
        class_eval = str(sheet['D23'].value) + '&' + str(sheet['G23'].value) + '&' + str(sheet['J23'].value) + '&' + str(sheet['N23'].value) + '&' + str(sheet['U23'].value) + '&' + str(sheet['AA23'].value)

        print(title)
        data = [title, est_year, session, department_title, category, unit, prof, grade, class_prog, class_eval]
        
    
        with open('./saveDatas.csv','a') as f: 
            wt = csv.writer(f) 
            wt.writerow(data)


        print(report_name+'완료')



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
