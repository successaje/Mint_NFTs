import smartpy as sp
FA2 = sp.io.import_script_from_url("https://smartpy.io/templates/fa2_lib.py")

class ExampleFa2Nft(FA2.Fa2Nft):
    pass

class ExampleFa2Fungible(FA2.Fa2Fungible):
    pass


class FA2_core(sp.Contract):
    def __init__(self):
        pass


