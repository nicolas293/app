class Track:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return f"{self.title} - {self.artist} ({self.duration})"

class Playlist:
    def __init__(self, name):
        self.name = name
        self.tracks = []

    def add_track(self, track):
        self.tracks.append(track)
        print(f"Трек добавлен: {track}")

    def remove_track(self, index):
        if 0 <= index < len(self.tracks):
            removed = self.tracks.pop(index)
            print(f"Удален трек: {removed}")
        else:
            print("Неверный номер трека")

    def show_playlist(self):
        print(f"\nПлейлист: {self.name}")
        for i, track in enumerate(self.tracks):
            print(f"{i + 1}. {track}")

    def play_track(self, index):
        if 0 <= index < len(self.tracks):
            print(f"\nВоспроизводится: {self.tracks[index]}")
        else:
            print("Трек не найден")

# Пример использования
if __name__ == "__main__":
    playlist = Playlist("Мой плейлист")
    
    while True:
        print("\n1. Добавить трек")
        print("2. Удалить трек")
        print("3. Показать плейлист")
        print("4. Воспроизвести трек")
        print("5. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            title = input("Название трека: ")
            artist = input("Исполнитель: ")
            duration = input("Длительность: ")
            playlist.add_track(Track(title, artist, duration))
            
        elif choice == '2':
            index = int(input("Номер трека для удаления: ")) - 1
            playlist.remove_track(index)
            
        elif choice == '3':
            playlist.show_playlist()
            
        elif choice == '4':
            index = int(input("Номер трека для воспроизведения: ")) - 1
            playlist.play_track(index)
            
        elif choice == '5':
            break
        else:
            print("Неверный выбор")