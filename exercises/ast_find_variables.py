"""
Simple example how to use Abstract Syntax Tree
doc: https://docs.python.org/3/library/ast.html

"""
import ast
import builtins


def find_variable_assignments(source, target_var_names):
    tree = ast.parse(source)
    # print(ast.dump(tree))
    lookingfor = lambda item: item in target_var_names
    variables_assigned = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            tuple_itens = []
            name_itens = []
            targets = []

            for x in node.targets:
                if isinstance(x, ast.Tuple):
                    tuple_itens = [i.id for i in x.elts]

                if isinstance(x, ast.Name):
                    name_itens.append(x.id)

            targets.extend(tuple_itens)
            targets.extend(name_itens)

            for i in filter(lookingfor, targets):
                variables_assigned.append(i)

        elif isinstance(node, ast.ClassDef):
            variables_assigned.append(node.name)

        elif isinstance(node, ast.FunctionDef):
            variables_assigned.append(node.name)
            for arg in node.args.args:
                if arg.arg not in ["self", "baz"]:
                    arg_name = arg.arg.replace("foo", "next")
                    variables_assigned.append(arg_name)

    return list(set(variables_assigned))


if __name__ == "__main__":
    code = """
    def fn():
        str = 42
        x = 1
        next, b = 1, 2
        print(str, a, b)
    """
    results = []
    targets = dir(builtins)
    expected = ["next", "str"]
    print(len(find_variable_assignments(code, targets)) == len(expected))

    print(expected)
    print(find_variable_assignments(code, targets))

    code = """
    def list(str, foo, iter): 
        def bin(set): 
            dict = 42 
            foo = zip
            bar = 0
        return str[::-1]
    """

    targets = dir(builtins)
    expected = ["str", "list", "iter", "bin", "set", "dict"]

    print(len(find_variable_assignments(code, targets)) == len(expected))

    print(expected)
    print(find_variable_assignments(code, targets))
