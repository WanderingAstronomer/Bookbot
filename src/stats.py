def get_book_as_str(path: str) -> str:
    with open(path) as f:
        return f.read()


def get_words(book_string: str) -> str:
    return book_string.split()


def get_wordcount(words: list) -> int:
    return sum(1 for word in words)


def get_char_count(book_string: str) -> dict:
    counts = {}
    for ch in book_string.lower():
        counts[ch] = counts.get(ch, 0) + 1
    return counts


# Returns list of dictionaries sorted by character frequency, descending, each on a new line.
def sort_dict(char_counts: dict) -> list:
    items = [{"char": k, "num": v} for k, v in char_counts.items()]
    items.sort(reverse=True, key=sort_on)
    return items


def sort_on(item: dict) -> int:
    return item["num"]
