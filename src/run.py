import argparse,json
from .system import run_system
EXAMPLE={"schema":"orders_v2","owner":"data platform","sla":"daily by 06:00 UTC","sources":["transactions"],"lineage":["transactions -> orders_clean -> analytics"],"consumers":["finance analytics"],"quality_checks":["not-null","uniqueness"],"quality_failures":[],"transformations":["normalize currency"],"transformation_tests":["fixture passed"],"schedule":"daily","retry":"3 attempts","recovery":"replay from checkpoint"}
def main():
 p=argparse.ArgumentParser();p.add_argument("--example",action="store_true");p.add_argument("--approve",action="store_true");a=p.parse_args();print(json.dumps(run_system(EXAMPLE if a.example else {},a.approve),indent=2))
if __name__=="__main__":main()
