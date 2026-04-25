# Chord Voicings Reference

A library of common guitar voicings organized by category. Use these as building
blocks when generating practice etudes.

---

## Open Chords (Beginner)

### Major
```
C: x32010     G: 320003     D: xx0232     A: x02220     E: 022100
```

### Minor
```
Am: x02210    Em: 022000    Dm: xx0231
```

### Seventh
```
A7:  x02020   E7:  020100   D7:  xx0212
Am7: x02010   Em7: 022030   Dm7: xx0211
G7:  320001   C7:  x32310   B7:  x21202
```

---

## Barre Chords (Intermediate)

### E-shape barres (root on 6th string)

```
Major:     Minor:      7th:        m7:         maj7:
1-344-1    1-344-x     1-3141-     1-3111-     1-3324-
(F at 1)   (Fm at 1)   (F7 at 1)  (Fm7 at 1)  (Fmaj7 at 1)

Fret formula: Root note on 6th string determines the chord.
  F=1  F#/Gb=2  G=3  Ab=4  A=5  Bb=6  B=7  C=8
```

### A-shape barres (root on 5th string)

```
Major:     Minor:      7th:        m7:         maj7:
x-1333-    x-1311-     x-1312-     x-1311-     x-1333-
(Bb at 1)  (Bbm at 1)  (Bb7 at 1)  (Bbm7 at 1) (Bbmaj7 at 1)

Fret formula: Root note on 5th string determines the chord.
  Bb=1  B=2  C=3  C#=4  D=5  Eb=6  E=7  F=8
```

---

## Jazz Voicings (Intermediate–Advanced)

### Drop 2 voicings (root on 5th string)

```
Cmaj7:  x-3-5-4-5-x     Dm7:   x-5-7-5-6-x
G7:     x-10-12-10-12-x  Em7:   x-7-9-7-8-x
Am7:    x-0-2-0-1-x      Fmaj7: x-x-3-2-1-0

(or movable shapes)
maj7: x-R-x-3-5-7     m7: x-R-x-b3-5-b7
dom7: x-R-x-3-5-b7
```

### Shell voicings (3rds and 7ths only)

Essential jazz voicings — just the defining tones:

```
Root on 6th string:        Root on 5th string:
maj7: x-x-x-4-5-x  (3+7)   maj7: x-x-x-x-5-4  (7+3)
dom7: x-x-x-4-5-x  (3+b7)  dom7: x-x-x-x-5-4  (b7+3)
m7:   x-x-x-3-5-x  (b3+b7) m7:   x-x-x-x-5-3  (b7+b3)

Cmaj7 shell (root 5th):  x-3-x-4-5-x
G7 shell (root 6th):     3-x-x-4-3-x
Dm7 shell (root 5th):    x-5-x-5-6-x
```

### Extended chords

```
C9:      x-3-2-3-3-x      Dm9:    x-5-3-5-5-x
G13:     3-x-3-4-5-x      Am11:   x-0-0-0-1-0
Cmaj9:   x-3-0-4-3-x      Fmaj9:  x-x-3-0-1-0
```

---

## Neo-Soul / R&B Voicings (Intermediate–Advanced)

These voicings emphasize extensions (9, 11, 13) and smooth voice leading.

### Common shapes

```
Gmaj9:     3-x-4-4-3-x      or  3-2-0-0-0-2
Em9:       0-2-0-0-0-2      or  x-7-5-7-7-x
Cmaj7#11:  x-3-4-4-5-x
D9:        x-5-4-5-5-x
Am9:       x-0-2-4-0-0
Bbmaj7#11: x-1-2-2-3-x
```

### Two-chord neo-soul loops

```
Loop 1:  Gmaj9 → Am9         (I → ii)
Loop 2:  Dmaj9 → Em11        (I → ii)
Loop 3:  Cmaj9 → Dm9         (IV → v in G)
Loop 4:  Fmaj9 → Em7         (IV → iii in C)
Loop 5:  Bbmaj7 → Am7        (bVII → vi)
```

---

## Blues Voicings

### Basic 12-bar shapes

```
E7:  020100    A7:  x02020    B7:  x21202
E9:  020132    A9:  x02102    B9:  x21222
```

### Dominant 9th movable shape (funky blues)

```
9th chord (root on 5th string):
x-R-2-1-2-x

E9:  x-7-6-7-7-x
A9:  x-0-2-1-2-x  (open)  or  x-12-11-12-12-x
D9:  x-5-4-5-5-x
```

---

## Fingerpicking Chord Shapes

Voicings that work well for fingerstyle — open strings and close intervals.

```
Cadd9:   x-3-2-0-3-0     Em7:    0-2-2-0-3-0
Dadd9:   x-x-0-2-3-0     Asus2:  x-0-2-2-0-0
G6/9:    3-x-0-2-0-0     Am9:    x-0-2-4-0-0
Dsus2:   x-x-0-2-3-0     Fsus2:  x-x-3-0-1-1
```

---

## Chord Suffix Quick Reference

| Suffix     | Formula (from root)            | Sound          |
|------------|-------------------------------|----------------|
| (major)    | R 3 5                         | Bright, happy  |
| m          | R b3 5                        | Sad, dark      |
| 7          | R 3 5 b7                      | Bluesy, tense  |
| maj7       | R 3 5 7                       | Smooth, jazzy  |
| m7         | R b3 5 b7                     | Mellow, cool   |
| dim / °    | R b3 b5                       | Tense, eerie   |
| aug / +    | R 3 #5                        | Unsettled      |
| sus2       | R 2 5                         | Open, airy     |
| sus4       | R 4 5                         | Suspended       |
| 9          | R 3 5 b7 9                    | Funky, rich    |
| m9         | R b3 5 b7 9                   | Lush, mellow   |
| maj9       | R 3 5 7 9                     | Dreamy         |
| 11         | R 3 5 b7 9 11                 | Complex        |
| 13         | R 3 5 b7 9 13                 | Full, soulful  |
| 7#9        | R 3 5 b7 #9                   | "Hendrix chord"|
| maj7#11    | R 3 5 7 #11                   | Lydian, floaty |
