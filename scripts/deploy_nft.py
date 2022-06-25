from scripts.helpful_scripts import get_account
from brownie import ShapeNft


sample_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"


def main():
    account = get_account()
    shape_nft = ShapeNft.deploy({"from": account})
    tx = shape_nft.createShapeNft(sample_token_uri, {"from": account})
    tx.wait(1)
