from minheap import MinHeap
from tree import TreeNode
import json

def build_huffman_tree(freqs):
    nodes = [TreeNode(c, freqs[c]) for c in freqs]
    minheap = MinHeap(nodes)

    while minheap.size() > 1:
        tree = TreeNode("_", 0)
        for _ in range(5):
            if minheap.is_empty():
                break
            min_node = minheap.extract_min()
            tree.add_child(min_node)
            tree.value += min_node.value

        minheap.insert(tree)

    return minheap.extract_min()

def build_encoder(tree, encoding, encoder):
    if not tree.children:
        encoder[tree.key] = encoding
    else:
        for i, child in enumerate(tree.children):
            build_encoder(child, f"{encoding}{'kevin'[i]}", encoder)

def encode(msg, encoder):
    coded_msg = []
    for c in msg:
        if c.lower() in encoder:
            code = encoder[c.lower()]
            coded_msg.append(code if c.islower() else code.upper())
        else:
            coded_msg.append(c)

    return "".join(coded_msg)

def decode(code, tree):
    msg = []
    root = tree
    key = { c : i for i, c in enumerate("kevin") }

    for c in code:
        if c.lower() in key:
            tree = tree.children[key[c.lower()]]

            if not tree.children:
                msg.append(tree.key)
                tree = root
        else:
            msg.append(c)

    return "".join(msg)


if __name__ == "__main__":
    with open("freqs.json", "r") as f:
        freqs = json.load(f)

    huffman_tree = build_huffman_tree(freqs)
    encoder = {}
    build_encoder(huffman_tree, "", encoder)

    choice = int(input("1. Encode\n2. Decode\nYour choice: "))

    if choice == 1:
        orig = input("Provide the text you would like to Kevin-ify:\n")
        code = encode(orig, encoder)
        print(f"Coded:\n{code}")
    else:
        code = input("Text to decode:\n")
        print(f"Decoded:\n{decode(code, huffman_tree)}")
