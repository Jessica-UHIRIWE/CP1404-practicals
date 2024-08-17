import wikipedia


def main():
    """Main function to interact with the Wikipedia API."""
    while True:
        # Prompt the user for input
        query = input("Enter page title: ").strip()

        # Break the loop if the input is blank
        if not query:
            print("Thank you.")
            break

        try:
            # Attempt to get the Wikipedia page
            page = wikipedia.page(query, autosuggest=False)
            # Print the page details
            print(page.title)
            print(page.summary)
            print(page.url)
        except wikipedia.DisambiguationError as e:
            # Handle the case where the query is ambiguous
            print(f"We need a more specific title. Try one of the following, or a new search:\n{e.options}")
        except wikipedia.PageError:
            # Handle the case where the page is not found
            print(f'Page id "{query}" does not match any pages. Try another id!')
        except Exception as e:
            # Handle any other exceptions
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
