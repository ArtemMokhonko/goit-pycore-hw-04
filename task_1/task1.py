def total_salary(path):
    try:
        total_sum = 0
        num_employers = 0

        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                employer, salary = line.strip().split(',')
                total_sum += int(salary)
                num_employers += 1
                
        if num_employers > 0:
            average_salary = total_sum // num_employers
        else:
            average_salary = 0

        return total_sum, average_salary
    
    except FileNotFoundError:
        print('File not found')
        return 0, 0
    except Exception as error:
        print(error)
    


total, average = total_salary("task_1\\salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")