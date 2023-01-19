import vlc


def play_audio(yt):
    vlc_instance = vlc.Instance()
    player = vlc_instance.media_player_new()
    media = vlc_instance.media_new(yt.streams.get_audio_only().url)
    player.set_media(media)
    player.play()
