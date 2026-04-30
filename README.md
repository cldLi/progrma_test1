### 1. Legacy Turtle Project (8th Grade)

#### Background:
I developed this program in 8th grade for a school project. While I initially used AI to help with the logic path, I completely rebuilt the core engine myself. I presented it to the commission and scored **60/64**. I lost a few points on documentation/registration, but the code itself was solid!

#### Features:
The program visualizes 3 basic mathematical graphs: **parabola, hyperbola, and line**. 
1. The program draws the coordinate axes (X and Y).
2. The user chooses a function (e.g., a parabola).
3. The program prompts for coefficients (a, b, and c).

#### The Core Logic (The Kernel):
The heart of the program is the `draw_g` function. It’s a flexible engine that can render any mathematical function passed to it.

```python
def draw_g(func, from_x, to_x):
    t.penup()
    for x in range(from_x, to_x + 1):
        y = func(x)
        if y is not None:
            t.goto(x, y)
            t.pendown()
        else:
            t.penup()
```

#### How it works:
* **Parameters:** The function takes `func` (the math formula), and `from_x` / `to_x` (the rendering range).
* **Process:** The Turtle picks up the pen and iterates through the X-range.
* **Calculation:** For every X, the program calculates Y using the provided formula.
* **Execution:** If the result is valid, the Turtle moves to the coordinates and draws a point. This happens about 600 times, resulting in a smooth, high-quality graph.




