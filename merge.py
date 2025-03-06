def merge_dictionaries():
    dict1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
    dict2 = {"f": 6, "g": 7, "h": 8, "i": 9, "j": 10}
    merged_dict = {**dict1, **dict2}
    print("Merged Dictionary:", merged_dict)

def main():
    dict1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
    dict2 = {"f": 6, "g": 7, "h": 8, "i": 9, "j": 10}
    merged_dict = {**dict1, **dict2}
    print("Dictionary 1:", dict1)
    print("Dictionary 2:", dict2)
    print("Merged Dictionary:", merged_dict)

if __name__ == "__main__":
    main()

       
        
       