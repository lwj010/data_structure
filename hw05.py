# 2013120311 이우진
import os


class Node:

    def __init__(self, newval): 
        self.key = newval
        self.left = None
        self.right = None
        self.parent = None
        self.color = "black"


class rb_tree:

	def __init__(self):
		self.nil = Node(None)
		self.root = self.nil


	def left_rotate(self, x):
		y = x.right
		x.right = y.left
		if y.left != self.nil:
			y.left.parent = x	
		y.parent = x.parent
		if x.parent == self.nil:
			self.root = y
		elif x == x.parent.left :
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
		elif x == x.parent.left:
			x.parent.left = y
		else:
			x.parent.right = y
		y.right = x
		x.parent = y


	def rb_insert(self, z):
		y = self.nil
		x = self.root
		while x is not self.nil:
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
		self.rb_insert_fixup(z)


	def rb_insert_fixup(self, z):
		while z.parent.color == "red":
			if z.parent == z.parent.parent.left:
				y = z.parent.parent.right
				if y.color == "red":
					z.parent.color = "black"
					y.color = "black"
					z.parent.parent.color = "red"
					z = z.parent.parent
				elif z == z.parent.right:
					z = z.parent
					self.left_rotate(z)
				else:
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
				elif z == z.parent.left:
					z = z.parent
					self.right_rotate(z)
				else:
					z.parent.color = "black"
					z.parent.parent.color = "red"
					self.left_rotate(z.parent.parent)
		self.root.color = "black"

	def rb_min(self, tree):
		while tree.left.key != None:  
			tree = tree.left
		return tree

	def rb_max(self, tree):
		while tree.right.key != None:
			tree = tree.right
		return tree


	def rb_transplant(self, u, v):
		if u.parent == self.nil:
			self.root = v
		elif u == u.parent.left:
			u.parent.left = v
		else:
			u.parent.right = v
		v.parent = u.parent


	def rb_delete(self, z):
		y = z
		y_original_color = y.color
		if z.left == self.nil:
			x = z.right
			self.rb_transplant(z, z.right)
		elif z.right == self.nil:
			x = z.left
			self.rb_transplant(z, z.left)
		else:
			y = self.rb_min(z.right) 
			y_original_color = y.color
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
		if y_original_color == "black":
			self.rb_delete_fixup(x)

	def rb_delete_fixup(self, x):
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
						w.right.color == "black"
						w.color = "red"
						self.left_rotate(w)
						w = x.parent.left		
					w.color = x.parent.color
					x.parent.color = "black"
					w.left.color = "black"
					self.right_rotate(x.parent)
					x = self.root
		x.color = "black"



	def search(self, tree, k):
		if tree.key == None or k == tree.key:
			return tree
		if k < tree.key:
			return self.search(tree.left, k)
		else:
			return self.search(tree.right, k)

  	#inorder_result에 inorder traversal 결과 저장 / blacknode에 black nodes들 저장
	inorder_result = [ ]
	blacknode = [ ]

	def inorder(self,tree):
		if tree is None:
			return
		else:
			self.inorder(tree.left)
			if tree.color is "black":
				rb_tree.blacknode.append(tree.key)
			rb_tree.inorder_result.append((tree.key,tree.color))
			self.inorder(tree.right)
		

	def print(self,tree,level):
	    if tree.right is not None:
	        self.print(tree.right,level + 1)
	    for i in range(level):
	        print('   	', end='')
	    print((tree.key, tree.color))
	    if tree.left is not None:
	        self.print(tree.left, level + 1)

	def rb_bh(self):
		x = self.root
		bh = 0
		while x is not self.nil:
			if x.color is "black":
				bh = bh + 1
			x = x.right
		return bh



# input.txt read
f = open("test02.txt", 'r')
lines = f.readlines()

tree_ = rb_tree()
cannot_del = [ ]
deleted = [ ]
inserted = [ ]

# >0 일때는 바로 insert, <0 일때는 확인후 있으면 delete, 
# 0이면 inorder traversal후 저장된 결과 length 프린트
for i in range(0,len(lines)):
	x = int(lines[i])
	if x > 0:
		tree_.rb_insert(Node(x))
		inserted.append(Node(x).key)
	elif x < 0:
		searched = tree_.search(tree_.root, abs(x))
		if searched.key == None:
			cannot_del.append("%d is not in the tree" %x)
		else:
			tree_.rb_delete(searched)
			deleted.append(searched)
	else:
		# print input filename
		filenames = os.listdir()
		for filename in filenames:
			if filename == f.name:
				print("filename = %s" %filename)

		tree_.inorder(tree_.root)
		total = tree_.inorder_result
		
		# None 제거
		total_withoutleaf = [ ]
		for i in total:
		 	if i[0] is not None:
		 		total_withoutleaf.append(i)



		blacknodes = tree_.blacknode

		# None 제거
		blacknodes_withoutleaf = [ ]
		for i in blacknodes:
			if i is not None:
				blacknodes_withoutleaf.append(i)

		print("total = %d" %len(total_withoutleaf))
		print("insert = %d" %len(inserted))
		print("deleted = %d" %len(deleted))
		print("miss = %d" %len(cannot_del))
		print("nb = %d" %len(blacknodes_withoutleaf))
		print("bh = %d" %tree_.rb_bh())

		# to print '1 R' form
		total_col = [ ]
		total_num = [ ]

		for i in total_withoutleaf:
			total_num.append(i[0])
			if i[1] == 'red':
				total_col.append("R")
			else:
				total_col.append("B")

		for i, j in zip(total_num, total_col):
		  	print(i, j)
		

		break



