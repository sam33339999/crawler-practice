# SELENIUM PYTHON 動態爬蟲

```shell
# 更新 pip
python -m pip install --upgrade pip

# 安裝依賴
pip install -r requirement.txt

# 導出依賴
pip freeze > requirement.txt
```

```
在 browser 中 輸入 chrome://version
可以查看到當前 chrome 版本，再根據該版本去下載適配的 webdriver
```

- [Chrome driver](https://chromedriver.chromium.org/downloads)

下載好後，可以根據自己喜好的方法使用
- 1: `driver = webdriver.Chrome()` 放在環境變數下，自動加載對應的 chromedriver
- 2: `driver = webdriver.Chrome("/usr/local/bin/chromedriver")` 放在固定位置，然後使用路徑指向該驅動


觀察 fb `c_user`, `xs` 這兩個值可能為登入依據


##### 取得所有 cookies
```python
driver.get_cookies()
```
##### 設置 cookies
```python
driver.add_cookie({"name":"c_user","domain":".facebook.com","value":"???"})
driver.add_cookie({"name":"xs","domain":".facebook.com","value":"???"})
```

##### 重新整理
```python
driver.refresh()
```

https://medium.com/marketingdatascience/selenium%E6%95%99%E5%AD%B8-%E4%B8%80-%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8webdriver-send-keys-988816ce9bed
