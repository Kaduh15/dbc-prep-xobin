import pytest

from solution import reproduz_audio


@pytest.mark.parametrize(
    "caminho,esperado",
    [
        ("musica.mp3", "Reproduzindo: musica.mp3"),
        ("audio/voz.mp3", "Reproduzindo: audio/voz.mp3"),
        ("PODCAST.MP3", "Reproduzindo: PODCAST.MP3"),
        ("clipe.mp4", "Formato de áudio não suportado"),
        ("sem_extensao", "Formato de áudio não suportado"),
    ],
)
def test_reproduz_audio(caminho, esperado):
    assert reproduz_audio(caminho) == esperado