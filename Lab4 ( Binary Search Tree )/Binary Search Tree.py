class BSTNode :
    def __init__(self, data: int = None) :
        self.data = data
        self.left = None
        self.right = None

class BST :
    def __init__(self, data = None) :
        self.root = data

    def is_empty(self) :
        return self.root is None

    def insert(self, data) :
        if self.is_empty() :
            self.root = BSTNode(data)
            self.root.left = BST()
            self.root.right = BST()
        else :
            if self.root.data >= data :
                self.root.left.insert(data)
            else :
                self.root.right.insert(data)

    def pre_order(self) :
        if self.root != None :
            print(" -> " + str(self.root.data), end = "")
            self.root.left.pre_order()
            self.root.right.pre_order()

    def in_order(self) :
        if self.root != None :
            self.root.left.in_order()
            print(" -> " + str(self.root.data), end = "")
            self.root.right.in_order()

    def post_order(self) :
        if self.root != None :
            self.root.left.post_order()
            self.root.right.post_order()
            print(" -> " + str(self.root.data), end = "")

    def traverse(self) :
        if self.root != None :
            print("Preorder:", end="")
            self.pre_order()
            print()
            print("Inorder:", end="")
            self.in_order()
            print()
            print("Postorder:", end="")
            self.post_order()
        else :
            print("This is an empty binary search tree.")

    def find_min(self) :
        if self.root != None :
            if self.root.left.root is None :
                return self.root.data
            else :
                return self.root.left.find_min()
        else :
            return None

    def find_max(self) :
        if self.root != None :
            if self.root.right.root is None :
                return self.root.data
            else :
                return self.root.right.find_max()
        else :
            return None

    def delete(self, data) :
        value = self.deleteRecursive(data)
        if not value :
            print("Delete Error, " + str(data) + " is not found in Binary Search Tree.")
        return value

    def deleteRecursive(self, data) :
        value = None
        if self.root != None :
            if self.root.data != data :
                value = self.root.left.deleteRecursive(data)
                if not value :
                    value = self.root.right.deleteRecursive(data)
            else :
                if self.root.left.is_empty() and self.root.right.is_empty() :
                    value = self.root.data
                    self.root = None
                elif not self.root.left.is_empty() and not self.root.right.is_empty() :
                    max_value = self.root.left.find_max()
                    self.root.left.deleteRecursive(max_value)
                    value = self.root.data
                    self.root.data = max_value
                elif not self.root.left.is_empty() :
                    value = self.root.data
                    self.root = self.root.left.root
                elif not self.root.right.is_empty() :
                    value = self.root.data
                    self.root = self.root.right.root
        return value

    def isExist(self, data) :
        result = False
        if self.root != None and not result :
            if self.root.data == data :
                result = True
            else :
                result = self.root.left.isExist(data)
                if not result :
                    result = self.root.right.isExist(data)
        return result
    
    def treeHeight(self) :
        if self.root != None :
            height_left = self.root.left.treeHeight()
            height_right = self.root.right.treeHeight()
            return max(height_right, height_left) + 1
        return 0

def main():
    my_bst = BST()
    while 1:
        text = input()
        if text == "Done":
            break
        condition, data = text.split(": ")
        if condition == "I":
            my_bst.insert(int(data))
        elif condition == "D":
            my_bst.delete(int(data))
        else:
            print("Invalid Condition")
    print(my_bst.treeHeight())
main()
