from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAdNabuStore:

    # Setup browser  
  def setup_method(self):
    self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    self.driver.maximize_window()
    self.wait = WebDriverWait(self.driver,10)
    self.driver.get("https://adnabu-store-assignment1.myshopify.com/")
    
  def test_search_add_to_cart(self):
    driver = self.driver
    wait = self.wait

    # Enter store password
    password_field = wait.until(EC.presence_of_element_located((By.ID,"password")))
    password_field.send_keys("AdNabuQA")

    # Click on enter button
    enter_button = driver.find_element(By.XPATH,"//button[@type='submit']")
    enter_button.click()

    # Click search icon
    search_icon = wait.until(EC.element_to_be_clickable((By.XPATH,"//summary[contains(@class,'search')]")))
    search_icon.click()

    # Search the product in search field
    search_box = wait.until(EC.presence_of_element_located((By.NAME,"q")))
    search_box.send_keys("snowboard")

    # Click search button
    search_button = driver.find_element(By.CSS_SELECTOR,".search__button.field__button")
    search_button.click()

    # Click the first product
    products = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//a[contains(@href,'/products')]")))
    first_product = products[0]
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});",first_product)
    driver.execute_script("arguments[0].click();",first_product)

    # Click add to cart button   
    add_to_cart = driver.find_elements(By.NAME,"add")
    add_to_cart[0].click()

    # Print product added successful     
    cart_drawer = wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@aria-label='Your cart']")))
    assert cart_drawer.is_displayed()
    print("Product successfully added to cart")

    # Close browser
  def teardown_method(self, method):
    self.driver.quit()


