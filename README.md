# Page Rank

Utility for scraping website metadata and generating page rank values

# Usage

TODO

# Development

### Setup

Download and install dependencies.

```sh
virtualenv env
source env/bin/activate
pip install -r requirements
```

### Tests

Run tests to make sure project was setup correctly.

```sh
python src/pageRank.py --tests=true
```


### Execution

`pageRank.py` is a script which will crawl, index, and run page rank on a large number of websites. It will then write a networkx graph or JSON file to `/output/{date and time}`.

## Authors

* **David Goldstein** - [DavidCharlesGoldstein.com](http://www.davidcharlesgoldstein.com/?github-pagerank) - [Decipher Technology Studios](http://deciphernow.com/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
