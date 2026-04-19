import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import locale
import csv

# Configurar locale para formato de moneda
try:
    locale.setlocale(locale.LC_ALL, 'es_MX.UTF-8')
except:
    try:
        locale.setlocale(locale.LC_ALL, 'es_MX')
    except:
        try:
            locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
        except:
            try:
                locale.setlocale(locale.LC_ALL, 'es_ES')
            except:
                locale.setlocale(locale.LC_ALL, '')


def format_currency(value):
    try:
        return locale.currency(value, grouping=True)
    except Exception:
        return f"$ {value:,.2f}"


class MiniRetirosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Retiros - Planificación Financiera")
        self.root.geometry("1300x700")
        self.root.resizable(True, True)

        # Configurar colores
        self.bg_color = "#f0f2f5"
        self.primary_color = "#0066cc"
        self.secondary_color = "#00a86b"
        self.accent_color = "#ff6b35"
        self.text_color = "#2c3e50"
        self.light_gray = "#ecf0f1"

        # Aplicar tema
        self.root.configure(bg=self.bg_color)

        # Variables de entrada
        self.current_expenses_var = tk.StringVar(value='15000')
        self.current_age_var = tk.StringVar(value='30')
        self.current_investment_var = tk.StringVar(value='0')
        self.inflation_rate_var = tk.StringVar(value='4')
        self.return_rate_var = tk.StringVar(value='8')
        self.first_withdrawal_age_var = tk.StringVar(value='50')
        self.mini_retirement_duration_var = tk.StringVar(value='6')  # meses
        self.total_withdrawals_var = tk.StringVar(value='5')
        self.withdrawal_frequency_var = tk.StringVar(value='2')
        self.final_withdrawal_age_var = tk.StringVar(value='65')
        self.monthly_investment_mini_input_var = tk.StringVar(value='0')  # inversión mensual a mini retiros
        self.monthly_investment_final_input_var = tk.StringVar(value='0')  # inversión mensual a retiro final

        # Variables de salida
        self.each_withdrawal_amount_var = tk.StringVar(value='$ 0.00')
        self.final_withdrawal_amount_var = tk.StringVar(value='$ 0.00')
        self.current_allocation_mini_var = tk.StringVar(value='$ 0.00')
        self.current_allocation_final_var = tk.StringVar(value='$ 0.00')
        self.monthly_investment_mini_var = tk.StringVar(value='$ 0.00')
        self.monthly_investment_final_var = tk.StringVar(value='$ 0.00')

        # Datos para tabla
        self.table_data = []

        self.create_widgets()

    def create_widgets(self):
        # Frame principal
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)

        # ===== HEADER =====
        header_frame = tk.Frame(main_frame, bg=self.primary_color, height=80)
        header_frame.pack(fill=tk.X, padx=0, pady=0)
        header_frame.pack_propagate(False)

        title_label = tk.Label(header_frame, text="💰 Planificación de Mini Retiros y Retiro Final",
                              font=("Arial", 20, "bold"), bg=self.primary_color, fg="white")
        title_label.pack(pady=15)

        # ===== CONTENT FRAME =====
        content_frame = tk.Frame(main_frame, bg=self.bg_color)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # ===== LEFT PANEL (ENTRADA) =====
        left_panel = tk.Frame(content_frame, bg="white", relief=tk.RAISED, bd=1, width=450)
        left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 15))
        left_panel.pack_propagate(False)

        # Título del panel
        input_title = tk.Label(left_panel, text="📊 Planificación Financiera",
                              font=("Arial", 14, "bold"), bg="white", fg=self.primary_color)
        input_title.pack(pady=(15, 20), padx=15)

        # Separator
        separator = tk.Frame(left_panel, height=2, bg=self.light_gray)
        separator.pack(fill=tk.X, padx=15, pady=(0, 15))

        # Frame principal para inputs organizados en dos columnas
        inputs_container = tk.Frame(left_panel, bg="white")
        inputs_container.pack(fill=tk.BOTH, expand=True, padx=15, pady=0)

        # Crear inputs en una cuadrícula más compacta
        # Fila 1: Edad actual y Monto actual para gastos fijos
        row1 = tk.Frame(inputs_container, bg="white")
        row1.pack(fill=tk.X, pady=(0, 10))

        # Edad actual
        age_frame = tk.Frame(row1, bg="white")
        age_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        tk.Label(age_frame, text="🎂 Edad:", font=("Arial", 9, "bold"),
                bg="white", fg=self.text_color).pack(anchor=tk.W)
        self.age_entry = tk.Entry(age_frame, font=("Arial", 9), width=8, bg=self.light_gray,
                                 relief=tk.FLAT, bd=2, textvariable=self.current_age_var)
        self.age_entry.pack(fill=tk.X, pady=(2, 0))

        # Monto actual para gastos fijos
        expenses_frame = tk.Frame(row1, bg="white")
        expenses_frame.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(5, 0))
        tk.Label(expenses_frame, text="💵 Gastos mensuales:", font=("Arial", 9, "bold"),
                bg="white", fg=self.text_color).pack(anchor=tk.W)
        self.expenses_entry = tk.Entry(expenses_frame, font=("Arial", 9), width=12, bg=self.light_gray,
                                      relief=tk.FLAT, bd=2, textvariable=self.current_expenses_var)
        self.expenses_entry.pack(fill=tk.X, pady=(2, 0))

        # Fila 2: Monto invertido hoy y Tasa de inflación
        row2 = tk.Frame(inputs_container, bg="white")
        row2.pack(fill=tk.X, pady=(0, 10))

        # Monto invertido hoy
        investment_frame = tk.Frame(row2, bg="white")
        investment_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        tk.Label(investment_frame, text="💰 Inversión actual:", font=("Arial", 9, "bold"),
                bg="white", fg=self.text_color).pack(anchor=tk.W)
        self.investment_entry = tk.Entry(investment_frame, font=("Arial", 9), width=8, bg=self.light_gray,
                                        relief=tk.FLAT, bd=2, textvariable=self.current_investment_var)
        self.investment_entry.pack(fill=tk.X, pady=(2, 0))

        # Tasa de inflación
        inflation_frame = tk.Frame(row2, bg="white")
        inflation_frame.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(5, 0))
        tk.Label(inflation_frame, text="📈 Inflación (%):", font=("Arial", 9, "bold"),
                bg="white", fg=self.text_color).pack(anchor=tk.W)
        self.inflation_entry = tk.Entry(inflation_frame, font=("Arial", 9), width=8, bg=self.light_gray,
                                       relief=tk.FLAT, bd=2, textvariable=self.inflation_rate_var)
        self.inflation_entry.pack(fill=tk.X, pady=(2, 0))

        # Fila 3: Tasa de rendimiento y Edad primer retiro
        row3 = tk.Frame(inputs_container, bg="white")
        row3.pack(fill=tk.X, pady=(0, 10))

        # Tasa de rendimiento
        return_frame = tk.Frame(row3, bg="white")
        return_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        tk.Label(return_frame, text="📊 Rendimiento (%):", font=("Arial", 9, "bold"),
                bg="white", fg=self.text_color).pack(anchor=tk.W)
        self.return_entry = tk.Entry(return_frame, font=("Arial", 9), width=8, bg=self.light_gray,
                                    relief=tk.FLAT, bd=2, textvariable=self.return_rate_var)
        self.return_entry.pack(fill=tk.X, pady=(2, 0))

        # Edad del primer mini retiro
        first_age_frame = tk.Frame(row3, bg="white")
        first_age_frame.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(5, 0))
        tk.Label(first_age_frame, text="🎯 Edad 1er retiro:", font=("Arial", 9, "bold"),
                bg="white", fg=self.text_color).pack(anchor=tk.W)
        self.first_age_entry = tk.Entry(first_age_frame, font=("Arial", 9), width=8, bg=self.light_gray,
                                       relief=tk.FLAT, bd=2, textvariable=self.first_withdrawal_age_var)
        self.first_age_entry.pack(fill=tk.X, pady=(2, 0))

        # Fila 4: Duración mini retiros, Total mini retiros y Frecuencia
        row4 = tk.Frame(inputs_container, bg="white")
        row4.pack(fill=tk.X, pady=(0, 10))

        # Duración de cada mini retiro
        duration_frame = tk.Frame(row4, bg="white")
        duration_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 3))
        tk.Label(duration_frame, text="📅 Duración mini retiro (meses):", font=("Arial", 8, "bold"),
                bg="white", fg=self.text_color).pack(anchor=tk.W)
        self.duration_entry = tk.Entry(duration_frame, font=("Arial", 9), width=6, bg=self.light_gray,
                                      relief=tk.FLAT, bd=2, textvariable=self.mini_retirement_duration_var)
        self.duration_entry.pack(fill=tk.X, pady=(2, 0))

        # Total de mini retiros
        total_frame = tk.Frame(row4, bg="white")
        total_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(3, 3))
        tk.Label(total_frame, text="🔢 Total retiros:", font=("Arial", 9, "bold"),
                bg="white", fg=self.text_color).pack(anchor=tk.W)
        self.total_entry = tk.Entry(total_frame, font=("Arial", 9), width=6, bg=self.light_gray,
                                   relief=tk.FLAT, bd=2, textvariable=self.total_withdrawals_var)
        self.total_entry.pack(fill=tk.X, pady=(2, 0))

        # Frecuencia en años
        freq_frame = tk.Frame(row4, bg="white")
        freq_frame.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(3, 0))
        tk.Label(freq_frame, text="⏰ Frecuencia (años):", font=("Arial", 9, "bold"),
                bg="white", fg=self.text_color).pack(anchor=tk.W)
        self.freq_entry = tk.Entry(freq_frame, font=("Arial", 9), width=6, bg=self.light_gray,
                                  relief=tk.FLAT, bd=2, textvariable=self.withdrawal_frequency_var)
        self.freq_entry.pack(fill=tk.X, pady=(2, 0))

        # Fila 5: Edad retiro final
        row5 = tk.Frame(inputs_container, bg="white")
        row5.pack(fill=tk.X, pady=(0, 15))

        # Edad del retiro final
        final_age_frame = tk.Frame(row5, bg="white")
        final_age_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        tk.Label(final_age_frame, text="🏁 Edad retiro final:", font=("Arial", 9, "bold"),
                bg="white", fg=self.text_color).pack(anchor=tk.W)
        self.final_age_entry = tk.Entry(final_age_frame, font=("Arial", 9), width=8, bg=self.light_gray,
                                       relief=tk.FLAT, bd=2, textvariable=self.final_withdrawal_age_var)
        self.final_age_entry.pack(fill=tk.X, pady=(2, 0))

        # Fila 6: Inversiones mensuales
        row6 = tk.Frame(inputs_container, bg="white")
        row6.pack(fill=tk.X, pady=(0, 15))

        # Inversión mensual a mini retiros
        mini_investment_frame = tk.Frame(row6, bg="white")
        mini_investment_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        tk.Label(mini_investment_frame, text="💰 Inversión mensual mini retiros:", font=("Arial", 8, "bold"),
                bg="white", fg=self.text_color).pack(anchor=tk.W)
        self.mini_investment_entry = tk.Entry(mini_investment_frame, font=("Arial", 9), width=10, bg=self.light_gray,
                                             relief=tk.FLAT, bd=2, textvariable=self.monthly_investment_mini_input_var)
        self.mini_investment_entry.pack(fill=tk.X, pady=(2, 0))

        # Inversión mensual a retiro final
        final_investment_frame = tk.Frame(row6, bg="white")
        final_investment_frame.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(5, 0))
        tk.Label(final_investment_frame, text="💰 Inversión mensual retiro final:", font=("Arial", 8, "bold"),
                bg="white", fg=self.text_color).pack(anchor=tk.W)
        self.final_investment_entry = tk.Entry(final_investment_frame, font=("Arial", 9), width=10, bg=self.light_gray,
                                              relief=tk.FLAT, bd=2, textvariable=self.monthly_investment_final_input_var)
        self.final_investment_entry.pack(fill=tk.X, pady=(2, 0))

        # Botones y resultados al final del panel izquierdo
        bottom_section = tk.Frame(left_panel, bg="white")
        bottom_section.pack(fill=tk.X, padx=15, pady=(10, 15))


        # Botón de calcular
        calculate_btn = tk.Button(bottom_section, text="✓ Calcular Plan Financiero",
                                 command=self.calculate_plan,
                                 font=("Arial", 11, "bold"), bg=self.secondary_color,
                                 fg="white", relief=tk.FLAT, bd=0, padx=20, pady=12,
                                 cursor="hand2", activebackground="#009960")
        calculate_btn.pack(fill=tk.X, pady=(0, 8))

        # Botón de exportar
        export_btn = tk.Button(bottom_section, text="📁 Exportar a CSV",
                              command=self.export_to_csv,
                              font=("Arial", 10, "bold"), bg=self.primary_color,
                              fg="white", relief=tk.FLAT, bd=0, padx=20, pady=10,
                              cursor="hand2", activebackground="#004c99")
        export_btn.pack(fill=tk.X, pady=(0, 15))

        # ===== PANEL DERECHO: TABLA DE PROYECCIÓN =====
        right_panel = tk.Frame(content_frame, bg="white", relief=tk.RAISED, bd=1)
        right_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Título de la tabla
        table_title = tk.Label(right_panel, text="📅 Proyección Anual de Fondos",
                              font=("Arial", 13, "bold"), bg="white", fg=self.primary_color)
        table_title.pack(pady=(15, 5))

        # Frame para la tabla y scrollbars
        table_frame = tk.Frame(right_panel, bg="white")
        table_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

        columns = ("Edad", "Fondo Mini Retiros", "Fondo Retiro Final", "Retiro Mini", "Gasto Anual", "Retiro Final")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=22)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor=tk.CENTER, width=130)

        v_scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        h_scrollbar = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        v_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        h_scrollbar.grid(row=1, column=0, sticky=(tk.W, tk.E))

        table_frame.columnconfigure(0, weight=1)
        table_frame.rowconfigure(0, weight=1)

    def calculate_plan(self):
        try:
            # Obtener valores de entrada
            current_expenses = float(self.current_expenses_var.get().replace(',', '').replace('$', ''))
            current_age = int(self.current_age_var.get())
            current_investment = float(self.current_investment_var.get().replace(',', '').replace('$', ''))
            inflation_rate = float(self.inflation_rate_var.get()) / 100
            return_rate = float(self.return_rate_var.get()) / 100
            first_withdrawal_age = int(self.first_withdrawal_age_var.get())
            mini_retirement_duration_months = int(self.mini_retirement_duration_var.get())
            total_withdrawals = int(self.total_withdrawals_var.get())
            withdrawal_frequency = int(self.withdrawal_frequency_var.get())
            final_withdrawal_age = int(self.final_withdrawal_age_var.get())
            monthly_investment_mini = float(self.monthly_investment_mini_input_var.get().replace(',', '').replace('$', ''))
            monthly_investment_final = float(self.monthly_investment_final_input_var.get().replace(',', '').replace('$', ''))

            # Validaciones
            if any(value < 0 for value in [current_expenses, current_age, current_investment, inflation_rate, return_rate, first_withdrawal_age, mini_retirement_duration_months, total_withdrawals, withdrawal_frequency, final_withdrawal_age, monthly_investment_mini, monthly_investment_final]):
                raise ValueError("Todos los valores deben ser positivos")

            if current_age >= first_withdrawal_age or first_withdrawal_age >= final_withdrawal_age:
                raise ValueError("Las edades deben ser lógicas: actual < primer retiro < retiro final")

            # Calcular montos necesarios ajustados por inflación
            # Monto por mini retiro: cubrir X meses de gastos
            each_withdrawal_amount = current_expenses * mini_retirement_duration_months * (1 + inflation_rate) ** (first_withdrawal_age - current_age)

            # Monto retiro final: ya no se usa un monto fijo, se retira anual ajustado por inflación
            final_withdrawal_amount = 0  # No se usa, los retiros se calculan año a año en la tabla

            # Calcular retiros de mini retiros
            mini_withdrawals = []
            for i in range(total_withdrawals):
                withdrawal_year = first_withdrawal_age + (i * withdrawal_frequency) - current_age
                if withdrawal_year <= (final_withdrawal_age - current_age):
                    withdrawal_amount = current_expenses * mini_retirement_duration_months * (1 + inflation_rate) ** withdrawal_year
                    mini_withdrawals.append((withdrawal_year, withdrawal_amount))

            # Generar tabla de proyección usando las inversiones mensuales ingresadas
            self.generate_projection_table(current_age, final_withdrawal_age - current_age, current_investment,
                                        monthly_investment_mini, monthly_investment_final,
                                        return_rate, mini_withdrawals, final_withdrawal_age - current_age, final_withdrawal_amount, mini_retirement_duration_months,
                                        current_expenses * 12, inflation_rate)

            # Mostrar mensaje de éxito
            messagebox.showinfo("Cálculo Completado", "La proyección anual ha sido generada exitosamente.")

        except ValueError as e:
            messagebox.showerror("Error", f"Por favor ingresa valores válidos: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al calcular: {str(e)}")

    def generate_projection_table(self, current_age, total_years, current_investment,
                                monthly_investment_mini, monthly_investment_final,
                                return_rate, mini_withdrawals, final_year, final_withdrawal_amount, mini_retirement_duration_months,
                                current_expenses_annual, inflation_rate):
        # Limpiar tabla anterior
        for item in self.tree.get_children():
            self.tree.delete(item)

        monthly_rate = return_rate / 12


        # La inversión inicial solo va al fondo de retiro final
        balance_mini = 0
        balance_final = current_investment

        # Crear diccionarios de retiros
        mini_withdrawal_dict = {year: amount for year, amount in mini_withdrawals}


        # Determinar los años en los que hay mini retiro activo (suspender aportaciones)
        mini_retiro_anios = set()
        for yr, _ in mini_withdrawals:
            # Cada mini retiro dura mini_retirement_duration_months meses
            años_duracion = max(1, (mini_retirement_duration_months + 11) // 12)
            for offset in range(años_duracion):
                mini_retiro_anios.add(yr + offset)

        retired = False  # Indica si ya se llegó al retiro final
        year = 0
        max_age = 120  # Límite de seguridad

        while True:
            age = current_age + year

            # Protección contra loop infinito
            if age > max_age:
                break

            # --- FASE DE ACUMULACIÓN (antes del retiro final) ---
            if not retired:
                # Suspender aportaciones durante mini retiro activo
                if year in mini_retiro_anios:
                    aportacion_mini = 0
                    aportacion_final = 0
                else:
                    aportacion_mini = monthly_investment_mini
                    aportacion_final = monthly_investment_final

                # Agregar aportaciones (año 0 ya tiene inversión inicial en balance_final)
                if year > 0:
                    balance_mini += aportacion_mini * 12
                    balance_final += aportacion_final * 12

                # Rendimientos
                balance_mini *= (1 + monthly_rate) ** 12
                balance_final *= (1 + monthly_rate) ** 12

                # Retiros de mini retiros
                mini_withdrawal = mini_withdrawal_dict.get(year, 0)
                if mini_withdrawal > 0:
                    balance_mini -= mini_withdrawal

                retiro_mini_col = format_currency(mini_withdrawal) if mini_withdrawal > 0 else "-"
                gasto_anual_col = "-"
                retiro_final_col = "-"

                # ¿Llegamos al año de retiro final?
                if year == final_year:
                    retired = True
                    # No se retira nada aún este año, solo se marca el inicio del retiro

            # --- FASE DE RETIRO FINAL (retiro anual de gastos) ---
            else:
                # Rendimientos sobre lo que queda (fondo sigue invertido)
                balance_mini *= (1 + monthly_rate) ** 12
                balance_final *= (1 + monthly_rate) ** 12

                # Gasto anual ajustado por inflación desde el año 0
                gasto_anual = current_expenses_annual * ((1 + inflation_rate) ** year)
                gasto_anual_col = format_currency(gasto_anual)

                # Retirar primero del fondo mini, luego del fondo final
                retiro_de_mini = 0
                retiro_de_final = 0

                if balance_mini > 0:
                    retiro_de_mini = min(balance_mini, gasto_anual)
                    balance_mini -= retiro_de_mini
                    gasto_restante = gasto_anual - retiro_de_mini
                else:
                    gasto_restante = gasto_anual

                if gasto_restante > 0 and balance_final > 0:
                    retiro_de_final = min(balance_final, gasto_restante)
                    balance_final -= retiro_de_final

                retiro_mini_col = format_currency(retiro_de_mini) if retiro_de_mini > 0 else "-"
                retiro_final_col = format_currency(retiro_de_final) if retiro_de_final > 0 else "-"

            # Evitar saldos negativos por redondeo
            balance_mini = max(0, balance_mini)
            balance_final = max(0, balance_final)

            # Agregar fila a la tabla
            self.tree.insert("", "end", values=(
                age,
                format_currency(balance_mini),
                format_currency(balance_final),
                retiro_mini_col,
                gasto_anual_col,
                retiro_final_col
            ))

            # Detener si ya estamos en fase de retiro y ambos fondos se agotaron
            if retired and balance_mini <= 0 and balance_final <= 0:
                break

            year += 1

    def export_to_csv(self):
        # Verificar que haya datos en la tabla
        items = self.tree.get_children()
        if not items:
            messagebox.showwarning("Sin datos", "Primero calcula el plan financiero antes de exportar.")
            return

        # Solicitar ubicación del archivo
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
            title="Exportar Plan Financiero"
        )
        if not file_path:
            return

        try:
            with open(file_path, 'w', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f)

                # Escribir inputs
                writer.writerow(["=== PARÁMETROS DE ENTRADA ==="])
                writer.writerow(["Edad actual", self.current_age_var.get()])
                writer.writerow(["Gastos mensuales", self.current_expenses_var.get()])
                writer.writerow(["Inversión actual", self.current_investment_var.get()])
                writer.writerow(["Inflación (%)", self.inflation_rate_var.get()])
                writer.writerow(["Rendimiento (%)", self.return_rate_var.get()])
                writer.writerow(["Edad 1er mini retiro", self.first_withdrawal_age_var.get()])
                writer.writerow(["Duración mini retiro (meses)", self.mini_retirement_duration_var.get()])
                writer.writerow(["Total mini retiros", self.total_withdrawals_var.get()])
                writer.writerow(["Frecuencia (años)", self.withdrawal_frequency_var.get()])
                writer.writerow(["Edad retiro final", self.final_withdrawal_age_var.get()])
                writer.writerow(["Inversión mensual mini retiros", self.monthly_investment_mini_input_var.get()])
                writer.writerow(["Inversión mensual retiro final", self.monthly_investment_final_input_var.get()])
                writer.writerow([])

                # Escribir encabezados de tabla
                columns = [self.tree.heading(col)["text"] for col in self.tree["columns"]]
                writer.writerow(["=== PROYECCIÓN ANUAL ==="])
                writer.writerow(columns)

                # Escribir datos de tabla
                for item in items:
                    writer.writerow(self.tree.item(item)["values"])

            messagebox.showinfo("Exportación Exitosa", f"Archivo exportado correctamente:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al exportar: {str(e)}")


def main():
    root = tk.Tk()
    app = MiniRetirosApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
