import json

def process_data():
    with open('haskell_code_desc.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    string1 = """
    analyze the following json file, it contains haskell code as Statement & Description as Description, generate more such examples and return only the new generated results, if the function requires additional code such as import of libraries also include it in haskell code, also strictly follow that the haskell code is correct and the description is in affermative tone:"""
    string2 = "generate 50 such quality examples in one json file."

    output_data = []
    for i in range(0, len(data), 25):
        batch = data[i:i+25]
        output_data.append(f"index:{i}\n")
        output_data.append(string1)
        output_data.append(f"[")
        for j, item in enumerate(batch):
            # new_item = f"\n{item},\n"
            output_data.append(f"{item},")
        # Append String1 and String2 after every 25 items
        output_data.append(f"]")
        output_data.append(string2)

    with open('more_haskell_code_desc.txt', 'w', encoding='utf-8') as txt_file:
        for line in output_data:
            txt_file.write(line + '\n')

process_data()
