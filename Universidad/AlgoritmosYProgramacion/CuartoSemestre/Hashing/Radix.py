import time

# Returns a random 8-digit key.
def get_key(key):
        tamaño = len(str(key)) // 2
        hash_key = ""
        for i in range(tamaño, len(str(key ** 2)) - tamaño):
            hash_key = hash_key + str(key ** 2)[i]
        return hash_key

if __name__ == "__main__":
    # Get the first key
    print(get_key(675248))
