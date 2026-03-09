from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAdNabuStore:

  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
    self.wait = WebDriverWait(self.driver,10)
    self.driver.get("https://adnabu-store-assignment1.myshopify.com/")

  def test_search_add_to_cart(self):
    driver = self.driver
    wait = self.wait

# Enter store password

    password_field = wait.until(EC.presence_of_element_located((By.ID,"password")))
    password_field.send_keys("AdNabuQA")

    enter_button = driver.find_element(By.XPATH,"//button[@type='submit']")
    enter_button.click()

    search_icon = wait.until(EC.element_to_be_clickable((By.XPATH,"//summary[contains(@class,'search')]")))
    search_icon.click()

    search_box = wait.until(EC.presence_of_element_located((By.NAME,"q")))
    search_box.send_keys("snowboard")

    search_button = driver.find_element(By.CSS_SELECTOR,".search__button.field__button")
    search_button.click()

    products = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//a[contains(@href,'/products')]")))
    first_product = products[0]
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});",first_product)
    driver.execute_script("arguments[0].click();",first_product)
#click add to cart button   
    add_to_cart = driver.find_elements(By.NAME,"add")
    add_to_cart[0].click()
#print product added successful     
    cart_drawer = wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@aria-label='Your cart']")))
    assert cart_drawer.is_displayed()
    print("Product successfully added to cart")

#cloce the browser
  def teardown_method(self, method):
    self.driver.quit()


