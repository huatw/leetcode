class Solution:
    def evaluate(self, expression):
        def tokenize(s):
            return s.replace('(', ' ( ').replace(')', ' ) ').split()

        def parse(tokens):
            stacks = [[]]
            for token in tokens:
                if token == '(':
                    stacks.append([])
                elif token == ')':
                    substack = stacks.pop()
                    stacks[-1].append(substack)
                elif token.lstrip('-').isdigit():
                    stacks[-1].append(int(token))
                else:
                    stacks[-1].append(token)

            return stacks[-1][-1]

        def find_in_env(var, env):
            k, v, next_env = env
            return v if var == k else find_in_env(var, next_env)

        def evaluate(ast, env):
            if isinstance(ast, int):
                return ast
            if isinstance(ast, str):
                return find_in_env(ast, env)
            op, first, second, *rest = ast
            if op == 'add':
                return evaluate(first, env) + evaluate(second, env)
            if op == 'mult':
                return evaluate(first, env) * evaluate(second, env)
            if op == 'let':
                for i in range(1, len(ast) - 1, 2):
                    env = (ast[i], evaluate(ast[i + 1], env), env)
                return evaluate(ast[-1], env)
        tokens = tokenize(expression)
        ast = parse(tokens)
        res = evaluate(ast, ())

        return res



class Solution:
    def evaluate(self, expression):
        def tokenize(s):
            return s.replace('(', ' ( ').replace(')', ' ) ').split()

        def parse(tokens):
            token = tokens.popleft()
            if token == '(':
                stack = []
                while tokens[0] != ')':
                    stack.append(parse(tokens))
                tokens.popleft()
                return stack
            return int(token) if token.lstrip('-').isdigit() else token

        def find_in_env(name, env):
            k, v, rest_env = env
            return v if name == k else find_in_env(name, rest_env)

        def eval(ast, env):
            if isinstance(ast, int):
                return ast
            if isinstance(ast, str):
                return find_in_env(ast, env)
            if isinstance(ast, list):
                op, first, second, *rest = ast
                if op == 'add':
                    return eval(first, env) + eval(second, env)
                if op == 'mult':
                    return eval(first, env) * eval(second, env)
                if op == 'let':
                    for i in range(2, len(ast), 2):
                        env = (ast[i - 1], eval(ast[i], env), env)
                    return eval(ast[-1], env)

        tokens = tokenize(expression)
        ast = parse(collections.deque(tokens))
        res = eval(ast, ())

        return res
