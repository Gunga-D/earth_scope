from obspy import read

if __name__ == '__main__':
    file_path = input("Enter the path of mseed file:\n")
    mseed = read(file_path)
    print(mseed)