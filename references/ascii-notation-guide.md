# ASCII Notation Guide for Guitar

Standard formats for all notation in practice etudes and exercises.

---

## 1. Standard Tablature (TAB)

Six lines representing strings, high to low. Numbers indicate fret positions.

```
e|---0---1---3---0---|    ← 1st string (highest pitch)
B|---1---1---0---1---|    ← 2nd string
G|---0---2---0---0---|    ← 3rd string
D|---2---3---0---2---|    ← 4th string
A|---3---3---2---3---|    ← 5th string
E|-------1---3-------|    ← 6th string (lowest pitch)
     C    F    G    C
```

### Symbols in TAB

| Symbol | Meaning                    | Example        |
|--------|----------------------------|----------------|
| `0`    | Open string                | `e\|--0--`     |
| `1-24` | Fret number                | `B\|--5--`     |
| `h`    | Hammer-on                  | `e\|--5h7--`   |
| `p`    | Pull-off                   | `e\|--7p5--`   |
| `/`    | Slide up                   | `e\|--5/7--`   |
| `\`    | Slide down                 | `e\|--7\5--`   |
| `b`    | Bend                       | `e\|--7b9--`   |
| `r`    | Release bend               | `e\|--9r7--`   |
| `~`    | Vibrato                    | `e\|--7~~~--`  |
| `x`    | Muted / ghost note         | `e\|--x--`     |
| `t`    | Tap (right hand)           | `e\|--t12--`   |
| `*`    | Harmonic                   | `e\|--*12*--`  |
| `---`  | Sustained / rest           | `e\|------`    |

### Timing Markers

Place above the tab to indicate rhythm:

```
     1  +  2  +  3  +  4  +       ← beat subdivisions
e|---0-----0-----0-----0-----|
B|---1-----1-----1-----1-----|
G|---0-----0-----0-----0-----|
D|---2-----2-----2-----2-----|
A|---3-----3-----3-----3-----|
E|----------------------------|
```

Use `|` for bar lines:

```
e|--0---1---|---3---0---|
```

---

## 2. Chord Box Diagrams

Vertical orientation. Nut (or fret marker) at top. Strings left-to-right: low E to high e.

### Open chord example

```
   C
x     o   o          x = muted, o = open
┌──┬──┬──┬──┬──┐
│  │  │  │  │  │  1
├──┼──┼──┼──┼──┤
│  │  │  │ ●│  │  2    ● = finger
├──┼──┼──┼──┼──┤
│  │  │ ●│  │ ●│  3
└──┴──┴──┴──┴──┘
E  A  D  G  B  e
      3  2     1         ← fingering (1=index, 2=mid, 3=ring, 4=pinky)
```

### Barre chord example

```
   Bm7 (2fr)
x
╒══╤══╤══╤══╤══╕  2fr   ← starting fret
│  ●──●──●──●──│  2     ● with ── = barre
├──┼──┼──┼──┼──┤
│  │  │  │  │  │  3
├──┼──┼──┼──┼──┤
│  │  ●│  │  │  4
└──┴──┴──┴──┴──┘
E  A  D  G  B  e
   1  1  1  1  1         ← barre with index
         3               ← ring finger on D
```

### Compact inline format

For quick reference when full diagrams aren't needed:

```
C:  x32010    (low E to high e, x=mute, 0=open)
Am: x02210
G:  320003
D:  xx0232
F:  133211
```

---

## 3. Scale Diagrams

Fretboard grid showing scale tones. Use `R` for root, numbers for scale degrees.

### Linear (horizontal) format

```
   Fret: 5    6    7    8    9    10
e|------ R ------- 2 ------- 3 ------
B|------ 5 ------- 6 --- b7 --------
G|------ 2 --- b3 ------- 4 --------
D|------ 6 --- b7 ------- R --------
A|------ 3 ------- 4 ------- 5 ------
E|------ R ------- 2 ------- 3 ------

