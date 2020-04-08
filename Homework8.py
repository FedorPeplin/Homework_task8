from pprint import pprint
from collections import defaultdict
import pprint
cook_book={}
dishnumber=[]
dishnames_string = []
ingridient_names_final=[]
ingridient_quantity=[]
ingridient_quantity_final=[]
ingridient_measure=[]
ingridient_measure_final=[]
ingridient_names = []

def dishnumbersearch():
    with open ('recipes.txt') as f:
        for line in f:
            line = line.strip()
            # print (line)
            line2=line.split()
            try:
                a=int(list(line2[0])[0])
                dishnumber.append(a)
            except ValueError:
                pass
            except IndexError:
                pass
            except ValueError:
                pass
    #result - dishnumber
dishnumbersearch()

def namesearch():
    with open ('recipes.txt') as f:
        dishnames = []
        for line in f:
            line = line.strip()
            # print (line)
            line2=line.split()
            if len(line2) <= 3:
                pass
                try:
                    a=(int(line2[0])/1)
                except IndexError:
                    pass
                except ValueError:
                    dishnames.append(line2)
        for i in dishnames:
            if len(i) > 1:
                j=' '.join(i)
            else:
                j = str(i[0])
            dishnames_string.append(j)
    #result - dishnames
namesearch()

def search_ingridientsnames():
    global ingridient_names_final
    with open('recipes.txt') as f:
        for line in f:
            line = line.strip()
            # print (line)
            line2 = line.split()
            try:
                i=0
                if len(line2) > 3 or len(line2)<1:
                    ingridient_names.append(line2[0])
                    if line2[1] != '|':
                        ingridient_names.append(line2[1])
            except IndexError:
                ingridient_names.append('_')
    from itertools import groupby
    ingridient_names_final=[list(g) for k, g in groupby(ingridient_names, key=lambda i: i != '_') if k]
    for lst in ingridient_names_final:
        new_lst = []
        for s in lst:
            if s[0].islower():
                new_lst[-1] += ' ' + s
            else:
                new_lst.append(s)
        lst[:] = new_lst
    #result - ingridient_names_final
search_ingridientsnames()

def search_ingridientquantity():
    global ingridient_quantity_final
    with open('recipes.txt') as f:
        for line in f:
            line = line.strip()
            # print (line)
            line2 = line.split()
            try:
                i=0
                if len(line2) > 3 or len(line2) == 0:
                    ingridient_quantity.append(line2[-3])
            except IndexError:
                ingridient_quantity.append('_')
        from itertools import groupby
        ingridient_quantity_final = [list(g) for k, g in groupby(ingridient_quantity, key=lambda i: i != '_') if k]
        for j in ingridient_quantity_final:
            for i, item in enumerate(j):
                j[i] = int(item)
    #result - ingridient_quantity_final
search_ingridientquantity()

def search_ingridientmeasure():
    global ingridient_measure_final
    with open('recipes.txt') as f:
        for line in f:
            line = line.strip()
            # print (line)
            line2 = line.split()
            try:
                i=0
                if len(line2) > 3 or len(line2) == 0:
                    ingridient_measure.append(line2[-1])
            except IndexError:
                ingridient_measure.append('_')
        from itertools import groupby
        ingridient_measure_final = [list(g) for k, g in groupby(ingridient_measure, key=lambda i: i != '_') if k]
    #result - ingridient_measure_final
search_ingridientmeasure()

def print_final_dict():
    global cook_book
    # zip data together, extract the typ again, put the remainder into R
    for typ, *R in zip(dishnames_string, ingridient_names_final, ingridient_quantity_final, ingridient_measure_final):
        # add the typ-list
        cook_book.setdefault(typ,[])
        # now handle the inner dicts data that have to be added to your lists
        # first create tuples for each animal as r
        for r in zip(*R):
            # then create tuples of (key,value) and make dicts from it
            cook_book[typ].append(dict(zip(["ingridient_name","quantity","measure"],r)))

    from pprint import pprint

    pprint(cook_book)
print_final_dict()

def get_shop_list_by_dishes():
    from collections import defaultdict
    import pprint
    desiredhowmuchdish=input('Введите ингридиенты для блюд для скольки персон вы хотите получить? ')
    desireddish = [str(i) for i in input('Введите желаемые блюда через пробел(если в имени блюда два слова - то добавить "_" между словами) ').split()]
    print (desireddish)
    print (dishnames_string)
    try:
        desired_index=[]
        desired_ingridients=[]
        zipped_ingridients=[]
        zipped=[]
        finalzip=[]
        finestzip=[]
        new_book={}
        for element in desireddish:
            desired_index.append(dishnames_string.index(element))
        for element in desired_index:
            zipped_ingridients=zip(ingridient_names_final[element],ingridient_quantity_final[element],ingridient_measure_final[element])
            zipped=finalzip.append((list(zipped_ingridients)))
        for elems in finalzip:
            finestzip.extend(elems)
        # print (finestzip)
        counts = defaultdict(int)
        for ingredient, quantity, measure in finestzip:
            quantity_real=(int(desiredhowmuchdish))*quantity
            counts[(ingredient, measure)] += quantity_real
        result = {ingredient: {'measure': measure, 'quantity': quantity} for (ingredient, measure), quantity in
                  counts.items()}
        pprint.pprint(result)
    except ValueError:
        print ('Таких блюд нет в списке')
    except IndexError:
        pass
get_shop_list_by_dishes()
