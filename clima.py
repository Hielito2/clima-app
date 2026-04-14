import argparse
from src.main import main

parser = argparse.ArgumentParser(prog='Clima', description="Ver el clima de tu ciudad")

parser.add_argument("city", type=str, help="The city code")

args = parser.parse_args()

main(city=args.city)
