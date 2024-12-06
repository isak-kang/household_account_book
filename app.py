from flask import Flask, render_template, request, redirect, url_for
import csv
import money_book.input_save as ipsv
import money_book.review as rev


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/input_data',methods = ["GET","POST"])
def input_data():
    if request.method == "GET": #GET 127.0.0.1:5000/
        return render_template("input.html")

    else : #무조건 post method
        p_comment = request.form["input_comment"]
        p_date = request.form["input_date"]
        p_amount = request.form["input_amount"]

        print(p_amount,p_date,p_comment)

        data = ipsv.get_date(p_date)
        amount = ipsv.get_amount(p_amount)
        ipsv.save_to_csv(data, amount, p_comment)


        return redirect(url_for('index'))

@app.route("/search",methods = ["GET","POST"])
def search():
    if request.method == "GET": #GET 127.0.0.1:5000/
        return render_template("search.html")

    else : #무조건 post method
        p_date = request.form["input_date"]
        data_list = rev.get_expense_and_income(p_date)
        return render_template("search_result.html",context = data_list)

@app.route("/summary")
def summary():
    return render_template("summary.html")

@app.route("/get_monthly_total")
def get_monthly_total():
    rev.total_month_save()
    total = rev.total_month_memo
    max_total = rev.max_amount_month()
    min_total = rev.min_amount_month()
    return render_template("get_monthly_total.html",context = total,max_total=max_total,min_total=min_total)

@app.route("/get_monthly_income")
def get_monthly_income():

    rev.income_month_save()
    income = rev.income_month_memo
    max_income = rev.max_income_month()
    return render_template("get_monthly_income.html",context = income,max_income=max_income)

@app.route("/get_monthly_expense")
def get_monthly_expense():

    rev.expense_month_save()
    expense = rev.expense_month_memo
    max_expense = rev.max_expense_month()
    return render_template("get_monthly_expense.html",context = expense,max_expense=max_expense)

@app.route("/get_day_with_highest_income_and_expense")
def get_day_with_highest_income_and_expense():

    rev.income_day_save()
    rev.expense_day_save()
    max_income = rev.max_income_day()
    max_expense = rev.max_expense_day()
    return render_template("get_day_with_highest_income_and_expense.html",max_income = max_income,max_expense=max_expense)

@app.route("/get_data")
def get_data():
    print("asd")
    data_list = rev.get_data()
    print(data_list)
    return render_template("get_data.html",context = data_list)

if __name__ == "__main__":
    app.run(debug = True)



