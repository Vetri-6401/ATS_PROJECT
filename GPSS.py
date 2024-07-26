import gps

def get_gps_coordinates():
    session = gps.gps()  # Create a GPS session
    session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)  # Start streaming GPS data
    
    try:
        while True:
            report = session.next()  # Get the next GPS report
            if report['class'] == 'TPV':
                latitude = getattr(report, 'lat', None)
                longitude = getattr(report, 'lon', None)
                
                if latitude and longitude:
                    print(f"Latitude: {latitude}, Longitude: {longitude}")
                    break
    except KeyboardInterrupt:
        print("GPS data retrieval stopped.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    get_gps_coordinates()
