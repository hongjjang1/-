from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome("c:/chromedriver.exe")
browser.get("https://map.naver.com/v5/")
browser.implicitly_wait(10)
browser.maximize_window()

# 검색창 입력
search = browser.find_element(By.CSS_SELECTOR, "input.input_search")
search.click()
time.sleep(1)
search.send_keys("정릉동 맛집")
time.sleep(1)
search.send_keys(Keys.ENTER)
time.sleep(2)



browser.switch_to.frame("searchIframe")

browser.find_element(By.CSS_SELECTOR,"#_pcmap_list_scroll_container").click()


# 로딩된 데이터 갯수 확인
lis = browser.find_elements(By.CSS_SELECTOR,"head")
before_len = len(lis)


browser.implicitly_wait(0)

while True:

    # 맨 아래로 스크롤 내린다.

    browser.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.END)



    # 스크롤 사이 페이지 로딩 시간

    time.sleep(1.5)



    # 스크롤 후 로딩된 데이터 개수 확인

    lis = browser.find_element(By.CSS_SELECTOR,"head")

    after_len = len(lis)



    # 로딩된 데이터 개수가 같다면 반복 멈춤

    if before_len == after_len:

        break

    before_len = after_len



# 데이터 기다리는 시간을 0. (데이터가 없더라도 빠르게 넘어감)

browser.implicitly_wait(0)



for li in lis:

    # 별점이 있는 것만

    if len(li.find_element(By.CSS_SELECTOR,"span._2FqTn._1mRAM > em")) > 0:

        # 가게명

        name = li.find_element(By.CSS_SELECTOR,"span.OXiLu").text

        # 별점

        star = li.find_element(By.CSS_SELECTOR,"span._2FqTn._1mRAM > em").text



        # 영업 시간이 있다면

        if len(li.find_element(By.CSS_SELECTOR,"span._2FqTn._4DbfT")) > 0:

            # 방문자 리뷰수

            try:

                visit_review = li.find_element(By.CSS_SELECTOR,"span._2FqTn:nth-child(3)").text

            except:

                visit_review = "0"

            # 블로그 리뷰수

            try:

                blog_review = li.find_element(By.CSS_SELECTOR,"span._2FqTn:nth-child(4)").text

            except:

                blog_review = "0"

        # 영업 시간이 없다면

        else:

            # 방문자 리뷰수

            try:

                visit_review = li.find_element(By.CSS_SELECTOR,"span._2FqTn:nth-child(2)").text

            except:

                visit_review = "0"

            # 블로그 리뷰수

            try:

                blog_review = li.find_element(By.CSS_SELECTOR,"span._2FqTn:nth-child(3)").text

            except:

                blog_review = "0"



        print(name, star, visit_review, blog_review)