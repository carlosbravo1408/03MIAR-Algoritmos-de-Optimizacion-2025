from manim import *

def create_water_mark(text: str):
    water_mark = Text(
        text,
        font_size=26,
        color=GREY
    )
    water_mark.to_corner(DR).set_opacity(0.9)
    return water_mark

class ModeladoSolucion(Scene):
    def construct(self):
        self.add(create_water_mark("Autor: Carlos Javier Bravo"))
        valores = [2, 0, 1, 0, 2, 1]

        cuadros = VGroup(*[Square(side_length=1) for _ in valores]).arrange(
            RIGHT, buff=0.1)

        textos_valores = VGroup(*[Text(str(v), font_size=36) for v in valores])
        for txt, cuad in zip(textos_valores, cuadros):
            txt.move_to(cuad.get_center())

        textos_indices = VGroup(
            *[Text(f"T{i}", font_size=24, color=LIGHT_GREY) for i in
              range(len(valores))])
        for txt, cuad in zip(textos_indices, cuadros):
            txt.next_to(cuad, DOWN, buff=0.2)

        arreglo = VGroup(cuadros, textos_valores, textos_indices)
        arreglo.center()
        self.add(arreglo)
        self.wait(1)

        idx_ejemplo = 2
        marco = SurroundingRectangle(cuadros[idx_ejemplo], color=YELLOW,
                                     buff=0.05)
        self.play(Create(marco), run_time=0.5)

        flecha_idx = Arrow(start=DOWN, end=UP, color=BLUE).next_to(
            textos_indices[idx_ejemplo], DOWN)
        lbl_idx = Text("Índice = Toma", font_size=28, color=BLUE,
                       weight=BOLD).next_to(flecha_idx, DOWN)

        flecha_val = Arrow(start=UP, end=DOWN, color=GREEN).next_to(
            cuadros[idx_ejemplo], UP)
        lbl_val = Text("Valor = Día", font_size=28, color=GREEN,
                       weight=BOLD).next_to(flecha_val, UP)

        self.play(GrowArrow(flecha_idx), Write(lbl_idx), run_time=0.6)
        self.play(GrowArrow(flecha_val), Write(lbl_val), run_time=0.6)
        self.wait(1.5)

        grupo_explicacion = VGroup(marco, flecha_idx, lbl_idx, flecha_val,
                                   lbl_val)
        self.play(FadeOut(grupo_explicacion), run_time=0.5)


        puntos = Text("...", font_size=48).next_to(cuadros, RIGHT, buff=0.3)
        cuadro_final = Square(side_length=1).next_to(puntos, RIGHT, buff=0.3)
        val_final = Text("4", font_size=36).move_to(cuadro_final.get_center())
        idx_final = Text("T29", font_size=24, color=LIGHT_GREY).next_to(
            cuadro_final, DOWN, buff=0.2)

        extremo_derecho = VGroup(puntos, cuadro_final,
                                 val_final, idx_final)

        grupo_total = VGroup(arreglo,extremo_derecho, )
        self.play(
            FadeIn(extremo_derecho),
            grupo_total.animate.center().shift(DOWN * 0.5),
            run_time=0.8
        )

        llave = Brace(grupo_total, direction=UP)
        lbl_llave = llave.get_text("$N = 30$ tomas")
        lbl_llave.set_font_size(48)

        self.play(GrowFromCenter(llave), Write(lbl_llave), run_time=0.8)
        self.wait(2)

        self.play(
            FadeOut(llave),
            FadeOut(lbl_llave),
            FadeOut(extremo_derecho),
            run_time=0.6
        )

        self.play(arreglo.animate.center(), run_time=0.6)
        self.wait(0.5)


