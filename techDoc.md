# technical documentation

## freeCodeCamp project

coded in haml; 
```
gem install haml\
sudo gem install haml
```

a lot of illegal nesting errors lol;  
was finally able to convert it to html w/:
```
haml render my1st.haml
haml render my1st.haml > my1st.html\
```

nothing was nested in the html file!
& this was only a partial fix:
```
gem install htmlbeautifier
sudo gem install htmlbeautifier\
haml render my1st.haml | htmlbeautifier > myBeautiful1st.html
```

ended up lint checking & cleaning the code manually.

css has been a chore!
totally unable to get the `main` offset & laying on the `body` background like the `.sidebar` is

![Screenshot 2025-04-11 at 4.10.14 PM.png](:/9ad73a2d4176424faba142ed8dbb4dba)

oh well, we move. . .
now i notice:
`main { display: flex; }`
makes the sections line up vertically in columns 
- (body was already` display: flex`)
- it wasnt in columns until its child was
- ??


![Screenshot 2025-04-11 at 4.30.52 PM.png](:/cdec23060b2c4fa297ac37704ac8f243)


nav-links had only padding and were just all run on sentence side by side .. 
just placed them inside of a `<ul>` tho and now they look like a list.

think everything is good now...
💬 helped me lay the .sidebar out w/
```
	position: fixed; /* Fixes the sidebar to the side */
    top: 0;
    left: 0;
    height: 100vh; /* 100% of viewport height */
    display: flex;
    flex-direction: column;
```
i just chose a width & color & moved the main over w/ margin-left to cover the .sidebar width...
started last nite ... finally fixed the haml render this am .. & now ... back at it
🔋69% 04.11.2025 | 16:40:18 
powerhouse OS 1% 
<hr>
just need to style the copy!
<hr>
struggles with background color of navbar hover.
w/ color switch on body > main ...<br>
🔋86% 04.12.2025 | 0:39:42 
powerhouse OS 1%  nigga :zzz: gbwm <br>
🔋83% 04.12.2025 | 7:01:51 
powerhouse OS 1% 
	- changing colors;
	- link text decoration + hovers;<br>

`html, body { padding: 10px; }`  offset the `main` & left some `body` background-color, yet i am still ?? on body > main background: 💬 chg `main { min-height: 100vh; }` so it grows taller if content overflows **but that aint do the trick**;<br>
🔋78% 04.12.2025 | 7:28:11 
powerhouse OS 1% 
**i am about to just hit upload w/ no lint-check & ✅  fcc rwd off the list**
2 questions first w/ 💬:
the chng of background - *1 more time smh*;
why some `<p>` text is unsized to 1.2rem;
??
also: fix` @media ( ) { }` not right now tho get this cert!
<hr>

[chat💬assist](https://chatgpt.com/share/67fa5cc2-edc0-800c-9104-1b07569c6d50)
<hr>

i lowkey fixed the 2nd question myself w/ nesting adjustments plus i overlooked a nesting error. then i got confirmation via💬:
Ahh yes — the issue here is actually semantic HTML: you're nesting a `<ul>` list inside a `<p>` tag, which is invalid HTML.
You can’t place block-level elements like `<ul>` inside a `<p>`
<hr>im not sure whether this answered the first question or not; i dont feel like doing it rtfn ... plus i want my main to sit in the body w/ the color around it - even though it may be a better way to do that im thinking ... 💭 🤔  ... 🤷🏽‍♂️ ...<br>
💬:
Ah, you're **really close** again — and I totally get why it's confusing! Here's what’s likely happening:


### 🔍 Problem:
You're setting a `padding: 10px;` on the `body`, and since the `body` only naturally stretches as far as its content, it doesn’t necessarily fill beyond the viewport. When content overflows (i.e. you scroll), the **gap at the bottom** might show the **html background (default transparent)** or unexpected spacing.

### 📌 Also — `main` has a `min-height: 100vh`, which is good — **but** that only ensures it fills the *initial* viewport, not the entire height of content **plus** padding.

### ✅ Fix Strategy:
1. **Remove padding from `body`** and move it to `main`, since `main` is your main content area.
2. Or if you *really* want the body to have padding, wrap your layout in a container div and style that instead.
3. Ensure `main` has a `min-height` **greater than** or equal to `100vh` **plus** any spacing.


### ✅ Best Practice Fix:
```css
html, body {
    height: 100%;
    margin: 0;
    padding: 0; /* no padding here */
}

body {
    background-color: #D2C3D0;
    display: flex;
}

main {
    margin-left: 400px;
    padding: 40px;
    background-color: #C3D2C5;
    width: 100%;
    min-height: 100vh;
    box-sizing: border-box;
}
```


### 🛠 Bonus tip:
If you're still seeing background inconsistencies, add this to `html` too:
```css
html {
    background-color: #D2C3D0;
}
```

This ensures that if *anything* leaks outside the `body`, the background remains consistent.

Let me know if you're building a sticky footer or if you want to make sure scrolling behaves smoothly — happy to help set that up too!
	
