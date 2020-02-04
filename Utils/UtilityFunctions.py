def is_validate_english_string(string):
    try:
        string.encode(encoding='utf-8').decode('ascii')

    except UnicodeDecodeError:
        return False
    else:
        return True
