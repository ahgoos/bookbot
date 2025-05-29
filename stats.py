def count_words(text) -> int:
    return len(text.split())


def count_characters(text) -> int:
    text = text.lower()
    return {char: text.count(char) for char in set(text)}


def sort_characters(symbols_dict) -> list:

    def sort_on(dict):
        return dict["num"]

    symbols = [{"char": char, "num": num} for char, num in symbols_dict.items()]
    symbols.sort(key=sort_on, reverse=True)
    return symbols
