# Crawl Tester

A powerful web crawler tool that extracts website content and converts it to Markdown format. Perfect for analyzing how search engines, AI agents, and bots perceive your website structure.

## 📋 Overview

Crawl Tester is a Python-based web crawler that helps you understand how your website appears to search engines and AI agents. It crawls a given URL and outputs the extracted content as clean, well-formatted Markdown, allowing you to verify that your site structure, metadata, and content are properly accessible to bots and agents.

### Key Features

- 🕷️ **Async Web Crawling**: Fast, non-blocking crawling using async/await
- 📝 **Markdown Output**: Clean, readable Markdown conversion of web content
- ⚙️ **Configurable**: Easily customize crawl behavior and output
- 🤖 **Bot-Friendly Analysis**: Test how bots and search engines see your content
- 🎯 **Flexible URLs**: Crawl any website and verify its structure
- ⏱️ **Timestamped Output**: Automatic file naming with timestamps for organization

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/crawl-tester.git
cd crawl-tester
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install Playwright browsers (one-time setup):
```bash
playwright install
```

### Basic Usage

Run the crawler on a website:

```bash
python main.py --output my_site
```

This will crawl `http://rdjarbeng.com` by default and save output to `my_site_YYYYMMDD_HHMMSS.md`.

### Custom URL

To crawl a different URL, modify the `url` parameter in `main.py`:

```python
result = await crawler.arun(url="https://your-website.com", crawler_config=config)
```

## 📦 Dependencies

- **crawl4ai**: Advanced web crawling library
- **playwright**: Browser automation for rendering JavaScript-heavy sites
- **fastapi**: (Optional) For building APIs around the crawler
- **uvicorn**: (Optional) ASGI server for FastAPI

## 📚 Project Structure

```
crawl-tester/
├── main.py              # Main crawler script
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── LICENSE             # MIT License
└── .gitignore         # Git ignore patterns
```

## 🔧 Configuration

### CrawlerRunConfig Options

The crawler can be configured using `CrawlerRunConfig()`. Some useful options:

- `verbose`: Enable detailed logging
- `wait_until`: Wait for specific page load conditions
- `timeout`: Set crawl timeout
- Custom headers and user agents

Example:
```python
config = CrawlerRunConfig(
    verbose=True,
    timeout=30
)
result = await crawler.arun(url="https://example.com", crawler_config=config)
```

## 💡 Use Cases

- **SEO Analysis**: Verify how search engines see your content
- **Bot Testing**: Check how AI agents perceive your site structure
- **Content Verification**: Ensure metadata and structured data are properly exposed
- **Accessibility Audit**: Verify semantic HTML is crawlable
- **Web Scraping**: Extract and archive website content as Markdown
- **Monitoring**: Track how bots index your site over time

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Troubleshooting

### Playwright not installed
If you get errors related to Playwright browsers, run:
```bash
playwright install
```

### Connection timeouts
Increase the timeout in `CrawlerRunConfig`:
```python
config = CrawlerRunConfig(timeout=60)  # 60 seconds
```

### JavaScript rendering
The crawler automatically handles JavaScript-rendered content through Playwright.

## 📮 Support

For issues, questions, or suggestions, please open an [Issue](https://github.com/yourusername/crawl-tester/issues).

## 🙏 Acknowledgments

- [crawl4ai](https://github.com/unclecode/crawl4ai) - Advanced web crawling library
- [Playwright](https://playwright.dev/) - Browser automation
- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework

---

Made with ❤️ by developers, for developers
