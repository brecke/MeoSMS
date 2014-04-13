#!/usr/bin/env python
# encoding: utf-8

# Encoding
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import time
from splinter import Browser 
import argparse

# parsing the command line
parser = argparse.ArgumentParser(prog="meosms", description='Tell me the recipient and then the message to be sent.')
parser.add_argument('number', nargs=1, type=int, help="the number you want to text", metavar="number")
parser.add_argument('message', nargs="+", help="the message you want to text", metavar="message")
args = vars(parser.parse_args())
# print(args)

SMS_MESSAGE = " ".join(args['message']).decode('utf-8')
DESTINATION_NUMBER = args['number'][0]


# URL and DOM variables
URL = "https://cliente.meo.pt/pag/Homepage"
username_textbox_name = "ctl00$ContentPlaceHolder1$LoginTemplate$Template$WebSSOUsernameTextBox"
password_textbox_name = "ctl00$ContentPlaceHolder1$LoginTemplate$Template$WebSSOPasswordTextBox"
login_button_id = "ctl00_ContentPlaceHolder1_LoginTemplate_Template_WebSSOSubmitButton"
number_input_field = "div.tag-cont textarea"
sms_textarea_field = "ctl00$bodyContentPlaceHolder$mainDashboard$Dash342$Temp$rightWidGrp$widRpt$ctl02$widPUP$SendSMSUc$GenericTextBoxMsg$phTxtBox_txtBox"
modal_javascript_open = "$find('ctl00_bodyContentPlaceHolder_mainDashboard_Dash342_Temp_rightWidGrp_widRpt_ctl02_widPUP').doPostBack('ctl00$bodyContentPlaceHolder$mainDashboard$Dash342$Temp$rightWidGrp$widRpt$ctl02$widPUP$SendSMSUc$sendSmsLinkButton','');"
modal_javascript_confirm = "$find('ctl00_bodyContentPlaceHolder_mainDashboard_Dash342_Temp_rightWidGrp_widRpt_ctl02_widPUP').doPostBack('ctl00$bodyContentPlaceHolder$mainDashboard$Dash342$Temp$rightWidGrp$widRpt$ctl02$widPUP$SendSMSUc$SendSMSLightBoxConfirmUC$ucLightBox$ucButtonAndLink$btnSubmit','')"

# credentials FILL IN HERE
my_username = ""
my_password = ""

# sms details
LOGIN_PROOF = "ENVIAR SMS"

# Splinter crawling
browser = Browser('phantomjs')
with browser: 
    
    # Visit URL 
    browser.visit(URL) 
    browser.fill(username_textbox_name, my_username) 
    browser.fill(password_textbox_name, my_password) 
    
    # Find and click the 'search' button 
    button = browser.find_by_id(login_button_id) 
    
    # Interact with elements 
    button.click() 
    
    # DOM garbage is not my fault
    if browser.is_text_present(LOGIN_PROOF): 
        element = browser.find_by_css(number_input_field)[0]
        element.fill(DESTINATION_NUMBER)
        browser.fill(sms_textarea_field, SMS_MESSAGE)
        # Enviar button
        browser.execute_script(modal_javascript_open)
        # waiting for javascript
        time.sleep(2)
        browser.execute_script(modal_javascript_confirm)
        # waiting for javascript
        time.sleep(2)
        
        # Success message print
        print "Message \"%s\" sent to %s" %(SMS_MESSAGE, DESTINATION_NUMBER)
        
        
        
        