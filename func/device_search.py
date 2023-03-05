import asyncio
from bleak import BleakScanner


def device_search():
    async def run():
        devices = await BleakScanner.discover()
        return [i for i in devices if 'WT901' in i.name]    
     
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(run())