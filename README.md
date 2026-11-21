# The Geometric Anatomy of Theoretical Physics: lecture notes

LaTeX study notes of Frederic P. Schuller's *Lectures on the Geometric Anatomy of Theoretical Physics*
(FAU Erlangen, WS 2013/14, 28 lectures, 46.6 h): one chapter per lecture, every point linked to the second
of the video where it is said.

- Videos: [YouTube playlist](https://www.youtube.com/playlist?list=PLPH7f_7ZlzxTi6kS4vCmv4ZKm9u8g5yic),
  [FAU.tv](https://www.fau.tv/series/lectures-on-the-geometric-anatomy-of-theoretical-physics-w13).
- Build: `cd lecture-notes && python build.py all` (latexmk + scroll book `build/book.pdf`).
- Transcripts: `python -I -X utf8 tools/transcripts.py` turns YouTube captions or whisper output in
  `materials/transcripts/raw/` into `materials/transcripts/CXX-V01.txt`; `tools/whisper.py` transcribes
  lectures without captions. `materials/` is gitignored (third-party material, never committed).

## Backup sources (checking only, never copied)
- Simon Rea, notes on this course: [PDF](https://tales.mbivert.com/Lectures_on_Geometric_Anatomy_of_Theoretical_Physics.pdf),
  LaTeX [sreahw/schuller-geometric](https://github.com/sreahw/schuller-geometric). No licence stated: all rights
  reserved, used only to check symbols and statements.

Full inventory of Schuller's material: `../lecture-notes-schuller-courses/SOURCES.md` (local).
All rights on the lectures belong to their author; these are personal, non-commercial study notes.
