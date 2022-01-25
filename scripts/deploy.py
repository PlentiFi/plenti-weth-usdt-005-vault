from brownie import CellarPoolShare, accounts

def main():
    acct = accounts.load("deployer_account")
    name = "Plenti WETH USDT 0.05 Vault"
    symbol = "PLENTIWETHUSDT05"
    token0 = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
    token1 = "0xdac17f958d2ee523a2206206994597c13d831ec7"
    cellarTickInfo = [[0, -192520, -199360, 1]]
    CellarPoolShare.deploy(name, symbol, token0, token1, 500, cellarTickInfo, {"from":acct})