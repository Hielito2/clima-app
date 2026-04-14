import argparse
from src.main import main
import time

parser = argparse.ArgumentParser(prog='Clima', description="Ver el clima de tu ciudad")

parser.add_argument("city", type=str, help="The city code")
parser.add_argument("-d", metavar="days", type=int, default=5, help="The days to see the weather (max=5)")

args = parser.parse_args()

main(city=args.city, days=args.d)
