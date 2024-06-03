import sys

def get_input():
    shelf_dict = {}
    shopping_list = []

    def process_shelf_input(shelves_processed, num_shelves):
        if shelves_processed < num_shelves:
            item = input(f"Zadejte zboží pro regál {shelves_processed}: ").strip()
            if item == "":
                process_shelf_input(shelves_processed + 1, num_shelves)
            else:
                shelf_dict[item.lower()] = shelves_processed
                process_shelf_input(shelves_processed, num_shelves)
        else:
            process_shopping_list_input()

    def process_shopping_list_input():
        item = input("Zadejte zboží, které chcete koupit: ").strip()
        if item == "":
            optimized_shopping_list = optimize_shopping_list(shelf_dict, shopping_list)
            print("Optimalizovaný nákupní seznam:")
            for index, item in enumerate(optimized_shopping_list):
                print(f"{index}. {item[1].upper()} -> #{item[0]} {item[1]}")
        else:
            shopping_list.append(item.lower())
            process_shopping_list_input()

    num_shelves = int(input("Zadejte počet regálů: "))
    process_shelf_input(0, num_shelves)

def find_item(shelf_dict, item):
    for key in shelf_dict:
        if item in key:
            return shelf_dict[key]
    return float('inf')

def optimize_shopping_list(shelf_dict, shopping_list):
    shopping_list.sort(key=lambda item: find_item(shelf_dict, item))
    return [(find_item(shelf_dict, item), item) for item in shopping_list]

if __name__ == "__main__":
    get_input()