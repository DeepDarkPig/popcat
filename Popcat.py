from selenium import webdriver

path = r'C:\Users\Sorry\Desktop\XOI\Python\chromedriver.exe'        #The path of the webdriver. Must match the version of Chrome.
driver = webdriver.Chrome(path)

driver.get("http://www.popcat.click/")
driver.implicitly_wait(3)

time = 100       #Repeat times.
element = driver.find_elements_by_id('app')[0]
for i in range(time):
    element.click()

#Addition commands below. Sometimes doesn't work.
'''
sum = driver.find_elements_by_class_name('counter.rot-l')[0]
file = open('sum.txt','w+')
file.write(str(sum.text()))      #Show you the real clicks.
file.close()

driver.close()
'''