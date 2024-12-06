import csv

#입력받기(날짜)
def get_date(date_str):  # 날짜를 튜플로 저장
    month, day = list(map(int, date_str.split("/")))
    return month, day

#입력받기(수익, 지출)
def get_amount(amount):  # 수익과 지출을 튜플로 저장
    amount = int(amount)    
    if amount > 0:
        return amount, 0
    elif amount < 0:
        return 0, -amount
    else:
        return 0, 0

#CSV 파일에 저장하기
def save_to_csv(date, income_expense, detail):
    with open("./money_book/data.csv", mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([date[0], date[1], income_expense[0], income_expense[1], detail])


if __name__ == "__main__":
    detail = input("내역을 입력하시오 : ")
    date_str = input("날짜 입력 (MM/DD): ")
    amount = input("입출금액을 입력하시오 (5000 or -5000): ")
    save_to_csv(get_date(date_str), get_amount(amount), detail)

