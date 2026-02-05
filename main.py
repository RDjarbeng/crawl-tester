import asyncio
import argparse
from datetime import datetime
from crawl4ai import AsyncWebCrawler, BrowserConfig
from crawl4ai import CrawlerRunConfig

async def main():
    parser = argparse.ArgumentParser(description='Crawl a website and save output.')
    parser.add_argument('--output', type=str, default='output', help='Base filename for the output')
    args = parser.parse_args()

    async with AsyncWebCrawler(verbose=True) as crawler:
        config = CrawlerRunConfig()
        result = await crawler.arun(url="https://rdjarbeng.com/gallery", crawler_config=config)
        if result is not None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{args.output}_{timestamp}.md"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(result.markdown)
            print(f"Successfully saved crawl output to {filename}")
        else:
            print("Crawler returned no result.")

if __name__ == "__main__":
    asyncio.run(main())
