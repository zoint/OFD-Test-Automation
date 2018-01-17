"""[This is an example unit test class to open Google. This is
meant to demonstrate a simple unit test look and feel.
Example Refernece: https://pypi.python.org/pypi/selenium 1/15/18]"
"""
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
""""[Sample tests to open Google and show a quick demonstration of Selenium usage.]"
"""
class GoogleTestCase(unittest.TestCase):
    """Sample test case"""
    # preparing to test
    def setUp(self):
        """ Setting up for the test """
        print("GoogleTestCase:setUp_:begin")

        # Optional argument, if not specified will search path.
        # TODO: UPDATE THIS PATH TO REFLECT WHERE YOU HAVE YOUR SOURCE CODE STORED.
        #       WE SHOULD UPDATE THIS LATER TO A CLEANER METHOD.
        self.browser = webdriver.Chrome('C:\git\OFD-Test-Automation\TestAutomation\Drivers\chromedriver.exe')

        self.addCleanup(self.browser.quit)
        name = self.shortDescription()
        print("setting up for " + name)

        print("GoogleTestCase:setUp_:end")

    # ending the test
    def tearDown(self):
        """Cleaning up after the test"""
        print("GoogleTestCase:tearDown_:begin")

        name = self.shortDescription()
        print("cleaning up after " + name)

        print("GoogleTestCase:tearDown_:end")

    # test that Google's page title says 'Google'
    def testGooglePageTitle(self):
        """Test routine: testGooglePageTitle"""
        print ("GoogleTestCase:testGooglePageTitle")
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)

    #test Google's search functionality by searching for selenium
    def testSearch(self):
        """Test routine: testGoogleSearch"""
        print("GoogleTestCase:testGoogleSearch")
        self.browser.get('http://www.google.com')
        elem = self.browser.find_element_by_id('lst-ib')
        elem.send_keys('seleniumhq' + Keys.RETURN)
        time.sleep(5) #pause for 5 seconds to see the result

# Run the test case
if __name__ == '__main__':
    googleSuite = unittest.TestLoader().loadTestsFromTestCase(GoogleTestCase)

    googleRunner = unittest.TextTestRunner()
    googleResult = googleRunner.run(googleSuite)

    print()
    print("---- START OF TEST RESULTS")
    print(googleResult)
    print()
    print("fooResult::errors")
    print(googleResult.errors)
    print()
    print("fooResult::failures")
    print(googleResult.failures)
    print()
    print("fooResult::skipped")
    print(googleResult.skipped)
    print()
    print("fooResult::successful")
    print(googleResult.wasSuccessful())
    print()
    print("fooResult::test-run")
    print(googleResult.testsRun)
    print("---- END OF TEST RESULTS")
    print()
