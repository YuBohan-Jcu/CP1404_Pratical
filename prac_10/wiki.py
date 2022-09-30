import wikipedia


def main():
        full_page = input("Shows: ")
        while full_page != "":
            try:
                full_page = wikipedia.page(full_page)
                print(f"{full_page.title} {full_page.summary} {full_page.url}")
            except wikipedia.exceptions.DisambiguationError as e:
                print(e.options)
            full_page = input("Title: ")

main()