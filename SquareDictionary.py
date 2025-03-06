class SquareDictionary:
    @staticmethod
    def generate_square_dict():
        return {x: x**2 for x in range(1, 31)}

if __name__ == "__main__":
    print("Dictionary of squares:", SquareDictionary.generate_square_dict())
