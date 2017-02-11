import xml.etree.ElementTree
from selenium import webdriver
from Assistant import printSubjectList

ClusterSet = [[]]

def CreateCluster(url):

    tagNames = ["ol", "ul", "dl", "dt", "tr", "th", "table", "col"]
    links = []

    driver = webdriver.Chrome()
    driver.get(url)

    for tag in tagNames:
        links.append(driver.find_elements_by_tag_name(tag))


if __name__ == '__main__':

    printSubjectList()


