class Node:

    # Constructor to create  a new node 
    def __init__(self, data):
        self.data = data
        self.next = None


class ListaCircularEncadeada:

    # Constructor to create a empty circular linked list 
    def __init__(self):
        self.head = None

    modifiedWord = ""

    # Function to insert a node at the beginning of a
    # circular linked list 
    def inserir_elemento(self, data):
        modifiedWord = data
        if data.istitle():
            modifiedWord = data[0].lower() + data[1:]

        ptr1 = Node(modifiedWord)
        temp = self.head

        ptr1.next = self.head

        # If linked list is not None then set the next of 
        # last node 
        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = ptr1

        else:
            ptr1.next = ptr1  # For the first node

        self.head = ptr1

        # Function to print nodes in a given circular linked list

    def imprimir_lista(self):
        temp = self.head
        if self.head is not None:
            print("")
            while True:
                print("%s => " % temp.data, end=" "),
                temp = temp.next
                if temp == self.head:
                    break

                # Driver program to test above function


# Initialize list as empty
cllist = ListaCircularEncadeada()

# Created linked list will be 11->2->56->12


while True:
    option = input('Digite p para adicionar uma palavra ou s para sair, ou v para ver a lista')

    if option == "p":
        word = input("Digite uma palavra")
        cllist.inserir_elemento(word)
    elif option == "v":
        print("Contents of circular Linked List")
        cllist.imprimir_lista()

    elif option == "s":
        break
