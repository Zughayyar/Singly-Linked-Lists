## Singly Linked Lists
## Anas Zughayyar

class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SList:
    def __init__(self):
        self.head = None

    def print_values(self):
        runner = self.head
        counter = 0
        while runner is not None:
            print(counter," > ",runner.value)
            runner = runner.next
            counter += 1
        return self    

    def add_to_front(self, value):
        new_node = SLNode(value)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    def add_to_back(self, value):
        if self.head == None:
            self.add_to_front(value)
            return self
        else:
            new_node = SLNode(value)
            runner = self.head
            while runner.next is not None:
                runner = runner.next
            runner.next = new_node
            return self
    
    def remove_from_front(self):
        new_head = self.head.next
        del self.head
        self.head = new_head
        return self
    
    def remove_from_back(self):
        runner = self.head
        prev_runner = self.head
        while runner.next is not None:
            prev_runner = runner
            runner = runner.next
        prev_runner.next = None
        del runner
        return self
    
    def remove_val(self, val):
        runner = self.head              #find the Node 
        prev_runner = self.head
        while runner.value != val:
            prev_runner = runner
            runner = runner.next

        tail = self.head                #Find the tail
        while tail.next is not None:
            tail = tail.next

        if runner == self.head:         #head already given
            self.remove_from_front()
            return self 
        elif runner == tail:
            self.remove_from_back()
            return self
        else:
            prev_runner.next = runner.next
            del runner
            return self
    
    def inser_at(self, val, n):
        #find length of linked list
        runner = self.head
        prev_runner = self.head
        size = 0
        while runner.next != None:
            size += 1
            prev_runner = runner
            runner = runner.next
        
        if n < 0 or n > size:
            print("range error")
            return self
        elif n == 0:
            self.add_to_front(val)
            return self
        elif n == size:
            self.add_to_back(val)
            return self
        else:
            runner = self.head
            prev_runner = self.head
            for i in range(n):
                prev_runner = runner
                runner = runner.next
            new_node = SLNode(val)
            prev_runner.next = new_node
            new_node.next = runner
            print(prev_runner.value,new_node.value,runner.value)
            return self


        
    
    

my_list = SList()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun").add_to_back("Hello").add_to_back("world!").print_values()

#my_list.remove_from_front().print_values()

#my_list.remove_from_back().print_values()

#my_list.remove_val("Linked lists").print_values()

my_list.inser_at("n",2).print_values()
