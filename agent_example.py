"""
browser-use örnek agent scripti.
Önceden yüklenmiş Chromium'u kullanır — playwright install gerekmez.
"""

import asyncio
import os

from browser_use import Agent
from browser_use.browser.profile import BrowserProfile
from browser_use.browser.session import BrowserSession
from langchain_anthropic import ChatAnthropic

CHROMIUM_PATH = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

async def run_agent(task: str) -> str:
    llm = ChatAnthropic(
        model="claude-haiku-4-5-20251001",
        api_key=os.environ["ANTHROPIC_API_KEY"],
    )

    profile = BrowserProfile(
        executable_path=CHROMIUM_PATH,
        headless=True,
        args=["--no-sandbox", "--disable-dev-shm-usage"],
    )
    session = BrowserSession(browser_profile=profile)

    agent = Agent(task=task, llm=llm, browser_session=session)
    result = await agent.run()
    return result

if __name__ == "__main__":
    task = "Go to example.com and return the page title."
    result = asyncio.run(run_agent(task))
    print(result)
