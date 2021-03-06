import selenium
import pickle
import requests


# def load_dict():
#     netids = pickle.load(open('logwrite.p', 'rb+'))
#     for elems in items:
#         oldpass = netids[elems]
#         selenium_script(oldpass, newpass, elems)


def selenium_script(oldp, newp, key):
    import requests
    from selenium import webdriver
    # sets Google Chrome as browser
    browser = webdriver.Chrome('/usr/local/bin/chromedriver')
    # opens browser to log in page
    browser.get('https://ds.utk.edu/passwords/login.asp?redirect=%2Fpasswords%2Fpassword%2Easp')
    # finds user name field
    user_name_element = browser.find_element_by_css_selector(
        '#inputusername')
    # sends username to log in field
    user_name_element.send_keys('lib' + str(key))
    # selects password field
    old_pass_element = browser.find_element_by_css_selector(
        '#inputpassword')
    # sends current/old password to password field
    old_pass_element.send_keys(oldp)
    # selects then presses log in button
    login_element = browser.find_element_by_css_selector(
        '#login-button-frame > input:nth-child(1)')
    login_element.click()
    # Add error check for new bad password here

    try:
        browser.find_element_by_css_selector('#view-frame > form > p.bg-danger')
        print("Password incorrect for Lib" + str(key))
        print("Reset password manually")
        return
    except:
        # r = requests.get('https://ds.utk.edu/passwords/login.asp?redirect=%2Fpasswords%2Fpassword%2Easp')
        # if r.status_code == 200:
        #     print("Password incorrect for lib" + str(key))
        #     print("Reset manually")
        #     return
        # selects new password field and enters new password
        new_pass_elem = browser.find_element_by_css_selector(
            '#inputnewpassword')
        new_pass_elem.send_keys(newp)
        # selects verify new password field and enters new password
        new_pass_elem2 = browser.find_element_by_css_selector('#inputverifypassword')
        new_pass_elem2.send_keys(newp)
        # selects and clicks verification check box
        check_Box = browser.find_element_by_css_selector('#auponsubmit > td:nth-child(1) > input[type="checkbox"]')
        check_Box.click()
        continue_box = browser.find_element_by_css_selector('#aupbtn')
        continue_box.click()

