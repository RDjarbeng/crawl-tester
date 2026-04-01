"""Setup script for Crawl Tester."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="crawl-tester",
    version="1.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A web crawler tool that converts website content to Markdown for bot analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/crawl-tester",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: Console",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "crawl-tester=main:main",
        ],
    },
    include_package_data=True,
    keywords="crawler web-scraping markdown seo bots",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/crawl-tester/issues",
        "Source": "https://github.com/yourusername/crawl-tester",
        "Documentation": "https://github.com/yourusername/crawl-tester#readme",
    },
)
