# Example usage configurations for Crawl Tester

## Basic Example

```python
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig

async def basic_crawl():
    async with AsyncWebCrawler(verbose=True) as crawler:
        config = CrawlerRunConfig()
        result = await crawler.arun(
            url="https://example.com",
            crawler_config=config
        )
        print(result.markdown)

if __name__ == "__main__":
    asyncio.run(basic_crawl())
```

## Advanced Configuration

```python
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, BrowserConfig

async def advanced_crawl():
    # Configure browser behavior
    browser_config = BrowserConfig(
        headless=True,
        viewport_width=1920,
        viewport_height=1080,
    )
    
    # Configure crawl behavior
    crawler_config = CrawlerRunConfig(
        verbose=True,
        timeout=30,
        wait_until="load_event",  # wait_complete, wait_event, load_event
    )
    
    async with AsyncWebCrawler(browser_config=browser_config, verbose=True) as crawler:
        result = await crawler.arun(
            url="https://example.com",
            crawler_config=crawler_config
        )
        
        if result:
            print(f"Status: {result.status_code}")
            print(f"Content: {result.markdown}")
            print(f"Links found: {len(result.links) if result.links else 0}")

if __name__ == "__main__":
    asyncio.run(advanced_crawl())
```

## Batch Crawling

```python
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from datetime import datetime

async def batch_crawl(urls: list):
    """Crawl multiple URLs and save results."""
    async with AsyncWebCrawler(verbose=True) as crawler:
        config = CrawlerRunConfig()
        
        for url in urls:
            try:
                result = await crawler.arun(url=url, crawler_config=config)
                
                if result:
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"crawl_{timestamp}.md"
                    
                    with open(filename, "w", encoding="utf-8") as f:
                        f.write(result.markdown)
                    
                    print(f"✓ Crawled {url} -> {filename}")
                else:
                    print(f"✗ Failed to crawl {url}")
                    
            except Exception as e:
                print(f"✗ Error crawling {url}: {e}")

if __name__ == "__main__":
    urls = [
        "https://example.com",
        "https://example.com/about",
        "https://example.com/contact",
    ]
    asyncio.run(batch_crawl(urls))
```

## With Custom Headers

```python
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig

async def crawl_with_headers():
    """Crawl with custom user agent and headers."""
    async with AsyncWebCrawler(verbose=True) as crawler:
        config = CrawlerRunConfig(
            headers={
                "User-Agent": "My Custom Bot 1.0",
                "Accept-Language": "en-US,en;q=0.9",
            }
        )
        
        result = await crawler.arun(
            url="https://example.com",
            crawler_config=config
        )
        
        if result:
            print(result.markdown)

if __name__ == "__main__":
    asyncio.run(crawl_with_headers())
```

## Error Handling

```python
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig

async def crawl_with_error_handling():
    """Crawl with comprehensive error handling."""
    try:
        async with AsyncWebCrawler(verbose=False) as crawler:
            config = CrawlerRunConfig(timeout=30)
            
            result = await crawler.arun(
                url="https://example.com",
                crawler_config=config
            )
            
            if not result:
                print("No result returned from crawler")
                return
            
            if result.status_code != 200:
                print(f"HTTP Error {result.status_code}")
                return
            
            if not result.markdown:
                print("No content extracted")
                return
            
            print("Crawl successful!")
            print(f"Content length: {len(result.markdown)} characters")
            
    except asyncio.TimeoutError:
        print("Crawl timed out")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    asyncio.run(crawl_with_error_handling())
```

## For SEO Analysis

```python
import asyncio
import json
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig

async def seo_analysis(url: str):
    """Analyze URL for SEO-relevant information."""
    async with AsyncWebCrawler(verbose=True) as crawler:
        config = CrawlerRunConfig()
        result = await crawler.arun(url=url, crawler_config=config)
        
        if not result:
            return None
        
        # Extract SEO information
        seo_data = {
            "url": url,
            "status": result.status_code,
            "title": result.metadata.get("title", ""),
            "description": result.metadata.get("description", ""),
            "content_length": len(result.markdown),
            "links_count": len(result.links) if result.links else 0,
            "has_content": bool(result.markdown),
        }
        
        return seo_data

if __name__ == "__main__":
    url = "https://example.com"
    data = asyncio.run(seo_analysis(url))
    print(json.dumps(data, indent=2))
```
