def get_total_of_words(text: str) -> int:
    return len(text.split())


def get_total_chars_by_book(book: str) -> dict[str, int]:
    result: dict[str, int] = {}

    for c in book:
        fixed_character = c.lower()
        if fixed_character in result:
            result[fixed_character] += 1
        else:
            result[fixed_character] = 1

    return result


def sort_on(payload: dict[str, str | int]) -> int:
    if type(payload["num"]) == int:
        return payload["num"]
    else:
        return 0


def get_alphabetical_order_list_of_chars(
    result: dict[str, int],
) -> list[dict[str, str | int]]:
    order_list: list[dict[str, str | int]] = []

    for c in result:
        if c.isalpha():
            order_list.append({"name": c, "num": result[c]})

    order_list.sort(reverse=True, key=sort_on)

    return order_list
