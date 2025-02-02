def read():
    #lista de lista que representa um sudoku 9x9
    sudoku_list = []

    #abrindo um arquivo txt com elementos separados por "," e linhas separadas por \n
    with open('Sudoku.txt') as f:

        #criando sublistas e usando função append para liga-las a "sudoku_list"
        for line in f:
            inner_list = [int(elt.strip()) for elt in line.split(',')]
            sudoku_list.append(inner_list)
    return sudoku_list
