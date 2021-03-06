# Consonance Color Themes for VS Code

Collection of minimalistic dark color themes that each consist of one primary hue.

# About

1. **Colors are defined using LCh(ab)**, a cylindrical transformation of CIELAB color space, which was designed to be perceptually uniform and approximate human vision. This ensures the colors are accurate and consistent within and across themes.
2. **Color palettes consist of one primary hue and a secondary hue that complements it.** The primary hue is mostly used for more colorful elements while the complementary hue is mostly used for subdued, neutral elements. This creates a soothing, minimalist aesthetic while still adding a bit of color contrast between colorful and neutral elements.
3. **Relies on lightness + chroma and bold + italic text over color to provide contrast.** This adds contrast while still allowing for a limited color palette. Lightness and chroma values were carefully tweaked to try to provide high enough contrast between elements without overdoing it.

# Templates

`hue1` is the primary hue and `hue2` is the secondary hue. `hue2` is 120 degrees away from `hue1`.
For more details see the `generate-theme-dark.py` script in the repo, which was used to generate the themes.

## Editor

color   | L  | C  | h    | usage
---     |--- |--- |---   | ---
bg0     | 10 | 0  | 0    | default background
bg1     | 15 | 0  | 0    | line highlight
bg2     | 25 | 0  | 0    | selection
fg0     | 40 | 10 | hue2 | whitespace foreground
fg1     | 60 | 10 | hue2 | keywords, storage, tags, storage types, attributes
fg2     | 80 | 10 | hue2 | default foreground, entities, cursor, markup italic
fg3     | 90 | 10 | hue2 | method/function declarations, markup bold
color0  | 50 | 20 | hue1 | comments, markup quotes
color1  | 60 | 50 | hue1 | strings, CSS tags, markup code
color2  | 70 | 20 | hue1 | variables, markup underline
color3  | 80 | 50 | hue1 | constants, HTML tags, markup headings
red     | 60 | 50 | 30   | errors, invalid, diff deleted
orange  | 60 | 50 | 60   | warnings
green   | 60 | 50 | 150  | diff inserted
blue    | 60 | 50 | 270  | diff changed

Italics are used for comments, library/support entities, storage types, attributes, and markup italic. Bold is used for method/function declarations and markup bold.

## Terminal

color             | L   | C  | h
---               |---  |--- |---
ansiBlack         | 0   | 0  | hue2
ansiRed           | 80  | 20 | hue1
ansiGreen         | 65  | 50 | hue1
ansiYellow        | 80  | 50 | hue1
ansiBlue          | 50  | 10 | hue2
ansiMagenta       | 50  | 50 | hue1
ansiCyan          | 65  | 20 | hue1
ansiWhite         | 90  | 10 | hue2
ansiBrightBlack   | 50  | 10 | hue2
ansiBrightRed     | 80  | 20 | hue1
ansiBrightGreen   | 65  | 50 | hue1
ansiBrightYellow  | 80  | 50 | hue1
ansiBrightBlue    | 50  | 10 | hue2
ansiBrightMagenta | 50  | 50 | hue1
ansiBrightCyan    | 65  | 20 | hue1
ansiBrightWhite   | 100 | 10 | hue2
background        | 10  | 0  | 0
foreground        | 80  | 10 | hue2
