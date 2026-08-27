import { describe, expect, it } from "vitest";
import { reproduzAudio } from "./solution";

describe("reproduzAudio", () => {
  it.each([
    ["musica.mp3", "Reproduzindo: musica.mp3"],
    ["audio/voz.mp3", "Reproduzindo: audio/voz.mp3"],
    ["PODCAST.MP3", "Reproduzindo: PODCAST.MP3"],
    ["clipe.mp4", "Formato de áudio não suportado"],
    ["sem_extensao", "Formato de áudio não suportado"],
  ])("reproduzAudio(%s) retorna %s", (caminho, esperado) => {
    expect(reproduzAudio(caminho)).toBe(esperado);
  });
});