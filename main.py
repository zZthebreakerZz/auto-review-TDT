import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SurveyBotTDT:

    def setUp(self):
        self.driver = webdriver.Chrome()
        url = "http://teaching-quality-survey.tdt.edu.vn/stdlogin.aspx?ReturnUrl=http%3a%2f%2fteaching-quality-survey.tdt.edu.vn%3a80%2fchoosesurvey.aspx"
        self.driver.get(url)

    def login(self):
        driver = self.driver
        while True:
            try:
                user = input("Nhập tài khoản: ")
                pw = input("Nhập mật khẩu: ")
                elem = driver.find_element_by_name("txtUser")
                elem.clear()
                elem.send_keys(user)
                elem = driver.find_element_by_name("txtPass")
                elem.send_keys(pw)
                elem = driver.find_element_by_xpath("//input[@value='Đăng nhập']").click()
                elem = driver.find_element_by_id("lbThongBao")
                print("\nSai mật khẩu hoặc MSSV. Xin vui lòng nhập lại!\n")
            except Exception:
                print("\n*Đăng nhập thành công*\n")
                return 1
    
    def isSurveyed(self):
        arr = []
        num = 0
        driver = self.driver
        print("Chương trình đang check các mục chưa đánh giá\n")
        try:
            while True:
                elem = driver.find_element_by_id("gvMonHoc_lbTinhTrang_" + str(num))
                if "Đã" not in elem.text:
                    arr.append(num)
                    elem = driver.find_element_by_id("gvMonHoc_lbLecturerName_" + str(num))
                    print("Cậu chưa đánh giá giảng viên " + elem.text)
                num += 1
        except Exception:
            mtp = input("Check xong! Cậu có muốn tiếp tục đánh giá (y/n): ")
            if mtp not in ['y', 'Y']:
                raise NameError()
        return arr

    def randomSurvey(self):
        return str(randint(3, 5))

    def runSurvey(self, arr):
        if not(arr):
            print("\n\nBạn đã đánh giá xong trước đó. Mọi thông tin vui lòng đọc ở file LuuY.txt!")
            return -1
        driver = self.driver
        print("Chương trình sẽ bắt đầu tự đánh giá ngẫu nhiên (4-6).")
        try:
            for num in arr:
                elem = driver.find_elements_by_tag_name("a")[num + 1]
                elem.click()

                for i in [1,2,3,4,5,7]:
                    for j in range(0, 5):
                        try:
                            rand = self.randomSurvey()
                            elem = driver.find_element_by_id("gv" + str(i) + "_rd" + rand + "_" + str(j))
                            elem.click()
                        except Exception:
                            break
                elem = driver.find_element_by_name("btnTiepTuc")
                elem.click()

                elem = driver.find_element_by_name("btnTiepTucDanhGia")
                elem.click()
            print("\n\nThành công! Mời bạn mở lại trình duyệt :D")
        except Exception:
            print("\n*Ngắt trình duyệt làm đ*o gì vậy cậu? :)")
        
    def finish(self):
        try:
            self.driver.close()
        except Exception:
            print('')

def main():
    try:
        a = SurveyBotTDT()
        a.setUp()
        a.login()
        arr = a.isSurveyed()
        a.runSurvey(arr)
        a.finish()
    except NameError:
        print("\nFinish!")

main()