from behave import *
from selenium import webdriver


@given('user launch the LD1/LD2 reports page')
def launch_the_site(context):
    # initialize ChromeDriver
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://lda.senate.gov/filings/public/filing/search/")


@when('user enters report details')
def enter_report_details(context):
    search_report_type_control = context.driver.find_element("xpath", '//span[@class="select2-selection select2-selection--multiple"]')
    search_report_type_control.click()

    # Select 1st Quarter-Report
    select_report_type_option = context.driver.find_element("xpath", '//li[contains (text(),"1st Quarter - Report")][1]')
    select_report_type_option.click()

    search_filing_period_control = context.driver.find_element("xpath", '//span[@id="select2-id_report_period-container"]')
    search_filing_period_control.click()

    # Select 1st Quarter (Jan 1 - Mar 31)
    select_filing_period_option = context.driver.find_element("xpath", '//li[contains(text(),"1st Quarter (Jan 1 - Mar 31)")]')
    select_filing_period_option.click()

    search_filing_year_control = context.driver.find_element("xpath", '//span[(@id="select2-id_report_year-container")and(@title="Any Year")]')
    search_filing_year_control.click()

    # Select 2021 as Filing Year
    select_filing_year_option = context.driver.find_element("xpath", '//li[(@class="select2-results__option")and(contains(text(),"2023"))]')
    select_filing_year_option.click()


@when('user clicks search report button')
def click_search_report_button(context):
    search_button = context.driver.find_element("xpath", '//button[@id="id_search_button"]')
    search_button.click()


@then('user should land on the reports page')
def lands_on_reports_page(context):
    is_edit_button_displayed = context.driver.find_element("xpath", '//a[@class="btn btn-info"]')
    if is_edit_button_displayed.is_displayed():
        print("EXPECTED: The Edit Button Is Visible i.e. The User Is On The Reports Page")
    else:
        print("NOT EXPECTED: The Edit Button Is Not Visible i.e. The User Is Not On The Reports Page")

    # Getting the values to assert if the report search criteria is correctly passed and displayed
    entered_report_type_option = context.driver.find_element("xpath", '//ul[@class = "searchedBy-category-list"]/li[1]/span[2]').text
    entered_report_filing_period_option = context.driver.find_element("xpath", '//ul[@class = "searchedBy-category-list"]/li[2]/span[2]').text
    entered_report_filing_year = context.driver.find_element("xpath", '//ul[@class = "searchedBy-category-list"]/li[3]/span[2]').text

    assert entered_report_type_option == "1st Quarter - Report"
    assert entered_report_filing_period_option == "1st Quarter (Jan 1 - Mar 31)"
    assert entered_report_filing_year == "2023"


@then('user should be able to see the desired reports')
def able_to_see_reports(context):
    report_to_search = context.driver.find_element("xpath", '//div[@id="searchResults_filter"]')
    report_to_search.click()
    context.driver.find_element("xpath", '//div[@id="searchResults_filter"]/label/input').send_keys('ULTRA WIDE BAND ALLIANCE')

    # Checking if the table reacts to the specific report search above and number of reports displayed
    filter_match_num_reports = context.driver.find_element("xpath", '//div[@class="dataTables_info"]').text
    assert filter_match_num_reports == "1 – 1 of 1 Total Matching Filter"

    context.driver.close()
    context.driver.quit()
