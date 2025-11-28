from manim import *
import math

class PascalTriangleExplainer(Scene):
    
    def get_pascal_row(self, n):
        """Calculates the coefficients for row n (n=0 is the top row)."""
        return [math.comb(n, k) for k in range(n + 1)]

    def construct(self):
        ROWS_TO_SHOW = 6  # Rows 0 through 5

        # --- 0. Student & Class Intro ---
        student_name = Text("Presented by Rob Deniro", font_size=48, color=YELLOW)
        class_name = Text("Intro to Computation", font_size=40, color=BLUE_B)
        
        intro_group = VGroup(student_name, class_name).arrange(DOWN, buff=0.5)
        
        self.play(Write(intro_group), run_time=1.5)
        self.wait(2.0)
        self.play(FadeOut(intro_group, shift=UP), run_time=1.0)

        # --- 1. Introduction ---
        title = MathTex(
            r"\text{Pascal's Triangle}", r"\text{ \& The Binomial Theorem}", 
            font_size=64, 
            color=BLUE
        ).scale(1.2)
        
        self.play(Write(title), run_time=2.0)
        self.wait(1.0)
        
        self.play(
            Indicate(title[1], scale_factor=1.1, color=YELLOW),
            run_time=1.5
        )
        self.wait(0.5)
        self.play(FadeOut(title, shift=UP))

        # --- 2. Build the Triangle and Center It ---
        all_rows = VGroup()
        for i in range(ROWS_TO_SHOW):
            row_coeffs = self.get_pascal_row(i)
            row_mobjects = VGroup(*[MathTex(str(coeff), font_size=48) for coeff in row_coeffs])
            row_mobjects.arrange(RIGHT, buff=0.8)
            
            if i == 0:
                row_mobjects.to_edge(UP, buff=1.0)
            else:
                last_row = all_rows[-1]
                row_mobjects.next_to(last_row, DOWN, buff=0.7)
                row_mobjects.set_x(last_row.get_x())
            
            all_rows.add(row_mobjects)

        self.play(
            LaggedStart(*[FadeIn(row, shift=DOWN) for row in all_rows], lag_ratio=0.3),
            run_time=3.0
        )
        self.wait(1.0)

        # --- 3. Explain the Summation Rules ---
        explanation_text = Text("Rule: The sum of two adjacent numbers forms the number directly below them.", font_size=32).to_edge(DOWN)
        self.play(Write(explanation_text))
        self.wait(1.0)
        
        # -- First Summation: Row 2 (1, 2, 1) -> Row 3 --
        row_2 = all_rows[2]
        row_3 = all_rows[3]
        
        num_a = row_2[1]  # The '2'
        num_b = row_2[2]  # The '1'
        pos_sum = row_3[2] # The '3' below them

        self.play(
            num_a.animate.set_color(GREEN), 
            num_b.animate.set_color(GREEN),
            Indicate(VGroup(num_a, num_b)),
            run_time=1.0
        )
        
        path_a = Line(num_a.get_bottom(), pos_sum.get_top(), color=GREEN, stroke_width=4)
        path_b = Line(num_b.get_bottom(), pos_sum.get_top(), color=GREEN, stroke_width=4)
        
        self.play(Create(path_a), Create(path_b), run_time=1.0)
        
        self.play(
            pos_sum.animate.set_color(YELLOW),
            path_a.animate.set_color(YELLOW),
            path_b.animate.set_color(YELLOW),
            run_time=1.0
        )
        self.wait(0.5)

        # Reset colors and lines for the first set
        self.play(
            FadeToColor(VGroup(num_a, num_b, pos_sum), WHITE),
            FadeOut(VGroup(path_a, path_b)),
            run_time=1.0
        )

        # -- Second Summation: Row 3 (1, 3, 3, 1) -> Row 4 --
        row_3 = all_rows[3]
        row_4 = all_rows[4]

        num_c = row_3[1] # The first '3'
        num_d = row_3[2] # The second '3'
        pos_sum_2 = row_4[2] # The '6' below them (3+3)

        self.play(
            num_c.animate.set_color(GREEN),
            num_d.animate.set_color(GREEN),
            Indicate(VGroup(num_c, num_d)),
            run_time=1.0
        )

        path_c = Line(num_c.get_bottom(), pos_sum_2.get_top(), color=GREEN, stroke_width=4)
        path_d = Line(num_d.get_bottom(), pos_sum_2.get_top(), color=GREEN, stroke_width=4)

        self.play(Create(path_c), Create(path_d), run_time=1.0)

        self.play(
            pos_sum_2.animate.set_color(YELLOW),
            path_c.animate.set_color(YELLOW),
            path_d.animate.set_color(YELLOW),
            run_time=1.0
        )
        self.wait(1.0)

        # Reset and clean up text
        self.play(
            FadeToColor(VGroup(num_c, num_d, pos_sum_2), WHITE),
            FadeOut(VGroup(path_c, path_d, explanation_text), shift=DOWN),
            run_time=1.5
        )
        self.wait(0.5)


        # --- 4. Introduce the Binomial Theorem Connection ---
        
        # Isolate Row 4 for the equations
        row_4_coeffs = all_rows[4] # [1, 4, 6, 4, 1]
        
        # Create a group of everything EXCEPT Row 4 to fade it out
        rows_to_remove = VGroup(*[row for i, row in enumerate(all_rows) if i != 4])

        self.play(
            FadeOut(rows_to_remove),
            row_4_coeffs.animate.move_to(ORIGIN).shift(UP * 0.5), # Move Row 4 to center
            run_time=1.5
        )

        # Equation 1: General Formula
        binomial_formula = MathTex(
            r"(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k",
            font_size=54,
            color=PURPLE
        ).next_to(row_4_coeffs, UP, buff=1.0)

        self.play(Write(binomial_formula), run_time=2.0)
        self.wait(0.5)

        # Equation 2: Expansion for n=4
        expansion = MathTex(
            r"(a+b)^4 = ",
            r"1", r"a^4 + ",
            r"4", r"a^3b + ",
            r"6", r"a^2b^2 + ",
            r"4", r"ab^3 + ",
            r"1", r"b^4"
        ).next_to(row_4_coeffs, DOWN, buff=1.0)
        
        self.play(Write(expansion[0]), run_time=0.5) 
        
        coeff_indices = [1, 3, 5, 7, 9]
        row_4_indices = [0, 1, 2, 3, 4]
        
        for exp_i, row_i in zip(coeff_indices, row_4_indices):
            self.play(
                Write(expansion[exp_i:exp_i+2]),
                row_4_coeffs[row_i].animate.scale(1.5).set_color(PURPLE).set_opacity(0.8),
                run_time=0.5
            )
            self.wait(0.2)
            self.play(
                row_4_coeffs[row_i].animate.scale(1/1.5).set_color(WHITE).set_opacity(1.0),
                run_time=0.3
            )
        
        self.wait(2.0)
        
        # --- 5. Clean up and Outro ---
        self.play(
            FadeOut(row_4_coeffs),
            FadeOut(binomial_formula),
            FadeOut(expansion),
            run_time=2.0
        )

        final_message = VGroup(
            Text("Pascal's Triangle: Simple Rule, Deep Connections.", font_size=48, color=GREEN_B),
            Text("Thank you for watching!", font_size=36, color=YELLOW)
        ).arrange(DOWN, buff=0.8)

        self.play(Write(final_message), run_time=2.0)
        self.wait(3.0)
        self.play(FadeOut(final_message))
        self.wait(1.0)