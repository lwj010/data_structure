


class Node():

    def __init__(self, newval):
        self.key = newval
        self.parent = None
        self.left = None
        self.right = None
        self.color = "black"


class RB_tree():

	def __init__(self):
		nil = Node("Nil")
		self.root = nil
		self.nil = nil

	def tree_min(self, tree):
		while tree.left != self.nil:
			tree = tree.left
		return tree

	def tree_max(self, tree):
		while tree.right != self.nil:
			tree = tree.right
		return tree

	def rb_insert(self, z):
	    y = self.nil
	    x = self.root
	    while x != self.nil:
	        y = x
	        if z.key < x.key:
	            x = x.left
	        else:
	            x = x.right
	    z.parent = y

	    if y == self.nil:
	        self.root = z

	    elif z.key < y.key:
	        y.left = z
	    else:
	        y.right = z

	    z.left = self.nil
	    z.right = self.nil
	    z.color = "red"
	    self.insert_fixup(z)

	def insert_fixup(self, z):
	    while z.parent.color == "red":
	        if z.parent == z.parent.parent.left:
	            y = z.parent.parent.right
	            if y.color == "red":
	                z.parent.color = "black"
	                y.color = "black"
	                z.parent.parent.color = "red"
	                z = z.parent.parent
	            else:
	                if z == z.parent.right:
	                    z = z.parent
	                    self.left_rotate(z)
	                z.parent.color = "black"
	                z.parent.parent.color = "red"
	                self.right_rotate(z.parent.parent)
	        else:
	            y = z.parent.parent.left
	            if y.color == "red":
	                z.parent.color = "black"
	                y.color = "black"
	                z.parent.parent.color = "red"
	                z = z.parent.parent
	            else:
	                if z == z.parent.left:
	                    z = z.parent
	                    self.right_rotate(z)
	                z.parent.color = "black"
	                z.parent.parent.color = "red"
	                self.left_rotate(z.parent.parent)
	    self.root.color = "black"

	def bt_print(self, tree, level):
	    if tree.right.key != None:
	        self.bt_print(tree.right, level + 1)
	    for i in range(level):
	        print("   ", end="")
	    print(tree.key, end="")
	    print(tree.color)
	    if tree.left.key != None:
	        self.bt_print(tree.left, level + 1)

	def inorder_iter(self, tree):
	    stk = []
	    while len(stk) != 0 or tree != self.nil:
	        if tree != self.nil:
	            stk.append(tree)
	            tree = tree.left
	        else:
	            tree = stk.pop()
	            print(tree.key, end=" ")
	            print(tree.color)
	            tree = tree.right

	def left_rotate(self, x):
	    y = x.right
	    x.right = y.left
	    if y.left != self.nil:
	        y.left.parent = x
	    y.parent = x.parent
	    if x.parent == self.nil:
	        self.root = y
	    elif x.parent.left == x:
	        x.parent.left = y
	    else:
	        x.parent.right = y
	    y.left = x
	    x.parent = y

	def right_rotate(self, x):
	    y = x.left
	    x.left = y.right
	    if y.right != self.nil:
	        y.right.parent = x
	    y.parent = x.parent
	    if x.parent == self.nil:
	        self.root = y
	    elif x.parent.left == x:
	        x.parent.left = y
	    else:
	        x.parent.right = y
	    y.right = x
	    x.parent = y

	def rb_transplant(self, u, v):
	    if u.parent == self.nil:
	        self.root = v
	    elif u.parent.left == u:
	        u.parent.left = v
	    else:
	        u.parent.right = v
	    v.parent = u.parent

	def rb_delete(self, z):
	    y = z
	    yoc = y.color
	    if z.left == self.nil:
	        x = z.right
	        self.rb_transplant(z, z.right)
	    elif z.right == self.nil:
	        x = z.left
	        self.rb_transplant(z, z.left)
	    else:
	        y = self.tree_min(z.right)
	        yoc = y.color
	        x = y.right
	        if y.parent == z:
	            x.parent = y
	        else:
	            self.rb_transplant(y, y.right)
	            y.right = z.right
	            y.right.parent = y
	        self.rb_transplant(z, y)
	        y.left = z.left
			y.left.parent = y
			y.color = z.color
		if yoc == "black":
			self.delete_fixup(x)

	def delete_fixup(self, x):
	    while x != self.root and x.color == "black":
	        if x == x.parent.left:
	            w = x.parent.right
	            if w.color == "red":
	                w.color = "black"
	                x.parent.color = "red"
	                self.left_rotate(x.parent)
	                w = x.parent.right
	            if w.left.color == "black" and w.right.color == "black":
	                w.color = "red"
	                x = x.parent
	            else:
	                if w.right.color == "black":
	                    w.left.color = "black"
	                    w.color = "red"
	                    self.right_rotate(w)
	                    w = x.parent.right
	                w.color = x.parent.color
	                x.parent.color = "black"
	                w.right.color = "black"
	                self.left_rotate(x.parent)
	                x = self.root
	        else:
	            w = x.parent.left
	            if w.color == "red":
	                w.color = "black"
	                x.parent.color = "red"
	                self.right_rotate(x.parent)
	                w = x.parent.left
	            if w.right.color == "black" and w.left.color == "black":
	                w.color = "red"
	                x = x.parent
	            else:
	                if w.left.color == "black":
	                    w.right.color = "black"
	                    w.color = "red"
	                    self.left_rotate(w)
	                    w = x.parent.left
	                w.color = x.parent.color
	                x.parent.color = "black"
	                w.left.color = "black"
	                self.right_rotate(x.parent)
	                x = self.root
	    x.color = "black"

	def bt_search(self, tree, x):
	    if tree != self.nil:
	        if x < tree.key:
	            return self.bt_search(tree.left, x)
			elif x > tree.key:
	            return self.bt_search(tree.right, x)
			else:
	            return tree
		else:
			return -1


	def hw6(self, node, outputfile):
		if node == 0:
			return -1
		tree = self.root
		x = self.nil
		while tree != self.nil and tree.key != node:
		if node < tree.key:
		    x = tree
		    tree = tree.left
		else:
		    x = tree
		    tree = tree.right
		if tree != self.nil:
		print(self.b_pre(tree).key, end=" ", file=outputfile)
		print(tree.key, end=" ", file=outputfile)
		print(self.b_succ(tree).key, file=outputfile)
		elif node < x.key:
		print(self.l_pre(x).key, end=" ", file=outputfile)
		print("Nil", end=" ", file=outputfile)
		print(x.key, file=outputfile)
		else:
		print(x.key, end=" ", file=outputfile)
		print("Nil", end=" ", file=outputfile)
		print(self.b_succ(x).key, file=outputfile)

	def b_pre(self, x):
	    if x.left != self.nil:
	        return self.tree_max(x.left)
	    y = x.parent
	    while y and x == y.left:
	        x = y
	        y = y.parent
	    return y

	def b_succ(self, x):
	    if x.right != self.nil:
	        return self.tree_min(x.right)
	    y = x.parent
	    while y and x == y.right:
	        x = y
	        y = y.parent
	    return y

	def l_pre(self, x):
	    if x == x.parent.right:
	        return x.parent
	    else:
	        y = x.parent
	        while y and x == y.left:
	            x = y
	            y = y.parent
	        return y

	def l_succ(self, x):
	    if x == x.parent.left:
	        return x.parent
	    else:
	        y = x.parent
	        while y and x == y.right:
	            x = y
	            y = y.parent
	        return y




