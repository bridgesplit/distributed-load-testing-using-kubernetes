from locust import FastHttpUser, task

class BSApis(FastHttpUser):
    @task
    def basic(self):
        self.client.get("/bs_token_list")
        self.client.get("/collection/stats")
        self.client.get("/user/ta/4PvYpgZLarj2dbMEYPuCwaPd7aZ6fvmsZqvDswq4EjUn/So11111111111111111111111111111111111111112")
        self.client.get("/user/ta/4PvYpgZLarj2dbMEYPuCwaPd7aZ6fvmsZqvDswq4EjUn/4v3UTV9jibkhPfHi5amevropw6vFKVWo7BmxwQzwEwq6")
        self.client.get("/user/tokens/4PvYpgZLarj2dbMEYPuCwaPd7aZ6fvmsZqvDswq4EjUn")
        self.client.get("/get_all_magic_eden_prices")
        self.client.get("/magic_eden_stats/4v3UTV9jibkhPfHi5amevropw6vFKVWo7BmxwQzwEwq6")
        self.client.get("/fractional_pools/mint/4v3UTV9jibkhPfHi5amevropw6vFKVWo7BmxwQzwEwq6")
        self.client.get("/single_asset_vaults/mint/AsUbiXVvVv9xAgRVvEfi441QUizgr3MaZVj5sdX11vqY")
        self.client.get("/user/nfts/4PvYpgZLarj2dbMEYPuCwaPd7aZ6fvmsZqvDswq4EjUn")
        self.client.get("/num_staked_in_pool/4PvYpgZLarj2dbMEYPuCwaPd7aZ6fvmsZqvDswq4EjUn/4v3UTV9jibkhPfHi5amevropw6vFKVWo7BmxwQzwEwq6")
        self.client.get("/token/lookup_table/4v3UTV9jibkhPfHi5amevropw6vFKVWo7BmxwQzwEwq6")
        self.client.get("/rarity/4v3UTV9jibkhPfHi5amevropw6vFKVWo7BmxwQzwEwq6")
        self.client.get("/fractional_pools/cached_mint/4v3UTV9jibkhPfHi5amevropw6vFKVWo7BmxwQzwEwq6")