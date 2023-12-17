import pandas as pd
from selenium import webdriver

file_path = 'D:/KRILA/data/'

# https://googlechromelabs.github.io/chrome-for-testing/
driver = webdriver.Chrome(file_path + 'chromedriver.exe')
driver.implicitly_wait(3)

er = pd.DataFrame()

# 경북
for page_num in range(1, 4):
    driver.get(f"https://www.e-gen.or.kr/egen/search_emergency_room.do?currentPageNum={page_num}&lon=127.0537796&lat=37.5956295&searchType=general&sidoCode=47&emogdstr=&gugunCode=&emogdesc=&nightcareon=&loca=27&roadaddr=&radioCode=road&addrhosp=&dongCode=&trtPrtCod=&day=&time=")
    driver.implicitly_wait(5)
    
    if page_num == 7:
        for i in range(1, 7):
            text = driver.find_element_by_xpath(
                f"//*[@id='placesList']/li[{i}]").text
            info_list = text.split('\n')
            temp_df = pd.DataFrame([info_list])
            er = pd.concat([er, temp_df], ignore_index=True)
    else:
        for i in range(1, 11):
            text = driver.find_element_by_xpath(
                f"//*[@id='placesList']/li[{i}]").text
            info_list = text.split('\n')
            temp_df = pd.DataFrame([info_list])
            er = pd.concat([er, temp_df], ignore_index=True)

# 서울
for page_num in range(1, 8):
    driver.get(f"https://www.e-gen.or.kr/egen/search_emergency_room.do?currentPageNum={page_num}&loca=11&addrhosp=&dongCode=&trtPrtCod=&roadaddr=&radioCode=road&lat=37.5956313&lon=127.0537867&sidoCode=11&gugunCode=&emogdesc=&searchType=general&emogdstr=&nightcareon=&day=&time=")
    driver.implicitly_wait(5)  # 3초 대기
    
    if page_num == 7:
        for i in range(1, 6):
            text = driver.find_element_by_xpath(
                f"//*[@id='placesList']/li[{i}]").text
            info_list = text.split('\n')
            temp_df = pd.DataFrame([info_list])
            er = pd.concat([er, temp_df], ignore_index=True)
    else:
        for i in range(1, 11):
            text = driver.find_element_by_xpath(
                f"//*[@id='placesList']/li[{i}]").text
            info_list = text.split('\n')
            temp_df = pd.DataFrame([info_list])
            er = pd.concat([er, temp_df], ignore_index=True)

driver.quit()
driver.close()

er.columns = ['거리', '병원명', '업무구분', '전화번호', '주소', '진료상태', 
              '응급실운영', '입원실운영', '기타']            
er = er[['병원명', '업무구분']]
er['병원명'] = er['병원명'].str.replace('상세보기', '')

er.to_csv(file_path + '1 raw/er.csv', encoding='euc-kr')
