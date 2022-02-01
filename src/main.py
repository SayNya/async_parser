import asyncio

from src.crawler.weather_crawler import WeatherCrawler

if __name__ == '__main__':
    # запускаем crawler
    weather_crawler = WeatherCrawler()
    asyncio.get_event_loop().run_until_complete(weather_crawler.crawl_content())
