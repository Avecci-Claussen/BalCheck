# BalCheck

This Python code fetches the balance and xBalance for a list of Bitcoin addresses using authorized APIs, making sure the users interact with their own API. Here's a simple explanation of how it works:

The code uses asyncio, aiohttp, and lxml libraries for asynchronous HTTP requests, handling responses, and parsing HTML content.

The fetch_balance function asynchronously retrieves the balance and xBalance for a given Bitcoin address from an authorized API.

The main function reads Bitcoin addresses from "adr.txt", fetches their balances using fetch_balance, and writes the results to "bala.txt" if the balance is greater than or equal to 0.000001 BTC.

To use their own authorized API, users need to replace the url variable in the fetch_balance function with the endpoint of their API. Additionally, if the API requires authentication, users can include the necessary headers or credentials in the HTTP request.

The code executes the main function using asyncio.run(main()), initiating the asynchronous process to fetch balances for the provided addresses from the user's authorized API.

Note: Users should ensure that they have proper authorization to access the API they are using. set max 10 addresses per run and respect API rules
