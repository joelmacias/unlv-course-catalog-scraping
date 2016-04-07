from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# removing duplicates from class list
def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output


# Creates a Firefox instance 
driver = webdriver.Firefox()

# Navigate to a page given by the URL
driver.get("http://catalog.unlv.edu")


# Locates search field and saves it 
elem = driver.find_element_by_name("filter[keyword]")

# Types "CS" into saved search field
elem.send_keys("CS")

# Presses enter to search for "CS"
elem.send_keys(Keys.RETURN)

# In case nothing is found
assert "No results found." not in driver.page_source

# Save all links that begin with "CS"
classLinks = driver.find_elements_by_partial_link_text('CS')

# Course names will be written to this file
f = open('computer-science-list','w')

# Wrtie course names to file
for i in classLinks:
	f.write(i.text)
	f.write('\n')

# Empty list
plainTextClassLinks = []

# Save link text to list
for i in classLinks:
	plainTextClassLinks.append(i.text)

# function call to remove duplicates items from list
plainTextClassLinks = remove_duplicates(plainTextClassLinks)

# Click all class links to expose number of credits and pre reqs
for i in classLinks:
	linkToClick = i
	linkToClick.click()

# Empty list
classDescriptions = []

# starting expath for class descriptions
# tbody/tr[3] is the first course on the site
classDescriptionsXpath ='//*[@id="gateway-page"]/body/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[3]/td/table/tbody/tr/td/div[2]'

# number of courses
numberOfClassLinks = len(classLinks)
# Save class descriptions
classDescriptions = driver.find_elements_by_xpath('//*[@id="gateway-page"]/body/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[4]/td/table/tbody/tr/td/div[2]')

#classDescriptions = driver.find_elements_by_xpath('//*[@id="gateway-page"]/body/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/')


for description in classDescriptions:
	print description.text

# Close Firefox browser