class MascaraBitsRoles(Scene):
    def construct(self):
        # este método genera un watermark en la esquina inferior derecha
        self.add(create_water_mark("Autor: Carlos Javier Bravo"))

        tabla = Table(
            [["RRD", "1", "1", "1", "7"],
             ["LHL", "1", "0", "1", "5"],
             ["HLC", "0", "1", "1", "3"]],
            col_labels=[Text("Profesor"), Text("P"), Text("S"), Text("V"),
                        MathTex("B_{10}")],
            include_outer_lines=True
        ).scale(0.5).to_edge(RIGHT, buff=0.5)

        elementos_tabla = tabla.get_entries()
        lineas_tabla = VGroup(tabla.get_horizontal_lines(),
                              tabla.get_vertical_lines())
        elementos_tabla.set_opacity(0)
        self.add(lineas_tabla)

        roles = [
            ("Presidente", "¿Puede ser Presidente?", 2),
            ("Secretario", "¿Puede ser Secretario?", 3),
            ("Vocal", "¿Puede ser Vocal?", 4)
        ]

        for nombre, pregunta, col_idx in roles:
            txt_pregunta = Text(pregunta, font_size=32).shift(LEFT * 4)
            txt_si = Text("Sí=1", font_size=32, color=GREEN).next_to(txt_pregunta, RIGHT, buff=0.3)
            txt_no = Text("No=0", font_size=32, color=RED).next_to(txt_pregunta, RIGHT, buff=0.3)

            self.play(FadeIn(txt_pregunta))
            self.play(FadeIn(txt_si))
            self.play(FadeOut(txt_si))
            self.play(FadeIn(txt_no))
            header_celda = tabla.get_entries((1, col_idx))
            self.play(header_celda.animate.set_opacity(1),
                      FadeOut(txt_pregunta), FadeOut(txt_no))

        header_prof = tabla.get_entries((1, 1))
        header_b10 = tabla.get_entries((1, 5))
        self.play(
            header_prof.animate.set_opacity(1),
            header_b10.animate.set_opacity(1)
        )

        casos = [
            ("Profesor RRD, puede\ncubrir los 3 roles", 2),
            ("Profesor LHL, presidente\ny vocal", 3),
            ("Profesor HLC, secretario\ny vocal", 4)
        ]

        for texto_caso, fila_idx in casos:
            txt_explicacion = Text(texto_caso, font_size=32).shift(LEFT * 4)
            self.play(FadeIn(txt_explicacion))
            animaciones_fila = []
            for col in range(1, 6):
                celda = tabla.get_entries((fila_idx, col))
                animaciones_fila.append(celda.animate.set_opacity(1))
            self.play(*animaciones_fila)
            self.play(FadeOut(txt_explicacion))
        self.play(elementos_tabla.animate.set_opacity(0))

