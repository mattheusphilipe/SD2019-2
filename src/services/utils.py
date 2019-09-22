def encode_decode(data, option):
    if option == 1:
        return data.encode("utf-8")
    elif option == 2:
        return data.decode("utf-8")
    else:
        return None
