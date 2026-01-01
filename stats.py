def count_words(text):
    """Return the number of words in the text."""
    return len(text.split())


def count_characters_in_words(text):
    """Return a dictionary with character counts."""
    character_count = {}

    for word in text.split():
        for character in word.lower():
            if not character.isalpha():
                continue
            if character in character_count:
                character_count[character] += 1
            else:
                character_count[character] = 1

    return character_count


def convert_counts_to_list(counts_dict):
    """Convert character count dictionary to list of dictionaries."""
    counts_list = []

    for character, count in counts_dict.items():
        counts_list.append({"character": character, "count": count})

    return counts_list


def get_count_for_sorting(item):
    """Return the count value for sorting."""
    return item["count"]


def get_sorted_character_counts(text):
    """Return sorted character counts as a formatted string."""

    character_counts = count_characters_in_words(text)
    count_list = convert_counts_to_list(character_counts)
    count_list.sort(reverse=True, key=get_count_for_sorting)

    formatted_lines = []

    for item in count_list:
        formatted_lines.append(f"{item['character']}: {item['count']}")

    return "\n".join(formatted_lines)
