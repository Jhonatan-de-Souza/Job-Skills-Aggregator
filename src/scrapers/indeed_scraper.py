from playwright.sync_api import sync_playwright, Page
from seleniumbase import sb_cdp
from time import sleep
from data.models import Job
from typing import List
from database.database import create_tables, save_jobs
import random
from utils.helper_functions import sleep_random


def scrape_jobs_on_current_page(page:Page,job_title:str) -> List[Job]:
    job_search_field = page.get_by_role('combobox',name='search: Job title, keywords, or company')
    job_search_field.click()
    job_search_field.clear()
    job_search_field.type(job_title)
    page.get_by_role('button',name='Achar vagas').click()
    
    jobs = []
    job_listings = page.locator("td.resultContent")
    listings_count = job_listings.count()
    
    try:
        for job_index in range(listings_count):
            sleep_random(4,6)
            
            current_job = page.locator("td.resultContent").nth(job_index)
            
            current_job.scroll_into_view_if_needed()
            
            job_title = str(current_job.locator("h2.jobTitle span").text_content())
            print(f"Scraping job number {job_index+1} of {listings_count}")
            print(f"📄 Scraping job: {job_title}")

            current_job.locator("a[data-jk]").click()
            sleep_random(4,6)
            
            page.locator("#jobDescriptionText").wait_for(state="visible", timeout=15000)
            job_description = str(page.locator("#jobDescriptionText").text_content())
            
            jobs.append(Job(title=job_title, description=job_description))
                
    except Exception as error:
        print(error)
    
    return jobs
        

def start_indeed_scraper(job_title:str):
    sb = sb_cdp.Chrome(headless=False, args=["--start-maximized"])
    endpoint_url = sb.get_endpoint_url()
    create_tables()

    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(endpoint_url)
        context = browser.contexts[0]
        
        if context.pages:
            page = context.pages[0]
        else:
            page = context.new_page()
            
        page.set_default_timeout(30000) 
        page.set_default_navigation_timeout(60000)
        
        page.goto("https://indeed.com",wait_until='domcontentloaded')
        jobs = scrape_jobs_on_current_page(page=page,job_title=job_title)
        save_jobs(jobs)
        input('Digite algo para encerrar a automação')
        context.close()
