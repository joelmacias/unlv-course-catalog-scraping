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

plainTextClassLinks = remove_duplicates(plainTextClassLinks)

for i in plainTextClassLinks:
	print i



'''
#Close file
#f.close()

# click all the class links 
for i in classLinks:
	linkToClick = i
	linkToClick.click()



# Close Firefox browser
driver.quit()
'''











'''
for i in classLinks:
	print i.text
'''

#print len(classLinks)

'''

'''

# Array to hold course abbreveation(e.g., CS 135)
#print classLinks[3].text

#courseNamesAbbrevations 

'''

for i in classLinks:
	 courseNamesAbbrevations = i.text
print len(courseNamesAb

for i in courseNamesAbbrevations:
	print i

print len(classLinks)
print classLinks[1]
'''
# courseNamesAbbrevations = list(classLinks)
