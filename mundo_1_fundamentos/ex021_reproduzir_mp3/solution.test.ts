import { describe, expect, it } from "vitest";
import { reproduzAudio } from "./solution";

describe("reproduzAudio", () => {
  it.each([["musica.mp3", "Reproduzindo: musica.mp3"],
    ["audio/voz.mp3", "Reproduzindo: audio/voz.mp3"],
    ["PODCAST.MP3", "Reproduzindo: PODCAST.MP3"],
    ["clipe.mp4", "Formato de \u00e1udio n\u00e3o suportado"],
    ["sem_extensao", "Formato de \u00e1udio n\u00e3o suportado"],
    ["arquivo.Mp3", "Reproduzindo: arquivo.Mp3"],
    ["", "Formato de \u00e1udio n\u00e3o suportado"],
    ["x.mp33", "Formato de \u00e1udio n\u00e3o suportado"],
    ["a.b.mp3", "Reproduzindo: a.b.mp3"]])
    ("reproduzAudio(%s) retorna %s", (caminho, esperado) => {
    expect(reproduzAudio(caminho)).toBe(esperado);
  });
});
