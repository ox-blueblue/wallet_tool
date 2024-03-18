from playwright.sync_api import Playwright, sync_playwright, Page
from logger import log
import sys
from mylib import *

OKX_SELECT = "//p[@class='_name_qdhwz_51'][text()='OKX']"
OKX_CONNECT = "//div[text()='Connect']"
OKX_PWD_INPUT = "//div[@class='okui-input-box']/input"
OKX_UNLOCK = "//span[@class='btn-content'][text()='Unlock']"
OKX_WEB_PWD_INPUT = '//*[@id="app"]/div/div/div/div[3]/form/div[1]/div/div/div/div/div/input'
OKX_WEB_UNLOCK = '//*[@id="app"]/div/div/div/div[3]/form/div[2]/div/div/div/button/span'
OKX_CONFIRM = "//span[text()='Confirm']"

class WalletTool:    
    def __init__(self, page:Page, password:str):
        self.pwd = password
        self.page = page

    def oper_sleep(self):
        base = 2000
        self.page.wait_for_timeout(random.randint(base-100, base+100))
        
    def okx_login_web(self):
        # 打开okx钱包页面
        log.debug('login okx wallet')   
        self.page.goto('chrome-extension://dkaonkcpflfhalioalibgpdiamnjcpbn/home.html')
        # 等待页面加载完成
        logined = '.okui-select-value-box'
        self.page.wait_for_load_state("domcontentloaded")
        if wait_for_selector_attached(self.page, OKX_WEB_UNLOCK, timeout=5000) is None:
            if selector_is_exist(self.page, logined):
                log.info('okx wallet logined')   
                return True
            else:
                log.error('login okx wallet fail')
                return False    
        # 登录钱包
        self.page.locator(OKX_WEB_PWD_INPUT).fill(self.pwd)
        self.oper_sleep()
        self.page.locator(OKX_WEB_UNLOCK).click()    
        # 检查是否登录成功    
        if wait_for_selector_attached(self.page, logined, timeout=5000) is None:
            loc = self.page.locator('.okui-form-item-control-extra')
            if loc.count():
                log.error(f"login faile: {loc.inner_text()}")
        else:
            log.info('login okx wallet success')
        return True
        
    def okx_ex_login(self):
        context = self.page.context
        wallet_page = context.pages[len(context.pages)-1] 
        loc = wait_for_selector_attached(wallet_page, OKX_UNLOCK, timeout=2000)
        if loc :
            wallet_page.locator(OKX_PWD_INPUT).fill(self.pwd)
            self.oper_sleep()        
            loc.click()  
            log.debug('login okx wallet...')  
            self.oper_sleep()

    def okx_ex_connect(self):    
        context = self.page.context
        wallet_page = context.pages[len(context.pages)-1] 
        loc = wait_for_selector_attached(wallet_page, OKX_CONNECT, timeout=5000)
        if loc :     
            loc.click()  
            log.debug('connect okx wallet...')  
            self.oper_sleep()               

    def okx_ex_select(self):
        context = self.page.context
        wallet_page = context.pages[len(context.pages)-1]    # 认为最后一个弹窗为弹出的钱包
        loc = wait_for_selector_attached(wallet_page, OKX_SELECT, timeout=2000)
        if loc :
            loc.click()  
            log.debug('select okx wallet...')  
            self.oper_sleep()
        return True

    def okx_ex_oper(self):           
        if selector_is_exist(self.page, OKX_SELECT):
            self.page.locator(OKX_SELECT).click() 
            log.debug('select okx wallet...') 
        elif selector_is_exist(self.page, OKX_CONNECT):
            self.page.locator(OKX_CONNECT).click()
            log.debug('connect okx wallet...') 
        elif selector_is_exist(self.page, OKX_PWD_INPUT):
            self.page.locator(OKX_PWD_INPUT).fill(self.pwd)
            self.oper_sleep()        
            self.page.locator(OKX_UNLOCK).click()
            log.debug('unlock okx wallet...') 
        else:
            log.error(f"unknow okx wallet page:{self.page.content()}")
            self.page.close()   
        
    def okx_connect(self):
        try: 
            context = self.page.context
            oper = True
            while oper:
                oper = False
                page_num = len(context.pages)
                for i in range(page_num):
                    page_okx = context.pages[i]
                    if page_okx.title().find("Wallet") != -1: 
                        oper = True
                        break
                if oper:
                    self.okx_ex_oper(page_okx)
                    self.oper_sleep()
                    continue
                break
        except Exception as r:
            s = sys.exc_info()
            log.debug("Error '%s' happened on line %d" % (s[1],s[2].tb_lineno))     

    def okx_confirm(self):
        context = self.page.context
        wallet_page = context.pages[len(context.pages)-1]        
        loc = wait_for_selector_attached(wallet_page, OKX_CONFIRM, timeout=10000) 
        if loc:
            loc.click()
            log.info("okx confirm success")
            return True   
        log.error("okx confirm faile")
        return False

if __name__ == "__main__":   
    with sync_playwright() as playwright:           
        browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
        default_context = browser.contexts[0]
        page = default_context.new_page()
        wallet = WalletTool(page, 'wallet password')
        wallet.okx_login_web()   



