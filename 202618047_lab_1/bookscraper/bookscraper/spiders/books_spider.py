import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]

    start_urls = [
        "https://books.toscrape.com/catalogue/page-1.html"
    ]

    page_count = 1
    max_pages = 5

    def parse(self, response):

        # Get all book links on the current page
        books = response.css("article.product_pod h3 a::attr(href)").getall()

        # Visit each book
        for book in books:
            book_url = response.urljoin(book)
            yield scrapy.Request(url=book_url, callback=self.parse_book)

        # Go to next page (only until page 5)
        if self.page_count < self.max_pages:
            next_page = response.css("li.next a::attr(href)").get()

            if next_page:
                self.page_count += 1
                next_page_url = response.urljoin(next_page)
                yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_book(self, response):

        yield {

            "title": response.css("div.product_main h1::text").get(),

            "category": response.css(
                "ul.breadcrumb li:nth-child(3) a::text"
            ).get(),

            "price": response.css(
                "p.price_color::text"
            ).get(),

            "rating": response.css(
                "p.star-rating::attr(class)"
            ).get().replace("star-rating ", ""),

            "availability": response.css(
                "p.availability::text"
            ).getall()[-1].strip(),

            "product_description": response.css(
                "#product_description + p::text"
            ).get(),

            "upc": response.xpath(
                '//th[text()="UPC"]/following-sibling::td/text()'
            ).get(),

            "number_of_reviews": response.xpath(
                '//th[text()="Number of reviews"]/following-sibling::td/text()'
            ).get(),

            "product_url": response.url
        }