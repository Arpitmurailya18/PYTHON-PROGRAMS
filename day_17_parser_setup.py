import tree_sitter_cpp as tscpp
from tree_sitter import Language, Parser

# 1. Load the C++ Grammar
CPP_LANGUAGE = Language(tscpp.language())

# 2. Create the Parser
parser = Parser()

parser.language = CPP_LANGUAGE

code = b"""
#include<iostream>
using namespace std;
int main(int x = 10){return 0;}"""

tree = parser.parse(code)

print(tree.root_node)
    