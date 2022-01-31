from brownie import CellarPoolShare, accounts

def main():
    acct = accounts.load("deployer_account")
    name = "Plenti WETH USDT 0.05 Vault"
    symbol = "PLENTIWETHUSDT05"
    token0 = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
    token1 = "0xdac17f958d2ee523a2206206994597c13d831ec7"
    gravity_bridge = "0x69592e6f9d21989a043646fE8225da2600e5A0f7"
    cellarTickInfo = [[0, -195000, -201360, 1]]
    CellarPoolShareContract = CellarPoolShare.deploy(name, symbol, token0, token1, 500, cellarTickInfo, {"from":acct})
    CellarPoolShareContract.setAdjuster(gravity_bridge, True, {"from": acct})
    CellarPoolShareContract.setValidator(gravity_bridge, True, {"from": acct})