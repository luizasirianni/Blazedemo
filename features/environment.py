from selenium import webdriver


def before_all(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(5)
    context.driver.maximize_window()

    print('Passo A - antes de tudo')
def after_all(context):
    context.driver.quit()
    print('Passo B - depois de tudo')