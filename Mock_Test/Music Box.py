class Song :
    def __init__(self, name, genre, duration) :
        self.name = name
        self.genre = genre
        self.duration = duration
    def show_info(self) :
        m = int(self.duration) // 60
        s = int(self.duration) - (m * 60)
        print(f"{self.name} <|> {self.genre} <|> {m}.{s:>02}")

class Queue:
    def __init__(self):
        self.data = None
        self.right = None

    def enqueue(self, item: "Song"):
        if self.data is None :
            self.data = item
            self.right = Queue()
        else :
            self.right.enqueue(item)

    def dequeue(self):
        result = None
        if self.data is None :
            print("Underflow! Dequeue from an empty queue")
        elif self.right.isEmpty() :
            result = self.data
            self.data = None
        else :
            result = self.data
            self.data = self.right.data
            self.right = self.right.right
        print("Dequeue item: ", end = "")
        return result
        
    def peek(self):
        if self.data is None :
            print("Underflow! Dequeue from an empty queue")
            return None
        return self.data

    def isEmpty(self):
        if self.data is None :
            return True
        return False
    
    def show_Queue(self):
        if self.data is None :
            print("Queue is empty!")
        else :
            p = self.data
            count = 1
            while p :
                if count < 2 :
                    print(f"Queue#{count} {p.show_info()}")
                    p = self.right
                else :
                    print(f"Queue#{count} {p.data.show_info()}")
                    p = p.right
                count += 1

    # def lastSong(self, time):
    #     if self.data is None :
    #         print("Nothing here! Please add some song")
    #     p = self.data
    #     while time :
    #         while time :
    #             time -= self.data.duration
    #             if time :
    #             p = self.right

    def removeSong(self):
        pass
    def groupSong(self):
        pass
    def undo(self):
        pass
    def rev_queue(self):
        pass

def main():
    """this is main function"""
    q = Queue()
    while (choice := input()) != "End":
        command, data = choice.split(": ")
        match command:
            case "enqueue":
                q.enqueue(Song(*data.split("|")))
            case "dequeue":
                temp = q.dequeue()
                if temp:
                    temp.show_info()
            case "peek":
                temp= q.peek()
                if temp:
                    temp.show_info()
            case "isEmpty":
                print(q.isEmpty())
            case "showQueue":
                q.show_Queue()
            case "lastSong":
                q.lastSong(int(data))
            case "removeSong":
                q.removeSong(data)
            case "groupSong":
                q.groupSong()
            case "undo":
                q.undo()
            case "rev":
                q.rev_queue()
    q.show_Queue()
main()