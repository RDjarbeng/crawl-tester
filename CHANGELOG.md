# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-04-01

### Added
- New `--url` parameter for specifying custom URLs to crawl
- Default URL changed to `https://rdjarbeng.com` for easier testing
- Improved help descriptions for command-line arguments

### Changed
- Command-line interface now fully configurable with both `--url` and `--output` parameters
- Updated argument parser description for clarity

### Usage
```bash
# Crawl specific URL and save to custom file
python main.py --url https://example.com --output my_crawl

# Use defaults (crawls rdjarbeng.com, saves to output_*.md)
python main.py
```

## [1.0.0] - 2025-03-16

### Added
- Initial release of Crawl Tester
- Async web crawling functionality using crawl4ai
- Markdown output format for crawled content
- Command-line interface with configurable output naming
- Playwright browser automation support
- Comprehensive documentation and examples
- MIT License for open-source distribution

### Features
- Crawl websites and extract content as Markdown
- Analyze how bots and search engines perceive website structure
- Automatic timestamp-based output file naming
- Verbose logging for debugging
- Support for JavaScript-rendered content
- Configurable crawler behavior

---

## Future Releases

### [Planned]
- Configuration file support (YAML/JSON)
- Multiple URL crawling in batch
- Content filtering and post-processing options
- Output to multiple formats (HTML, JSON, PDF)
- Web UI dashboard
- REST API wrapper
- Export to common note-taking apps
- Advanced SEO analysis features

---

## How to Report Issues

If you find a bug or have a suggestion, please open an [issue on GitHub](https://github.com/yourusername/crawl-tester/issues).

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for details.
