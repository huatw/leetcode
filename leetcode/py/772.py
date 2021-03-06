class Solution:
    def calculate(self, s):
        def tokenize(s):
            tokens = []
            token = ''
            for ch in s:
                if ch == ' ':
                    continue
                elif ch in '+-()*/':
                    if token:
                        tokens.append(token)
                        token = ''
                    tokens.append(ch)
                else:
                    token += ch
            if token:
                tokens.append(token)
            return tokens

        def parse(tokens):
            stacks = [[]]
            for token in tokens:
                if token == '(':
                    stacks.append([])
                elif token == ')':
                    substack = stacks.pop()
                    stacks[-1].append(substack)
                else:
                    stacks[-1].append(token)
                if len(stacks[-1]) > 2 and (stacks[-1][-2] == '/' or stacks[-1][-2] == '*'):
                    right = stacks[-1].pop()
                    op = stacks[-1].pop()
                    left = stacks[-1].pop()
                    stacks[-1].append([left, op, right])

            return stacks[-1]

        def get_val(var):
            return evaluate(var) if isinstance(var, list) else int(var)

        def evaluate(ast):
            total = get_val(ast[0])
            for i in range(1, len(ast), 2):
                op, val = ast[i], get_val(ast[i + 1])
                if op == '+':
                    total += val
                elif op == '-':
                    total -= val
                elif op == '*':
                    total *= val
                elif op == '/':
                    total //= val
            return total

        tokens = tokenize(s)
        ast = parse(tokens)
        res = evaluate(ast)
        return res
