import selenium
import pickle

# def load_dict():
#     netids = pickle.load(open('logwrite.p', 'rb+'))
#     for elems in items:
#         oldpass = netids[elems]
#         selenium_script(oldpass, newpass, elems)


def selenium_script(oldp, newp, key):
    from selenium import webdriver
    browser = webdriver.Chrome('/usr/local/bin/chromedriver')
    browser.get('https://ds.utk.edu/passwords/login.asp?redirect=%2Fpasswords%2Fpassword%2Easp')

    user_name_element = browser.find_element_by_css_selector(
        '#inputusername')
    user_name_element.send_keys('lib' + str(key))
    old_pass_element = browser.find_element_by_css_selector(
        '#inputpassword')
    old_pass_element.send_keys(oldp)
    login_element = browser.find_element_by_css_selector(
        '#login-button-frame > input:nth-child(1)')
    login_element.click()
    new_pass_elem = browser.find_element_by_css_selector(
        '#inputnewpassword')
    new_pass_elem.send_keys(newp)
    new_pass_elem2 = browser.find_element_by_css_selector('#inputverifypassword')
    new_pass_elem2.send_keys(newp)
    check_Box = browser.find_element_by_css_selector('#auponsubmit > td:nth-child(1) > input[type="checkbox"]')
    check_Box.click()

    continue_box = browser.find_element_by_css_selector('#aupbtn')
    continue_box.click()

