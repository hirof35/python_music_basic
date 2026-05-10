import pygame
import os
import sys

class MusicPlayer:
    def __init__(self, folder_path):
        pygame.init()
        pygame.mixer.init()
        self.folder_path = folder_path
        self.playlist = self._load_playlist()
        self.current_index = 0
        self.is_paused = False

        if not self.playlist:
            print(f"Error: No music files found in '{folder_path}'")
            sys.exit()

    def _load_playlist(self):
        """サポートされている拡張子のファイルを自動取得"""
        supported_ext = ('.mp3', '.ogg', '.wav')
        if not os.path.exists(self.folder_path):
            return []
        return [f for f in os.listdir(self.folder_path) if f.lower().endswith(supported_ext)]

    def play(self):
        track_path = os.path.join(self.folder_path, self.playlist[self.current_index])
        try:
            pygame.mixer.music.load(track_path)
            pygame.mixer.music.play()
            self.is_paused = False
            print(f"Now Playing: {self.playlist[self.current_index]}")
        except pygame.error as e:
            print(f"Failed to play {track_path}: {e}")

    def toggle_pause(self):
        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False
            print("Resume")
        else:
            pygame.mixer.music.pause()
            self.is_paused = True
            print("Paused")

    def stop(self):
        pygame.mixer.music.stop()
        print("Stopped")

    def next(self):
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.play()

    def prev(self):
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.play()

def main():
    # フォルダパスを指定
    player = MusicPlayer(folder_path="musi")

    print("\n=== Professional Music Player ===")
    print("[P]Play  [S]Stop  [Space]Pause/Unpause")
    print("[N]Next  [B]Prev  [Q]Quit")
    print("=================================\n")

    player.play()

    while True:
        # 入力待ち（標準入力）
        command = input(">> ").lower().strip()

        if command == 'p':
            player.play()
        elif command == 's':
            player.stop()
        elif command == ' ':
            player.toggle_pause()
        elif command == 'n':
            player.next()
        elif command == 'b':
            player.prev()
        elif command == 'q':
            player.stop()
            break
        
    pygame.quit()

if __name__ == "__main__":
    main()
