from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
import assistant

class Cluster:

    def __init__(self, cluster_id):
        self._cluster_id = cluster_id
        self.cluster = []

    def add(self, web_element: WebElement):
        if not isinstance(web_element, WebElement):
            raise
        self.cluster.append(web_element)

    @property
    def cluster_id(self):
        return self._cluster_id


class XACluster:

    def __init__(self):
        self._cluster_set = []
        self._valid_clusters = []

    def create_cluster(self, url: str):
        driver = webdriver.Firefox()
        links = driver.find_elements_by_name('ul')
        links.extend(driver.find_elements_by_name('ol'))
        links.extend(driver.find_elements_by_name('dl'))
        links.extend(driver.find_elements_by_name('dt'))
        links.extend(driver.find_elements_by_name('tr'))
        links.extend(driver.find_elements_by_name('th'))
        links.extend(driver.find_elements_by_name('table'))
        links.extend(driver.find_elements_by_name('col'))

        for i in range(len(links)):
            a_tags = links[i].find_elements_by_name('a')
            cluster = Cluster(i)
            [cluster.add(a) for a in a_tags]
            self._cluster_set.append(cluster)