"""
Example usage of the Wellfound scraper.

This file demonstrates various ways to use the scraper.
"""
import asyncio
from src.scrapers.indeed_scraper import WellfoundScraper


# Example 1: Basic usage (login + navigate to jobs)
async def example_basic_usage():
    """Simple login and navigation to job search page."""
    print("\n" + "=" * 60)
    print("EXAMPLE 1: Basic Usage")
    print("=" * 60)
    
    scraper = WellfoundScraper(headless=False, persistent=True)
    await scraper.run()


# Example 2: Custom job search
async def example_job_search():
    """Login and search for specific jobs."""
    print("\n" + "=" * 60)
    print("EXAMPLE 2: Job Search")
    print("=" * 60)
    
    scraper = WellfoundScraper(headless=False, persistent=True)
    
    try:
        # Initialize
        await scraper.initialize()
        
        # Get credentials
        credentials = await scraper.get_credentials()
        if not credentials:
            print("No credentials provided.")
            return
        
        email, password = credentials
        
        # Login
        if not await scraper.login(email, password):
            print("Login failed.")
            return
        
        # Navigate to jobs page
        if not await scraper.navigate_to_jobs():
            print("Failed to navigate to jobs page.")
            return
        
        # Search for jobs
        job_titles = ["Backend Engineer", "Full Stack Developer"]
        
        for job_title in job_titles:
            print(f"\nSearching for: {job_title}")
            await scraper.search_jobs(job_title)
            await asyncio.sleep(3)  # Wait to see results
            
            # Take screenshot of results
            screenshot_filename = f"jobs_{job_title.replace(' ', '_')}.png"
            await scraper.page.screenshot(path=screenshot_filename)
            print(f"Screenshot saved: {screenshot_filename}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        await scraper.close()


# Example 3: Browser inspection (keep browser open for manual inspection)
async def example_manual_inspection():
    """Login and keep browser open for manual inspection."""
    print("\n" + "=" * 60)
    print("EXAMPLE 3: Manual Inspection")
    print("=" * 60)
    print("Browser will stay open - you can manually inspect the page.")
    print("The scraper can be controlled from the browser.")
    
    scraper = WellfoundScraper(headless=False, persistent=True)
    
    try:
        await scraper.initialize()
        
        credentials = await scraper.get_credentials()
        if not credentials:
            return
        
        email, password = credentials
        
        if not await scraper.login(email, password):
            return
        
        if not await scraper.navigate_to_jobs():
            return
        
        print(f"\n✓ Successfully logged in and on jobs page")
        print(f"Current URL: {scraper.page.url}")
        print("\nBrowser is open. You can now:")
        print("  - Manually interact with the page")
        print("  - Test selectors")
        print("  - Inspect the DOM")
        
        # Keep browser open indefinitely
        while True:
            await asyncio.sleep(1)
            
    except KeyboardInterrupt:
        print("\nBrowser closed by user.")
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        await scraper.close()


# Example 4: Headless mode (for production/CI/CD)
async def example_headless_mode():
    """Run scraper in headless mode (no GUI visible)."""
    print("\n" + "=" * 60)
    print("EXAMPLE 4: Headless Mode")
    print("=" * 60)
    print("Running in headless mode (browser not visible)")
    
    scraper = WellfoundScraper(headless=True, persistent=True)
    
    try:
        await scraper.initialize()
        
        credentials = await scraper.get_credentials()
        if not credentials:
            return
        
        email, password = credentials
        
        print("Logging in...")
        success = await scraper.login(email, password)
        print(f"Login result: {success}")
        
        if success:
            print("Navigating to jobs page...")
            await scraper.navigate_to_jobs()
            print(f"Current page: {scraper.page.url}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        await scraper.close()


async def main():
    """Run examples based on user selection."""
    print("\nWellfound Scraper Examples")
    print("=" * 60)
    print("1. Basic Usage (login + navigate)")
    print("2. Job Search")
    print("3. Manual Inspection (keep browser open)")
    print("4. Headless Mode")
    print("0. Exit")
    
    choice = input("\nSelect example to run (0-4): ").strip()
    
    examples = {
        "1": example_basic_usage,
        "2": example_job_search,
        "3": example_manual_inspection,
        "4": example_headless_mode,
    }
    
    if choice in examples:
        await examples[choice]()
    elif choice == "0":
        print("Goodbye!")
    else:
        print(f"Invalid choice: {choice}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\nInterrupted by user.")
