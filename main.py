import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Username and password
print("Lưu ý: Sau khi web bật lên mọi thao tác đều thực hiện trên đây (kể cả đăng nhập)")
time.sleep(3)

url = "http://teaching-quality-survey.tdt.edu.vn/stdlogin.aspx?ReturnUrl=http%3a%2f%2fteaching-quality-survey.tdt.edu.vn%3a80%2fchoosesurvey.aspx"
driver = webdriver.Chrome()
driver.get(url)


# Check if it reviewed
def is_review():
    num = 0
    arr = []
    print("Chương trình đang check các mục chưa đánh giá")
    try:
        while True:
            elem = driver.find_element_by_id("gvMonHoc_lbTinhTrang_" + str(num))
            if "Đã" not in elem.text:
                arr.append(num)
                print("Bạn chưa review mục số:" + str(num + 1))
            num += 1
    except Exception:
        print("Check xong! Chương trình sẽ bắt đầu tự review.")
        if not(arr):
            print("\n\nBạn đã đánh giá xong trước đó. Mọi thông tin vui lòng đọc ở file LuuY.txt!")
            return -1
    return arr
    


# nums: number of teachers
def run(arr):
    for num in arr:
        try:
            elem = driver.find_elements_by_tag_name("a")[num + 1]
            elem.click()

            for i in [1,2,3,4,5,7]:
                for j in range(0, 5):
                    try:
                        elem = driver.find_element_by_id("gv" + str(i) + "_rd5_" + str(j))
                        elem.click()
                    except Exception:
                        break
            elem = driver.find_element_by_name("btnTiepTuc")
            elem.click()

            elem = driver.find_element_by_name("btnTiepTucDanhGia")
            elem.click()
        except Exception:
            break

# Login
def login():
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
            return
            

def main():
    login()
    arr = is_review()
    if arr != -1:
        run(arr)
        print("\n\nThành công! Mời bạn mở lại trình duyệt :D")
    driver.close()

main()

