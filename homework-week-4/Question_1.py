'''
Question 1 of Homework 4 is there to test some of your theory.
If when first looking at questions such as these you stuggle to find
the answer, please make sure you find a reliable online resource, or 
have some suitable and efficient notes on hand should such a question
arise in the assessment.
'''

# 1.1 Give three properties of a tree.
'''
    We discussed this in class, some suitable answers are to mention:
    ● Connected
    ● Undirected
    ● Acyclic
    ● Has a root
    ● Has leaf nodes
'''

# 1.2 What is the meaning of a k-nary tree?
'''
    As we covered in class, and have recapped a few times. The k-nary (or k-ary)
    value of any tree can be determined by the maximum number of child nodes any
    parent in the tree can have.
    For example, a Binary Tree has a k-ary value of 2, meaning any node can have 
    0-2 children.
'''

# 1.3 What makes this tree an efficient binary search tree?
'''
    As you may recall from class, a binary search tree is a specific type of 
    binary tree that has some order to it's movement through children. In the
    case of the tree shown:
    For every node, any value smaller is placed to the left and any value larger is
    placed to the right. This makes for a "Balanced" binary tree and in turn improves
    any searching algorithm due to the even split.
'''

# 1.4 Design the most inefficient binary search tree using the value nodes from the previous question.
'''
    In class I covered a problem with insertion into the binary search tree. If the values are placed in
    order, you end up with only a single direction moving down the tree where each node is sequential.
    [1,2,3,4,5,6,7] placed into the tree in order would result in each item being placed in the larger slot
    to the right of its parent. Meaning it wouldn't really be a tree, but just a chain of values.
    For this question a diagram is expected.

    Mentioning that the linear result would effectively negate the benefit of tree by rendering the search
    O(N) would also be a great addition to your explanation.
'''

