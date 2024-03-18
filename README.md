# wallet_tool [![Version][version-badge]][version-link] ![MIT License][license-badge]

This is a web3 wallet operation tool
okx wallet is currently supported, additional wallet operations will continue to be added in the future

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

[MIT](https://github.com/pythonml/wallet_tool/blob/master/LICENSE)

