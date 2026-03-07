import requests
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

MAX_WORKERS = 30
REQUEST_TIMEOUT = 15
SESSION = requests.Session()

def fetch_link(link: str) -> str:
    try:
        return SESSION.get(link.strip(), timeout=REQUEST_TIMEOUT).text
    except Exception:
        return ""

def filter_proxies(raw_lines: list[str]) -> set[str]:
    # Extract valid IP:PORT entries
    proxies = set()
    for line in raw_lines:
        try:
            i = line[line.find("/")+1:]
            i = i[i.find("/")+1:].strip()
            if 7 < len(i) < 22 and ":" in i:
                proxies.add(i)
        except Exception:
            pass
    return proxies

def main():
    os.system("cls" if os.name == "nt" else "clear")

    with open("links.txt") as f:
        links = [l.strip() for l in f if l.strip()]

    print(f"Scraping {len(links)} sources using {MAX_WORKERS} threads...")

    raw_lines = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(fetch_link, l): l for l in links}
        for i, fut in enumerate(as_completed(futures), 1):
            text = fut.result()
            if text:
                raw_lines.extend(text.splitlines())
            print(f"\rProgress: {i}/{len(links)}", end="")

    print("\nFiltering and removing duplicates...")
    proxies = filter_proxies(raw_lines)

    # Sort for consistent output
    with open("proxies.txt", "w") as f:
        f.write("\n".join(sorted(proxies)))

    print(f"Done - {len(proxies)} unique proxies saved to proxies.txt")

if __name__ == "__main__":
    main()
