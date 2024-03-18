# wallet_tool

这是一个web3钱包操作工具
Okx钱包目前支持，其他钱包操作将在未来继续添加

### 使用方式

```
with sync_playwright() as playwright:           
	browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
	default_context = browser.contexts[0]
	page = default_context.new_page()
	wallet = WalletTool(page, 'wallet password')
	wallet.okx_login_web()  
```


### 安装

```
$ pip install wallet_tool
```


### License

[MIT](https://github.com/embzheng/wallet_tool?tab=MIT-1-ov-file)

