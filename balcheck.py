import asyncio
import aiohttp
from lxml import html

async def fetch_balance(session, address):
    url = f"https://bitcoin.atomicwallet.io/address/{address}"
    async with session.get(url) as response:
        byte_string = await response.read()
        source_code = html.fromstring(byte_string)
        xpath_balance = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[3]/td[2]'
        xpath_xbalance = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[4]/td[2]'
        balance = source_code.xpath(xpath_balance)[0].text_content().strip()
        xbalance = source_code.xpath(xpath_xbalance)[0].text_content().strip()
        return address, balance, xbalance

async def main():
    addresses = []
    with open("adr.txt", "r") as adr_file:
        addresses = [line.split(':')[-1].strip() for line in adr_file]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_balance(session, address) for address in addresses]
        results = await asyncio.gather(*tasks)

    with open("bala.txt", "w") as bala_file:
        for i, (address, balance, xbalance) in enumerate(results):
            print(f"Address {i + 1}: {address}")
            print(f"  Balance: {balance}")
            print(f"  xBalance: {xbalance}\n")

            balance_float = float(balance.split()[0])
            if balance_float >= 0.000001:
                bala_file.write(f"Address {i + 1}: {address}\n")
                bala_file.write(f"  Balance: {balance}\n")
                bala_file.write(f"  xBalance: {xbalance}\n\n")

asyncio.run(main())