# Input files: game1.txt, game2.txt, game3.txt
# Extracted function
def load_list_of_lists(file_name):
    fin = open(file_name, "r")
    rows = [["frame0"]]
    for line in fin:
        items = line.split(" ")
        row = [ ]
        for item in items:
            value = int(item)
            row.append(value)
        
        rows.append(row)
    fin.close( )
    return rows
        


