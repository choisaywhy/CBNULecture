from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time

# 크롬 드라이버 연결
driver = wd.Chrome(executable_path =r'./chromedriver/chromedriver.exe')
# 접속 주소
driver.get('https://eis.cbnu.ac.kr/cbnuLogin')

# 로그인 아이디
uid = driver.find_element_by_name("uid")
# 로그인 비밀번호
pswd = driver.find_element_by_name("pswd")
commonLoginBtn = driver.find_element_by_xpath("//*[@id='commonLoginBtn']")

# 로그인 정보 입력
uid.send_keys("2018038082")
pswd.send_keys("chltpghk98!")
print("로그인 정보 입력 완료")

commonLoginBtn.click()
print("로그인 버튼 클릭")

# 해당 태그를 찾기 전까지 실행 기다림
try:
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "mainframe_VFS_HFS_SubFrame_form_tab_subMenu_tpg_bssMenu_grd_menu_body_gridrow_8_cell_8_0_controltree"))
    )
finally:
    {}
    
print("로그인 로딩 완료")

## driver.implicitly_wait(10)   # 드라이버를 멈추고 10초 기다림      
time.sleep(5)                   # 전체 프로세스를 멈추고 5초 기다림

# 네비게이션 수업 / 성적 클릭
lecture = driver.find_element_by_id("mainframe_VFS_HFS_SubFrame_form_tab_subMenu_tpg_bssMenu_grd_menu_body_gridrow_8_cell_8_0_controltree")
lecture.click()

print("수업 성적 클릭")

# 네비게이션 수업정보 클릭
lecture2 = driver.find_element_by_id("mainframe_VFS_HFS_SubFrame_form_tab_subMenu_tpg_bssMenu_grd_menu_body_gridrow_9_cell_9_0_controltree")
lecture2.click()

print("수업 정보 클릭")

# 네비게이션 개설강좌(계획서)조회 클릭
lecture3 = driver.find_element_by_id("mainframe_VFS_HFS_SubFrame_form_tab_subMenu_tpg_bssMenu_grd_menu_body_gridrow_16_cell_16_0_controltree")
lecture3.click()

print("개설강좌 클릭")


try:
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "mainframe_VFS_HFS_INVFS_WorkFrame_win_2275_form_div_work_btn_search"))
    )
finally:
    {}

print("조회 버튼 찾음")

search = driver.find_element_by_id("mainframe_VFS_HFS_INVFS_WorkFrame_win_2275_form_div_work_btn_search")
search.click()

print("조회 버튼 클릭")

time.sleep(30)


# 출력 버튼 0~17까지 총 3841개
for j in range(0, 208):
    for i in range(0,16):
        download_id = 'mainframe_VFS_HFS_INVFS_WorkFrame_win_2275_form_div_work_grd_master_body_gridrow_'+str(i)+'_cell_'+str(i)+'_12GridCellContainerElement'

        try:
            element = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.ID, download_id))
                )
        except TimeoutException :
            scroll = driver.find_element_by_id("mainframe_VFS_HFS_INVFS_WorkFrame_win_2275_form_div_work_grd_master_vscrollbar_incbutton") 
            scroll.click()
            print("없는 번호" +str(i))
            continue


        print("출력 버튼 찾음")
        print(download_id)

        download = driver.find_element_by_id(download_id)
        download.click()


        print("출력 버튼 클릭")

        # popup창으로 frame 전환
        try:
            element = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='mainframe_VFS_HFS_INVFS_WorkFrame_win_2275_popup_form_div_popWork_web_report_WebBrowser']"))
                )
        finally:
            {}

        popup = driver.find_element_by_xpath("//*[@id='mainframe_VFS_HFS_INVFS_WorkFrame_win_2275_popup_form_div_popWork_web_report_WebBrowser']")
        driver.switch_to.frame(popup)

        print("popup 전환 완료")

        try:
            element = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='iWeb']"))
                )
        finally:
            {}
        
        popup2 = driver.find_element_by_xpath("//*[@id='iWeb']")
        driver.switch_to.frame(popup2)

        print("popup2 전환 완료")

        try:
            element = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//button[@title='저장']"))
                )
        finally:
            {}

        print("저장 버튼 찾음")

        # driver.implicitly_wait(10) # seconds
        time.sleep(4)

        download2 = driver.find_element_by_xpath("//*[@title='저장']")  
        download2.click()
        download2.click()

        print("저장 버튼 클릭")

        time.sleep(3)

        # rename = driver.find_element_by_xpath("//*[@id='targetDiv1']/div[2]/div[1]/div[2]/input")
        # rename.clear()
        # rename.send_keys("report"+" ("+str((i+1)*(j+1))+")")

        # print("파일 이름 바꿈")
        
        download3 = driver.find_element_by_xpath("//*[@id='targetDiv1']/div[2]/div[1]/button[1]")
        download3.click()
        

        print("파일 최종 저장")
        time.sleep(4)

        # popup 전환
        driver.switch_to.default_content()  # popup2 -> popup
        driver.switch_to.default_content()  # popup -> default

        print("popup 전환 완료")


        # driver.implicitly_wait(10) # seconds

        close = driver.find_element_by_id("mainframe_VFS_HFS_INVFS_WorkFrame_win_2275_popup_titlebar_closebutton")
        close.click()
            
        print("popup 닫기")

        time.sleep(3)

        scroll = driver.find_element_by_id("mainframe_VFS_HFS_INVFS_WorkFrame_win_2275_form_div_work_grd_master_vscrollbar_incbutton") 
        
        scroll.click()
        print("스크롤 버튼 클릭")
    

#driver.quit()
