from antlr4 import *
from antlr4.tree.Tree import TerminalNodeImpl
import antlr_ast.ast as ast

from languages_grammars.java.java9 import Java9Lexer, Java9Listener, Java9Parser, Java9Visitor

j_lexer = Java9Lexer.Java9Lexer
j_listener = Java9Listener.Java9Listener
j_parser = Java9Parser.Java9Parser
j_visitor = Java9Visitor.Java9Visitor


def traverse(tree, rule_names, indent=0):
    if tree.getText() == "<EOF>":
        return
    elif isinstance(tree, TerminalNodeImpl):
        print("{0}TOKEN='{1}'".format("  " * indent, tree.getText()))
    else:
        print("{0}{1}".format("  " * indent, rule_names[tree.getRuleIndex()]))
        for child in tree.children:
            traverse(child, rule_names, indent + 1)


if __name__ == '__main__':
    # main()

    code = open(
        '/home/dmitry/PycharmProjects/py3antlr4book/from_another_project/grammars/java/java9/examples/helloworld.java',
        'r').read()
    codeStream = InputStream(code)
    lexer = j_lexer(codeStream)

    tokensStream = CommonTokenStream(lexer)
    parser = j_parser(tokensStream)

    # tokens = lexer.getAllTokens()
    # tokensSource = ListTokenSource(tokens)
    # tokensStream = CommonTokenStream(tokensSource)
    # parser = j_parser(tokensStream)

    tree = parser.compilationUnit()

    # print(tree.toStringTree(recog=parser))
    traverse(tree, parser.ruleNames)

    derevo = j_visitor().visit(tree)
    print(derevo)
