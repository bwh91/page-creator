import argparse

# This script creates as many test html files as needed
# with links on everypage linking to all other pages
# It allows the use of templates for header and footer and adds
# Links in the middle of the two templates


def get_html_template(header_path, footer_path):
    start_html = "<html></body>"
    end_html = "</body></html>"

    if(header_path != ""):
        with open(header_path) as f:
            start_html = f.read()

    if(footer_path != ""):
        with open(footer_path) as f:
            end_html = f.read()

    return start_html, end_html



def create_links(num_pages, page_name, header, footer):
    #count = 0
    links = ""

    for count in  range(num_pages):
        links += "<a href='" + page_name + str(count) + ".html'>" + page_name + str(count) + "</a><br />"
    start_html, end_html = get_html_template(header, footer)
    html = start_html + links + end_html

    for count in  range(num_pages):
        file_name = page_name + str(count) + ".html"
        with open(file_name, 'w') as f:
            f.write(html)


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-n', dest="number", default=5, type=int, help="Number of pages to create")
    parser.add_argument('-f', dest="filename", default="test", help="Base filename")
    parser.add_argument('-b', dest="header", default="", required=False, help="Header template path")
    parser.add_argument('-e', dest="footer", default="", required=False, help="Footer template path")
    args = parser.parse_args()

    create_links(args.number, args.filename, args.header, args.footer)





#create_links(10, "test")


if __name__ == "__main__":
   main()
