import pytest

from solution_ex021_reproduzir_mp3 import reproduz_audio


@pytest.mark.parametrize(
    "caminho,esperado",
    [
        ('musica.mp3', 'Reproduzindo: musica.mp3'),
        ('audio/voz.mp3', 'Reproduzindo: audio/voz.mp3'),
        ('PODCAST.MP3', 'Reproduzindo: PODCAST.MP3'),
        ('clipe.mp4', 'Formato de áudio não suportado'),
        ('sem_extensao', 'Formato de áudio não suportado'),
        ('arquivo.Mp3', 'Reproduzindo: arquivo.Mp3'),
        ('', 'Formato de áudio não suportado'),
        ('x.mp33', 'Formato de áudio não suportado'),
        ('a.b.mp3', 'Reproduzindo: a.b.mp3'),
    ],
)
def test_reproduz_audio(caminho, esperado):
    assert reproduz_audio(caminho) == esperado
