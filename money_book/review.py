import csv
total_month_memo = {1:0,2:0,3:0,4:0,5:0,7:0,8:0,9:0,10:0,11:0,12:0}
income_month_memo = {1:0,2:0,3:0,4:0,5:0,7:0,8:0,9:0,10:0,11:0,12:0}
expense_month_memo = {1:0,2:0,3:0,4:0,5:0,7:0,8:0,9:0,10:0,11:0,12:0}
income_day_memo = {}
expense_day_memo = {}
search_memo = []

# 달마다 얼마의 잔고가 남았나 저장
def total_month_save():
    with open("./money_book/data.csv", 'r', newline='', encoding='utf-8') as file:
        datas = csv.reader(file)
        headers = next(datas, None)# 첫 줄이 헤더일 수 있으므로 읽어들이기
        datas = list(datas)
    '''
    datas = [
    [월_1, 일_1, 이익_1, 지출_1, 내역_1],
    [월_2, 일_2, 이익_2, 지출_2, 내역_2],
    .....
    [월_n, 일_n, 이익_n, 지출_n, 내역_n]
    ]
    ''' 
    total_money = 0
    # 1~12월 선택
    for j in range(1,13):
        for data in datas: # csv파일에 저장된 월 가져오고 그 월에 맞는 이익과 지출을 딕셔너리(total_month_memo)에 저장
                data_month, data_day, income, expense, comment = data[:5] # data = [월, 일, 이익, 지출, 내역]
                if int(data_month) == j: 
                    total_money += int(income) 
                    total_money -= int(expense) 
                    total_month_memo[j]=total_money # total_month_memo = {1 : 0, 2: 5000, 3 : 6000 ....... 12:200000}
        total_money=0
    '''
    total_month_memo = {
    1 : 0, 
    2: 5000, 
    3 : 6000 
    ....... 
    12:200000
    }
    '''    
    
#달마다 입금 총합 저장.
def income_month_save():
    with open("./money_book/data.csv", 'r', newline='', encoding='utf-8') as file:
        datas = csv.reader(file)
        headers = next(datas, None)# 첫 줄이 헤더일 수 있으므로 읽어들이기
        datas= list(datas)

    income_money = 0
    # 1~12월 선택
    for j in range(1,13):
        for data in datas: # csv파일에 저장된 월 가져오고 그 월에 맞는 이익과 지출을 딕셔너리(income_month_memo)에 저장
                data_month, data_day, income, expense, comment = data[:5] # data = [월, 일, 이익, 지출, 내역]
                if int(data_month) == j: 
                    income_money += int(income) 
                    income_month_memo[j]=income_money # 
        income_money=0
    '''
    income_month_memo = {
    1 : 0, 
    2: 5000, 
    3 : 6000 
    ....... 
    12:200000
    }
    '''

#달마다 지출 총합 저장.
def expense_month_save():
    with open("./money_book/data.csv", 'r', newline='', encoding='utf-8') as file:
        datas = csv.reader(file)
        headers = next(datas, None)# 첫 줄이 헤더일 수 있으므로 읽어들이기
        datas= list(datas)

    expense_money = 0
    # 1~12월 선택
    for j in range(1,13):
        for data in datas: # csv파일에 저장된 월 가져오고 그 월에 맞는 이익과 지출을 딕셔너리(expense_month_memo)에 저장
                data_month, data_day, income, expense, comment = data[:5] # data = [월, 일, 이익, 지출, 내역]
                if int(data_month) == j: 
                    expense_money += int(expense) 
                    expense_month_memo[j]=expense_money # expense_month_memo = {1 : 0, 2: 5000, 3 : 6000 ....... 12:200000}
        expense_money=0
    '''
    income_month_memo = {
    1 : 0, 
    2: 5000, 
    3 : 6000 
    ....... 
    12:200000
    }
    '''


#날짜마다 입금총합저장
def income_day_save():
    with open("./money_book/data.csv", 'r', newline='', encoding='utf-8') as file:
        datas = csv.reader(file)
        headers = next(datas, None)
        datas= list(datas)

        for data in datas: # 월/일을 키로하고 이익을 값으로 딕셔너리(income_day_memo)에저장
            data_month, data_day, income, expense, comment = data[:5] # data = [월, 일, 이익, 지출, 내역]
            data_key = f"{data_month}/{data_day}" # 키를 "월/일"로 저장 
            income = int(income)
            if data_key in income_day_memo.keys(): #키가 존재하면 기존 키가 해당하는 값에 더해줌.
                income_day_memo[data_key] += income
            else : # 키가 존재하지 않는다면 키를 생성하고 값을 저장
                income_day_memo[data_key] = income
        '''
        income_day_memo = {
        "5/6" : 4000,
        "5/8" : 5000,
        ...
        "12/31" : 8000
        }
        '''


