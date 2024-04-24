from obspy import read

if __name__ == '__main__':
    file_path = input("Enter the path of mseed file:\n")
    channel = read(file_path)
    channel.plot()