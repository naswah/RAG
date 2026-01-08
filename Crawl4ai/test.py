import asyncio
from crawl4ai import(
    AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, DefaultMarkdownGenerator, PruningContentFilter, CrawlResult
)

async def main():
    browser_configg= BrowserConfig(
        headless=True,
        verbose=True
    )

    async with AsyncWebCrawler(config = browser_configg) as crawler:
        crawler_config = CrawlerRunConfig(
            markdown_generator=DefaultMarkdownGenerator(
                content_filter=PruningContentFilter()
            )
        )

        result: CrawlResult= await crawler.arun (
            url= "https://hamrocsit.com/" , config= crawler_config
        )

    print(result.markdown.raw_markdown[:500])

if __name__ == "__main__":
    asyncio.run (main())