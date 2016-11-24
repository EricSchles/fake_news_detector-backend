def find_urls(text):
    tokens = text.split()
    urls = []
    for token in tokens:
        if token.startswith("http"):
            urls.append(token)
    return urls