#날짜마다 지출총합저장
def expense_day_save():
    with open("./money_book/data.csv", 'r', newline='', encoding='utf-8') as file:
        datas = csv.reader(file)
        headers = next(datas, None)
        datas= list(datas)

        for data in datas: # 월/일을 키로하고 지출을 값으로 딕셔너리(expense_day_memo)에저장
            data_month, data_day, income, expense, comment = data[:5] # data = [월, 일, 이익, 지출, 내역]
            data_key = f"{data_month}/{data_day}" # 키를 "월/일"로 저장 
            expense = int(expense)
            if data_key in expense_day_memo.keys(): #키가 존재하면 기존 키가 해당하는 값에 더해줌
                expense_day_memo[data_key] += expense   
            else : # 키가 존재하지 않는다면 키를 생성하고 값을 저장
                expense_day_memo[data_key] = expense 
        '''
        expense_day_memo = {
        "5/6" : 4000,
        "5/8" : 5000,
        ...
        "12/31" : 8000
        }
        '''


#가장 잔고가 많은달
def max_amount_month():
    max_value = 0
    max_month = 0
    for i in total_month_memo.keys(): # 잔고가 많은 달과 그 달의 잔고를 저장.
        if total_month_memo[i] > max_value :
            max_value = total_month_memo[i]
            max_month = i
            
    return max_month, max_value


# 가장 이익이 가장 많은달
def max_income_month():
    max_value = 0
    max_month = 0
    for i in income_month_memo.keys():  # 잔고가 많은 달과 그 달의 잔고를 저장.
        if income_month_memo[i] > max_value:
            max_value = income_month_memo[i]
            max_month = i

    return max_month, max_value


# 가장 지출이 많은달
def max_expense_month():
    max_value = 0
    max_month = 0
    for i in expense_month_memo.keys():  # 잔고가 많은 달과 그 달의 잔고를 저장.
        if expense_month_memo[i] > max_value:
            max_value = expense_month_memo[i]
            max_month = i

    return max_month, max_value


#가장 잔고가 작은달
def min_amount_month():
    min_value = 10000000000000000000000000000000000 # 가장 작은 잔고를 저장해야함으로 첫 시작은 무한에 가까운 큰 수를 저장 
    min_month = 0
    for i in total_month_memo.keys(): # 잔고가 적은 달과 그 달의 잔고를 저장
        if total_month_memo[i] < min_value:
            min_value = total_month_memo[i]
            min_month = i

    return min_month, min_value


#가장 이익이 많은날
def max_income_day():
    max_income = 0
    max_month = 0
       
    for i in income_day_memo.keys():
        if income_day_memo[i]>max_income:
            max_income = income_day_memo[i]
            max_month = i

    return max_month, max_income


#가장 지출이 많은날
def max_expense_day():
    max_expense = 0
    max_month = 0
       
    for i in expense_day_memo.keys():
        if expense_day_memo[i] > max_expense:
            max_expense = expense_day_memo[i]
            max_month = i
    return max_month, max_expense

#특정 날짜를 검색해서 어떤 이익과 지출이 있었는지 저장 및 출력
def get_expense_and_income(date_str):
    month, day = date_str.split("/")
    result = []
    
    with open("./money_book/data.csv", 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader, None)
        datas= list(reader)
        
        for data in datas:
            data_month, data_day, income, expense, comment = data[:5] # row = [월, 일, 이익, 지출, 내역]
            if data_month == month and data_day == day: # 월과 일이 일치하는지 확인
                result.append({
                    'month': data_month,
                    'day': data_day,
                    'expense': int(expense),
                    'income': int(income),
                    'comment': comment
                })
                search_memo.append([data_month, data_day, expense, income, comment])

    return result

#모든 입력 데이터 출력
def get_data():
    result = []

    with open("./money_book/data.csv", 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader, None)
        datas = list(reader)

        for data in datas:
            data_month, data_day, income, expense, comment = data[:5]  # row = [월, 일, 이익, 지출, 내역]
            result.append({
                'month': data_month,
                'day': data_day,
                'expense': int(expense),
                'income': int(income),
                'comment': comment
            })

    return result



if __name__ == "__main__":
    # 인풋할 때 모두 저장되어야할 데이터.
    total_month_save()
    expense_day_save()
    income_day_save()
    expense_month_save()
    income_month_save()

    print("달마다 이익")
    print(income_month_memo)
    print("달마다 지출")
    print(expense_month_memo)
    print("달마다 총합")
    print(total_month_memo)

    # 
    print(max_amount_month())
    print(min_amount_month())

    print("날짜마다 최고 이익,지출 저장")
    print(income_day_memo)
    print(expense_day_memo)

    print("가장많은 이익,지출")
    print(max_income_day())
    print(max_expense_day())    

    #검색.
    date = input("날짜를 입력하시오 (ex>5/6) >")
    get_expense_and_income(date)