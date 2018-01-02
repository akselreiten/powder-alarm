# powder-alarm
Powder alarm for Isfjorden, Sunndalsøra, Hemne, Åre, Midsund, Storlidalen, based on weather forecasts from www.yr.no. Fetching data once every 6 hours and communicates through a slack webhook integration. 

## Install:
1. git clone https://github.com/akselreiten/powder-alarm
2. cd powder-alarm
3. virtualenv venv
4. source venv/bin/activate
5. pip install -r requirements.txt


Warning: The webook integration with slack will not be accessible unless you have access to the slack work space (need to change webhook_url in communicator.py to integrate with private slack workspace)
