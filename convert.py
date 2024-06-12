from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import base64


import argparse


arg_parser = argparse.ArgumentParser(description="Convert a webpage to PDF")
arg_parser.add_argument("--url", type=str, help="URL of the webpage to convert")
arg_parser.add_argument("--pdf", type=str, help="Output PDF file path")
arg_parser.add_argument(
    "--size", type=str, help="'A4' or 'Letter' size of the PDF", default="A4"
)
args = arg_parser.parse_args()


# path to chromedriver
chromedriver_path = "/usr/bin/chromedriver"

# set up chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# initialize chromedriver
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# open the url
driver.get(args.url)


match args.size:
    case "A4":
        width = 8.27
        height = 11.69
    case "Letter":
        width = 8.5
        height = 11
    case _:
        raise ValueError("Invalid size argument. Use 'A4' or 'Letter'")


# command to print to PDF with options
print_options = {
    "printBackground": True,
    "displayHeaderFooter": False,
    "paperWidth": width,
    "paperHeight": height,
}

# execute the command to print to pdf
result = driver.execute_cdp_cmd("Page.printToPDF", print_options)
pdf_data = base64.b64decode(result["data"])

# set the output file path
with open(args.pdf, "wb") as f:
    f.write(pdf_data)

# close the browser
driver.quit()
