```mermaid
flowchart TD;

classDiagram
    class PlaySongsLyrics {
        + sing_lyrics(): void
    }

    class PlaySongsMusic {
        + play_guitar(): void
        + play_drums(): void
    }

    class PlayInstrumentalSong {
        + play_drums(): void
        + play_guitar(): void
    }

    class PlayRockSong {
        + play_guitar(): void
        + sing_lyrics(): void
        + play_drums(): void
    }

    PlaySongsLyrics <|-- PlayRockSong
    PlaySongsMusic <|-- PlayInstrumentalSong
    PlaySongsMusic <|-- PlayRockSong
```