class MascaraBitsRolesComparacion(Scene):
    def construct(self):

        self.add(create_water_mark("Autor: Carlos Javier Bravo"))

        tabla = Table(
            [["RRD", "1", "1", "1", "7"],
             ["LHL", "1", "0", "1", "5"],
             ["HLC", "0", "1", "1", "3"]],
            col_labels=[Text("Profesor"), Text("P"), Text("S"), Text("V"),
                        MathTex("B_{10}")],
            include_outer_lines=True
        ).scale(0.5).to_edge(RIGHT, buff=0.5)

        elementos_tabla = tabla.get_entries()
        lineas_tabla = VGroup(tabla.get_horizontal_lines(),
                              tabla.get_vertical_lines())
        self.add(lineas_tabla)
        self.add(elementos_tabla)



        titulo_rrd = Text("¿RRD puede ser Presidente?", font_size=32).shift(LEFT * 3 + UP * 2)
        explicacion_rol_rrd = MathTex("Presidente: 100_2, 4_{10}", font_size=28).next_to(titulo_rrd, DOWN)
        self.play(FadeIn(titulo_rrd), FadeIn(explicacion_rol_rrd))

        calc_rrd_1 = MathTex("1", "1", "1_2", " \\, 7_{10}").next_to(explicacion_rol_rrd, DOWN)
        calc_rrd_2 = MathTex("1", "0", "0_2", " \\, 4_{10}").next_to(calc_rrd_1, DOWN)
        line_rrd = Underline(calc_rrd_2)
        op_rrd = MathTex("\\&").next_to(calc_rrd_2, LEFT)
        res_rrd = MathTex("1", "0", "0_2", " \\, 4_{10}").next_to(line_rrd, DOWN)

        veredicto_rrd = MathTex(r"4_{10} > 0_{10} \text{ Verdadero}",
                                font_size=32,
                                color=GREEN).next_to(res_rrd, DOWN, buff=0.5)

        self.play(FadeIn(calc_rrd_1))
        self.play(FadeIn(calc_rrd_2), FadeIn(op_rrd))
        self.play(Create(line_rrd))
        self.play(FadeIn(res_rrd))
        self.play(FadeIn(veredicto_rrd))
        self.wait(1)
        grupo_rrd = VGroup(titulo_rrd, explicacion_rol_rrd, calc_rrd_1,
                           calc_rrd_2, line_rrd, op_rrd,
                           res_rrd, veredicto_rrd)
        self.play(FadeOut(grupo_rrd))

        titulo_lhl = Text("¿LHL puede ser Secretario?", font_size=32).shift(LEFT * 3 + UP * 2)
        explicacion_rol_lhl = MathTex("Secretario: 010_2, 2_{10}", font_size=28).next_to(titulo_lhl, DOWN)
        self.play(FadeIn(titulo_lhl), FadeIn(explicacion_rol_lhl))

        calc_lhl_1 = MathTex("1", "0", "1_2", " \\, 5_{10}").next_to(explicacion_rol_lhl, DOWN)
        calc_lhl_2 = MathTex("0", "1", "0_2", " \\, 2_{10}").next_to(calc_lhl_1, DOWN)
        line_lhl = Underline(calc_lhl_2)
        op_lhl = MathTex("\\&").next_to(calc_lhl_2, LEFT)
        res_lhl = MathTex("0", "0", "0_2", " \\, 0_{10}").next_to(line_lhl, DOWN)

        veredicto_lhl = MathTex(r"0_{10} \ngtr  0_{10} \text{ Falso}  ", font_size=32,
                                color=RED).next_to(
            res_lhl, DOWN, buff=0.5)

        self.play(FadeIn(calc_lhl_1))
        self.play(FadeIn(calc_lhl_2), FadeIn(op_lhl))
        self.play(Create(line_lhl))
        self.play(FadeIn(res_lhl))
        self.play(FadeIn(veredicto_lhl))
        self.wait(1)
        grupo_lhl = VGroup(titulo_lhl, explicacion_rol_lhl, calc_lhl_1,
                           calc_lhl_2, line_lhl, op_lhl,
                           res_lhl, veredicto_lhl)
        self.play(FadeOut(grupo_lhl))
