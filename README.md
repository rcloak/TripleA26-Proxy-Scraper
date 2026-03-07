# proxy-scraper

A fast, multi-threaded proxy scraper that collects proxies from multiple public sources, removes duplicates, and saves them to a single file.

> Updated it because I ran out of paid proxies xd. Free ones it is.

## Features

- Scrapes from 70+ public proxy sources simultaneously
- Removes duplicate proxies automatically
- Outputs a clean, sorted list ready to use
- Configurable thread count and timeout

## Requirements

- Python 3.10+
- `requests`

Install dependencies:

```
pip install requests
```

## Usage

1. Add your source URLs to `links.txt`, one per line.
2. Run the script:

```
python main.py
```

3. Results are saved to `proxies.txt`.

## Configuration

Edit these values at the top of `scraper.py`:

| Variable | Default | Description |
|---|---|---|
| `MAX_WORKERS` | `30` | Number of parallel threads |
| `REQUEST_TIMEOUT` | `15` | Seconds before a request is dropped |

Increase `MAX_WORKERS` for faster scraping on a good connection. Decrease `REQUEST_TIMEOUT` to skip slow sources faster.

## Output

- `proxies.txt` — all unique proxies in `IP:PORT` format, one per line, sorted

## Sources

The included `links.txt` contains 70+ sources updated daily or hourly, including:

- [TheSpeedX/PROXY-List](https://github.com/TheSpeedX/PROXY-List)
- [monosans/proxy-list](https://github.com/monosans/proxy-list)
- [ErcinDedeoglu/proxies](https://github.com/ErcinDedeoglu/proxies)
- [proxifly/free-proxy-list](https://github.com/proxifly/free-proxy-list)
- [ShiftyTR/Proxy-List](https://github.com/ShiftyTR/Proxy-List)
- [zevtyardt/proxy-list](https://github.com/zevtyardt/proxy-list)
- proxyscrape.com, proxyspace.pro, spys.me, and more

## Notes

- This tool only collects and deduplicates proxies. It does not verify whether they are alive or anonymous.
- Proxy availability changes constantly. For best results, run the scraper shortly before you need the proxies.
- Some sources may go offline over time. Remove dead links from `links.txt` to keep scraping fast.

## Disclaimer

This tool is provided for educational and research purposes only. I am not responsible for how you use the proxies collected by this script. Using proxies to bypass restrictions, conduct illegal activities, or violate any terms of service is entirely your own responsibility.
