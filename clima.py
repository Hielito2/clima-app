import argparse
from src.main import initialize


parser = argparse.ArgumentParser(prog='Clima', description="Ver el clima de tu ciudad")

parser.add_argument("city_code", type=str, nargs="?", default='0', help="The city code")
parser.add_argument("-d", dest="days", metavar="days", type=int, default=2, help="The days to see the weather (0-5)")
parser.add_argument("-n", dest="name", metavar="name", type=str, default="0", help="Search the city code by name")
parser.add_argument("-v", action='store', dest='verbose', const=True, nargs='?',help="Show extra info") #  https://stackoverflow.com/a/50871450

args = parser.parse_args()

initialize(city_code=args.city_code, city_name=args.name, days=args.days, verbose=args.verbose)
