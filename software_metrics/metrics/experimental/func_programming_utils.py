import ast
import networkx as nx

def is_higher_order(node):
    for arg in node.args.args + node.args.kwonlyargs:
        if isinstance(arg.annotation, ast.Name) and arg.annotation.id == 'Callable':
            return True
    if isinstance(node.returns, ast.Name) and node.returns.id == 'Callable':
        return True
    return False

def get_function_calls(node):
    calls = []
    for child in ast.iter_child_nodes(node):
        if isinstance(child, ast.Call) and isinstance(child.func, ast.Name):
            calls.append(child.func.id)
        calls.extend(get_function_calls(child))
    return calls

def analyze_ast(tree):
    higher_order_functions = 0
    function_graph = nx.DiGraph()
    
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, ast.FunctionDef):
            function_name = node.name
            
            if is_higher_order(node):
                higher_order_functions += 1
            
            calls = get_function_calls(node)
            
            for call in calls:
                function_graph.add_edge(function_name, call)
    
    return higher_order_functions, function_graph

def calculate_function_degrees(function_graph):
    function_degrees = {}
    for func in function_graph.nodes():
        in_degree = function_graph.in_degree(func)
        out_degree = function_graph.out_degree(func)
        function_degrees[func] = (in_degree, out_degree)
    return function_degrees

def print_results(higher_order_functions, function_degrees, function_graph):
    print(f"Number of higher-order functions: {higher_order_functions}")
    print("\nFunction degrees (in-degree, out-degree):")
    for func, degree in function_degrees.items():
        print(f"{func}: {degree}")
    
    print("\nFunction relationship diagram:")
    for func in function_graph.nodes():
        print(f"{func}")
        for called_func in function_graph.successors(func):
            print(f"  └─> {called_func}")

def analyze_python_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    tree = ast.parse(content)
    
    higher_order_functions, function_graph = analyze_ast(tree)
    function_degrees = calculate_function_degrees(function_graph)
    print_results(higher_order_functions, function_degrees, function_graph)

