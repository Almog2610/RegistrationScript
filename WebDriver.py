from InputBox import InputBox


def fill_input_boxes(browser, haste_user):
    input_boxes = get_all_input_boxes(browser)

    for input_box in input_boxes:

        if input_box.name == "FirstName":
            input_box.web_element.send_keys(haste_user.first_name)

        elif input_box.name == "Username":
            input_box.web_element.send_keys(haste_user.username)

        elif input_box.name == "Email":
            input_box.web_element.send_keys(haste_user.email)

        elif input_box.name == "Password":
            input_box.web_element.send_keys(haste_user.password)

        elif input_box.name == "ConfirmPassword":
            input_box.web_element.send_keys(haste_user.password)


def get_all_input_boxes(browser):
    first_name_web_element = browser.find_element_by_id("firstName")
    username_web_element = browser.find_element_by_id("userName")
    email_web_element = browser.find_element_by_id("email")
    password_web_element = browser.find_element_by_id("password")
    confirm_password_web_element = browser.find_element_by_id("confirmPassword")

    return [InputBox("FirstName", first_name_web_element), InputBox("Username", username_web_element),
            InputBox("Email", email_web_element), InputBox("Password", password_web_element),
            InputBox("ConfirmPassword", confirm_password_web_element)]


def click_sign_up_button(browser, button_id):
    sign_up_button = browser.find_element_by_id(button_id)
    sign_up_button.click()
