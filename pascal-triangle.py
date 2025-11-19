from manim import *
import math

class CreatePascalTriangleExplainer(Scene):
    def get_pascal_row(self, n):
        return [math.comb(n, k) for k in range(n + 1)]

    def create_pascal_triangle(self, num_rows):
        triangle_group = VGroup()
        starting_point = UP * 3

        for i in range(num_rows):
            row_coeffs = self.get_pascal_row(i)
            row_mobjects = VGroup(*[MathTex(str(coeff), font_size=40) for coeff in row_coeffs])
            
            row_mobjects.arrange(RIGHT, buff=0.8)
            
            if i == 0:
                row_mobjects.move_to(starting_point).align_to(ORIGIN, LEFT).shift(RIGHT * 0)
            else:
                last_row = triangle_group[-1]
                
                row_mobjects.next_to(last_row, DOWN, buff=0.6).align_to(ORIGIN, LEFT).shift(RIGHT * 0)


            triangle_group.add(row_mobjects)

        return triangle_group

    def construct(self):
        ROWS_TO_SHOW = 6
        full_triangle_mobs = self.create_pascal_triangle(ROWS_TO_SHOW)

        first_title = MathTex(
            r"\text{Pascal's Triangle}", r"\text{ Explained!}", 
            font_size=60, 
            color=RED
        )

        self.play(Write(first_title), run_time=2.0)
        
        self.wait(1.0)
        
        self.play(
            Indicate(first_title[0], scale_factor=1.2, color=YELLOW),
            run_time=1.5
        )
        
        self.play(
            Indicate(first_title[0], scale_factor=1.2, color=YELLOW),
            run_time=1.5
        )

        second_title = MathTex(
            r"\text{Presented by Gavin Waako}", 
            font_size=50, 
            color=BLUE_C
        )

        self.wait(2.0)

        self.play(FadeOut(first_title), run_time=2.0)

        self.play(Write(second_title), run_time=2.0)
        
        self.wait(6.0)
        
        self.play(FadeOut(second_title), run_time=2.0)

        initial_triangle = VGroup(*full_triangle_mobs[:3])
        self.play(
            LaggedStart(*[FadeIn(row, shift=DOWN) for row in initial_triangle], lag_ratio=0.3),
            run_time=2.0
        )
        
        row_1 = full_triangle_mobs[1]
        num_a = row_1[0] 
        num_b = row_1[1] 
        pos_sum = full_triangle_mobs[2][1].get_center() # Position of the '2'
        
        self.play(
            num_a.animate.set_color(GREEN), num_b.animate.set_color(GREEN),
            Indicate(num_a), Indicate(num_b),
            run_time=1.0
        )
        
        path = VGroup(
            Line(num_a.get_bottom(), pos_sum, color=GREEN, stroke_width=4),
            Line(num_b.get_bottom(), pos_sum, color=GREEN, stroke_width=4)
        )
        self.play(Create(path), run_time=1.5)
        
        self.play(
            FadeOut(path),
            full_triangle_mobs[2][1].animate.set_color(GREEN),
            Indicate(full_triangle_mobs[2][1]),
            run_time=1.5
        )
        
        self.play(
            FadeToColor(VGroup(num_a, num_b, full_triangle_mobs[2][1]), WHITE),
            run_time=1.0
        )
        
        rows_to_generate = VGroup(*full_triangle_mobs[3:ROWS_TO_SHOW])
        self.play(
            LaggedStart(*[FadeIn(row, shift=DOWN) for row in rows_to_generate], lag_ratio=0.1),
            run_time=3.0
        )
        
        self.wait(13.0) 
        
        self.play(
            FadeOut(full_triangle_mobs),
            run_time=2.0
        )
    