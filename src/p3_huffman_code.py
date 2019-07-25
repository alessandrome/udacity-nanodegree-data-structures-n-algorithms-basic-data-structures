import sys
import queue
from collections import defaultdict


class HuffmanNode:
    def __init__(self, char=None, frequency=0, bin_code=''):
        self.char = char
        self.frequency = frequency
        self.bin_code = bin_code
        self.left = None
        self.right = None

    def __str__(self, level=0):
        ret = "\t" * level + repr(self) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1)
        if self.right:
            ret += self.right.__str__(level + 1)
        return ret

    def __repr__(self):
        return '{{{}, {}, {}}}'.format(('\'' + self.char + '\'') if self.char else 'None', self.frequency,
                                       self.bin_code)

    def get_char_codes(self):
        return self._get_char_codes({}, '')

    def _get_char_codes(self, codes_dict, code):
        if not (self.left or self.right):
            codes_dict[self.char] = code + self.bin_code
            return codes_dict
        if self.left:
            codes_dict.update(self.left._get_char_codes(codes_dict, code + self.bin_code))
        if self.right:
            codes_dict.update(self.right._get_char_codes(codes_dict, code + self.bin_code))
        return codes_dict


def get_ordered_frequencies(string):
    frequencies = defaultdict(int)
    for char in string:
        frequencies[char] += 1
    frequencies = sorted(list(frequencies.items()), key=lambda k: k[1], reverse=True)
    # print(frequencies)
    return frequencies


def huffman_encoding(data):
    frequencies = get_ordered_frequencies(data)
    if len(frequencies) == 0:
        return '', None
    for index in range(len(frequencies)):
        frequencies[index] = HuffmanNode(frequencies[index][0], frequencies[index][1], '0')
    # Build tree
    while len(frequencies) > 1:
        left, right = frequencies.pop(), frequencies.pop()
        left.bin_code = '0'
        right.bin_code = '1'
        new_root = HuffmanNode(frequency=(left.frequency + right.frequency))
        new_root.left, new_root.right = left, right
        frequencies.append(new_root)
        frequencies.sort(key=lambda node: node.frequency, reverse=True)
    huffman_tree = frequencies[0]
    huffman_encoding_table = huffman_tree.get_char_codes()
    # Encode data
    encoded_data = ''
    for char in data:
        encoded_data += huffman_encoding_table[char]
    return encoded_data, huffman_tree


def huffman_decoding(data, huffman_tree):
    # Invert the huffman encoding table to get character given a binary code string of encoded text
    if not data:
        return data
    inverted_huffman_encoding_table = {v: k for k, v in huffman_tree.get_char_codes().items()}
    replaced_char_list = []
    char_sequence = ''
    for bin_char in data:
        char_sequence += bin_char
        if char_sequence in inverted_huffman_encoding_table:
            replaced_char_list.append(inverted_huffman_encoding_table[char_sequence])
            char_sequence = ''
    return ''.join(replaced_char_list)


if __name__ == "__main__":
    codes = {}

    # Normal sentence test
    a_great_sentence = "The bird is the word"

    print("## GREAT SENTENCE ##")
    print("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))


    # Single letter test
    a_little_sentence = "!"

    print("\n## LITTLE SENTENCE ##")
    print("The size of the data is: {}".format(sys.getsizeof(a_little_sentence)))
    print("The content of the data is: {}\n".format(a_little_sentence))

    encoded_data, tree = huffman_encoding(a_little_sentence)

    print("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))


    # Repeated letter test
    a_repeated_sentence = "S" * 10

    print("\n## REPEATED SENTENCE ##")
    print("The size of the data is: {}".format(sys.getsizeof(a_repeated_sentence)))
    print("The content of the data is: {}\n".format(a_repeated_sentence))

    encoded_data, tree = huffman_encoding(a_repeated_sentence)

    print("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))


    # Empty data test
    a_little_sentence = ""

    print("\n## EMPTY SENTENCE ##")
    print("The content of the data is: {}\n".format(a_little_sentence))

    encoded_data, tree = huffman_encoding(a_little_sentence)

    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The content of the decoded data is: {}\n".format(decoded_data))
