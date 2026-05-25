import tree_sitter_cpp as tscpp
from tree_sitter import Language, Parser

# 1. Load the C++ Grammar
CPP_LANGUAGE = Language(tscpp.language())

# 2. Create the Parser
parser = Parser()
parser.language = CPP_LANGUAGE

# 3. Read your mocked local file
with open("code1.cpp", "r") as file:
    code = file.read()

# 4. Parse the code into an AST
tree = parser.parse(bytes(code, "utf8"))

# 5. Print the raw tree structure!
print(tree.root_node)