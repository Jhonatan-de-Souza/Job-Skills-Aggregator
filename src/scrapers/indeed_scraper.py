from playwright.sync_api import sync_playwright, Page
from seleniumbase import sb_cdp
from time import sleep
from dataclasses import dataclass
from typing import List
from database.database import create_tables, save_jobs
import random
import re

@dataclass
class Job:
    title: str
    description: str
    website: str = "Indeed"
    
    
def scrape_jobs_on_current_page(page:Page,job_title:str) -> List[Job]:
    job_search_field = page.get_by_role('combobox',name='search: Job title, keywords, or company')
    job_search_field.click()
    job_search_field.clear()
    job_search_field.type(job_title)
    page.get_by_role('button',name='Achar vagas').click()
    
    jobs = []
    job_listings = page.locator("td.resultContent")
    listings_count = job_listings.count()
    
    for job_index in range(listings_count):
        sleep(random.randint(2,4))
        
        current_job = page.locator("td.resultContent").nth(job_index)
        
        current_job.scroll_into_view_if_needed()
        
        job_title = str(current_job.locator("h2.jobTitle span").text_content())
        print(f"Scraping job number {job_index+1} of {listings_count}")
        print(f"📄 Scraping job: {job_title}")
        # Clicking updates the right pane — no page navigation occurs
        current_job.locator("a[data-jk]").click()
        sleep(random.randint(2,4))
        
        # Wait for the right pane to update with the new description
        page.locator("#jobDescriptionText").wait_for(state="visible", timeout=15000)
        job_description = str(page.locator("#jobDescriptionText").text_content())
        
        jobs.append(Job(title=job_title, description=job_description))
    
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
            context.new_page()
            
        page.set_default_timeout(30000) 
        page.set_default_navigation_timeout(60000)
        
        page.goto("https://indeed.com",wait_until='domcontentloaded')
        jobs = scrape_jobs_on_current_page(page=page,job_title=job_title)
        save_jobs(jobs)
        input('Digite algo para encerrar a automação')
        context.close()
