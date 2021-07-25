import pytest
import selenium.webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://the-internet.herokuapp.com/challenging_dom"

b = selenium.webdriver.Chrome()

b.get(URL)

Names = ["qux","foo","bar","baz"]
Header = "Challenging DOM"
Text= """The hardest part in automated web testing is finding the best locators (e.g., ones that well named, unique, and unlikely to change). It's more often than not that the application you're testing was not built with this concept in mind. This example demonstrates that with unique IDs, a table with no helpful locators, and a canvas element."""
def test_1():
    elem1 = b.title
    assert "The Internet" == elem1
    print(elem1)
  
@pytest.mark.repeat(5)
def test_2():
    elem1 = b.find_element(By.XPATH, 'html/body/div[2]/div/div/div/div/div[1]/a[1]')
    a=(elem1.text)
    elem1.click()
    assert a in Names
    print (a)

@pytest.mark.repeat(5)
def test_3():
    elem1 = b.find_element(By.XPATH, 'html/body/div[2]/div/div/div/div/div[1]/a[2]')
    a=(elem1.text)
    elem1.click()
    assert a in Names
    print (a)

@pytest.mark.repeat(5)
def test_4():
    elem1 = b.find_element(By.XPATH, 'html/body/div[2]/div/div/div/div/div[1]/a[3]')
    a=(elem1.text)
    elem1.click()
    assert a in Names
    print (a)

def test_5():
    elem1 = b.find_element(By.XPATH, '/html/body/div[2]/div/div/h3')
    a=(elem1.text)
    assert a == Header
    print(a)

def test_6():
    elem1 = b.find_element(By.XPATH, '/html/body/div[2]/div/div/p')
    a=(elem1.text)
    assert a == Text
    print(a)

    
    #Test looking at edit button at top of table
def test_7():
    elem1 = WebDriverWait(b, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[1]/td[7]/a[1]')))
    elem1.click()
    
     #Test looking at delete button at top of table
def test_8():
    elem1 = WebDriverWait(b, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[1]/td[7]/a[2]')))
    elem1.click()

    
    
    #Test looking at edit button at bottom of table 
def test_9():
    elem1 = WebDriverWait(b, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[10]/td[7]/a[1]')))
    elem1.click()
    
    #Test looking at delete button at bottom of table
def test_10():
    elem1 = WebDriverWait(b, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[10]/td[7]/a[2]')))
    elem1.click()
    b.quit()