DAY_COLOR = BLUE
HOUR_COLOR = GREEN
PRES_COLOR = RED
SECR_COLOR = YELLOW
VOC_COLOR = PURPLE
TEXT_COLOR = WHITE
TEXT_OPACITY = 0.9
class EspacioSolucionesAnimacionTribunales(Scene):
    def construct(self):
        self.add(create_water_mark("Autor: Carlos Javier Bravo"))

        solucion_valida = [
            [0, 1, 0, 1, 4], [0, 1, 5, 6, 7], [0, 2, 0, 1, 2],
            [0, 2, 5, 3, 6], [0, 3, 0, 1, 2], [0, 3, 4, 5, 6],
            [0, 3, 8, 7, 9], [1, 0, 2, 3, 4], [1, 0, 5, 6, 7],
            [1, 1, 1, 6, 2], [1, 1, 4, 7, 8], [1, 2, 0, 1, 2],
            [1, 2, 4, 5, 8], [2, 0, 0, 1, 2], [2, 0, 4, 5, 7]
        ]

        m = Matrix(
            solucion_valida,
            v_buff=0.5,
            h_buff=0.8
        ).scale(0.65).move_to(RIGHT * 1.5)

        colores = [DAY_COLOR, HOUR_COLOR, PRES_COLOR, SECR_COLOR, VOC_COLOR]
        for j, col in enumerate(m.get_columns()):
            for elemento in col:
                elemento.set_color(colores[j])

        row0_copy = m.get_rows()[0].copy()
        row0_copy.scale(2.0).move_to(ORIGIN)
        row0_inicial = row0_copy.copy()

        left_bracket = MathTex("[").scale(2.5).next_to(row0_copy, LEFT, buff=0.2)
        right_bracket = MathTex("]").scale(2.5).next_to(row0_copy, RIGHT, buff=0.2)
        vector_brackets = VGroup(left_bracket, right_bracket)

        si_label = MathTex("S_i = ", font_size=48).next_to(left_bracket, LEFT)

        indices = VGroup(*[
            Text(str(i), font_size=20, color=GRAY).next_to(row0_copy[i], UP, buff=0.2)
            for i in range(5)
        ])

        self.add(row0_copy)
        self.play(FadeIn(si_label), FadeIn(vector_brackets))
        self.play(FadeIn(indices))
        # self.wait(1)

        tiempo_label = Text("Tiempo", font_size=26, color=DAY_COLOR)
        recursos_label = Text("Recursos", font_size=26, color=PRES_COLOR)

        t_group = VGroup(tiempo_label).shift(DOWN * 1 + LEFT * 4)
        r_group = VGroup(recursos_label).shift(DOWN * 1 + RIGHT * 4)

        t_texts = VGroup(
            Text("Día (0=15 Abr)", font_size=20, color=DAY_COLOR),
            Text("Hora (1=16h)", font_size=20, color=HOUR_COLOR)
        ).arrange(DOWN, buff=0.2).next_to(t_group, DOWN)

        r_texts = VGroup(
            Text("Presidente (ID=0)", font_size=20, color=PRES_COLOR),
            Text("Secretario (ID=1)", font_size=20, color=SECR_COLOR),
            Text("Vocal (ID=4)", font_size=20, color=VOC_COLOR)
        ).arrange(DOWN, buff=0.2).next_to(r_group, DOWN)

        def create_orthogonal_arrow(start_mobj, end_mobj, color, is_left=True):
            start_pt = start_mobj.get_bottom()
            if is_left:
                end_pt = end_mobj.get_right()
            else:
                end_pt = end_mobj.get_left()

            l1 = Line(start_pt, [start_pt[0], end_pt[1], 0]).set_color(color)
            l2 = Line([start_pt[0], end_pt[1], 0], [end_pt[0], end_pt[1], 0]).set_color(color).add_tip(tip_length=0.15)

            return VGroup(l1, l2)

        arrows = VGroup(
            create_orthogonal_arrow(row0_copy[0], t_texts[0], DAY_COLOR),
            create_orthogonal_arrow(row0_copy[1], t_texts[1], HOUR_COLOR),
            create_orthogonal_arrow(row0_copy[2], r_texts[0], PRES_COLOR, False),
            create_orthogonal_arrow(row0_copy[3], r_texts[1], SECR_COLOR, False),
            create_orthogonal_arrow(row0_copy[4], r_texts[2], VOC_COLOR, False)
        )

        self.play(FadeIn(t_group), FadeIn(t_texts), FadeIn(r_group), FadeIn(r_texts))
        self.play(Create(arrows[0]), Create(arrows[1]), Create(arrows[2]), Create(arrows[3]), Create(arrows[4]))
        self.wait(1)

        self.play(
            FadeOut(indices),
            FadeOut(t_group), FadeOut(t_texts),
            FadeOut(r_group), FadeOut(r_texts),
            FadeOut(arrows),
            FadeOut(si_label), FadeOut(vector_brackets)
        )

        self.play(Transform(row0_copy, m.get_rows()[0]))

        s_matrix_label = MathTex("S_{15 \\times 5} = ", font_size=40).next_to(
            m.get_brackets()[0], LEFT, buff=0.2)

        self.play(FadeIn(m.get_brackets()), FadeIn(s_matrix_label))

        rows = m.get_rows()
        prev_row = row0_copy

        for row in rows[1:]:
            self.play(ReplacementTransform(prev_row.copy(), row),
                      run_time=0.075)
            prev_row = row
        self.wait(1)

        self.play(
            Circumscribe(rows[0], color=WHITE, fade_out=True, run_time=1.5))

        elementos_a_borrar = [s_matrix_label, m.get_brackets()[0],
                              m.get_brackets()[1]] + list(rows[1:])
        self.play(*[FadeOut(obj) for obj in elementos_a_borrar], run_time=1)

        self.play(Transform(row0_copy, row0_inicial))
