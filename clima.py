import argparse
from src.main import main


parser = argparse.ArgumentParser(prog='Clima', description="Ver el clima de tu ciudad")

parser.add_argument("city_code", type=int, help="The city code")
parser.add_argument("-d", metavar="days", type=int, default=2, help="The days to see the weather (0-5)")
parser.add_argument("-v", action='store', dest='param', const=True, nargs='?',help="Show extra info") #  https://stackoverflow.com/a/50871450

args = parser.parse_args()

if args.param == None:
    args.param = False

main(city=args.city_code, days=args.d, verbose=args.param)
