# JavaJam Chapter 7 — source notes

The HTML and CSS were developed from the **user-provided JavaJamWK5.zip** as the Chapter 6 starting point and the Chapter 7 JavaJam case study of the supplied textbook PDF.

## Source files not supplied

The Chapter 7 starter pack calls for `cup.jpg`, `road.jpg`, `guitar.jpg`, and `threemugs.jpg`, which were not in either provided Week 5 ZIP. To keep the code functional offline, these four files were **derived by cropping or resizing the actual Week 5 images** (`coffeelogo.jpg`, `hero.jpg`, `heroguitar.jpg`, and `heromugs.jpg`). These are substitutes, **not verified publisher-original Chapter 7 images**. You can swap in the official images using exactly these filenames without changing the CSS.

The provided Week 5 files link to `jobs.html` but do not include it. A clearly labeled placeholder page was added to avoid a broken navigation link. Jobs content was **not assigned in the Chapter 7 case study**.

## Practical display adjustments beyond named textbook steps

Because the provided Chapter 6 source CSS used `line-height:150px` in its heading, the smaller 128px Chapter 7 mobile header would not fit correctly with the inherited setting. The stylesheet changes header alignment and uses a smaller heading line height. At the 600px breakpoint, the four links also need shorter padding and flexible widths to avoid horizontal overflow with the existing large font sizes. At desktop width, `grid-template` uses an explicit `1fr` for the right column. These extras are comments in `javajam.css`; textbook-required properties remain visible and unchanged.

Chapter 7 Tasks 1–4 are complete for the Home, Menu, and Music pages. Both small-screen and wider-screen layouts are in one stylesheet (mobile first).
