from Set_AVL_Tree import BST_Node, Set_AVL_Tree
#######################################
# DO NOT REMOVE THIS IMPORT STATEMENT #
# DO NOT MODIFY IMPORTED CODE         #
#######################################

class Key_Val_Item:
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __str__(self):
        return "%s,%s" % (self.key, self.val)

class Part_B_Node(BST_Node):
    def subtree_update(A):
        super().subtree_update()
        #########################################
        left_sum = A.left.sum if A.left else 0
        left_max = A.left.max_left_prefix if A.left else float('-inf')

        right_sum = A.right.sum if A.right else 0
        right_max = A.right.max_left_prefix if A.right else float('-inf')

        A.sum = left_sum + A.item.val + right_sum

        zone_1 = left_max
        zone_2 = left_sum + A.item.val
        zone_3 = left_sum + A.item.val + right_max

        A.max_left_prefix = max(zone_1, zone_2, zone_3)
        #########################################

class Part_B_Tree(Set_AVL_Tree):
    def __init__(self):
        super().__init__(Part_B_Node)

    def max_prefix(self):
        '''
        Output: (k, s) | a key k stored in tree whose
                       | prefix sum s is maximum
        '''
        k, s = 0, 0
        ##################
        if self.root is None:
            return (None, 0)

        s = self.root.max_left_prefix
        curr = self.root
        target_val = s

        while curr:
            left_sum = curr.left.sum if curr.left else 0
            left_max = curr.left.max_left_prefix if curr.left else float('-inf')

            if curr.left and target_val == left_max:
                curr = curr.left
            elif target_val == left_sum + curr.item.val:
                k = curr.item.key
                break
            else:
                target_val -= (left_sum + curr.item.val)
                curr = curr.right
        ##################
        return (k, s)

def tastiest_slice(toppings):
    '''
    Input:  toppings | List of integer tuples (x,y,t) representing
                     | a topping at (x,y) with tastiness t
    Output: tastiest | Tuple (X,Y,T) representing a tastiest slice
                     | at (X,Y) with tastiness T
    '''
    B = Part_B_Tree()   # use data structure from part (b)
    X, Y, T = 0, 0, 0
    ##################
    if not toppings:
        return (0, 0, 0)

    T = float('-inf')
    y_groups = {}
    for x, y, t in toppings:
        y_groups.setdefault(y, []).append((x, t))

    for current_y in sorted(y_groups.keys()):
        for x, t in y_groups[current_y]:
            existing = B.find(x)
            if existing is not None:
                B.delete(x)
                B.insert(Key_Val_Item(x, existing.val + t))
            else:
                B.insert(Key_Val_Item(x, t))

        best_x_for_y, max_t_for_y = B.max_prefix()
        if max_t_for_y > T:
            T = max_t_for_y
            X = best_x_for_y
            Y = current_y
    ##################
    return (X, Y, T)
