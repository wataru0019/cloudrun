import yfinance as yf

def get_stock_price(ticker_symbol):
  """
  yfinanceを使って株価を取得する関数

  Args:
    ticker_symbol: ティッカーシンボル (例: 'AAPL'、'7203.T')

  Returns:
    pandas.DataFrame: 株価データ
  """
  try:
    ticker = yf.Ticker(ticker_symbol)
    # 過去1年間の株価データを取得
    df = ticker.history(period="1y") 
    return df
  except Exception as e:
    print(f"株価の取得に失敗しました: {e}")
    return None

def get_company_news(ticker_symbol):
  """
  yfinanceを使って特定の企業のニュースを取得する関数

  Args:
    ticker_symbol: ティッカーシンボル (例: 'AAPL'、'7203.T')

  Returns:
    list: ニュースのリスト
  """
  try:
    ticker = yf.Ticker(ticker_symbol)
    news_list = ticker.news
    data = []
    for news in news_list:
        if news['content']['thumbnail']:
            data.append({
                'title': news['content']['title'],
                'date': news['content']['pubDate'],
                'summary': news['content']['summary'],
                'url': news['content']['thumbnail']['originalUrl']
            })
        else:
            data.append({
                'title': news['content']['title'],
                'date': news['content']['pubDate'],
                'summary': news['content']['summary'],
            })
    return data
  except Exception as e:
    print(f"ニュースの取得に失敗しました: {e}")
    return None

if __name__ == "__main__":
  # ティッカーシンボルを入力
  ticker_symbol = input("ティッカーシンボルを入力してください (例: AAPL, 7203.T): ")
  news_list = get_company_news(ticker_symbol)

  if news_list is not None:
    data = []
    for news in news_list:
      print(news)
      print('--------------')
    #     if news['content']['thumbnail']:
    #         data.append({
    #             'title': news['content']['title'],
    #             'date': news['content']['pubDate'],
    #             'summary': news['content']['summary'],
    #             'url': news['content']['thumbnail']['originalUrl']
    #         })
    #     else:
    #         data.append({
    #             'title': news['content']['title'],
    #             'date': news['content']['pubDate'],
    #             'summary': news['content']['summary'],
    #         })

    # print(data)
    #   print(f"タイトル: {news['title']}")
    #   print(f"発行元: {news['publisher']}")
    #   print(f"リンク: {news['link']}")
    #   print("-" * 20)