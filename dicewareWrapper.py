import diceware
import argparse

# Simulate a command-line argument as parsed by diceware
args = argparse.Namespace()
args.num = 4
args.infile = None
args.wordlist = 'en_eff'
args.randomsource = 'system'
args.caps = False
args.delimiter = '-'
args.specials = 0

def getReadableUuid():
    return diceware.get_passphrase(args)