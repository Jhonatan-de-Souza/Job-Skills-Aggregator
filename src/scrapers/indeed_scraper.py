from playwright.sync_api import sync_playwright
from seleniumbase import sb_cdp
from time import sleep

def scrape_jobs(job_title:str):
    # Loading undetect chrome browser
    sb = sb_cdp.Chrome()
    endpoint_url = sb.get_endpoint_url()

    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(endpoint_url)
        context = browser.contexts[0]
        
        if context.pages:
            page = context.pages[0]
        else:
            context.new_page()
            
        page.set_default_timeout(30000) 
        page.set_default_navigation_timeout(60000)
        
        page.goto("https://indeed.com",wait_until='domcontentloaded')
        job_search_field = page.get_by_role('combobox',name='search: Job title, keywords, or company')
        job_search_field.click()
        job_search_field.clear()
        job_search_field.type(job_title)
        # click through each job listing
        # get all of the information inside of a #jobDescriptionText id
        
        
        input('Digite algo para encerrar a automação')
        context.close()