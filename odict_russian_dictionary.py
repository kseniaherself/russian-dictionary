# 'odict.csv'
# 'zalizniak.txt'

import time
start_time = time.time()

# получение строк из файла
def F_get_lines(f_name):
    f = open(f_name, 'r', encoding='Windows-1251')
    my_lines = f.readlines()
    #print(my_lines)
    f.close()
    return my_lines

# запись в файл
def F_write_file_w(data, f_name):
    f = open(f_name, 'w')
    f.write(data)
    #print(data)
    f.close()

# дозапись в файл
def F_write_file_a(data, f_name):
    f = open(f_name, 'a')
    f.write(data)
    #print(data)
    f.close()

# создаёт файл со всеми словоформами и грамматической информацией
def F_all_wordforms_and_grammar():
    all_lexemes = 'lexemes'
    all_wordforms = 'wordform'
    all_grammar_t = 'grammar_tags'

    F_write_file_w(all_lexemes, 'lexemes_russian_v1.tsv')
    F_write_file_w(all_wordforms, 'wordforms_russian_v1.tsv')
    F_write_file_w(all_grammar_t, 'grammar_tags_russian_v1.tsv')

    all_grammar_l = []

    f_1 = F_get_lines('odict.csv')

    for i in range(0, 102375):              # вся выборка
    #for i in range(0, 50):               # тестовая выборка
        print('\t', i)
        #print(f_1[i])
        f_1[i] = f_1[i].replace('\n', '')
        #print(f_1[i])
        wordforms_list = f_1[i].split(',')
        #print(wordforms_list)
        #print(wordforms_list[1])

        #all_lexemes = all_lexemes + '\n' + wordforms_list[0]
        #print(wordforms_list[0])
        F_write_file_a(('\n' + wordforms_list[0]), 'lexemes_russian_v1.tsv')

        if wordforms_list[1] not in all_grammar_l:
            all_grammar_l.append(wordforms_list[1])
            print(wordforms_list[1])
            F_write_file_a(('\n' + wordforms_list[1]), 'grammar_tags_russian_v1.tsv')

        for j in range(0, len(wordforms_list)):
            if (j != 1) and (wordforms_list[j] != ''):
                #all_wordforms = all_wordforms + '\n' + wordforms_list[j]
                #print(wordforms_list[j])
                F_write_file_a(('\n' + wordforms_list[j]), 'wordforms_russian_v1.tsv')

    #for elem in all_grammar_l:
    #    all_grammar_t = all_grammar_t + '\n' + elem

    #print(all_wordforms)
    #print(all_grammar_l)
    #F_write_file_w(all_lexemes, 'lexemes_russian_v1.tsv')
    #F_write_file_w(all_wordforms, 'wordforms_russian_v1.tsv')
    #F_write_file_w(all_grammar_t, 'grammar_tags_russian_v1.tsv')


F_all_wordforms_and_grammar()


# ещё нужен файл с просто начальными словоформами
print('--- %.5s seconds ---' % (time.time() - start_time))
