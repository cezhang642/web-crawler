# rescale-web-crawler

This program is a web crawler which fetches URLs and outputs crawl results to the console as the crawl proceeds.
The program first fetches the HTML document for a parent URL, parses out the URLs in the parent document and prints the parents and then its children, and then concurrently runs this again with each child as a parent URL. In the output log, parent URLs will be aligned with the left side of output, its corresponding children URLs will be indented.

## Getting Started

You should have Python3 installed on your machine to use this program. This program will work on Linux or MacOS's terminal.

### Building and Running the Application

First download the entire file, CZhang_Crawler to your local machine. Then in your console, navigate to set CZhang_Crawler as your current directory. To download all requirements, run the following command:

```
$ pip install -r requirements.txt
```
This will download all the necessary libraries needed to build the application.

To run the application, run "python3 crawler2.py" followed by a URL. This is an example of what this might look like:

```
$ python3 crawler2.py https://www.testudo.umd.edu/
```
Then you will see a log of URLs begin to print.

### Demo of application

![](Crawler_gif.gif)

## Running the tests

To run the tests, run the following command:
```
$ python3 crawler_tests.py 
```

### test details

The test tests the application on https://crouton.net/, which is a website with no links. This tests the case of parents with no children. I anticipate the output of the program to be only https://crouton.net/, which asserts true in the test. 

## Built With

* [Beautiful Soup](https://pypi.org/project/beautifulsoup4/) - library used to scrape URLs from web pages
* [URLlib](https://docs.python.org/3/library/urllib.html) - used to perform several actions on URLs

## Authors

* **Christina Zhang** 

## Acknowledgments

* Big thanks Rescale for this interesting project! 


