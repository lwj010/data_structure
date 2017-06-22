#2013120311 이우진
import rb_tree as rb

rbt = rb.RB_tree()



with open('/Users/WooJin/OneDrive/3-1/3-1_data_structure/data_structure/prjtest/test01.txt') as testfile:
    for line in testfile:
        x = int(line)
        if x > 0:
            rbt.rb_insert(rb.Node(x))
        elif x < 0:
            s = rbt.bt_search(rbt.root, abs(x))
            if s == -1:
                s
            else:
                rbt.rb_delete(s)
        else:
            break

testfile.close()

inputfile = open('/Users/WooJin/OneDrive/3-1/3-1_data_structure/data_structure/prjtest/search01.txt', 'r')
outputfile = open('/Users/WooJin/OneDrive/3-1/3-1_data_structure/data_structure/prjtest/output01.txt', 'w')

for line in inputfile:
    x = int(line)
    rbt.hw6(x, outputfile)

outputfile.close()
inputfile.close()
