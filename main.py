from flask import Flask, jsonify, render_template, request
import yfinance as yf
import llm_app

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello, this is a test deployment!"

@app.route("/llm")
def llm():
  return render_template('llm.html')

@app.route('/answer', methods=['POST'])
def answer():
  """
  フォームから送信された株価コードを受け取り、株価情報を表示する
  """
  try:
    # フォームから株価コードを取得
    stock_code = request.form['stock'] 

    # yfinanceを使って株価データを取得
    ticker = yf.Ticker(stock_code)
    stock_info = ticker.info

    result_llm = llm_app.kenkai_kabuka(stock_code)

    # 株価情報から必要なデータを取り出す
    company_name = stock_info.get('longName')
    current_price = stock_info.get('currentPrice')
    day_high = stock_info.get('dayHigh')
    day_low = stock_info.get('dayLow')

    return render_template('answer.html',
                           company_name=company_name,
                           current_price=current_price,
                           day_high=day_high,
                           day_low=day_low,
                           result_llm=result_llm)

  except Exception as e:
    # エラーが発生した場合はエラーメッセージを表示
    error_message = f"エラーが発生しました: {e}"
    return render_template('error.html', error_message=error_message)

@app.route("/data")
def data():
  data = {
    "name": "Wataru",
    "id": "15",
    "age": "33",
    "from": "JP"
  }
  return jsonify(data)

if __name__ == "__main__":
  app.run(debug=True)