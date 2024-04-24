def get_cats_info(path):
    try:    
   
        with open(path, 'r', encoding='utf-8') as file:
            cats_list=[]
            for line in file:
                cats_info = line.strip().split(',')
                cats_list.append({"id":cats_info[0], "name":cats_info[1], "age":cats_info[2]})
             
            return cats_list
            
    except FileNotFoundError:
        print('File not found')
        return []
    except Exception:
        print('some outher mistake')
        return [] 


cats_info = get_cats_info("task_2\cats.txt")
for cat in cats_info:
    print(cat)