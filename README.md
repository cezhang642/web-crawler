# rescale-web-crawler

This program is a web crawler which fetches URLs and outputs crawl results to the console as the crawl proceeds.
The program first fetches the HTML document for a parent URL, parses out the URLs in the parent document and prints the parents and then its children, and then concurrently runs this again with each child as a parent URL.

## Getting Started

You should have Python3 installed on your machine to use this program. This program will work on Linux or MacOS's terminal.

### Building and Running the Application

First download crawler2.py to your local machine. Then in your console, navigate to the current directory that crawler2.py is in. To run the application, run the following command:
```
python3 crawler2.py

```
The program will then prompt you to type in the beginning URL. You should copy in the URL you want to run the program on, and then press enter. You will then see the program begin to print out the URLs. There is no stopping mechanism.

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
