def truncate_words(text, max_words=25):
    words = text.split()
    return " ".join(words[:max_words]) + ("..." if len(words) > max_words else "")

