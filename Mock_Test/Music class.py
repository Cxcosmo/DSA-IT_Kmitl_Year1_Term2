class Song :
    def __init__(self, name, genre, duration) :
        self.name = name
        self.genre = genre
        self.duration = duration
    def show_info(self) :
        m = self.duration // 60
        s = self.duration - (m * 60)
        return f"{self.name} <|> {self.genre} <|> {m}.{s:>02}"

def main() :
    Rickroll = Song(input(), input(), int(input()))
    print(Rickroll.show_info())
main()
