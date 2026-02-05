import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig
from crawl4ai import CrawlerRunConfig

async def main():
    async with AsyncWebCrawler(verbose=True) as crawler:
        config = CrawlerRunConfig()
        result = await crawler.arun(url="https://rdjarbeng.com/personal", crawler_config=config)
        if result is not None:
            with open("output.md", "w", encoding="utf-8") as f:
                f.write(result.markdown)
            print("Successfully saved crawl output to output.md")
        else:
            print("Crawler returned no result.")

if __name__ == "__main__":
    asyncio.run(main())