A minor pentatonic (position 1)
R = root (A), numbers = scale degrees
```

### Box pattern format

```
A Minor Pentatonic — Position 1

    5fr
e:  ○───●
B:  ○───●
G:  ○─●
D:  ○─●
A:  ○───●
E:  ○───●

○ = root tone
● = scale tone
```

---

## 4. Scale Degree / Harmonic Annotations

Place Roman numerals above the tab to show harmonic function:

```
    | IVmaj7     | V7         | iii7       | vi7        |

e|--| ---8-------|---7--------|---3--------|---5------- |
B|--| ---8-------|---7--------|---3--------|---5------- |
G|--| ---9-------|---7--------|---4--------|---5------- |
D|--| ---10------|---7--------|---5--------|---5------- |
A|--| ---8-------|---7--------|---3--------|---5------- |
E|--| ---------- |------------|------------|----------- |
      Fmaj7        G7           Em7          Am7
      (key of C)
```

### Degree labels

```
Major:  I   ii   iii   IV   V    vi   vii°
Minor:  i   ii°  III   iv   v/V  VI   VII
```

Uppercase = major, lowercase = minor, `°` = diminished, `+` = augmented.

Add extensions inline: `V7`, `IVmaj7`, `ii9`, `bVII7`.

---

## 5. Fingering Annotations

### Left hand (fretting)

| Label | Finger       |
|-------|-------------|
| `T`   | Thumb (over neck) |
| `1`   | Index        |
| `2`   | Middle       |
| `3`   | Ring         |
| `4`   | Pinky        |

Inline with tab — place in parentheses after the fret number:

```
e|---0-------------|
B|---1(1)----------|
G|---0-------------|
D|---2(2)----------|
A|---3(3)----------|
E|-----------------|
       C
```

Or below the chord box:

```
E  A  D  G  B  e
      3  2     1       ← finger assignment
```

### Right hand (picking)

| Label | Finger/Action |
|-------|---------------|
| `p`   | Thumb (pulgar) |
| `i`   | Index         |
| `m`   | Middle        |
| `a`   | Ring (anular) |
| `↓`   | Downstroke    |
| `↑`   | Upstroke      |
| `x`   | Muted strum   |

Picking pattern notation (below tab):

```
e|---0-------0-------0-------0---|
B|-------1-------1-------1-------|
G|---0-------0-------0-------0---|
D|-----------2-----------2-------|
A|---3-----------3-----------3---|
E|-------------------------------|
     p   i   m   i   p   i   m     ← right-hand fingering
```

---

## 6. Rhythm / Strum Patterns

Simple text notation for strumming:

```
Pattern: ↓   ↓ ↑   ↑ ↓ ↑
Beat:    1 + 2 + 3 + 4 +
```

Or with mutes:

```
Pattern: ↓   ↓ ↑ x ↑ ↓ ↑
Beat:    1 + 2 + 3 + 4 +
```

Accent marks above:

```
         >       >
Pattern: ↓   ↓ ↑   ↑ ↓ ↑
Beat:    1 + 2 + 3 + 4 +

> = accent (play louder)
```

---

## 7. Putting It All Together — Full Example

```
Etude: Smooth ii-V-I in C (bars 1-4)
Key: C major | Tempo: 72 BPM | Time: 4/4

    | ii7        | V7         | Imaj7      |            |

     1 + 2 + 3 + 4 +  1 + 2 + 3 + 4 +
e|---1-----------1---|--1-----------0---|
B|---1-----------1---|--0-----------0---|
G|---2-----------2---|--0-----------0---|
D|---0-----------0---|--0-----------2---|
A|---x-----------x---|--x-----------3---|
E|---x-----------x---|--3-----------x---|
     Dm7               G7         Cmaj7
     1(1) 2(3) 3(2)    3(2) 1(1)  2(2) 3(3)

Practice:
- Start at 60 BPM, one strum per chord
- Focus on clean transitions, no buzzing
- Increase 5 BPM when all changes are smooth
- Target tempo: 120 BPM with eighth-note strumming
```
