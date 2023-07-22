class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
        # A altura do nó é inicializada como 1, pois é a altura mínima de um nó recém-inserido.


class AVLTree:
    def __init__(self):
        self.root = None
        # Inicializa a árvore AVL com a raiz sendo None.

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None or node.value == value:
            return node
        # Se o nó atual é None ou o valor do nó é igual ao valor procurado, retorna o nó atual.

        if value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)
        # Se o valor procurado é menor que o valor do nó atual, realiza a busca na subárvore esquerda.
        # Caso contrário, realiza a busca na subárvore direita.

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return AVLNode(value)
        # Se o nó atual é None, cria um novo nó AVL com o valor fornecido.

        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)
        # Se o valor é menor que o valor do nó atual, insere o valor na subárvore esquerda.
        # Caso contrário, insere o valor na subárvore direita.

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        # Atualiza a altura do nó atual, levando em consideração as alturas das subárvores esquerda e direita.

        balance_factor = self._get_balance_factor(node)
        # Calcula o fator de balanceamento do nó atual.

        if balance_factor > 1:
            if value < node.left.value:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
        # Se o fator de balanceamento é maior que 1, significa que a subárvore esquerda está mais alta,
        # e é necessário realizar rotações para balancear a árvore.
        # Verifica se a inserção ocorreu na subárvore esquerda da subárvore esquerda (caso esquerda-esquerda)
        # ou na subárvore direita da subárvore esquerda (caso esquerda-direita).

        if balance_factor < -1:
            if value > node.right.value:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)
        # Se o fator de balanceamento é menor que -1, significa que a subárvore direita está mais alta,
        # e é necessário realizar rotações para balancear a árvore.
        # Verifica se a inserção ocorreu na subárvore direita da subárvore direita (caso direita-direita)
        # ou na subárvore esquerda da subárvore direita (caso direita-esquerda).

        return node

    def remove(self, value):
        self.root = self._remove(self.root, value)

    def _remove(self, node, value):
        if node is None:
            return node
        # Se o nó atual é None, retorna o nó atual.

        if value < node.value:
            node.left = self._remove(node.left, value)
        elif value > node.value:
            node.right = self._remove(node.right, value)
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self._find_min_value_node(node.right)
                node.value = successor.value
                node.right = self._remove(node.right, successor.value)
        # Se o valor é menor que o valor do nó atual, remove o valor na subárvore esquerda.
        # Se o valor é maior que o valor do nó atual, remove o valor na subárvore direita.
        # Caso contrário, o valor foi encontrado e é necessário realizar a remoção.

        if node is None:
            return node
        # Se o nó atual é None, retorna o nó atual.

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        # Atualiza a altura do nó atual, levando em consideração as alturas das subárvores esquerda e direita.

        balance_factor = self._get_balance_factor(node)
        # Calcula o fator de balanceamento do nó atual.

        if balance_factor > 1:
            if self._get_balance_factor(node.left) >= 0:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
        # Se o fator de balanceamento é maior que 1, significa que a subárvore esquerda está mais alta,
        # e é necessário realizar rotações para balancear a árvore.
        # Verifica se o fator de balanceamento da subárvore esquerda é maior ou igual a 0
        # (caso esquerda-esquerda) ou menor que 0 (caso esquerda-direita).

        if balance_factor < -1:
            if self._get_balance_factor(node.right) <= 0:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)
        # Se o fator de balanceamento é menor que -1, significa que a subárvore direita está mais alta,
        # e é necessário realizar rotações para balancear a árvore.
        # Verifica se o fator de balanceamento da subárvore direita é menor ou igual a 0
        # (caso direita-direita) ou maior que 0 (caso direita-esquerda).

        return node

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _get_height(self, node):
        if node is None:
            return 0
        return node.height
        # Retorna a altura do nó. Se o nó é None, retorna 0.

    def _get_balance_factor(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
        # Calcula o fator de balanceamento do nó.
        # Se o nó é None, retorna 0.
        # O fator de balanceamento é a diferença entre a altura da subárvore esquerda e a altura da subárvore direita.

    def _find_min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
        # Encontra e retorna o nó com o menor valor na subárvore com raiz no nó fornecido.

    def print_tree(self):
        self._print_tree(self.root)

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left)
            print(node.value)
            self._print_tree(node.right)
        # Imprime os valores da árvore em ordem.


tree = AVLTree()

tree.insert(6)
tree.insert(7)
tree.insert(8)
tree.insert(9)
tree.insert(10)
tree.insert(5)
tree.insert(4)
tree.insert(3)
tree.insert(2)


print("Árvore AVL em ordem simétrica:")
tree.print_tree()