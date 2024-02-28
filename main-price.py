import customtkinter

# Color themes
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Root config
app = customtkinter.CTk()
app.geometry('720x480')
app.title('Wire Price Calculator')

# Widget Frames
widget_frame = customtkinter.CTkFrame(master=app)
widget_frame.pack(expand=True, padx=20, pady=20)

final_value_frame = customtkinter.CTkFrame(master=app)
final_value_frame.pack(expand=True, padx=20, pady=0)


def calculate_total_price():
    price_value = float(price_per_foot_input.get())
    ft_amount_value = int(ft_input.get())
    if ft_amount_value <= 999:
        total_price = (price_value * ft_amount_value) / 1000
    elif ft_amount_value == 1000:
        total_price = price_value
    else:
        total_price = price_value * (ft_amount_value / 1000)
    formatted_price = f'{total_price:,.2f}'
    final_price.configure(text=f"Final price: ${formatted_price}")


# Inputs for footage and price
price_per_foot_input = customtkinter.CTkEntry(master=widget_frame, width=350, height=40,
                                              placeholder_text='Price per 1000ft')
price_per_foot_input.pack(pady=20)

ft_input = customtkinter.CTkEntry(master=widget_frame, width=350, height=40,
                                  placeholder_text='Amount of footage')
ft_input.pack(padx=20, pady=20)
# End Inputs

# Submit button
enter_button_one = customtkinter.CTkButton(master=widget_frame, text='Submit', command=calculate_total_price)
enter_button_one.pack(pady=20)

# Display final calculation
final_price = customtkinter.CTkLabel(master=final_value_frame,width=350, height=40, text='Final price:')
final_price.pack(pady=20)

app.mainloop()
