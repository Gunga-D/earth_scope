from lib.interactions.fdsn import FDSNClient

client = FDSNClient('IRIS')
stream = client.timeseries('G', 'CAN', '2024-01-18T22:17:57', '2024-01-18T22:23:57')
stream.plot()