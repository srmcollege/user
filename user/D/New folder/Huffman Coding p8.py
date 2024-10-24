class Node:
    def __init__(self, symbol=None, frequency=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

def build_huffman_tree(chars, freq):
    nodes = [Node(chars[i], freq[i]) for i in range(len(chars))]
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.frequency)
        left = nodes.pop(0)
        right = nodes.pop(0)
        merged = Node(frequency=left.frequency + right.frequency)
        merged.left = left
        merged.right = right
        nodes.append(merged)
    return nodes[0]

def generate_huffman_codes(node, current_code="", codes={}):
    if node is not None:
        if node.symbol is not None:  # Leaf node
            codes[node.symbol] = current_code
        generate_huffman_codes(node.left, current_code + "0", codes)
        generate_huffman_codes(node.right, current_code + "1", codes)
    return codes

chars = ['A', 'B', 'C', 'D']
freq = [5, 1, 3, 3]
root = build_huffman_tree(chars, freq)
huffman_codes = generate_huffman_codes(root)

print(f'{"Character":<10}{"Frequency":<10}{"Code":<10}{"Size":<10}')
print("-" * 42)
total_bits = 0

for char in chars:
    code = huffman_codes[char]
    size = freq[chars.index(char)] * len(code)
    total_bits += size
    print(f"{char:<10} {freq[chars.index(char)]:<10} {code:<10} {freq[chars.index(char)]} * {len(code)} = {size}")

original_bits = len(chars) * 8
print(f"\nOriginal: {len(chars)} * 8 = {original_bits} bits")
print(f"Compressed: {total_bits} bits")
