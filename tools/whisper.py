"""Transcribe uncaptioned lectures locally with faster-whisper large-v3 (CPU int8; the MX150 GPU has too
little memory). Writes materials/transcripts/raw/NNN-<id>.whisper.txt as 'seconds<TAB>text' lines,
which tools/transcripts.py turns into CXX-VYY.txt.
Run: python -I -X utf8 tools/whisper.py materials/audio/002-AAJB9l-HAZs.webm [more files]
"""
import os, sys, time
from pathlib import Path
import av
import numpy as np
from faster_whisper import WhisperModel

ROOT = Path(__file__).resolve().parent.parent


def decode(path):
    """16 kHz mono float32 (the installed PyAV is older than faster-whisper's own decoder expects)."""
    with av.open(str(path)) as c:
        rs = av.AudioResampler(format='s16', layout='mono', rate=16000)
        out = [f.to_ndarray() for fr in c.decode(audio=0) for f in rs.resample(fr)]
    return np.concatenate(out, axis=1).flatten().astype(np.float32) / 32768.0


# large-v3 on this CPU runs at ~0.25x real time (~7 h per lecture); distil-large-v3 (English only) is much
# faster. Choose with WHISPER_MODEL=large-v3|distil-large-v3 (default distil-large-v3).
import os
MODEL = os.environ.get('WHISPER_MODEL', 'distil-large-v3')
model = WhisperModel(MODEL, device='cpu', compute_type='int8', cpu_threads=8)
# Names the model tends to mishear; whisper uses the prompt as preceding context.
PROMPT = ('Lecture by Frederic Schuller on the geometric anatomy of theoretical physics: '
          'propositional logic, predicates, ZFC axioms, Hausdorff, Riemann, Lie, Cauchy, Banach.')
for a in sys.argv[1:]:
    a = Path(a)
    t0 = time.time()
    segs, _ = model.transcribe(decode(a), language='en', vad_filter=True, initial_prompt=PROMPT)
    out = ROOT / 'materials/transcripts/raw' / (a.stem + '.whisper.txt')
    with open(out, 'w', encoding='utf-8') as f:
        for s in segs:
            f.write(f'{int(s.start)}\t{s.text.strip()}\n')
            f.flush()
    print(out.name, f'{(time.time() - t0) / 60:.0f} min')
