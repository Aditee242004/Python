import zlib

if __name__ == "__main__":
    # Take user input
    user_input = input("Enter a string to compress: ").encode()  # Convert to bytes

    # Compress the string
    compressed_data = zlib.compress(user_input)
    print("\nCompressed Data:", compressed_data)

    # Decompress the string
    decompressed_data = zlib.decompress(compressed_data).decode()  # Convert back to string
    print("Decompressed Data:", decompressed_data)
