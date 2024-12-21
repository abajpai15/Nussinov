from nussinov import *
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("sequence", type=str, help="RNA sequence (e.g., GCAUCGG)")

    args = parser.parse_args()
    sequence = args.sequence.strip().upper()
    valid_bases = {'A', 'U', 'C', 'G'}
    for c in sequence:
        if c not in valid_bases:
            print("The provided sequence uses characters not in RNA! Please only use G, C, U, and A.")
            return

    max_base_pairs, structure = nussinov(sequence)

    print("\nResults:")
    print(f"RNA Sequence: {sequence}")
    print(f"Maximum Base Pairs: {max_base_pairs}")
    print(f"Secondary Structure: {structure}")

if __name__ == "__main__":
    main()