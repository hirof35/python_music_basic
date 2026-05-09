import pygame
import os

# Pygameの初期化
pygame.init()
pygame.mixer.init()

# 音楽フォルダのパス（適宜変更してください）
MUSIC_FOLDER = "music"

# フォルダ内の音楽ファイルを取得
playlist = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(('maou_14_shining_star.ogg', 'maou_11_soreha_shinkiro_datta.ogg', 'maou_12.ogg'))]
current_track = 0

# 音楽を再生する関数
def play_music():
    if playlist:
        pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, playlist[current_track]))
        pygame.mixer.music.play()

# 音楽を制御する関数
def stop_music():
    pygame.mixer.music.stop()

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    play_music()

def prev_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    play_music()

def set_volume(volume):
    pygame.mixer.music.set_volume(volume)

# メインループ
print("Simple Music Player Commands:")
print("P: Play, S: Stop, Space: Pause/Unpause, N: Next, B: Previous, Q: Quit")

running = True
play_music()
while running:
    command = input("Enter command: ").lower()
    if command == 'p': 
        play_music()
    elif command == 's':
        stop_music()
    elif command == ' ':  # Space key for pause/unpause
        if pygame.mixer.music.get_busy():
            pause_music()
        else:
            unpause_music()
    elif command == 'n':
        next_track()
    elif command == 'b':
        prev_track()
    elif command == 'q':
        stop_music()
        running = False
