# OFD Automation Tests - UNO Spring 2018 Capstone 

Welcome to the University of Nebraska Omaha's MS in Management Information Systems Spring 2018 section 2 Capsone project. This repository is used to house our automated unit test framework developed for the Omaha Fire Department's, or OFD's, Incident Tracking system. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

If you are brand new to GitHub I recommend checking  the following: 
* [GitHub Guide's Hello World example](https://guides.github.com/activities/hello-world/)
* [How to Clone a repository](https://help.github.com/articles/cloning-a-repository/)

### Prerequisites

* Install [python](https://www.python.org/downloads/release/python-363/) on your local machine
* [Python 3 Installation Guides](http://docs.python-guide.org/en/latest/starting/installation/)

```
[python 3.6.3](https://www.python.org/downloads/release/python-363/)
```

### Installing

Download the git repository and install the requirements 

```
$ pip install -r requirements.txt
```

## Running the tests

Change line 21 in `OFD\TestAutomation\UnitTests\GoogleTests.py` to reflect the path on disk you've downloaded the repository to, for me this is C:\git\..

We will change this to a cleaner method later.
```
self.browser = webdriver.Chrome('C:\git\OFD\TestAutomation\Drivers\chromedriver.exe')
```

Open command prompt and run the following command. You need be able to [run python from the PATH](https://docs.python.org/3/using/windows.html#configuring-python) for this to work.
```
python c:/git/OFD/TestAutomation/UnitTests/GoogleTests.py
```

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

## Deployment

TODO: Add additional notes about how to deploy this on a live system and integrate with source control deployments.

## Built With

* [Selenium](https://pypi.python.org/pypi/selenium) - The web framework used

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Joshua Shapland** - *Initial work* - [jmshapland](https://github.com/zoint)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Selenium automation framework
