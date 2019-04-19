from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(r"C:\Users\soyjn\PycharmProjects\FirstSeleniumTest1\Drivers\chromedriver.exe")

driver.set_page_load_timeout(10)
driver.get("http://www.bcra.gov.ar/PublicacionesEstadisticas/Principales_variables_datos.asp?serie=7923&detalle=Tasa%20de%20LELIQ%20(promedio%20en%20%%20n.a.)")


driver.find_element_by_name("fecha_desde").send_keys("04/01/2019")
driver.find_element_by_name("fecha_hasta").send_keys("04/10/2019")
driver.find_element_by_name("B1").send_keys(Keys.ENTER)
for row in driver.find_elements_by_tag_name("tbody"):
    for td in row.find_elements_by_tag_name("td"):
        if td.get_attribute("style") == "text-align: right;":
            print(td.text)

driver.quit()
