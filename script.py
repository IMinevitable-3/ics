import math


def haversine(lat1, lon1, lat2, lon2):

    dLat = (lat2 - lat1) * math.pi / 180.0
    dLon = (lon2 - lon1) * math.pi / 180.0

    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0

    a = pow(math.sin(dLat / 2), 2) + pow(math.sin(dLon / 2), 2) * math.cos(
        lat1
    ) * math.cos(lat2)
    rad = 6371
    c = 2 * math.asin(math.sqrt(a))
    return rad * c


def calculate_new_coordinates_positive(start_lat, start_lon, delta_lat, delta_lon):
    # Radius of the Earth in kilometers
    R = 6371.0

    lat1 = math.radians(start_lat)
    lon1 = math.radians(start_lon)

    # Calculate the angular distance covered by delta_lat and delta_lon
    angular_distance_lat = delta_lat / R
    angular_distance_lon = delta_lon / (R * math.cos(lat1))

    # Calculate the new latitude
    lat2 = lat1 + angular_distance_lat

    # Calculate the new longitude
    lon2 = lon1 + angular_distance_lon

    lon2 = (lon2 + math.pi) % (2 * math.pi) - math.pi

    new_lat = math.degrees(lat2)
    new_lon = math.degrees(lon2)

    return new_lat, new_lon


def calculate_new_coordinates_negative(start_lat, start_lon, delta_lat, delta_lon):
    # Radius of the Earth in kilometers
    R = 6371.0

    lat1 = math.radians(start_lat)
    lon1 = math.radians(start_lon)

    # Calculate the angular distance covered by delta_lat and delta_lon
    angular_distance_lat = delta_lat / R
    angular_distance_lon = delta_lon / (R * math.cos(lat1))

    # Calculate the new latitude
    lat2 = lat1 - angular_distance_lat

    # Calculate the new longitude
    lon2 = lon1 - angular_distance_lon

    lon2 = (lon2 + math.pi) % (2 * math.pi) - math.pi

    new_lat = math.degrees(lat2)
    new_lon = math.degrees(lon2)

    return new_lat, new_lon


def sample():
    start_lat = 90  # Example starting latitude
    start_lon = -180  # Example starting longitude
    distance_along_lat = 10.0  # Example distance in latitude direction (in kilometers)
    distance_along_lon = 10.0  # Example distance in longitude direction (in kilometers)

    new_lat, new_lon = calculate_new_coordinates_positive(
        start_lat, start_lon, distance_along_lat, distance_along_lon
    )
    new_lat_, new_lon_ = calculate_new_coordinates_negative(
        start_lat, start_lon, distance_along_lat, distance_along_lon
    )
    print("New Latitude:", new_lat, new_lat_)
    print("New Longitude:", new_lon, new_lon_)
    print("distance ", haversine(new_lat, start_lon, new_lat_, start_lon))


def ForACenter(lat, long, x):
    x = x / 4
    l = [(lat, long)]
    for i in range(1, 6):
        new_lat, new_lon = calculate_new_coordinates_positive(lat, long, x, x)
        new_lat_, new_lon_ = calculate_new_coordinates_negative(lat, long, x, x)
        l.append((new_lat, long))
        l.append((new_lat_, long))
        x *= i
    return l


def grid(center_lat, center_long, dis):
    x = dis / 4
    l = [ForACenter(center_lat, center_long, dis)]
    for i in range(1, 6):
        new_lat, new_lon = calculate_new_coordinates_positive(
            center_lat, center_long, x, x
        )
        new_lat_, new_lon_ = calculate_new_coordinates_negative(
            center_lat, center_long, x, x
        )

        p = ForACenter(center_lat, new_lon, dis)
        q = ForACenter(center_lat, new_lon_, dis)
        x *= i
        l.append(p)
        l.append(q)
    return l


def display_grid(l):
    for i in l:
        print(i)


if __name__ == "__main__":
    l = grid(89.212, 120.1213, 100)
    display_grid(l)
