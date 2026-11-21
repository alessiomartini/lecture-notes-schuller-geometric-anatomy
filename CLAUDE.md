# Instructions for Claude: Schuller, Geometric Anatomy notes

@~/.claude/templates/lecture-notes/RULES.md
Setup copied from `../lecture-notes-dynamical-systems-data` (Brunton), which copies Mehrling: same preamble
machinery, `build.py`, `scroll.py`. When in doubt, do as those repos do.

## Sources and how to use them
- The repo is **public**. `materials/` (transcripts, audio, PDFs, notes by others) is gitignored: check
  `git status` before every commit.
- One chapter per lecture (`chapters/chNN-<slug>.tex`), sections in the order of the lecture.
- Main source = the lecture itself: `materials/transcripts/CXX-V01.txt` (`[m:ss] text`, from YouTube
  auto-captions or local whisper). Paraphrase in clean English, fix mis-hearings ("girdle" -> Gödel,
  "x-files awkwardly" -> ex falso quodlibet, "a line" -> Erlangen, "drama tree" -> geometry, "Frigga" -> Frege).
  **Never drop content**: every definition, theorem, proof, example, remark, digression and student question goes
  in (side remarks in `aside`/`coursenote`, skippable material in `secondary`).
- Formal style: Definition / Theorem / Proof as on the blackboard, proofs in full. Ambiguous blackboard notation:
  reconstruct from context and the backup notes, mark `[?]` if unsure. Lecture wins over notes; note relevant
  differences in `secondary`.
- `\ts{C}{1}{m:ss}` on every point (C = lecture number; one video per lecture), `\seg{C}{1}{text}` in the Sources box.
- Backup notes (Rea, `materials/backup/`) only to check symbols and statements, never copied (no licence).
- Each chapter starts with Sources + a `reading` box pointing to the matching chapters of the other Schuller sets
  (Gravity and Light, Quantum, Mechanik) and to his papers where useful.
- Exercises: short in the text, long ones verbatim in `appendices/appA-exam.tex`; passages taken out of the text go
  to `\section*{Set aside}` at the chapter end. Chapter end: `keyconcepts` box.

## Build and check
`cd lecture-notes && python build.py all`, then grep `build/main.log` for `\.tex:[0-9]+:`, `undefined`, `Overfull`
and look at the rendered pages. When writing LaTeX through the shell backslashes get mangled: use Edit/Write.
