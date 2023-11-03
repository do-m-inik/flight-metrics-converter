import argparse
import sys


def converting_kmh_to_any_speed(speed):
    print('> ' + str(round(speed / 1.852, 2)) + ' kts')
    print('> ' + str(round(speed, 2)) + ' km/h')
    print('> ' + str(round(speed / 3.6, 2)) + ' m/s')
    print('> ' + str(round(speed / 1225.044, 2)) + ' mach')


def converting_ft_to_any_dist(dist):
    print('> ' + str(round(dist, 2)) + ' ft')
    print('> ' + str(round(dist / 6076.11549, 2)) + ' NM')
    print('> ' + str(round(dist / 3280.8398950131, 2)) + ' km')
    print('> ' + str(round(dist / 3.2808398950131, 2)) + ' m')


def main():
    print(' ')
    print('========== Flight Metrics Converter v1.0.0 ==========')

    # Parsing the arguments
    parser = argparse.ArgumentParser(description="Gets kts, km/h, m/s, mach, ft, NM, km and m as input and returns "
                                                 "conversations of it")
    parser.add_argument('--kts', metavar="KNOTS", type=float, help="Speed in knots")
    parser.add_argument('--kmh', metavar="KILOMETERS_PER_HOUR", type=float, help="Speed in kilometers per hour")
    parser.add_argument('--ms', metavar="METERS_PER_SECOND", type=float, help="Speed in meters per second")
    parser.add_argument('--mach', metavar="MACH", type=float, help="Speed in speed of sound")
    parser.add_argument('--nm', metavar="NAUTICAL_MILES", type=float, help="Distance in nautical miles")
    parser.add_argument('--ft', metavar="FOOT", type=float, help="Distance in foot")
    parser.add_argument('--km', metavar="KILOMETERS", type=float, help="Distance in kilometers")
    parser.add_argument('--m', metavar="METERS", type=float, help="Distance in meters")

    if len(sys.argv) != 3:
        parser.print_help(sys.stderr)
        print('=====================================================')
        sys.exit(1)

    args = parser.parse_args()

    # Converting all speeds to km/h and all distances to ft so only 2 functions are needed
    # Those 2 functions are printing the result of the conservations
    if args.kts:
        converting_kmh_to_any_speed(args.kts * 1.852)
    elif args.kmh:
        converting_kmh_to_any_speed(args.kmh)
    elif args.ms:
        converting_kmh_to_any_speed(args.ms * 3.6)
    elif args.mach:
        converting_kmh_to_any_speed(args.mach * 1225.044)
    elif args.ft:
        converting_ft_to_any_dist(args.ft)
    elif args.nm:
        converting_ft_to_any_dist(args.nm * 6076.11549)
    elif args.km:
        converting_ft_to_any_dist(args.km * 3280.8398950131)
    else:
        converting_ft_to_any_dist(args.m * 3.2808398950131)

    print('=====================================================')
    print('= Important Note: Almost all values are not exactly =')
    print('=====================================================')

    sys.exit(0)


if __name__ == "__main__":
    main()
